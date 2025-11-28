"""
Configuration file for Ledger Amnesia implementation.
Based on the research paper specifications.
"""

# =======================
# CIRCULAR BUFFER CONFIG
# =======================
# Number of slots in circular buffer (N in paper)
BUFFER_SIZE = 100

# Block generation interval in seconds (Δt in paper)
BLOCK_INTERVAL = 2  # seconds

# =======================
# PROOF-OF-WORK CONFIG
# =======================
# Difficulty level (D in paper) - requires 2^D hash computations
# D=12 means ~4,096 expected hash attempts
DIFFICULTY = 12

# Target hash value: hash must be < 2^(256-D)
TARGET = 2 ** (256 - DIFFICULTY)

# =======================
# BLOCK STRUCTURE CONFIG
# =======================
# Block size specifications (bytes)
HEADER_SIZE = 64      # bytes (index, timestamp, prev_hash, nonce, hash)
PAYLOAD_SIZE = 320    # bytes (sensor data)
TOTAL_BLOCK_SIZE = 384  # bytes (header + payload)

# Expected total storage: BUFFER_SIZE * TOTAL_BLOCK_SIZE = 38.4 KB
EXPECTED_STORAGE = BUFFER_SIZE * TOTAL_BLOCK_SIZE  # 38,400 bytes

# =======================
# TIMING CONSTRAINTS
# =======================
# Timestamp tolerance for validation (seconds)
# Increased to account for network propagation delays and simulation timing
TIMESTAMP_TOLERANCE = 30  # seconds

# =======================
# NETWORK CONFIG
# =======================
# Number of nodes in the network
NUM_NODES = 5

# Network propagation delay simulation (milliseconds)
MIN_PROPAGATION_DELAY = 50   # ms
MAX_PROPAGATION_DELAY = 200  # ms

# =======================
# SENSOR DATA CONFIG
# =======================
# Temperature range (Celsius)
TEMP_MIN = 15.0
TEMP_MAX = 30.0
TEMP_MEAN = 22.5
TEMP_STD = 3.0

# Humidity range (percentage)
HUMIDITY_MIN = 30.0
HUMIDITY_MAX = 80.0
HUMIDITY_MEAN = 55.0
HUMIDITY_STD = 10.0

# CO2 levels (ppm)
CO2_MIN = 400
CO2_MAX = 1000
CO2_MEAN = 600
CO2_STD = 100

# =======================
# SIMULATION CONFIG
# =======================
# Total number of blocks to generate in simulation
SIMULATION_BLOCKS = 500

# Performance monitoring interval (blocks)
MONITORING_INTERVAL = 10

# Results output directory
RESULTS_DIR = "results"

# =======================
# HASH ALGORITHM
# =======================
HASH_ALGORITHM = "SHA-256"
HASH_OUTPUT_SIZE = 32  # bytes (256 bits / 8)
