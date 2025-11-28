"""
Multi-Node Ledger Amnesia Simulation.

Each IoT node:
- Maintains its own circular ledger (100 slots)
- Generates its own blocks (500 blocks each)
- Has its own sensor for data generation
- Validates blocks from other nodes
- Maintains network consensus

This demonstrates distributed consensus with multiple block producers.
"""

import sys
import os
import time
import json
import threading
from datetime import datetime
from typing import Dict, List

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import config
from src.sensor_data import IoTSensorNode
from src.network import NetworkNode
from src.block import Block
from simulation.performance_monitor import PerformanceMonitor


class IoTNodeSimulator:
    """
    Simulates a single IoT node with circular ledger.
    
    Each node:
    - Generates blocks independently
    - Validates blocks from peers
    - Maintains its own circular buffer
    """
    
    def __init__(self, node_id: str, num_blocks: int):
        """
        Initialize IoT node simulator.
        
        Args:
            node_id: Unique node identifier
            num_blocks: Number of blocks this node will generate
        """
        self.node_id = node_id
        self.num_blocks = num_blocks
        
        # Create network node with circular ledger
        # IMPORTANT: Each node gets its OWN NetworkNode instance
        self.network_node = NetworkNode(
            node_id=node_id,
            buffer_size=config.BUFFER_SIZE,
            difficulty=config.DIFFICULTY
        )
        
        print(f"[{self.node_id}] Created with ledger id: {id(self.network_node.ledger)}")
        
        # Create dedicated sensor for this node
        self.sensor = IoTSensorNode(node_id)
        
        # Create performance monitor
        self.monitor = PerformanceMonitor()
        
        # Create output files
        os.makedirs(config.RESULTS_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Block details log
        self.block_log_file = os.path.join(
            config.RESULTS_DIR, 
            f"block_details_{node_id}_{timestamp}.txt"
        )
        self.block_log = open(self.block_log_file, 'w')
        
        # Write header
        self._write_log_header(timestamp)
        
        # Statistics
        self.blocks_created = 0
        self.blocks_validated = 0
        self.blocks_rejected = 0
        self.start_time = None
        
        print(f"[{self.node_id}] Initialized - will generate {num_blocks} blocks")
    
    def _write_log_header(self, timestamp):
        """Write header to block log file."""
        self.block_log.write("="*120 + "\n")
        self.block_log.write(f" LEDGER AMNESIA - NODE {self.node_id} - DETAILED BLOCK LOG ".center(120, "=") + "\n")
        self.block_log.write("="*120 + "\n")
        self.block_log.write(f"Node ID:              {self.node_id}\n")
        self.block_log.write(f"Simulation Start:     {timestamp}\n")
        self.block_log.write(f"Buffer Size (N):      {config.BUFFER_SIZE} slots\n")
        self.block_log.write(f"Difficulty (D):       {config.DIFFICULTY} (2^{config.DIFFICULTY} = {2**config.DIFFICULTY} hashes)\n")
        self.block_log.write(f"Block Interval (Δt):  {config.BLOCK_INTERVAL} seconds\n")
        self.block_log.write(f"Target Blocks:        {self.num_blocks}\n")
        self.block_log.write("="*120 + "\n\n")
    
    def connect_to_peer(self, peer_node: 'IoTNodeSimulator'):
        """
        Connect to another node as a peer.
        
        Args:
            peer_node: Another IoT node simulator
        """
        if peer_node != self:
            self.network_node.add_peer(peer_node.network_node)
    
    def generate_and_broadcast_block(self, broadcast_enabled=True) -> Dict:
        """
        Generate a new block and optionally broadcast to network.
        
        Args:
            broadcast_enabled: Whether to broadcast to peers
        
        Returns:
            dict: Block generation statistics
        """
        # Generate sensor data
        sensor_data = self.sensor.generate_reading()
        
        # Create and mine block
        start_time = time.time()
        new_block = self.network_node.ledger.add_block(sensor_data)
        creation_time = time.time() - start_time
        
        self.blocks_created += 1
        
        # Broadcast to peers only if enabled
        propagation_time = 0
        avg_propagation = 0
        if broadcast_enabled and self.network_node.peer_nodes:
            propagation_start = time.time()
            avg_propagation = self.network_node.broadcast_block(new_block)
            propagation_time = time.time() - propagation_start
        
        # Record metrics
        self.monitor.record_block_generation(
            creation_time,
            self.network_node.ledger.total_hash_computations
        )
        
        if broadcast_enabled:
            self.monitor.record_network_propagation(
                propagation_time,
                avg_propagation
            )
        
        # Log block details
        self._log_block_details(new_block, sensor_data, creation_time, 
                               propagation_time, avg_propagation)
        
        return {
            "block_index": new_block.index,
            "creation_time": creation_time,
            "propagation_time": propagation_time,
            "hash_computations": self.network_node.ledger.total_hash_computations
        }
    
    def _log_block_details(self, block, sensor_data, creation_time, 
                          propagation_time, avg_propagation):
        """Write detailed block information to log file."""
        ledger_stats = self.network_node.ledger.get_statistics()
        slot_num = self.network_node.ledger._phi(block.index)
        
        # Determine overwritten slot
        overwritten_slot = "-"
        if ledger_stats['overwritten_blocks'] > 0:
            overwritten_index = block.index - config.BUFFER_SIZE
            if overwritten_index >= 0:
                overwrite_slot = self.network_node.ledger._phi(overwritten_index)
                overwritten_slot = f"Slot {overwrite_slot}"
        
        self.block_log.write("-" * 120 + "\n")
        self.block_log.write(f"BLOCK #{block.index}\n")
        self.block_log.write("-" * 120 + "\n")
        
        # Block metadata
        self.block_log.write(f"Timestamp:        {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(block.timestamp))}\n")
        self.block_log.write(f"Physical Slot:    {slot_num} (φ({block.index}) = {block.index} mod {config.BUFFER_SIZE})\n")
        self.block_log.write(f"Overwritten Slot: {overwritten_slot}\n")
        self.block_log.write(f"Block Hash:       {block.hash}\n")
        self.block_log.write(f"Previous Hash:    {block.prev_hash}\n")
        self.block_log.write(f"Nonce:            {block.nonce}\n")
        
        # Mining statistics
        hash_count = ledger_stats['total_hash_computations']
        self.block_log.write(f"\nMining Statistics:\n")
        self.block_log.write(f"  Hash Computations: {hash_count:,}\n")
        self.block_log.write(f"  Mining Time:       {creation_time:.4f} seconds\n")
        if creation_time > 0:
            self.block_log.write(f"  Hashes/Second:     {hash_count/creation_time:,.0f}\n")
        
        # Network propagation
        self.block_log.write(f"\nNetwork Propagation:\n")
        self.block_log.write(f"  Propagation Time:  {propagation_time:.4f} seconds\n")
        self.block_log.write(f"  Avg Delay/Node:    {avg_propagation:.2f} ms\n")
        self.block_log.write(f"  Peers Notified:    {len(self.network_node.peer_nodes)}\n")
        
        # Block Validation Status
        self.block_log.write(f"\nValidation Statistics:\n")
        self.block_log.write(f"  Blocks Created:    {self.blocks_created}\n")
        self.block_log.write(f"  Blocks Received:   {self.network_node.blocks_received}\n")
        self.block_log.write(f"  Blocks Validated:  {self.network_node.blocks_validated}\n")
        self.block_log.write(f"  Blocks Rejected:   {self.network_node.blocks_rejected}\n")
        if self.network_node.blocks_received > 0:
            success_rate = (self.network_node.blocks_validated / self.network_node.blocks_received) * 100
            self.block_log.write(f"  Validation Rate:   {success_rate:.2f}%\n")
        
        # IoT Sensor Data
        self.block_log.write(f"\nIoT Sensor Data:\n")
        self.block_log.write(f"  Node ID:           {sensor_data.get('node_id', 'N/A')}\n")
        self.block_log.write(f"  Reading ID:        {sensor_data.get('reading_id', 'N/A')}\n")
        self.block_log.write(f"  Temperature:       {sensor_data.get('temperature', 0):.2f} °C\n")
        self.block_log.write(f"  Humidity:          {sensor_data.get('humidity', 0):.2f} %\n")
        self.block_log.write(f"  CO2 Level:         {sensor_data.get('co2', 0)} ppm\n")
        self.block_log.write(f"  Battery Level:     {sensor_data.get('battery_level', 0):.2f} %\n")
        self.block_log.write(f"  Signal Strength:   {sensor_data.get('signal_strength', 0)} dBm\n")
        
        # Ledger state
        self.block_log.write(f"\nLedger State:\n")
        self.block_log.write(f"  Total Blocks Created:  {ledger_stats['total_blocks_created']}\n")
        self.block_log.write(f"  Accessible Blocks:     {ledger_stats['accessible_blocks']}\n")
        self.block_log.write(f"  Overwritten Blocks:    {ledger_stats['overwritten_blocks']}\n")
        self.block_log.write(f"  Storage Usage:         {ledger_stats['storage_usage_kb']:.2f} KB\n")
        self.block_log.write(f"  Retention Window:      [{ledger_stats['window_start']}, {ledger_stats['window_end']}]\n")
        
        self.block_log.write("\n")
        self.block_log.flush()
    
    def run_simulation(self, broadcast_enabled=True):
        """
        Run the block generation simulation for this node.
        
        Args:
            broadcast_enabled: Whether to broadcast blocks to peers
        """
        self.start_time = time.time()
        
        # Verify starting state
        print(f"\n[{self.node_id}] Starting block generation...")
        print(f"[{self.node_id}] Initial ledger state:")
        print(f"[{self.node_id}]   Last index: {self.network_node.ledger.last_index}")
        
        # Safe genesis check
        genesis = self.network_node.ledger.get_block(0)
        if genesis is None:
            print(f"[{self.node_id}]   ERROR: Genesis block is None!")
            print(f"[{self.node_id}]   Storage slot 0: {self.network_node.ledger.storage[0]}")
            raise RuntimeError(f"{self.node_id}: Genesis block is missing!")
        
        print(f"[{self.node_id}]   Genesis hash: {genesis.hash[:16]}...")
        
        # Verify we're starting from genesis
        if self.network_node.ledger.last_index != 0:
            print(f"[{self.node_id}]   WARNING: last_index is {self.network_node.ledger.last_index}, expected 0!")
            print(f"[{self.node_id}]   Attempting to reset...")
            self.network_node.ledger.last_index = 0
            self.network_node.ledger.window_start = 0
            self.network_node.ledger.window_end = 0
        
        print(f"[{self.node_id}] Target: {self.num_blocks} blocks")
        if not broadcast_enabled:
            print(f"[{self.node_id}] Mode: Independent (no peer interaction)")
        
        # IMPORTANT: Temporarily disconnect from peers during independent simulation
        # This prevents rejection messages that are irrelevant for Option 1
        original_peers = self.network_node.peer_nodes.copy() if not broadcast_enabled else []
        if not broadcast_enabled:
            self.network_node.peer_nodes = []  # Disconnect from peers
            print(f"[{self.node_id}] Peers temporarily disconnected for independent simulation")
        
        for block_num in range(self.num_blocks):
            # Generate and optionally broadcast block
            result = self.generate_and_broadcast_block(broadcast_enabled)
            
            # Record system resources periodically (every 10 blocks)
            if block_num % config.MONITORING_INTERVAL == 0:
                self.monitor.record_system_resources()
            
            # Display ALL blocks in terminal
            ledger_stats = self.network_node.ledger.get_statistics()
            slot_num = self.network_node.ledger._phi(result['block_index'])
            
            # Determine overwritten slot for display
            overwrite_display = "  -"
            if ledger_stats['overwritten_blocks'] > 0:
                overwritten_index = result['block_index'] - config.BUFFER_SIZE
                if overwritten_index >= 0:
                    overwrite_slot = self.network_node.ledger._phi(overwritten_index)
                    overwrite_display = f"Slot {overwrite_slot:3d}"
            
            # Calculate progress
            elapsed = time.time() - self.start_time
            blocks_per_sec = (block_num + 1) / elapsed if elapsed > 0 else 0
            eta = (self.num_blocks - block_num - 1) / blocks_per_sec if blocks_per_sec > 0 else 0
            
            # Print EVERY block with detailed information
            print(f"[{self.node_id}] Block {block_num+1:3d}/{self.num_blocks} | "
                  f"Index: {result['block_index']:3d} | "
                  f"Slot: {slot_num:3d} | "
                  f"Storage: {ledger_stats['storage_usage_kb']:6.2f} KB | "
                  f"Overwrites: {overwrite_display} | "
                  f"Hash Ops: {result['hash_computations']:6d} | "
                  f"Time: {result['creation_time']:5.3f}s | "
                  f"ETA: {eta:6.1f}s")
            
            # Record storage utilization
            ledger_stats = self.network_node.ledger.get_statistics()
            self.monitor.record_storage_utilization(
                ledger_stats['storage_usage_bytes'],
                ledger_stats['accessible_blocks']
            )
            
            # Wait for block interval
            time.sleep(config.BLOCK_INTERVAL)
        
        # Restore peer connections after simulation
        if not broadcast_enabled and original_peers:
            self.network_node.peer_nodes = original_peers
            print(f"[{self.node_id}] Peer connections restored")
        
        total_time = time.time() - self.start_time
        print(f"[{self.node_id}] Completed in {total_time:.2f} seconds")
    
    def export_results(self):
        """Export all results to files."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Close block log
        if self.block_log:
            self.block_log.write("\n" + "="*120 + "\n")
            self.block_log.write(" END OF BLOCK LOG ".center(120, "=") + "\n")
            self.block_log.write("="*120 + "\n")
            self.block_log.close()
        
        # Export performance metrics
        metrics_file = os.path.join(
            config.RESULTS_DIR, 
            f"metrics_{self.node_id}_{timestamp}.json"
        )
        self.monitor.export_metrics(metrics_file)
        
        # Export node statistics
        node_stats = self.network_node.get_statistics()
        node_stats['simulation_summary'] = {
            'total_time_seconds': time.time() - self.start_time if self.start_time else 0,
            'target_blocks': self.num_blocks,
            'blocks_created': self.blocks_created,
            'average_time_per_block': (time.time() - self.start_time) / self.blocks_created if self.blocks_created > 0 else 0
        }
        
        node_file = os.path.join(
            config.RESULTS_DIR,
            f"node_{self.node_id}_{timestamp}.json"
        )
        with open(node_file, 'w') as f:
            json.dump(node_stats, f, indent=2)
        
        print(f"[{self.node_id}] Results exported:")
        print(f"  - {os.path.basename(self.block_log_file)}")
        print(f"  - {os.path.basename(metrics_file)}")
        print(f"  - {os.path.basename(node_file)}")


class MultiNodeSimulation:
    """
    Coordinates multiple IoT nodes in a distributed simulation.
    """
    
    def __init__(self, num_nodes: int = config.NUM_NODES, 
                 blocks_per_node: int = config.SIMULATION_BLOCKS):
        """
        Initialize multi-node simulation.
        
        Args:
            num_nodes: Number of IoT nodes
            blocks_per_node: Number of blocks each node will generate
        """
        self.num_nodes = num_nodes
        self.blocks_per_node = blocks_per_node
        
        # Create IoT node simulators
        self.nodes: List[IoTNodeSimulator] = []
        for i in range(num_nodes):
            node_id = f"NODE-{i+1:02d}"
            node = IoTNodeSimulator(node_id, blocks_per_node)
            self.nodes.append(node)
        
        # Connect nodes in mesh topology
        self._setup_mesh_network()
        
        # Synchronize genesis blocks
        self._synchronize_genesis_blocks()
        
        print(f"\nNetwork initialized:")
        print(f"  Nodes: {num_nodes}")
        print(f"  Topology: Full mesh")
        print(f"  Blocks per node: {blocks_per_node}")
        print(f"  Total blocks: {num_nodes * blocks_per_node}")
    
    def _setup_mesh_network(self):
        """Connect all nodes to each other (full mesh)."""
        print("\nSetting up mesh network topology...")
        for node in self.nodes:
            for peer in self.nodes:
                if node != peer:
                    node.connect_to_peer(peer)
        print(f"Each node connected to {self.num_nodes - 1} peers")
    
    def _synchronize_genesis_blocks(self):
        """Ensure all nodes start with the same genesis block."""
        print("Synchronizing genesis blocks across all nodes...")
        
        if not self.nodes:
            return
        
        # Use genesis from first node as reference
        reference_genesis = self.nodes[0].network_node.ledger.get_block(0)
        
        # Copy to all other nodes
        for node in self.nodes[1:]:
            node.network_node.ledger.storage[0] = reference_genesis
            node.network_node.ledger.last_index = 0
            node.network_node.ledger.window_start = 0
            node.network_node.ledger.window_end = 0
        
        print("✓ All nodes synchronized with same genesis block")
    
    def run(self):
        """Run the multi-node simulation."""
        print("\n" + "="*80)
        print(" MULTI-NODE LEDGER AMNESIA SIMULATION ".center(80, "="))
        print("="*80)
        print()
        
        start_time = time.time()
        
        # IMPORTANT: Each node needs to start fresh with NO blocks from peers
        # We need to disconnect peers during individual simulation, 
        # or accept blocks from peers during simulation
        
        print("Simulation Mode: Independent node simulations")
        print("Each node demonstrates circular buffer behavior independently")
        print("Broadcasting to peers is DISABLED to avoid validation conflicts")
        print()
        
        # Run each node's simulation in sequence WITHOUT broadcasting
        # Each node will create blocks independently to demonstrate circular buffer
        for node in self.nodes:
            # Before this node starts, reset its ledger to genesis
            print(f"\n{'='*80}")
            print(f"Resetting {node.node_id} to genesis before its simulation")
            print(f"{'='*80}")
            
            # Get the genesis block
            genesis = node.network_node.ledger.get_block(0)
            
            # Clear ALL slots
            for i in range(node.network_node.ledger.buffer_size):
                node.network_node.ledger.storage[i] = None
            
            # Re-insert genesis at slot 0
            node.network_node.ledger.storage[0] = genesis
            
            # Reset ledger state to genesis
            node.network_node.ledger.last_index = 0
            node.network_node.ledger.window_start = 0
            node.network_node.ledger.window_end = 0
            node.network_node.ledger.total_hash_computations = 0
            node.network_node.ledger.overwrite_count = 0
            
            # Reset node statistics
            node.network_node.blocks_received = 0
            node.network_node.blocks_validated = 0
            node.network_node.blocks_rejected = 0
            
            print(f"✓ {node.node_id} reset to genesis (index=0)")
            print()
            
            # Run this node's simulation WITHOUT broadcasting
            # This prevents validation conflicts
            node.run_simulation(broadcast_enabled=False)
        
        total_time = time.time() - start_time
        
        print("\n" + "="*80)
        print(" SIMULATION COMPLETE ".center(80, "="))
        print("="*80)
        print(f"\nTotal simulation time: {total_time:.2f} seconds")
        print(f"Total blocks generated: {self.num_nodes * self.blocks_per_node}")
        print()
        
        # Verify network consensus
        self._verify_consensus()
        
        # Print summary statistics
        self._print_summary()
        
        # Export all results
        self._export_all_results()
    
    def _verify_consensus(self):
        """Verify that all nodes maintain consensus."""
        print("-"*80)
        print("NETWORK CONSENSUS VERIFICATION")
        print("-"*80)
        
        # Check if all nodes have the same chain length
        chain_lengths = [node.network_node.ledger.last_index for node in self.nodes]
        
        print(f"\nChain lengths:")
        for node in self.nodes:
            ledger_index = node.network_node.ledger.last_index
            print(f"  {node.node_id}: {ledger_index} blocks")
        
        # Verify each node's validation statistics
        print(f"\nValidation Statistics:")
        for node in self.nodes:
            total_received = node.network_node.blocks_received
            validated = node.network_node.blocks_validated
            rejected = node.network_node.blocks_rejected
            rate = (validated / total_received * 100) if total_received > 0 else 0
            
            print(f"  {node.node_id}: Received={total_received}, "
                  f"Validated={validated}, Rejected={rejected}, "
                  f"Rate={rate:.2f}%")
        
        # Check storage consistency
        print(f"\nStorage Usage:")
        for node in self.nodes:
            stats = node.network_node.ledger.get_statistics()
            print(f"  {node.node_id}: {stats['storage_usage_kb']:.2f} KB "
                  f"(Accessible: {stats['accessible_blocks']}, "
                  f"Overwritten: {stats['overwritten_blocks']})")
        
        print()
    
    def _print_summary(self):
        """Print comprehensive summary."""
        print("-"*80)
        print("SIMULATION SUMMARY")
        print("-"*80)
        
        for node in self.nodes:
            print(f"\n{node.node_id}:")
            summary = node.monitor.get_summary_statistics()
            
            print(f"  Blocks Created: {node.blocks_created}")
            print(f"  Avg Mining Time: {summary['block_generation']['average_time_seconds']:.4f}s")
            print(f"  Avg Hash Computations: {summary['block_generation']['average_hash_computations']:.0f}")
            print(f"  Storage: {summary['storage']['final_kb']:.2f} KB (Constant: {summary['storage']['is_constant']})")
            print(f"  Validation Rate: {(node.network_node.blocks_validated / node.network_node.blocks_received * 100) if node.network_node.blocks_received > 0 else 0:.2f}%")
        
        print()
    
    def _export_all_results(self):
        """Export results from all nodes."""
        print("-"*80)
        print("EXPORTING RESULTS")
        print("-"*80)
        print()
        
        for node in self.nodes:
            node.export_results()
            print()
        
        # Create summary file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        summary_file = os.path.join(
            config.RESULTS_DIR,
            f"simulation_summary_{timestamp}.json"
        )
        
        summary = {
            "simulation_config": {
                "num_nodes": self.num_nodes,
                "blocks_per_node": self.blocks_per_node,
                "buffer_size": config.BUFFER_SIZE,
                "difficulty": config.DIFFICULTY,
                "block_interval": config.BLOCK_INTERVAL
            },
            "nodes": []
        }
        
        for node in self.nodes:
            node_summary = {
                "node_id": node.node_id,
                "blocks_created": node.blocks_created,
                "blocks_received": node.network_node.blocks_received,
                "blocks_validated": node.network_node.blocks_validated,
                "blocks_rejected": node.network_node.blocks_rejected,
                "storage_kb": node.network_node.ledger.get_statistics()['storage_usage_kb']
            }
            summary["nodes"].append(node_summary)
        
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"Summary file: {os.path.basename(summary_file)}")
        print()


def main():
    """Main entry point."""
    print("="*80)
    print(" LEDGER AMNESIA - MULTI-NODE IoT SIMULATION ".center(80, "="))
    print("="*80)
    print()
    print("Configuration:")
    print(f"  Number of IoT Nodes: {config.NUM_NODES}")
    print(f"  Blocks per Node: {config.SIMULATION_BLOCKS}")
    print(f"  Buffer Size: {config.BUFFER_SIZE} slots")
    print(f"  Difficulty: {config.DIFFICULTY} (2^{config.DIFFICULTY} = {2**config.DIFFICULTY} hashes)")
    print(f"  Block Interval: {config.BLOCK_INTERVAL} seconds")
    print()
    
    # Parse command line arguments
    num_nodes = config.NUM_NODES
    blocks_per_node = config.SIMULATION_BLOCKS
    
    if len(sys.argv) > 1:
        try:
            blocks_per_node = int(sys.argv[1])
        except ValueError:
            print(f"Invalid blocks per node: {sys.argv[1]}")
    
    if len(sys.argv) > 2:
        try:
            num_nodes = int(sys.argv[2])
        except ValueError:
            print(f"Invalid number of nodes: {sys.argv[2]}")
    
    # Create and run simulation
    simulation = MultiNodeSimulation(num_nodes, blocks_per_node)
    
    try:
        simulation.run()
    except KeyboardInterrupt:
        print("\n\nSimulation interrupted by user.")
        print("Saving partial results...")
        for node in simulation.nodes:
            if hasattr(node, 'block_log') and node.block_log:
                node.block_log.close()
            node.export_results()
    except Exception as e:
        print(f"\n\nError during simulation: {e}")
        import traceback
        traceback.print_exc()
    
    print("Simulation finished.")


if __name__ == "__main__":
    main()
