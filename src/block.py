"""
Block structure implementation for Ledger Amnesia.

Based on Section III.C of the research paper:
- index: Logical block number (4 bytes)
- timestamp: Block creation time (4 bytes, UNIX epoch)
- data: Application payload (variable, typically 32-256 bytes)
- prev_hash: Hash of previous block (32 bytes)
- nonce: Proof-of-work value (4 bytes)
- hash: Block's own hash (32 bytes)
"""

import hashlib
import json
import time
from typing import Dict, Any, Optional


class Block:
    """
    Represents a single block in the Ledger Amnesia circular blockchain.
    
    Attributes:
        index (int): Logical block number
        timestamp (float): Block creation time (UNIX epoch)
        data (dict): Application payload (sensor readings)
        prev_hash (str): SHA-256 hash of previous block
        nonce (int): Proof-of-work nonce value
        hash (str): SHA-256 hash of this block
    """
    
    def __init__(self, index: int, data: Dict[str, Any], 
                 prev_hash: str = "0" * 64, timestamp: Optional[float] = None):
        """
        Initialize a new block.
        
        Args:
            index: Logical block number (starting from 0)
            data: Dictionary containing sensor data or application payload
            prev_hash: Hash of previous block (genesis block uses zeros)
            timestamp: Block creation time (defaults to current time)
        """
        self.index = index
        self.timestamp = timestamp if timestamp is not None else time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0
        self.hash = ""
    
    def calculate_hash(self) -> str:
        """
        Calculate SHA-256 hash of the block.
        
        Implements the hash function from the paper:
        H(Bi) = SHA-256(index || timestamp || data || prev_hash || nonce)
        
        Returns:
            str: Hexadecimal representation of the block hash
        """
        # Concatenate block components
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "prev_hash": self.prev_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        
        # Compute SHA-256 hash
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty: int) -> int:
        """
        Mine the block using proof-of-work consensus.
        
        Implements Algorithm from Section IV.A:
        Find nonce such that H(Bi) < 2^(256-D)
        
        Args:
            difficulty: Difficulty level D (number of leading bits to check)
        
        Returns:
            int: Number of hash computations performed
        """
        target = 2 ** (256 - difficulty)
        hash_count = 0
        
        while True:
            self.hash = self.calculate_hash()
            hash_count += 1
            
            # Convert hex hash to integer for comparison
            hash_int = int(self.hash, 16)
            
            if hash_int < target:
                # Valid proof-of-work found
                return hash_count
            
            # Increment nonce and try again
            self.nonce += 1
    
    def is_valid(self, difficulty: int, prev_block: Optional['Block'] = None) -> bool:
        """
        Validate the block according to consensus rules.
        
        Implements validation checks from Algorithm 1 (Section IV.B):
        1. Index continuity
        2. Chain continuity (prev_hash verification)
        3. Proof-of-work verification
        4. Temporal validity
        
        Args:
            difficulty: Required difficulty level
            prev_block: Previous block in the chain (None for genesis)
        
        Returns:
            bool: True if block is valid, False otherwise
        """
        # Check 1: Hash integrity
        calculated_hash = self.calculate_hash()
        if self.hash != calculated_hash:
            return False
        
        # Check 2: Proof-of-work verification
        target = 2 ** (256 - difficulty)
        hash_int = int(self.hash, 16)
        if hash_int >= target:
            return False
        
        # Check 3: Chain continuity (if previous block exists)
        if prev_block is not None:
            if self.index != prev_block.index + 1:
                return False
            if self.prev_hash != prev_block.hash:
                return False
        
        return True
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert block to dictionary format.
        
        Returns:
            dict: Block data in dictionary format
        """
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "prev_hash": self.prev_hash,
            "nonce": self.nonce,
            "hash": self.hash
        }
    
    def get_size(self) -> int:
        """
        Calculate approximate block size in bytes.
        
        Based on paper specifications:
        - index: 4 bytes
        - timestamp: 4 bytes
        - data: variable (320 bytes in simulation)
        - prev_hash: 32 bytes
        - nonce: 4 bytes
        - hash: 32 bytes
        
        Returns:
            int: Block size in bytes
        """
        block_json = json.dumps(self.to_dict())
        return len(block_json.encode('utf-8'))
    
    def __repr__(self) -> str:
        """String representation of the block."""
        return (f"Block(index={self.index}, "
                f"timestamp={self.timestamp:.2f}, "
                f"hash={self.hash[:16]}..., "
                f"nonce={self.nonce})")
    
    @staticmethod
    def create_genesis_block() -> 'Block':
        """
        Create the genesis block (first block in the chain).
        
        Returns:
            Block: Genesis block with index 0
        """
        genesis_data = {
            "message": "Genesis Block - Ledger Amnesia",
            "temperature": 0.0,
            "humidity": 0.0,
            "co2": 0
        }
        genesis = Block(0, genesis_data, "0" * 64)
        genesis.hash = genesis.calculate_hash()
        return genesis
