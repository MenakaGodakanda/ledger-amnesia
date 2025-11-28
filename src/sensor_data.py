"""
Sensor data generation for IoT simulation.

Generates realistic environmental monitoring data:
- Temperature (°C)
- Humidity (%)
- CO2 levels (ppm)

Based on Section "Data Generation" in the implementation requirements.
"""

import random
import numpy as np
import time
from typing import Dict, Any
import config


class IoTSensorNode:
    """
    Simulates an IoT sensor node generating environmental data.
    
    Generates synthetic data following realistic distributions derived
    from publicly available IoT datasets.
    """
    
    def __init__(self, node_id: str = "NODE-01"):
        """
        Initialize the sensor node.
        
        Args:
            node_id: Unique identifier for this sensor node
        """
        self.node_id = node_id
        self.reading_count = 0
        
        # Initialize random seed for reproducibility in testing
        random.seed(time.time())
        np.random.seed(int(time.time()) % (2**32))
    
    def generate_temperature(self) -> float:
        """
        Generate temperature reading in Celsius.
        
        Uses normal distribution with parameters from config:
        - Mean: 22.5°C
        - Std Dev: 3.0°C
        - Range: 15-30°C
        
        Returns:
            float: Temperature in Celsius
        """
        temp = np.random.normal(config.TEMP_MEAN, config.TEMP_STD)
        # Clamp to realistic range
        temp = max(config.TEMP_MIN, min(config.TEMP_MAX, temp))
        return round(temp, 2)
    
    def generate_humidity(self) -> float:
        """
        Generate humidity reading in percentage.
        
        Uses normal distribution with parameters from config:
        - Mean: 55%
        - Std Dev: 10%
        - Range: 30-80%
        
        Returns:
            float: Humidity percentage
        """
        humidity = np.random.normal(config.HUMIDITY_MEAN, config.HUMIDITY_STD)
        # Clamp to realistic range
        humidity = max(config.HUMIDITY_MIN, min(config.HUMIDITY_MAX, humidity))
        return round(humidity, 2)
    
    def generate_co2(self) -> int:
        """
        Generate CO2 level reading in ppm (parts per million).
        
        Uses normal distribution with parameters from config:
        - Mean: 600 ppm
        - Std Dev: 100 ppm
        - Range: 400-1000 ppm
        
        Returns:
            int: CO2 level in ppm
        """
        co2 = np.random.normal(config.CO2_MEAN, config.CO2_STD)
        # Clamp to realistic range
        co2 = max(config.CO2_MIN, min(config.CO2_MAX, co2))
        return int(co2)
    
    def generate_reading(self) -> Dict[str, Any]:
        """
        Generate a complete sensor reading.
        
        Returns a dictionary containing all sensor measurements
        plus metadata about the reading.
        
        Returns:
            dict: Complete sensor data payload
        """
        self.reading_count += 1
        
        reading = {
            "node_id": self.node_id,
            "reading_id": self.reading_count,
            "timestamp": time.time(),
            "temperature": self.generate_temperature(),
            "humidity": self.generate_humidity(),
            "co2": self.generate_co2(),
            "battery_level": self._simulate_battery(),
            "signal_strength": self._simulate_signal()
        }
        
        return reading
    
    def _simulate_battery(self) -> float:
        """
        Simulate battery level (percentage).
        
        Battery slowly drains over time with some randomness.
        
        Returns:
            float: Battery percentage (0-100)
        """
        # Simulate battery drain: starts at 100%, drains slowly
        base_level = max(50, 100 - (self.reading_count * 0.01))
        noise = random.uniform(-2, 2)
        battery = max(0, min(100, base_level + noise))
        return round(battery, 2)
    
    def _simulate_signal(self) -> int:
        """
        Simulate wireless signal strength (dBm).
        
        Returns:
            int: Signal strength in dBm (typically -90 to -30)
        """
        # Typical WiFi/Zigbee signal strength range
        return random.randint(-85, -40)
    
    def get_data_size(self, reading: Dict[str, Any]) -> int:
        """
        Calculate approximate size of sensor data in bytes.
        
        Args:
            reading: Sensor data dictionary
        
        Returns:
            int: Approximate size in bytes
        """
        import json
        json_str = json.dumps(reading)
        return len(json_str.encode('utf-8'))


class MultiSensorNode(IoTSensorNode):
    """
    Extended sensor node with additional capabilities.
    
    Can simulate multiple types of sensors and environmental conditions.
    """
    
    def __init__(self, node_id: str = "NODE-01", location: str = "Indoor"):
        """
        Initialize multi-sensor node.
        
        Args:
            node_id: Unique identifier
            location: Physical location (affects data patterns)
        """
        super().__init__(node_id)
        self.location = location
    
    def generate_reading(self) -> Dict[str, Any]:
        """
        Generate enhanced sensor reading with location-specific patterns.
        
        Returns:
            dict: Enhanced sensor data payload
        """
        base_reading = super().generate_reading()
        
        # Add location-specific modifications
        if self.location == "Outdoor":
            # Outdoor locations have wider temperature variations
            base_reading["temperature"] += random.uniform(-2, 2)
            base_reading["humidity"] += random.uniform(-5, 5)
        elif self.location == "Server Room":
            # Server rooms are typically cooler and less humid
            base_reading["temperature"] = max(18, base_reading["temperature"] - 4)
            base_reading["humidity"] = max(30, base_reading["humidity"] - 15)
        
        # Add location metadata
        base_reading["location"] = self.location
        
        return base_reading


def generate_batch_data(node: IoTSensorNode, count: int) -> list:
    """
    Generate multiple sensor readings.
    
    Args:
        node: Sensor node instance
        count: Number of readings to generate
    
    Returns:
        list: List of sensor readings
    """
    return [node.generate_reading() for _ in range(count)]


def print_reading(reading: Dict[str, Any]):
    """
    Pretty-print a sensor reading.
    
    Args:
        reading: Sensor data dictionary
    """
    print(f"\n{'='*60}")
    print(f"Node: {reading['node_id']} | Reading #{reading['reading_id']}")
    print(f"{'='*60}")
    print(f"Temperature:     {reading['temperature']:6.2f} °C")
    print(f"Humidity:        {reading['humidity']:6.2f} %")
    print(f"CO2:             {reading['co2']:6d} ppm")
    print(f"Battery:         {reading['battery_level']:6.2f} %")
    print(f"Signal Strength: {reading['signal_strength']:6d} dBm")
    if 'location' in reading:
        print(f"Location:        {reading['location']}")
    print(f"{'='*60}\n")


# Example usage
if __name__ == "__main__":
    # Create sensor node
    sensor = IoTSensorNode("SENSOR-001")
    
    # Generate and display 5 readings
    print("Generating sample sensor data...")
    for i in range(5):
        reading = sensor.generate_reading()
        print_reading(reading)
        time.sleep(0.5)
