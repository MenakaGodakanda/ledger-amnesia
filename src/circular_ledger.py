"""
Circular Ledger implementation for Ledger Amnesia.

Implements the circular buffer structure from Section III.A and III.B:
- Fixed-size buffer with N slots
- FIFO overwriting of oldest blocks
- Constant O(N) storage complexity
- Mapping function φ(i) = i mod N
"""

import sys
from typing import List, Optional, Callable, Dict, Any
from src.block import Block
import config


class CircularLedger:
    """
    Implements the circular buffer blockchain structure.
    
    Key features:
    - Fixed storage size (N blocks)
    - Automatic overwriting of oldest blocks
    - Constant space complexity O(N)
    - Cryptographic chain linkage within retention window
    """
    
    def __init__(self, buffer_size: int, difficulty: int, 
                 archival_callback: Optional[Callable] = None):
        """
        Initialize the circular ledger.
        
        Args:
            buffer_size: Number of slots N in the circular buffer
            difficulty: Proof-of-work difficulty level D
            archival_callback: Optional function to call before overwriting blocks
        """
        self.buffer_size = buffer_size  # N in the paper
        self.difficulty = difficulty    # D in the paper
        self.archival_callback = archival_callback
        
        # Physical storage structure S = {s0, s1, ..., s_{N-1}}
        self.storage: List[Optional[Block]] = [None] * buffer_size
        
        # Ledger metadata
        self.last_index = -1  # Current logical block index
        self.window_start = 0  # Start of retention window
        self.window_end = -1   # End of retention window
        
        # Performance tracking
        self.total_hash_computations = 0
        self.overwrite_count = 0
        
        # Initialize with genesis block
        self._initialize_genesis()
    
    def _initialize_genesis(self):
        """Initialize the ledger with genesis block."""
        genesis = Block.create_genesis_block()
        genesis.mine_block(self.difficulty)
        
        position = self._phi(0)
        self.storage[position] = genesis
        self.last_index = 0
        self.window_start = 0
        self.window_end = 0
    
    def _phi(self, logical_index: int) -> int:
        """
        Mapping function φ: N → {0, 1, ..., N-1}
        
        Implements φ(i) = i mod N from Section III.B
        
        Args:
            logical_index: Logical block index i
        
        Returns:
            int: Physical storage slot (0 to N-1)
        """
        return logical_index % self.buffer_size
    
    def is_accessible(self, logical_index: int) -> bool:
        """
        Accessibility predicate R(i) from Section III.B.
        
        Determines if block Bi is still in the retention window:
        R(i) = true if c - N < i ≤ c, false otherwise
        
        Args:
            logical_index: Block index to check
        
        Returns:
            bool: True if block is accessible, False if overwritten
        """
        c = self.last_index
        return c - self.buffer_size < logical_index <= c
    
    def get_block(self, logical_index: int) -> Optional[Block]:
        """
        Retrieve a block by its logical index.
        
        Args:
            logical_index: Logical block index
        
        Returns:
            Block if accessible, None if overwritten or doesn't exist
        """
        if not self.is_accessible(logical_index):
            return None
        
        position = self._phi(logical_index)
        block = self.storage[position]
        
        # Verify this is actually the requested block
        if block and block.index == logical_index:
            return block
        return None
    
    def get_last_block(self) -> Optional[Block]:
        """
        Get the most recent block in the ledger.
        
        Returns:
            Block: Most recent block, or None if ledger is empty
        """
        if self.last_index < 0:
            return None
        return self.get_block(self.last_index)
    
    def add_block(self, data: Dict[str, Any]) -> Block:
        """
        Add a new block to the ledger with mining.
        
        Implements Algorithm 2: Block Insertion with Overwrite
        
        Args:
            data: Application payload (sensor data)
        
        Returns:
            Block: The newly created and mined block
        """
        # Create new block
        new_index = self.last_index + 1
        last_block = self.get_last_block()
        prev_hash = last_block.hash if last_block else "0" * 64
        
        new_block = Block(new_index, data, prev_hash)
        
        # Mine the block (proof-of-work)
        hash_count = new_block.mine_block(self.difficulty)
        self.total_hash_computations += hash_count
        
        # Insert block using insertion protocol
        self._insert_block(new_block)
        
        return new_block
    
    def _insert_block(self, block: Block):
        """
        Internal method to insert block into circular buffer.
        
        Handles overwriting and archival notifications.
        
        Args:
            block: Block to insert
        """
        # Calculate physical position
        position = self._phi(block.index)
        
        # Check if we're overwriting an existing block
        old_block = self.storage[position]
        if old_block is not None and old_block.index != block.index:
            self.overwrite_count += 1
            
            # Trigger archival notification
            if self.archival_callback:
                self.archival_callback(old_block)
            
            # Clear slot (security measure)
            self.storage[position] = None
        
        # Write new block to storage
        self.storage[position] = block
        
        # Update ledger metadata
        self.last_index = block.index
        self.window_start = max(0, block.index - self.buffer_size + 1)
        self.window_end = block.index
    
    def validate_block(self, block: Block, current_time: float) -> tuple[bool, str]:
        """
        Validate a block according to consensus rules.
        
        Implements Algorithm 1: Block Validation
        
        Args:
            block: Block to validate
            current_time: Current timestamp for temporal validation
        
        Returns:
            tuple: (is_valid, error_message)
        """
        # Check 1: Index continuity
        if block.index != self.last_index + 1:
            return False, f"Index discontinuity: expected {self.last_index + 1}, got {block.index}"
        
        # Check 2: Chain continuity
        last_block = self.get_last_block()
        if last_block and block.prev_hash != last_block.hash:
            return False, "Broken hash chain"
        
        # Check 3: Proof-of-work verification
        target = 2 ** (256 - self.difficulty)
        hash_int = int(block.hash, 16)
        if hash_int >= target:
            return False, "Insufficient proof-of-work"
        
        # Check 4: Hash integrity
        calculated_hash = block.calculate_hash()
        if block.hash != calculated_hash:
            return False, "Hash mismatch"
        
        # Check 5: Temporal validity
        time_diff = abs(block.timestamp - current_time)
        if time_diff > config.TIMESTAMP_TOLERANCE:
            return False, f"Timestamp out of range: {time_diff}s deviation"
        
        return True, "Valid"
    
    def get_retention_window(self) -> List[Block]:
        """
        Get all blocks in the current retention window.
        
        Returns:
            list: List of accessible blocks, ordered by index
        """
        blocks = []
        for i in range(self.window_start, self.window_end + 1):
            block = self.get_block(i)
            if block:
                blocks.append(block)
        return blocks
    
    def get_temporal_window(self, delta_t: float) -> float:
        """
        Calculate temporal retention window T = N × Δt.
        
        Args:
            delta_t: Average block generation interval
        
        Returns:
            float: Temporal window duration in seconds
        """
        return self.buffer_size * delta_t
    
    def get_block_age(self, logical_index: int, delta_t: float) -> float:
        """
        Calculate age of block a(Bi) = (c - i) × Δt.
        
        Args:
            logical_index: Block index
            delta_t: Average block generation interval
        
        Returns:
            float: Block age in seconds
        """
        return (self.last_index - logical_index) * delta_t
    
    def get_storage_usage(self) -> int:
        """
        Calculate current storage usage in bytes.
        
        Should remain constant at ~38.4 KB for N=100.
        
        Returns:
            int: Total storage in bytes
        """
        total_bytes = 0
        for block in self.storage:
            if block:
                total_bytes += block.get_size()
        return total_bytes
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get comprehensive ledger statistics.
        
        Returns:
            dict: Statistics including storage, blocks, overwrites
        """
        accessible_blocks = len([b for b in self.storage if b is not None])
        
        return {
            "total_blocks_created": self.last_index + 1,
            "accessible_blocks": accessible_blocks,
            "overwritten_blocks": self.overwrite_count,
            "storage_usage_bytes": self.get_storage_usage(),
            "storage_usage_kb": self.get_storage_usage() / 1024,
            "buffer_utilization": accessible_blocks / self.buffer_size * 100,
            "total_hash_computations": self.total_hash_computations,
            "window_start": self.window_start,
            "window_end": self.window_end
        }
    
    def __repr__(self) -> str:
        """String representation of the ledger."""
        stats = self.get_statistics()
        return (f"CircularLedger(size={self.buffer_size}, "
                f"blocks={stats['accessible_blocks']}, "
                f"storage={stats['storage_usage_kb']:.2f}KB)")
