"""
Performance monitoring and metrics collection.

Tracks all performance metrics mentioned in the research paper:
- Storage utilization
- Block generation time
- Block validation time
- Network propagation
- Memory usage (RAM)
- CPU utilization
- Synchronization time
"""

import time
import psutil
import os
from typing import Dict, List, Any
from collections import defaultdict
import json


class PerformanceMonitor:
    """
    Monitors and records system performance metrics during simulation.
    
    Collects metrics specified in the Implementation section of the paper.
    """
    
    def __init__(self):
        """Initialize performance monitor."""
        self.metrics = defaultdict(list)
        self.start_time = time.time()
        
        # Get process handle for monitoring
        self.process = psutil.Process(os.getpid())
        
        # Baseline measurements
        self.baseline_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.baseline_cpu = self.process.cpu_percent(interval=0.1)
    
    def record_block_generation(self, duration: float, hash_count: int):
        """
        Record block generation metrics.
        
        Args:
            duration: Time taken to generate block (seconds)
            hash_count: Number of hash computations performed
        """
        self.metrics['block_generation_time'].append(duration)
        self.metrics['hash_computations'].append(hash_count)
    
    def record_block_validation(self, duration: float, is_valid: bool):
        """
        Record block validation metrics.
        
        Args:
            duration: Time taken to validate block (seconds)
            is_valid: Whether block passed validation
        """
        self.metrics['block_validation_time'].append(duration)
        self.metrics['validation_results'].append(is_valid)
    
    def record_network_propagation(self, duration: float, avg_delay_ms: float):
        """
        Record network propagation metrics.
        
        Args:
            duration: Total propagation time (seconds)
            avg_delay_ms: Average per-node delay (milliseconds)
        """
        self.metrics['network_propagation_time'].append(duration)
        self.metrics['avg_propagation_delay_ms'].append(avg_delay_ms)
    
    def record_storage_utilization(self, bytes_used: int, block_count: int):
        """
        Record storage utilization metrics.
        
        Critical for validating O(N) complexity claim.
        
        Args:
            bytes_used: Total storage in bytes
            block_count: Number of blocks in storage
        """
        self.metrics['storage_bytes'].append(bytes_used)
        self.metrics['storage_kb'].append(bytes_used / 1024)
        self.metrics['block_count'].append(block_count)
        self.metrics['timestamp'].append(time.time() - self.start_time)
    
    def record_system_resources(self):
        """
        Record current system resource usage (CPU and RAM).
        """
        # Memory usage
        mem_info = self.process.memory_info()
        memory_mb = mem_info.rss / 1024 / 1024
        self.metrics['memory_usage_mb'].append(memory_mb)
        
        # CPU usage (percentage)
        cpu_percent = self.process.cpu_percent(interval=0.1)
        self.metrics['cpu_usage_percent'].append(cpu_percent)
    
    def record_synchronization(self, duration: float, blocks_synced: int):
        """
        Record node synchronization metrics.
        
        Args:
            duration: Time taken to synchronize (seconds)
            blocks_synced: Number of blocks synchronized
        """
        self.metrics['sync_time'].append(duration)
        self.metrics['blocks_synced'].append(blocks_synced)
    
    def get_summary_statistics(self) -> Dict[str, Any]:
        """
        Calculate summary statistics for all metrics.
        
        Returns:
            dict: Comprehensive performance summary
        """
        def safe_avg(values):
            return sum(values) / len(values) if values else 0
        
        def safe_min(values):
            return min(values) if values else 0
        
        def safe_max(values):
            return max(values) if values else 0
        
        summary = {
            "simulation_duration_seconds": time.time() - self.start_time,
            
            # Storage metrics (CRITICAL for paper validation)
            "storage": {
                "average_kb": safe_avg(self.metrics['storage_kb']),
                "min_kb": safe_min(self.metrics['storage_kb']),
                "max_kb": safe_max(self.metrics['storage_kb']),
                "final_kb": self.metrics['storage_kb'][-1] if self.metrics['storage_kb'] else 0,
                "is_constant": self._check_storage_constant(),
                "samples": len(self.metrics['storage_kb'])
            },
            
            # Block generation metrics
            "block_generation": {
                "average_time_seconds": safe_avg(self.metrics['block_generation_time']),
                "min_time_seconds": safe_min(self.metrics['block_generation_time']),
                "max_time_seconds": safe_max(self.metrics['block_generation_time']),
                "average_hash_computations": safe_avg(self.metrics['hash_computations']),
                "total_blocks": len(self.metrics['block_generation_time'])
            },
            
            # Block validation metrics
            "block_validation": {
                "average_time_seconds": safe_avg(self.metrics['block_validation_time']),
                "min_time_seconds": safe_min(self.metrics['block_validation_time']),
                "max_time_seconds": safe_max(self.metrics['block_validation_time']),
                "success_rate": self._calculate_success_rate(),
                "total_validations": len(self.metrics['block_validation_time'])
            },
            
            # Network propagation metrics
            "network_propagation": {
                "average_time_seconds": safe_avg(self.metrics['network_propagation_time']),
                "average_delay_ms": safe_avg(self.metrics['avg_propagation_delay_ms']),
                "min_delay_ms": safe_min(self.metrics['avg_propagation_delay_ms']),
                "max_delay_ms": safe_max(self.metrics['avg_propagation_delay_ms'])
            },
            
            # System resource metrics
            "system_resources": {
                "average_memory_mb": safe_avg(self.metrics['memory_usage_mb']),
                "peak_memory_mb": safe_max(self.metrics['memory_usage_mb']),
                "baseline_memory_mb": self.baseline_memory,
                "average_cpu_percent": safe_avg(self.metrics['cpu_usage_percent']),
                "peak_cpu_percent": safe_max(self.metrics['cpu_usage_percent'])
            },
            
            # Synchronization metrics
            "synchronization": {
                "average_time_seconds": safe_avg(self.metrics['sync_time']),
                "total_syncs": len(self.metrics['sync_time']),
                "average_blocks_synced": safe_avg(self.metrics['blocks_synced'])
            }
        }
        
        return summary
    
    def _check_storage_constant(self) -> bool:
        """
        Check if storage remains constant (validates O(N) complexity).
        
        Returns:
            bool: True if storage is constant within tolerance
        """
        if len(self.metrics['storage_kb']) < 2:
            return True
        
        # After initial fill, storage should remain constant
        # Check last 50% of measurements
        midpoint = len(self.metrics['storage_kb']) // 2
        recent_storage = self.metrics['storage_kb'][midpoint:]
        
        if not recent_storage:
            return True
        
        avg = sum(recent_storage) / len(recent_storage)
        max_deviation = max(abs(s - avg) for s in recent_storage)
        
        # Allow 5% deviation to account for JSON encoding variations
        tolerance = avg * 0.05
        return max_deviation <= tolerance
    
    def _calculate_success_rate(self) -> float:
        """
        Calculate validation success rate.
        
        Returns:
            float: Percentage of successful validations
        """
        if not self.metrics['validation_results']:
            return 0.0
        
        successful = sum(1 for r in self.metrics['validation_results'] if r)
        total = len(self.metrics['validation_results'])
        return (successful / total) * 100
    
    def export_metrics(self, filename: str):
        """
        Export all metrics to JSON file.
        
        Args:
            filename: Output file path
        """
        export_data = {
            "summary": self.get_summary_statistics(),
            "raw_metrics": dict(self.metrics)
        }
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        print(f"Metrics exported to {filename}")
    
    def print_summary(self):
        """
        Print formatted summary of performance metrics.
        """
        summary = self.get_summary_statistics()
        
        print("\n" + "="*70)
        print(" PERFORMANCE METRICS SUMMARY ".center(70, "="))
        print("="*70)
        
        print(f"\nSimulation Duration: {summary['simulation_duration_seconds']:.2f} seconds")
        
        # Storage metrics (MOST IMPORTANT)
        print("\n" + "-"*70)
        print("STORAGE UTILIZATION (Critical for O(N) validation)")
        print("-"*70)
        storage = summary['storage']
        print(f"  Average:     {storage['average_kb']:8.2f} KB")
        print(f"  Minimum:     {storage['min_kb']:8.2f} KB")
        print(f"  Maximum:     {storage['max_kb']:8.2f} KB")
        print(f"  Final:       {storage['final_kb']:8.2f} KB")
        print(f"  Is Constant: {'✓ YES' if storage['is_constant'] else '✗ NO'}")
        print(f"  Samples:     {storage['samples']}")
        
        # Block generation
        print("\n" + "-"*70)
        print("BLOCK GENERATION")
        print("-"*70)
        gen = summary['block_generation']
        print(f"  Average Time:    {gen['average_time_seconds']:8.4f} seconds")
        print(f"  Min Time:        {gen['min_time_seconds']:8.4f} seconds")
        print(f"  Max Time:        {gen['max_time_seconds']:8.4f} seconds")
        print(f"  Avg Hash Ops:    {gen['average_hash_computations']:8.0f}")
        print(f"  Total Blocks:    {gen['total_blocks']}")
        
        # Block validation
        print("\n" + "-"*70)
        print("BLOCK VALIDATION")
        print("-"*70)
        val = summary['block_validation']
        print(f"  Average Time:    {val['average_time_seconds']:8.6f} seconds")
        print(f"  Min Time:        {val['min_time_seconds']:8.6f} seconds")
        print(f"  Max Time:        {val['max_time_seconds']:8.6f} seconds")
        print(f"  Success Rate:    {val['success_rate']:8.2f} %")
        print(f"  Total Validations: {val['total_validations']}")
        
        # Network propagation
        print("\n" + "-"*70)
        print("NETWORK PROPAGATION")
        print("-"*70)
        net = summary['network_propagation']
        print(f"  Average Time:    {net['average_time_seconds']:8.4f} seconds")
        print(f"  Average Delay:   {net['average_delay_ms']:8.2f} ms")
        print(f"  Min Delay:       {net['min_delay_ms']:8.2f} ms")
        print(f"  Max Delay:       {net['max_delay_ms']:8.2f} ms")
        
        # System resources
        print("\n" + "-"*70)
        print("SYSTEM RESOURCES")
        print("-"*70)
        sys = summary['system_resources']
        print(f"  Average Memory:  {sys['average_memory_mb']:8.2f} MB")
        print(f"  Peak Memory:     {sys['peak_memory_mb']:8.2f} MB")
        print(f"  Baseline Memory: {sys['baseline_memory_mb']:8.2f} MB")
        print(f"  Average CPU:     {sys['average_cpu_percent']:8.2f} %")
        print(f"  Peak CPU:        {sys['peak_cpu_percent']:8.2f} %")
        
        # Synchronization
        if summary['synchronization']['total_syncs'] > 0:
            print("\n" + "-"*70)
            print("NODE SYNCHRONIZATION")
            print("-"*70)
            sync = summary['synchronization']
            print(f"  Average Time:    {sync['average_time_seconds']:8.4f} seconds")
            print(f"  Total Syncs:     {sync['total_syncs']}")
            print(f"  Avg Blocks Synced: {sync['average_blocks_synced']:6.1f}")
        
        print("\n" + "="*70 + "\n")
