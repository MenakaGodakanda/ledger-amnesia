"""
Network simulation for distributed ledger.

Simulates multi-node network with:
- Block propagation delays
- Node synchronization
- Network consensus
- Genesis block synchronization (CRITICAL FIX)
"""

import time
import random
import threading
from typing import List, Dict, Any, Optional
from src.block import Block
from src.circular_ledger import CircularLedger
import config


class NetworkNode:
    """
    Represents a single node in the distributed network.
    
    Each node maintains its own circular ledger and participates
    in block propagation and validation.
    """
    
    def __init__(self, node_id: str, buffer_size: int, difficulty: int):
        """
        Initialize network node.
        
        Args:
            node_id: Unique node identifier
            buffer_size: Circular buffer size N
            difficulty: Proof-of-work difficulty D
        """
        self.node_id = node_id
        self.ledger = CircularLedger(buffer_size, difficulty)
        self.peer_nodes: List['NetworkNode'] = []
        
        # Network statistics
        self.blocks_received = 0
        self.blocks_validated = 0
        self.blocks_rejected = 0
        self.total_propagation_time = 0.0
        
        # Synchronization state
        self.is_synchronized = True
        self.sync_lock = threading.Lock()
    
    def add_peer(self, peer: 'NetworkNode'):
        """
        Add a peer node to this node's network.
        
        Args:
            peer: Peer node to add
        """
        if peer not in self.peer_nodes and peer != self:
            self.peer_nodes.append(peer)
    
    def broadcast_block(self, block: Block) -> float:
        """
        Broadcast a block to all peer nodes.
        
        Simulates network propagation with realistic delays.
        
        Args:
            block: Block to broadcast
        
        Returns:
            float: Average propagation time in milliseconds
        """
        if not self.peer_nodes:
            return 0.0
        
        total_delay = 0.0
        successful_broadcasts = 0
        
        for peer in self.peer_nodes:
            # Simulate network propagation delay
            delay_ms = random.uniform(
                config.MIN_PROPAGATION_DELAY,
                config.MAX_PROPAGATION_DELAY
            )
            time.sleep(delay_ms / 1000.0)  # Convert to seconds
            
            # Send block to peer
            if peer.receive_block(block, self.node_id):
                total_delay += delay_ms
                successful_broadcasts += 1
        
        avg_delay = total_delay / successful_broadcasts if successful_broadcasts > 0 else 0
        return avg_delay
    
    def receive_block(self, block: Block, sender_id: str) -> bool:
        """
        Receive and validate a block from a peer.
        
        Args:
            block: Received block
            sender_id: ID of sending node
        
        Returns:
            bool: True if block accepted, False if rejected
        """
        with self.sync_lock:
            self.blocks_received += 1
            
            # Validate the block
            is_valid, error_msg = self.ledger.validate_block(block, time.time())
            
            if is_valid:
                # Accept block and add to ledger
                self.ledger._insert_block(block)
                self.blocks_validated += 1
                return True
            else:
                # Reject invalid block
                self.blocks_rejected += 1
                print(f"[{self.node_id}] Rejected block from {sender_id}: {error_msg}")
                return False
    
    def synchronize_with_peers(self) -> Dict[str, Any]:
        """
        Synchronize ledger with peer nodes.
        
        Implements Algorithm 3: Node Synchronization from Section IV.D
        
        Returns:
            dict: Synchronization statistics
        """
        if not self.peer_nodes:
            return {"status": "no_peers", "blocks_synced": 0}
        
        start_time = time.time()
        
        with self.sync_lock:
            # Find peer with highest block index
            max_peer_index = max(
                peer.ledger.last_index for peer in self.peer_nodes
            )
            
            # Calculate window start
            window_start = max(0, max_peer_index - self.ledger.buffer_size + 1)
            
            # Download missing blocks
            blocks_synced = 0
            for i in range(window_start, max_peer_index + 1):
                if not self.ledger.get_block(i):
                    # Request block from random peer
                    block = self._request_block_from_peers(i)
                    if block:
                        self.ledger._insert_block(block)
                        blocks_synced += 1
            
            self.is_synchronized = True
        
        sync_time = time.time() - start_time
        
        return {
            "status": "synchronized",
            "blocks_synced": blocks_synced,
            "sync_time_seconds": sync_time,
            "final_index": self.ledger.last_index
        }
    
    def _request_block_from_peers(self, index: int) -> Optional[Block]:
        """
        Request a specific block from peers.
        
        Args:
            index: Block index to request
        
        Returns:
            Block if found, None otherwise
        """
        # Try random peer
        if self.peer_nodes:
            peer = random.choice(self.peer_nodes)
            return peer.ledger.get_block(index)
        return None
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get node statistics.
        
        Returns:
            dict: Comprehensive node statistics
        """
        ledger_stats = self.ledger.get_statistics()
        
        return {
            "node_id": self.node_id,
            "is_synchronized": self.is_synchronized,
            "blocks_received": self.blocks_received,
            "blocks_validated": self.blocks_validated,
            "blocks_rejected": self.blocks_rejected,
            "peer_count": len(self.peer_nodes),
            "ledger_stats": ledger_stats
        }
    
    def __repr__(self) -> str:
        """String representation of node."""
        return f"NetworkNode(id={self.node_id}, peers={len(self.peer_nodes)})"


class BlockchainNetwork:
    """
    Manages a network of nodes with distributed ledger.
    
    Coordinates block creation, propagation, and consensus across multiple nodes.
    """
    
    def __init__(self, num_nodes: int, buffer_size: int, difficulty: int):
        """
        Initialize blockchain network.
        
        Args:
            num_nodes: Number of nodes in the network
            buffer_size: Circular buffer size N for each node
            difficulty: Proof-of-work difficulty D
        """
        self.num_nodes = num_nodes
        self.buffer_size = buffer_size
        self.difficulty = difficulty
        
        # Create nodes
        self.nodes: List[NetworkNode] = []
        for i in range(num_nodes):
            node_id = f"NODE-{i+1:02d}"
            node = NetworkNode(node_id, buffer_size, difficulty)
            self.nodes.append(node)
        
        # Connect nodes in mesh topology
        self._setup_mesh_network()
        
        # CRITICAL FIX: Synchronize all nodes to share the same genesis block
        self._synchronize_genesis_block()
        
        # Network-wide statistics
        self.total_blocks_created = 0
        self.total_propagation_times = []
    
    def _setup_mesh_network(self):
        """
        Set up full mesh network topology.
        
        Each node connects to all other nodes.
        """
        for node in self.nodes:
            for peer in self.nodes:
                if node != peer:
                    node.add_peer(peer)
    
    def _synchronize_genesis_block(self):
        """
        Ensure all nodes share the same genesis block.
        
        This is CRITICAL for network consensus. All nodes must start
        with the identical genesis block, otherwise they will reject
        each other's blocks due to chain mismatch.
        """
        if not self.nodes:
            return
        
        # Use the genesis block from the first node as the reference
        reference_node = self.nodes[0]
        genesis_block = reference_node.ledger.get_block(0)
        
        if not genesis_block:
            return
        
        # Copy this genesis block to all other nodes
        for node in self.nodes[1:]:
            # Replace their genesis block with the reference
            node.ledger.storage[0] = genesis_block
            node.ledger.last_index = 0
            node.ledger.window_start = 0
            node.ledger.window_end = 0
    
    def create_and_propagate_block(self, data: Dict[str, Any], 
                                   originating_node_index: int = 0) -> Dict[str, Any]:
        """
        Create a new block at one node and propagate to network.
        
        Args:
            data: Block payload data
            originating_node_index: Index of node that creates the block
        
        Returns:
            dict: Block creation and propagation statistics
        """
        start_time = time.time()
        
        # Create block at originating node
        originating_node = self.nodes[originating_node_index]
        new_block = originating_node.ledger.add_block(data)
        
        creation_time = time.time() - start_time
        
        # Broadcast to network
        propagation_start = time.time()
        avg_propagation = originating_node.broadcast_block(new_block)
        total_propagation = time.time() - propagation_start
        
        self.total_blocks_created += 1
        self.total_propagation_times.append(total_propagation)
        
        return {
            "block_index": new_block.index,
            "creation_time_seconds": creation_time,
            "avg_propagation_delay_ms": avg_propagation,
            "total_propagation_time_seconds": total_propagation,
            "hash_computations": originating_node.ledger.total_hash_computations
        }
    
    def verify_network_consensus(self) -> Dict[str, Any]:
        """
        Verify that all nodes have consensus on the blockchain state.
        
        Returns:
            dict: Consensus verification results
        """
        if not self.nodes:
            return {"consensus": False, "reason": "No nodes"}
        
        # Get last block from first node
        reference_block = self.nodes[0].ledger.get_last_block()
        
        if not reference_block:
            return {"consensus": True, "reason": "Empty ledgers"}
        
        # Check all nodes have same last block
        consensus = True
        mismatched_nodes = []
        
        for node in self.nodes[1:]:
            node_block = node.ledger.get_last_block()
            if not node_block or node_block.hash != reference_block.hash:
                consensus = False
                mismatched_nodes.append(node.node_id)
        
        return {
            "consensus": consensus,
            "reference_index": reference_block.index,
            "reference_hash": reference_block.hash[:16] + "...",
            "mismatched_nodes": mismatched_nodes,
            "total_nodes": len(self.nodes)
        }
    
    def get_network_statistics(self) -> Dict[str, Any]:
        """
        Get comprehensive network statistics.
        
        Returns:
            dict: Network-wide statistics
        """
        node_stats = [node.get_statistics() for node in self.nodes]
        
        avg_propagation = (sum(self.total_propagation_times) / 
                          len(self.total_propagation_times) 
                          if self.total_propagation_times else 0)
        
        return {
            "num_nodes": self.num_nodes,
            "total_blocks_created": self.total_blocks_created,
            "avg_propagation_time_seconds": avg_propagation,
            "consensus_status": self.verify_network_consensus(),
            "node_statistics": node_stats
        }
    
    def __repr__(self) -> str:
        """String representation of network."""
        return (f"BlockchainNetwork(nodes={self.num_nodes}, "
                f"blocks={self.total_blocks_created})")
