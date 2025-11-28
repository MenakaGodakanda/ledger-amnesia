import json
import struct
from datetime import datetime
import sys

class BlockSizeAnalyzer:
    def __init__(self):
        self.theoretical_sizes = {
            'index': 4,        # uint32
            'timestamp': 4,    # uint32  
            'data': 'variable', # bytes (32-256)
            'prev_hash': 32,   # bytes32
            'nonce': 4,        # uint32
            'hash': 32         # bytes32
        }
        
    def theoretical_block_size(self, data_size=32):
        """Calculate theoretical binary encoded block size"""
        fixed_size = (
            self.theoretical_sizes['index'] +
            self.theoretical_sizes['timestamp'] +
            self.theoretical_sizes['prev_hash'] +
            self.theoretical_sizes['nonce'] +
            self.theoretical_sizes['hash']
        )
        total_size = fixed_size + data_size
        return fixed_size, total_size
    
    def create_sample_block(self):
        """Create the sample block as specified"""
        return {
            "index": 100,
            "timestamp": "2025-11-11 16:17:51",
            "data": {
                "node_id": "SENSOR-001",
                "reading_id": 100,
                "temperature": 28.12,
                "humidity": 61.08,
                "co2": 633,
                "battery_level": 98.42,
                "signal_strength": -57,
            },
            "prev_hash": "000c305f0579e31ef4527346ff4a9af30590024785754bde905411e9b030b1a7",
            "nonce": 6349,
            "hash": "0006410f2dfd5528ad8921c3d4b5b9a418d261f7bbce39b10055fa045e78e473"
        }
    
    def calculate_json_sizes(self, block):
        """Calculate actual sizes when using JSON encoding"""
        sizes = {}
        
        # Calculate size of individual fields in JSON
        sizes['index'] = len(json.dumps(block['index']).encode('utf-8'))
        sizes['timestamp'] = len(json.dumps(block['timestamp']).encode('utf-8'))
        sizes['data'] = len(json.dumps(block['data']).encode('utf-8'))
        sizes['prev_hash'] = len(json.dumps(block['prev_hash']).encode('utf-8'))
        sizes['nonce'] = len(json.dumps(block['nonce']).encode('utf-8'))
        sizes['hash'] = len(json.dumps(block['hash']).encode('utf-8'))
        
        # Calculate total JSON size
        full_json = json.dumps(block, indent=2)
        sizes['total_json_pretty'] = len(full_json.encode('utf-8'))
        
        # Calculate compact JSON size
        compact_json = json.dumps(block, separators=(',', ':'))
        sizes['total_json_compact'] = len(compact_json.encode('utf-8'))
        
        # Calculate binary encoding size for comparison
        sizes['binary_equivalent'] = self.calculate_binary_size(block)
        
        return sizes, full_json, compact_json
    
    def calculate_binary_size(self, block):
        """Calculate what the size would be with binary encoding"""
        # Convert timestamp to UNIX timestamp (uint32)
        dt = datetime.strptime(block['timestamp'], "%Y-%m-%d %H:%M:%S")
        timestamp_int = int(dt.timestamp())
        
        # Convert data to binary (estimate)
        data_binary = json.dumps(block['data']).encode('utf-8')
        
        # Binary encoding sizes
        size = 0
        size += 4  # index (uint32)
        size += 4  # timestamp (uint32)
        size += len(data_binary)  # data (variable)
        size += 32  # prev_hash (bytes32)
        size += 4   # nonce (uint32)
        size += 32  # hash (bytes32)
        
        return size
    
    def analyze_field_overhead(self, block):
        """Analyze the overhead of JSON encoding for each field"""
        overhead = {}
        
        for field, value in block.items():
            if field == 'data':
                # For nested data, calculate total overhead
                json_size = len(json.dumps(value).encode('utf-8'))
                # Estimate binary size for comparison
                binary_estimate = len(str(value).encode('utf-8')) + 4  # length prefix
                overhead[field] = {
                    'json_size': json_size,
                    'binary_estimate': binary_estimate,
                    'overhead': json_size - binary_estimate
                }
            else:
                json_size = len(json.dumps(value).encode('utf-8'))
                if field in ['index', 'nonce']:
                    binary_size = 4  # uint32
                elif field in ['prev_hash', 'hash']:
                    binary_size = 32  # bytes32
                elif field == 'timestamp':
                    binary_size = 4  # uint32 (UNIX timestamp)
                else:
                    binary_size = len(str(value).encode('utf-8'))
                
                overhead[field] = {
                    'json_size': json_size,
                    'binary_size': binary_size,
                    'overhead': json_size - binary_size
                }
        
        return overhead

def main():
    analyzer = BlockSizeAnalyzer()
    block = analyzer.create_sample_block()
    
    print("=" * 70)
    print("BLOCK SIZE ANALYSIS: THEORETICAL vs PRACTICAL (JSON)")
    print("=" * 70)
    
    # Theoretical analysis
    print("\n1. THEORETICAL BINARY ENCODING")
    print("-" * 40)
    print("Field\t\t\tType\t\tSize (bytes)")
    print("-" * 40)
    for field, size in analyzer.theoretical_sizes.items():
        type_desc = "uint32" if field in ['index', 'timestamp', 'nonce'] else "bytes32" if field in ['prev_hash', 'hash'] else "bytes"
        print(f"{field:<15}\t\t{type_desc:<10}\t{size}")
    
    fixed_size, total_min = analyzer.theoretical_block_size(32)
    _, total_max = analyzer.theoretical_block_size(256)
    print(f"\nFixed components: {fixed_size} bytes")
    print(f"Data range: 32-256 bytes")
    print(f"Total range: {total_min}-{total_max} bytes")
    
    # Practical analysis
    print("\n\n2. PRACTICAL JSON ENCODING")
    print("-" * 40)
    
    sizes, pretty_json, compact_json = analyzer.calculate_json_sizes(block)
    overhead = analyzer.analyze_field_overhead(block)
    
    print("Field\t\t\tJSON Size\tBinary Size\tOverhead")
    print("-" * 60)
    for field in block.keys():
        json_size = sizes[field]
        if field == 'data':
            binary_size = overhead[field]['binary_estimate']
        else:
            binary_size = overhead[field]['binary_size']
        ovhd = overhead[field]['overhead']
        print(f"{field:<15}\t\t{json_size:<10}\t{binary_size:<12}\t{ovhd:+}")
    
    print("\n" + "-" * 60)
    print(f"{'Total (pretty JSON)':<15}\t\t{sizes['total_json_pretty']:<10}")
    print(f"{'Total (compact JSON)':<15}\t\t{sizes['total_json_compact']:<10}")
    print(f"{'Binary equivalent':<15}\t\t{sizes['binary_equivalent']:<10}")
    
    # Efficiency analysis
    print("\n\n3. EFFICIENCY ANALYSIS")
    print("-" * 40)
    binary_size = sizes['binary_equivalent']
    json_compact = sizes['total_json_compact']
    json_pretty = sizes['total_json_pretty']
    
    overhead_compact = ((json_compact - binary_size) / binary_size) * 100
    overhead_pretty = ((json_pretty - binary_size) / binary_size) * 100
    
    print(f"Binary encoding: {binary_size} bytes")
    print(f"Compact JSON: {json_compact} bytes ({overhead_compact:+.1f}% overhead)")
    print(f"Pretty JSON: {json_pretty} bytes ({overhead_pretty:+.1f}% overhead)")
    
    # Show JSON examples
    print("\n\n4. JSON REPRESENTATIONS")
    print("-" * 40)
    print("Compact JSON (for storage):")
    print(compact_json)
    print(f"\nSize: {len(compact_json)} characters, {sizes['total_json_compact']} bytes")
    
    print("\n" + "=" * 70)
    print("KEY FINDINGS:")
    print("=" * 70)
    print("✓ JSON adds significant overhead due to:")
    print("  - String encoding of numbers and hashes")
    print("  - Field names and delimiters")
    print("  - Whitespace (in pretty format)")
    print("✓ Binary encoding is more space-efficient")
    print("✓ JSON provides human readability and debugging benefits")
    print("✓ Pretty JSON adds ~30-50% more overhead than compact JSON")

if __name__ == "__main__":
    main()
