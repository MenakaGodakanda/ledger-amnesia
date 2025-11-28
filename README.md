# Ledger Amnesia: Circular Blockchain Design for IoT

## Overview

Ledger Amnesia is a novel blockchain architecture designed specifically for resource-constrained IoT devices. Unlike traditional blockchains that grow unbounded, Ledger Amnesia implements a circular buffer structure that maintains constant O(N) storage regardless of operational duration.

## Key Features

- **Constant Storage**: Fixed ≈ 40 KB storage (N=100 slots)
- **Lightweight Proof-of-Work**: Tuned for IoT devices (D=12, ≈4,096 hash ops)
- **Deterministic Overwriting**: FIFO circular buffer architecture
- **Fast Synchronization**: Bounded by buffer size, not chain history
- **Cryptographic Integrity**: SHA-256 hash chain within retention window

## System Requirements

### Software
- Ubuntu 22.04 LTS (or compatible Linux distribution)
- Python 3.10 or higher
- pip package manager
- 2 GB RAM (minimum)
- 1 GB free disk space

## Installation Guide

### Step 1: System Preparation

#### 1. Update system
```bash
sudo apt update && sudo apt upgrade -y
```

#### 2. Install Python and tools
```
sudo apt install python3 python3-pip python3-venv git -y
```

#### 3. Install monitoring tools
```
sudo apt install htop sysstat -y
```

#### Step 2: Clone the Repository

```bash
git clone https://github.com/MenakaGodakanda/ledger-amnesia.git
cd ledger-amnesia
```

### Step 3: Install Dependencies

#### 1. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 2. Install required packages
```
pip install numpy matplotlib psutil tabulate pytest
```

## Usage

### Running the Simulation 01

#### 1. Run simulation with default 500 blocks
```
python simulation/run_simulation.py
```
- Expected Terminal Output: <br>
<a href="https://github.com/MenakaGodakanda/ledger-amnesia/tree/main/results/simulation-01">Simulation 01 Terminal Output</a>

#### 2. Run with custom number of blocks
```
python simulation/run_simulation.py 1000
```

#### 3. Run Tests
- Run with pytest
```
pytest tests/ -v
```
- Expected Terminal Output:
<img width="1200" height="665" alt="Screenshot 2025-11-11 165229" src="https://github.com/user-attachments/assets/ba62192e-11fc-4a3f-bd61-74247e585ca7" />

#### 4. Output Files
Results are saved to the `results/` directory:

- `metrics_YYYYMMDD_HHMMSS.json` - Complete performance metrics
- `network_YYYYMMDD_HHMMSS.json` - Network statistics

### Running the Simulation 02

#### 1. Run simulation with default settings (5 nodes, 500 blocks each)
```
python simulation/run_multi_node_simulation.py
```
- Expected Terminal Output:<br>
<a href="https://github.com/MenakaGodakanda/ledger-amnesia/tree/main/results/simulation-02">Simulation 02 Terminal Output</a>

#### 2. Run with custom number of blocks per node
```
python simulation/run_multi_node_simulation.py 100
```
- Expected Terminal Output:


#### 3. Output Files
After simulation, you'll find these files in `results/`:

##### Per-Node Files

For each node (NODE-01 through NODE-05):

1. **`block_details_NODE-XX_TIMESTAMP.txt`** - Complete block log
   - All 500 blocks with full details
   - Slot mapping information
   - IoT sensor data
   - Validation statistics
   - Mining performance

2. **`metrics_NODE-XX_TIMESTAMP.json`** - Performance metrics
   - Storage utilization over time
   - Mining times
   - Hash computations
   - CPU and memory usage

3. **`node_NODE-XX_TIMESTAMP.json`** - Node statistics
   - Blocks created/received/validated
   - Ledger state
   - Peer information
   - Simulation summary

##### Summary File

**`simulation_summary_TIMESTAMP.json`** - Overall simulation data
- Configuration used
- Summary for all nodes
- Network-wide statistics

## Storge

- Expected Terminal Output:<br>
<img width="791" height="695" alt="Screenshot 2025-11-20 144450" src="https://github.com/user-attachments/assets/a3ea69b6-3cf7-4540-a84c-faf13dfb9f27" />

## Project Structure

```
ledger-amnesia/
│
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── config.py                 # System configuration
│
├── src/                      # Core implementation
│   ├── __init__.py
│   ├── block.py             # Block structure & PoW
│   ├── circular_ledger.py   # Circular buffer logic
│   ├── sensor_data.py       # IoT data generation
│   └── network.py           # Network simulation
│
├── simulation/               # Simulation scripts
│   ├── __init__.py
│   ├── run_simulation.py    # Main simulation
│   ├── run_multi_node_simulation.py # Multi-node simulation
│   └── performance_monitor.py  # Metrics collection
│
└── results/                  # Output directory
    ├── metrics_*.json       # Performance data
    └── network_*.json       # Network statistics
    └── block_details_*.json       # Block details
```

## License

This project is licensed under the MIT License. This implementation is provided for academic research purposes.
