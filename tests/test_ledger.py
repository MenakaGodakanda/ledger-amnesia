"""
Unit tests for Ledger Amnesia implementation.

Tests core functionality:
- Block creation and validation
- Circular buffer operations
- Storage constraints
- Hash chain integrity
"""

import sys
import os
import unittest
import time

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.block import Block
from src.circular_ledger import CircularLedger
from src.sensor_data import IoTSensorNode
import config


class TestBlock(unittest.TestCase):
    """Test Block class functionality."""
    
    def test_block_creation(self):
        """Test basic block creation."""
        data = {"temperature": 22.5, "humidity": 60.0}
        block = Block(0, data)
        
        self.assertEqual(block.index, 0)
        self.assertEqual(block.data, data)
        self.assertIsNotNone(block.timestamp)
    
    def test_genesis_block(self):
        """Test genesis block creation."""
        genesis = Block.create_genesis_block()
        
        self.assertEqual(genesis.index, 0)
        self.assertEqual(genesis.prev_hash, "0" * 64)
        self.assertIsNotNone(genesis.hash)
    
    def test_hash_calculation(self):
        """Test hash calculation consistency."""
        data = {"test": "data"}
        block = Block(1, data, "0" * 64)
        
        hash1 = block.calculate_hash()
        hash2 = block.calculate_hash()
        
        self.assertEqual(hash1, hash2)
        self.assertEqual(len(hash1), 64)  # SHA-256 hex = 64 chars
    
    def test_mining(self):
        """Test proof-of-work mining."""
        data = {"test": "data"}
        block = Block(1, data)
        
        difficulty = 8  # Low difficulty for testing
        hash_count = block.mine_block(difficulty)
        
        self.assertGreater(hash_count, 0)
        self.assertIsNotNone(block.hash)
        
        # Verify hash meets difficulty requirement
        target = 2 ** (256 - difficulty)
        hash_int = int(block.hash, 16)
        self.assertLess(hash_int, target)
    
    def test_block_validation(self):
        """Test block validation."""
        # Create valid chain
        prev_block = Block.create_genesis_block()
        prev_block.mine_block(8)
        
        new_block = Block(1, {"test": "data"}, prev_block.hash)
        new_block.mine_block(8)
        
        self.assertTrue(new_block.is_valid(8, prev_block))
    
    def test_invalid_prev_hash(self):
        """Test validation fails with wrong prev_hash."""
        prev_block = Block.create_genesis_block()
        prev_block.mine_block(8)
        
        new_block = Block(1, {"test": "data"}, "wrong_hash")
        new_block.mine_block(8)
        
        self.assertFalse(new_block.is_valid(8, prev_block))


class TestCircularLedger(unittest.TestCase):
    """Test CircularLedger class functionality."""
    
    def test_ledger_initialization(self):
        """Test ledger initialization."""
        ledger = CircularLedger(buffer_size=10, difficulty=8)
        
        self.assertEqual(ledger.buffer_size, 10)
        self.assertEqual(ledger.difficulty, 8)
        self.assertEqual(ledger.last_index, 0)  # Genesis block
    
    def test_mapping_function(self):
        """Test φ(i) = i mod N mapping function."""
        ledger = CircularLedger(buffer_size=8, difficulty=8)
        
        self.assertEqual(ledger._phi(0), 0)
        self.assertEqual(ledger._phi(7), 7)
        self.assertEqual(ledger._phi(8), 0)  # Wraps around
        self.assertEqual(ledger._phi(15), 7)
    
    def test_accessibility_predicate(self):
        """Test R(i) accessibility predicate."""
        ledger = CircularLedger(buffer_size=8, difficulty=8)
        
        # Add 15 blocks
        for i in range(15):
            ledger.add_block({"index": i})
        
        # Blocks 8-15 should be accessible (c=15, N=8)
        self.assertTrue(ledger.is_accessible(15))
        self.assertTrue(ledger.is_accessible(8))
        
        # Blocks 0-7 should be overwritten
        self.assertFalse(ledger.is_accessible(7))
        self.assertFalse(ledger.is_accessible(0))
    
    def test_block_overwriting(self):
        """Test that old blocks are overwritten."""
        ledger = CircularLedger(buffer_size=5, difficulty=8)
        
        # Add blocks beyond buffer size
        for i in range(10):
            ledger.add_block({"index": i})
        
        # Should have 5 accessible blocks
        accessible = ledger.get_retention_window()
        self.assertEqual(len(accessible), 5)
        
        # Should have 5 overwrites (genesis + 9 blocks - 5 slots = 5 overwrites)
        self.assertGreater(ledger.overwrite_count, 0)
    
    def test_constant_storage(self):
        """Test that storage remains constant after buffer fills."""
        buffer_size = 10
        ledger = CircularLedger(buffer_size=buffer_size, difficulty=8)
        
        storage_sizes = []
        
        # Add blocks and track storage
        for i in range(30):
            ledger.add_block({"index": i})
            storage_sizes.append(ledger.get_storage_usage())
        
        # After buffer fills, storage should be roughly constant
        # Check last 10 measurements
        recent_storage = storage_sizes[-10:]
        avg_storage = sum(recent_storage) / len(recent_storage)
        
        for size in recent_storage:
            deviation = abs(size - avg_storage) / avg_storage
            self.assertLess(deviation, 0.1)  # Within 10%
    
    def test_chain_integrity(self):
        """Test cryptographic chain linkage."""
        ledger = CircularLedger(buffer_size=10, difficulty=8)
        
        # Add several blocks
        for i in range(5):
            ledger.add_block({"index": i})
        
        # Verify chain continuity
        blocks = ledger.get_retention_window()
        for i in range(1, len(blocks)):
            self.assertEqual(blocks[i].prev_hash, blocks[i-1].hash)
    
    def test_temporal_window(self):
        """Test temporal window calculation."""
        ledger = CircularLedger(buffer_size=100, difficulty=8)
        
        delta_t = 2.0  # 2 seconds per block
        temporal_window = ledger.get_temporal_window(delta_t)
        
        self.assertEqual(temporal_window, 200.0)  # 100 * 2.0
    
    def test_block_age(self):
        """Test block age calculation."""
        ledger = CircularLedger(buffer_size=10, difficulty=8)
        
        # Add blocks
        for i in range(5):
            ledger.add_block({"index": i})
        
        delta_t = 2.0
        age = ledger.get_block_age(3, delta_t)
        
        # Current index is 5, block 3 is 2 blocks old
        expected_age = 2 * delta_t
        self.assertEqual(age, expected_age)


class TestSensorData(unittest.TestCase):
    """Test sensor data generation."""
    
    def test_sensor_initialization(self):
        """Test sensor node initialization."""
        sensor = IoTSensorNode("TEST-NODE")
        
        self.assertEqual(sensor.node_id, "TEST-NODE")
        self.assertEqual(sensor.reading_count, 0)
    
    def test_data_generation(self):
        """Test sensor data generation."""
        sensor = IoTSensorNode("TEST-NODE")
        reading = sensor.generate_reading()
        
        # Check all fields present
        self.assertIn("node_id", reading)
        self.assertIn("temperature", reading)
        self.assertIn("humidity", reading)
        self.assertIn("co2", reading)
        self.assertIn("timestamp", reading)
    
    def test_data_ranges(self):
        """Test that generated data is within realistic ranges."""
        sensor = IoTSensorNode("TEST-NODE")
        
        for _ in range(100):
            reading = sensor.generate_reading()
            
            # Temperature: 15-30°C
            self.assertGreaterEqual(reading["temperature"], config.TEMP_MIN)
            self.assertLessEqual(reading["temperature"], config.TEMP_MAX)
            
            # Humidity: 30-80%
            self.assertGreaterEqual(reading["humidity"], config.HUMIDITY_MIN)
            self.assertLessEqual(reading["humidity"], config.HUMIDITY_MAX)
            
            # CO2: 400-1000 ppm
            self.assertGreaterEqual(reading["co2"], config.CO2_MIN)
            self.assertLessEqual(reading["co2"], config.CO2_MAX)
    
    def test_reading_counter(self):
        """Test reading counter increments."""
        sensor = IoTSensorNode("TEST-NODE")
        
        for i in range(5):
            reading = sensor.generate_reading()
            self.assertEqual(reading["reading_id"], i + 1)
        
        self.assertEqual(sensor.reading_count, 5)


class TestPerformance(unittest.TestCase):
    """Test performance characteristics."""
    
    def test_block_generation_time(self):
        """Test block generation is reasonably fast."""
        ledger = CircularLedger(buffer_size=10, difficulty=12)
        
        start = time.time()
        ledger.add_block({"test": "data"})
        duration = time.time() - start
        
        # Should complete within reasonable time (< 10 seconds)
        self.assertLess(duration, 10.0)
    
    def test_validation_speed(self):
        """Test block validation is fast."""
        ledger = CircularLedger(buffer_size=10, difficulty=8)
        block = ledger.add_block({"test": "data"})
        
        start = time.time()
        is_valid, _ = ledger.validate_block(block, time.time())
        duration = time.time() - start
        
        # Validation should be near-instantaneous
        self.assertLess(duration, 0.01)  # < 10ms


def run_tests():
    """Run all tests and print results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestBlock))
    suite.addTests(loader.loadTestsFromTestCase(TestCircularLedger))
    suite.addTests(loader.loadTestsFromTestCase(TestSensorData))
    suite.addTests(loader.loadTestsFromTestCase(TestPerformance))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print(" TEST SUMMARY ".center(70, "="))
    print("="*70)
    print(f"Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures:  {len(result.failures)}")
    print(f"Errors:    {len(result.errors)}")
    print("="*70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
