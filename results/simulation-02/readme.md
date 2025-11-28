# Simulation 02 Results

## Results exported to `results/`

- **[NODE-01]**:
  - block_details_NODE-01_20251113_155215.txt
  - metrics_NODE-01_20251113_171818.json
  - node_NODE-01_20251113_171818.json

- **[NODE-02]**:
  - block_details_NODE-02_20251113_155215.txt
  - metrics_NODE-02_20251113_171818.json
  - node_NODE-02_20251113_171818.json

- **[NODE-03]**:
  - block_details_NODE-03_20251113_155215.txt
  - metrics_NODE-03_20251113_171818.json
  - node_NODE-03_20251113_171818.json

- **[NODE-04]**:
  - block_details_NODE-04_20251113_155215.txt
  - metrics_NODE-04_20251113_171818.json
  - node_NODE-04_20251113_171818.json

- **[NODE-05]**:
  - block_details_NODE-05_20251113_155215.txt
  - metrics_NODE-05_20251113_171818.json
  - node_NODE-05_20251113_171818.json

- **Summary file**: simulation_summary_20251113_171818.json

## Simulation 02 Output

- Storage vs Block Number:
<img width="750" height="501" alt="Screenshot 2025-11-14 at 3 06 42 am" src="https://github.com/user-attachments/assets/5a935c58-5304-4af5-8dbd-00532732a80a" />

- Block Generation Time vs Block Number:
<img width="641" height="367" alt="Screenshot 2025-11-14 at 3 15 51 pm" src="https://github.com/user-attachments/assets/168b4073-a420-4112-bebd-c1496459809c" />

- Hash Operations per Block vs Block Number:
<img width="654" height="355" alt="Screenshot 2025-11-15 at 6 45 59 am" src="https://github.com/user-attachments/assets/f95552cf-5f17-4886-840d-673a03ec9364" />

- Terminal Output (text):
```
(venv) mcyber@mcyber-VirtualBox:~/ledger-amnesia$ python simulation/run_multi_node_simulation.py 500
================================================================================
================== LEDGER AMNESIA - MULTI-NODE IoT SIMULATION ==================
================================================================================

Configuration:
  Number of IoT Nodes: 5
  Blocks per Node: 500
  Buffer Size: 100 slots
  Difficulty: 12 (2^12 = 4096 hashes)
  Block Interval: 2 seconds

[NODE-01] Created with ledger id: 139522867892192
[NODE-01] Initialized - will generate 500 blocks
[NODE-02] Created with ledger id: 139522698031472
[NODE-02] Initialized - will generate 500 blocks
[NODE-03] Created with ledger id: 139522698194544
[NODE-03] Initialized - will generate 500 blocks
[NODE-04] Created with ledger id: 139522698194832
[NODE-04] Initialized - will generate 500 blocks
[NODE-05] Created with ledger id: 139522698195552
[NODE-05] Initialized - will generate 500 blocks

Setting up mesh network topology...
Each node connected to 4 peers
Synchronizing genesis blocks across all nodes...
✓ All nodes synchronized with same genesis block

Network initialized:
  Nodes: 5
  Topology: Full mesh
  Blocks per node: 500
  Total blocks: 2500

================================================================================
===================== MULTI-NODE LEDGER AMNESIA SIMULATION =====================
================================================================================

Simulation Mode: Independent node simulations
Each node demonstrates circular buffer behavior independently
Broadcasting to peers is DISABLED to avoid validation conflicts


================================================================================
Resetting NODE-01 to genesis before its simulation
================================================================================
✓ NODE-01 reset to genesis (index=0)


[NODE-01] Starting block generation...
[NODE-01] Initial ledger state:
[NODE-01]   Last index: 0
[NODE-01]   Genesis hash: 000ac6d79f7c53bb...
[NODE-01] Target: 500 blocks
[NODE-01] Mode: Independent (no peer interaction)
[NODE-01] Peers temporarily disconnected for independent simulation
[NODE-01] Block   1/500 | Index:   1 | Slot:   1 | Storage:   0.70 KB | Overwrites:   - | Hash Ops:    746 | Time: 0.014s | ETA:   61.4s
[NODE-01] Block   2/500 | Index:   2 | Slot:   2 | Storage:   1.09 KB | Overwrites:   - | Hash Ops:   3036 | Time: 0.015s | ETA:  533.1s
[NODE-01] Block   3/500 | Index:   3 | Slot:   3 | Storage:   1.48 KB | Overwrites:   - | Hash Ops:   9978 | Time: 0.047s | ETA:  697.8s
[NODE-01] Block   4/500 | Index:   4 | Slot:   4 | Storage:   1.87 KB | Overwrites:   - | Hash Ops:  17622 | Time: 0.058s | ETA:  777.7s
[NODE-01] Block   5/500 | Index:   5 | Slot:   5 | Storage:   2.25 KB | Overwrites:   - | Hash Ops:  22332 | Time: 0.039s | ETA:  823.0s
[NODE-01] Block   6/500 | Index:   6 | Slot:   6 | Storage:   2.64 KB | Overwrites:   - | Hash Ops:  25008 | Time: 0.023s | ETA:  851.8s
[NODE-01] Block   7/500 | Index:   7 | Slot:   7 | Storage:   3.03 KB | Overwrites:   - | Hash Ops:  29784 | Time: 0.036s | ETA:  873.3s
[NODE-01] Block   8/500 | Index:   8 | Slot:   8 | Storage:   3.42 KB | Overwrites:   - | Hash Ops:  35036 | Time: 0.036s | ETA:  889.0s
[NODE-01] Block   9/500 | Index:   9 | Slot:   9 | Storage:   3.81 KB | Overwrites:   - | Hash Ops:  37705 | Time: 0.018s | ETA:  899.0s
[NODE-01] Block  10/500 | Index:  10 | Slot:  10 | Storage:   4.20 KB | Overwrites:   - | Hash Ops:  38517 | Time: 0.010s | ETA:  906.7s
[NODE-01] Block  11/500 | Index:  11 | Slot:  11 | Storage:   4.59 KB | Overwrites:   - | Hash Ops:  38965 | Time: 0.007s | ETA:  916.4s
[NODE-01] Block  12/500 | Index:  12 | Slot:  12 | Storage:   4.98 KB | Overwrites:   - | Hash Ops:  44178 | Time: 0.044s | ETA:  921.9s
[NODE-01] Block  13/500 | Index:  13 | Slot:  13 | Storage:   5.37 KB | Overwrites:   - | Hash Ops:  48500 | Time: 0.028s | ETA:  925.6s
[NODE-01] Block  14/500 | Index:  14 | Slot:  14 | Storage:   5.76 KB | Overwrites:   - | Hash Ops:  51641 | Time: 0.024s | ETA:  928.1s
[NODE-01] Block  15/500 | Index:  15 | Slot:  15 | Storage:   6.15 KB | Overwrites:   - | Hash Ops:  52317 | Time: 0.008s | ETA:  930.2s
[NODE-01] Block  16/500 | Index:  16 | Slot:  16 | Storage:   6.54 KB | Overwrites:   - | Hash Ops:  52887 | Time: 0.004s | ETA:  931.3s
[NODE-01] Block  17/500 | Index:  17 | Slot:  17 | Storage:   6.93 KB | Overwrites:   - | Hash Ops:  53932 | Time: 0.011s | ETA:  932.4s
[NODE-01] Block  18/500 | Index:  18 | Slot:  18 | Storage:   7.32 KB | Overwrites:   - | Hash Ops:  55304 | Time: 0.013s | ETA:  933.3s
[NODE-01] Block  19/500 | Index:  19 | Slot:  19 | Storage:   7.71 KB | Overwrites:   - | Hash Ops:  57532 | Time: 0.019s | ETA:  933.5s
[NODE-01] Block  20/500 | Index:  20 | Slot:  20 | Storage:   8.10 KB | Overwrites:   - | Hash Ops:  59705 | Time: 0.019s | ETA:  934.2s
[NODE-01] Block  21/500 | Index:  21 | Slot:  21 | Storage:   8.49 KB | Overwrites:   - | Hash Ops:  60263 | Time: 0.008s | ETA:  936.1s
[NODE-01] Block  22/500 | Index:  22 | Slot:  22 | Storage:   8.88 KB | Overwrites:   - | Hash Ops:  62469 | Time: 0.020s | ETA:  935.6s
[NODE-01] Block  23/500 | Index:  23 | Slot:  23 | Storage:   9.27 KB | Overwrites:   - | Hash Ops:  63416 | Time: 0.013s | ETA:  934.9s
[NODE-01] Block  24/500 | Index:  24 | Slot:  24 | Storage:   9.66 KB | Overwrites:   - | Hash Ops:  71873 | Time: 0.062s | ETA:  935.0s
[NODE-01] Block  25/500 | Index:  25 | Slot:  25 | Storage:  10.05 KB | Overwrites:   - | Hash Ops:  73494 | Time: 0.011s | ETA:  937.5s
[NODE-01] Block  26/500 | Index:  26 | Slot:  26 | Storage:  10.44 KB | Overwrites:   - | Hash Ops:  73999 | Time: 0.007s | ETA:  936.2s
[NODE-01] Block  27/500 | Index:  27 | Slot:  27 | Storage:  10.84 KB | Overwrites:   - | Hash Ops:  75892 | Time: 0.016s | ETA:  934.9s
[NODE-01] Block  28/500 | Index:  28 | Slot:  28 | Storage:  11.23 KB | Overwrites:   - | Hash Ops:  76148 | Time: 0.005s | ETA:  933.5s
[NODE-01] Block  29/500 | Index:  29 | Slot:  29 | Storage:  11.62 KB | Overwrites:   - | Hash Ops:  77981 | Time: 0.016s | ETA:  932.8s
[NODE-01] Block  30/500 | Index:  30 | Slot:  30 | Storage:  12.01 KB | Overwrites:   - | Hash Ops:  79050 | Time: 0.011s | ETA:  931.3s
[NODE-01] Block  31/500 | Index:  31 | Slot:  31 | Storage:  12.40 KB | Overwrites:   - | Hash Ops:  81068 | Time: 0.017s | ETA:  931.5s
[NODE-01] Block  32/500 | Index:  32 | Slot:  32 | Storage:  12.79 KB | Overwrites:   - | Hash Ops:  86629 | Time: 0.040s | ETA:  930.4s
[NODE-01] Block  33/500 | Index:  33 | Slot:  33 | Storage:  13.18 KB | Overwrites:   - | Hash Ops:  87818 | Time: 0.009s | ETA:  929.3s
[NODE-01] Block  34/500 | Index:  34 | Slot:  34 | Storage:  13.57 KB | Overwrites:   - | Hash Ops:  89184 | Time: 0.009s | ETA:  927.6s
[NODE-01] Block  35/500 | Index:  35 | Slot:  35 | Storage:  13.96 KB | Overwrites:   - | Hash Ops:  93703 | Time: 0.034s | ETA:  926.2s
[NODE-01] Block  36/500 | Index:  36 | Slot:  36 | Storage:  14.35 KB | Overwrites:   - | Hash Ops:  98765 | Time: 0.038s | ETA:  924.9s
[NODE-01] Block  37/500 | Index:  37 | Slot:  37 | Storage:  14.74 KB | Overwrites:   - | Hash Ops: 107273 | Time: 0.057s | ETA:  923.9s
[NODE-01] Block  38/500 | Index:  38 | Slot:  38 | Storage:  15.13 KB | Overwrites:   - | Hash Ops: 111807 | Time: 0.039s | ETA:  923.0s
[NODE-01] Block  39/500 | Index:  39 | Slot:  39 | Storage:  15.53 KB | Overwrites:   - | Hash Ops: 113979 | Time: 0.019s | ETA:  921.4s
[NODE-01] Block  40/500 | Index:  40 | Slot:  40 | Storage:  15.92 KB | Overwrites:   - | Hash Ops: 118883 | Time: 0.040s | ETA:  920.0s
[NODE-01] Block  41/500 | Index:  41 | Slot:  41 | Storage:  16.31 KB | Overwrites:   - | Hash Ops: 119515 | Time: 0.012s | ETA:  919.5s
[NODE-01] Block  42/500 | Index:  42 | Slot:  42 | Storage:  16.70 KB | Overwrites:   - | Hash Ops: 120140 | Time: 0.008s | ETA:  917.6s
[NODE-01] Block  43/500 | Index:  43 | Slot:  43 | Storage:  17.09 KB | Overwrites:   - | Hash Ops: 120512 | Time: 0.003s | ETA:  915.6s
[NODE-01] Block  44/500 | Index:  44 | Slot:  44 | Storage:  17.48 KB | Overwrites:   - | Hash Ops: 121676 | Time: 0.009s | ETA:  913.8s
[NODE-01] Block  45/500 | Index:  45 | Slot:  45 | Storage:  17.87 KB | Overwrites:   - | Hash Ops: 124752 | Time: 0.028s | ETA:  912.1s
[NODE-01] Block  46/500 | Index:  46 | Slot:  46 | Storage:  18.26 KB | Overwrites:   - | Hash Ops: 125186 | Time: 0.006s | ETA:  910.1s
[NODE-01] Block  47/500 | Index:  47 | Slot:  47 | Storage:  18.66 KB | Overwrites:   - | Hash Ops: 132531 | Time: 0.057s | ETA:  908.7s
[NODE-01] Block  48/500 | Index:  48 | Slot:  48 | Storage:  19.05 KB | Overwrites:   - | Hash Ops: 134716 | Time: 0.018s | ETA:  907.5s
[NODE-01] Block  49/500 | Index:  49 | Slot:  49 | Storage:  19.44 KB | Overwrites:   - | Hash Ops: 139377 | Time: 0.031s | ETA:  905.8s
[NODE-01] Block  50/500 | Index:  50 | Slot:  50 | Storage:  19.83 KB | Overwrites:   - | Hash Ops: 140352 | Time: 0.010s | ETA:  903.8s
[NODE-01] Block  51/500 | Index:  51 | Slot:  51 | Storage:  20.22 KB | Overwrites:   - | Hash Ops: 148389 | Time: 0.056s | ETA:  903.5s
[NODE-01] Block  52/500 | Index:  52 | Slot:  52 | Storage:  20.61 KB | Overwrites:   - | Hash Ops: 148847 | Time: 0.007s | ETA:  901.6s
[NODE-01] Block  53/500 | Index:  53 | Slot:  53 | Storage:  21.00 KB | Overwrites:   - | Hash Ops: 150450 | Time: 0.014s | ETA:  899.6s
[NODE-01] Block  54/500 | Index:  54 | Slot:  54 | Storage:  21.39 KB | Overwrites:   - | Hash Ops: 151196 | Time: 0.010s | ETA:  897.7s
[NODE-01] Block  55/500 | Index:  55 | Slot:  55 | Storage:  21.79 KB | Overwrites:   - | Hash Ops: 152199 | Time: 0.011s | ETA:  895.9s
[NODE-01] Block  56/500 | Index:  56 | Slot:  56 | Storage:  22.18 KB | Overwrites:   - | Hash Ops: 158414 | Time: 0.043s | ETA:  894.3s
[NODE-01] Block  57/500 | Index:  57 | Slot:  57 | Storage:  22.57 KB | Overwrites:   - | Hash Ops: 160684 | Time: 0.019s | ETA:  892.4s
[NODE-01] Block  58/500 | Index:  58 | Slot:  58 | Storage:  22.96 KB | Overwrites:   - | Hash Ops: 161750 | Time: 0.011s | ETA:  890.5s
[NODE-01] Block  59/500 | Index:  59 | Slot:  59 | Storage:  23.35 KB | Overwrites:   - | Hash Ops: 166491 | Time: 0.035s | ETA:  888.6s
[NODE-01] Block  60/500 | Index:  60 | Slot:  60 | Storage:  23.74 KB | Overwrites:   - | Hash Ops: 170200 | Time: 0.029s | ETA:  886.7s
[NODE-01] Block  61/500 | Index:  61 | Slot:  61 | Storage:  24.13 KB | Overwrites:   - | Hash Ops: 174877 | Time: 0.033s | ETA:  886.1s
[NODE-01] Block  62/500 | Index:  62 | Slot:  62 | Storage:  24.52 KB | Overwrites:   - | Hash Ops: 176412 | Time: 0.015s | ETA:  884.2s
[NODE-01] Block  63/500 | Index:  63 | Slot:  63 | Storage:  24.92 KB | Overwrites:   - | Hash Ops: 184803 | Time: 0.060s | ETA:  882.5s
[NODE-01] Block  64/500 | Index:  64 | Slot:  64 | Storage:  25.31 KB | Overwrites:   - | Hash Ops: 189028 | Time: 0.033s | ETA:  880.6s
[NODE-01] Block  65/500 | Index:  65 | Slot:  65 | Storage:  25.70 KB | Overwrites:   - | Hash Ops: 189919 | Time: 0.011s | ETA:  878.6s
[NODE-01] Block  66/500 | Index:  66 | Slot:  66 | Storage:  26.09 KB | Overwrites:   - | Hash Ops: 201005 | Time: 0.081s | ETA:  877.0s
[NODE-01] Block  67/500 | Index:  67 | Slot:  67 | Storage:  26.48 KB | Overwrites:   - | Hash Ops: 203436 | Time: 0.020s | ETA:  875.0s
[NODE-01] Block  68/500 | Index:  68 | Slot:  68 | Storage:  26.87 KB | Overwrites:   - | Hash Ops: 225037 | Time: 0.149s | ETA:  873.9s
[NODE-01] Block  69/500 | Index:  69 | Slot:  69 | Storage:  27.26 KB | Overwrites:   - | Hash Ops: 226742 | Time: 0.020s | ETA:  871.9s
[NODE-01] Block  70/500 | Index:  70 | Slot:  70 | Storage:  27.66 KB | Overwrites:   - | Hash Ops: 230062 | Time: 0.023s | ETA:  869.9s
[NODE-01] Block  71/500 | Index:  71 | Slot:  71 | Storage:  28.04 KB | Overwrites:   - | Hash Ops: 237676 | Time: 0.053s | ETA:  868.9s
[NODE-01] Block  72/500 | Index:  72 | Slot:  72 | Storage:  28.44 KB | Overwrites:   - | Hash Ops: 240417 | Time: 0.022s | ETA:  866.9s
[NODE-01] Block  73/500 | Index:  73 | Slot:  73 | Storage:  28.83 KB | Overwrites:   - | Hash Ops: 244792 | Time: 0.032s | ETA:  864.9s
[NODE-01] Block  74/500 | Index:  74 | Slot:  74 | Storage:  29.22 KB | Overwrites:   - | Hash Ops: 252775 | Time: 0.057s | ETA:  863.3s
[NODE-01] Block  75/500 | Index:  75 | Slot:  75 | Storage:  29.61 KB | Overwrites:   - | Hash Ops: 256520 | Time: 0.028s | ETA:  861.4s
[NODE-01] Block  76/500 | Index:  76 | Slot:  76 | Storage:  30.00 KB | Overwrites:   - | Hash Ops: 258127 | Time: 0.021s | ETA:  859.3s
[NODE-01] Block  77/500 | Index:  77 | Slot:  77 | Storage:  30.39 KB | Overwrites:   - | Hash Ops: 263479 | Time: 0.041s | ETA:  857.7s
[NODE-01] Block  78/500 | Index:  78 | Slot:  78 | Storage:  30.78 KB | Overwrites:   - | Hash Ops: 264371 | Time: 0.009s | ETA:  855.6s
[NODE-01] Block  79/500 | Index:  79 | Slot:  79 | Storage:  31.18 KB | Overwrites:   - | Hash Ops: 267029 | Time: 0.021s | ETA:  853.6s
[NODE-01] Block  80/500 | Index:  80 | Slot:  80 | Storage:  31.57 KB | Overwrites:   - | Hash Ops: 267826 | Time: 0.009s | ETA:  851.5s
[NODE-01] Block  81/500 | Index:  81 | Slot:  81 | Storage:  31.96 KB | Overwrites:   - | Hash Ops: 268726 | Time: 0.006s | ETA:  850.0s
[NODE-01] Block  82/500 | Index:  82 | Slot:  82 | Storage:  32.35 KB | Overwrites:   - | Hash Ops: 275154 | Time: 0.046s | ETA:  848.1s
[NODE-01] Block  83/500 | Index:  83 | Slot:  83 | Storage:  32.74 KB | Overwrites:   - | Hash Ops: 276180 | Time: 0.011s | ETA:  846.2s
[NODE-01] Block  84/500 | Index:  84 | Slot:  84 | Storage:  33.13 KB | Overwrites:   - | Hash Ops: 284608 | Time: 0.060s | ETA:  844.6s
[NODE-01] Block  85/500 | Index:  85 | Slot:  85 | Storage:  33.52 KB | Overwrites:   - | Hash Ops: 284869 | Time: 0.002s | ETA:  842.6s
[NODE-01] Block  86/500 | Index:  86 | Slot:  86 | Storage:  33.91 KB | Overwrites:   - | Hash Ops: 284995 | Time: 0.004s | ETA:  840.5s
[NODE-01] Block  87/500 | Index:  87 | Slot:  87 | Storage:  34.31 KB | Overwrites:   - | Hash Ops: 298137 | Time: 0.089s | ETA:  838.8s
[NODE-01] Block  88/500 | Index:  88 | Slot:  88 | Storage:  34.70 KB | Overwrites:   - | Hash Ops: 304012 | Time: 0.046s | ETA:  836.9s
[NODE-01] Block  89/500 | Index:  89 | Slot:  89 | Storage:  35.09 KB | Overwrites:   - | Hash Ops: 312144 | Time: 0.059s | ETA:  835.0s
[NODE-01] Block  90/500 | Index:  90 | Slot:  90 | Storage:  35.48 KB | Overwrites:   - | Hash Ops: 315888 | Time: 0.025s | ETA:  833.0s
[NODE-01] Block  91/500 | Index:  91 | Slot:  91 | Storage:  35.87 KB | Overwrites:   - | Hash Ops: 316012 | Time: 0.005s | ETA:  831.5s
[NODE-01] Block  92/500 | Index:  92 | Slot:  92 | Storage:  36.26 KB | Overwrites:   - | Hash Ops: 317434 | Time: 0.014s | ETA:  829.4s
[NODE-01] Block  93/500 | Index:  93 | Slot:  93 | Storage:  36.65 KB | Overwrites:   - | Hash Ops: 319868 | Time: 0.019s | ETA:  827.5s
[NODE-01] Block  94/500 | Index:  94 | Slot:  94 | Storage:  37.04 KB | Overwrites:   - | Hash Ops: 322891 | Time: 0.024s | ETA:  825.5s
[NODE-01] Block  95/500 | Index:  95 | Slot:  95 | Storage:  37.43 KB | Overwrites:   - | Hash Ops: 328178 | Time: 0.042s | ETA:  823.7s
[NODE-01] Block  96/500 | Index:  96 | Slot:  96 | Storage:  37.83 KB | Overwrites:   - | Hash Ops: 332258 | Time: 0.035s | ETA:  821.7s
[NODE-01] Block  97/500 | Index:  97 | Slot:  97 | Storage:  38.22 KB | Overwrites:   - | Hash Ops: 337764 | Time: 0.041s | ETA:  819.7s
[NODE-01] Block  98/500 | Index:  98 | Slot:  98 | Storage:  38.61 KB | Overwrites:   - | Hash Ops: 338574 | Time: 0.009s | ETA:  817.6s
[NODE-01] Block  99/500 | Index:  99 | Slot:  99 | Storage:  39.00 KB | Overwrites:   - | Hash Ops: 340491 | Time: 0.016s | ETA:  815.7s
[NODE-01] Block 100/500 | Index: 100 | Slot:   0 | Storage:  39.08 KB | Overwrites: Slot   0 | Hash Ops: 360121 | Time: 0.143s | ETA:  814.1s
[NODE-01] Block 101/500 | Index: 101 | Slot:   1 | Storage:  39.09 KB | Overwrites: Slot   1 | Hash Ops: 360201 | Time: 0.002s | ETA:  812.4s
[NODE-01] Block 102/500 | Index: 102 | Slot:   2 | Storage:  39.09 KB | Overwrites: Slot   2 | Hash Ops: 360604 | Time: 0.007s | ETA:  810.3s
[NODE-01] Block 103/500 | Index: 103 | Slot:   3 | Storage:  39.10 KB | Overwrites: Slot   3 | Hash Ops: 371045 | Time: 0.074s | ETA:  808.5s
[NODE-01] Block 104/500 | Index: 104 | Slot:   4 | Storage:  39.10 KB | Overwrites: Slot   4 | Hash Ops: 373886 | Time: 0.023s | ETA:  806.5s
[NODE-01] Block 105/500 | Index: 105 | Slot:   5 | Storage:  39.10 KB | Overwrites: Slot   5 | Hash Ops: 377563 | Time: 0.034s | ETA:  804.5s
[NODE-01] Block 106/500 | Index: 106 | Slot:   6 | Storage:  39.11 KB | Overwrites: Slot   6 | Hash Ops: 379537 | Time: 0.018s | ETA:  802.4s
[NODE-01] Block 107/500 | Index: 107 | Slot:   7 | Storage:  39.11 KB | Overwrites: Slot   7 | Hash Ops: 387058 | Time: 0.054s | ETA:  800.5s
[NODE-01] Block 108/500 | Index: 108 | Slot:   8 | Storage:  39.12 KB | Overwrites: Slot   8 | Hash Ops: 389662 | Time: 0.026s | ETA:  798.4s
[NODE-01] Block 109/500 | Index: 109 | Slot:   9 | Storage:  39.12 KB | Overwrites: Slot   9 | Hash Ops: 397030 | Time: 0.057s | ETA:  796.5s
[NODE-01] Block 110/500 | Index: 110 | Slot:  10 | Storage:  39.13 KB | Overwrites: Slot  10 | Hash Ops: 407282 | Time: 0.074s | ETA:  794.9s
[NODE-01] Block 111/500 | Index: 111 | Slot:  11 | Storage:  39.13 KB | Overwrites: Slot  11 | Hash Ops: 407657 | Time: 0.009s | ETA:  793.2s
[NODE-01] Block 112/500 | Index: 112 | Slot:  12 | Storage:  39.13 KB | Overwrites: Slot  12 | Hash Ops: 408946 | Time: 0.015s | ETA:  791.1s
[NODE-01] Block 113/500 | Index: 113 | Slot:  13 | Storage:  39.13 KB | Overwrites: Slot  13 | Hash Ops: 409202 | Time: 0.004s | ETA:  789.0s
[NODE-01] Block 114/500 | Index: 114 | Slot:  14 | Storage:  39.14 KB | Overwrites: Slot  14 | Hash Ops: 410305 | Time: 0.008s | ETA:  786.9s
[NODE-01] Block 115/500 | Index: 115 | Slot:  15 | Storage:  39.14 KB | Overwrites: Slot  15 | Hash Ops: 410459 | Time: 0.001s | ETA:  784.7s
[NODE-01] Block 116/500 | Index: 116 | Slot:  16 | Storage:  39.14 KB | Overwrites: Slot  16 | Hash Ops: 413357 | Time: 0.026s | ETA:  782.8s
[NODE-01] Block 117/500 | Index: 117 | Slot:  17 | Storage:  39.14 KB | Overwrites: Slot  17 | Hash Ops: 414999 | Time: 0.015s | ETA:  780.7s
[NODE-01] Block 118/500 | Index: 118 | Slot:  18 | Storage:  39.15 KB | Overwrites: Slot  18 | Hash Ops: 417214 | Time: 0.026s | ETA:  778.7s
[NODE-01] Block 119/500 | Index: 119 | Slot:  19 | Storage:  39.15 KB | Overwrites: Slot  19 | Hash Ops: 417287 | Time: 0.003s | ETA:  776.7s
[NODE-01] Block 120/500 | Index: 120 | Slot:  20 | Storage:  39.15 KB | Overwrites: Slot  20 | Hash Ops: 437567 | Time: 0.198s | ETA:  775.2s
[NODE-01] Block 121/500 | Index: 121 | Slot:  21 | Storage:  39.16 KB | Overwrites: Slot  21 | Hash Ops: 439560 | Time: 0.014s | ETA:  773.5s
[NODE-01] Block 122/500 | Index: 122 | Slot:  22 | Storage:  39.16 KB | Overwrites: Slot  22 | Hash Ops: 450864 | Time: 0.111s | ETA:  771.7s
[NODE-01] Block 123/500 | Index: 123 | Slot:  23 | Storage:  39.16 KB | Overwrites: Slot  23 | Hash Ops: 451060 | Time: 0.005s | ETA:  769.7s
[NODE-01] Block 124/500 | Index: 124 | Slot:  24 | Storage:  39.16 KB | Overwrites: Slot  24 | Hash Ops: 451748 | Time: 0.015s | ETA:  767.6s
[NODE-01] Block 125/500 | Index: 125 | Slot:  25 | Storage:  39.17 KB | Overwrites: Slot  25 | Hash Ops: 455669 | Time: 0.034s | ETA:  765.7s
[NODE-01] Block 126/500 | Index: 126 | Slot:  26 | Storage:  39.17 KB | Overwrites: Slot  26 | Hash Ops: 458908 | Time: 0.022s | ETA:  763.6s
[NODE-01] Block 127/500 | Index: 127 | Slot:  27 | Storage:  39.17 KB | Overwrites: Slot  27 | Hash Ops: 463353 | Time: 0.035s | ETA:  761.7s
[NODE-01] Block 128/500 | Index: 128 | Slot:  28 | Storage:  39.17 KB | Overwrites: Slot  28 | Hash Ops: 466019 | Time: 0.021s | ETA:  759.7s
[NODE-01] Block 129/500 | Index: 129 | Slot:  29 | Storage:  39.18 KB | Overwrites: Slot  29 | Hash Ops: 469463 | Time: 0.027s | ETA:  757.6s
[NODE-01] Block 130/500 | Index: 130 | Slot:  30 | Storage:  39.18 KB | Overwrites: Slot  30 | Hash Ops: 470998 | Time: 0.021s | ETA:  755.6s
[NODE-01] Block 131/500 | Index: 131 | Slot:  31 | Storage:  39.18 KB | Overwrites: Slot  31 | Hash Ops: 472803 | Time: 0.024s | ETA:  753.8s
[NODE-01] Block 132/500 | Index: 132 | Slot:  32 | Storage:  39.18 KB | Overwrites: Slot  32 | Hash Ops: 475261 | Time: 0.022s | ETA:  751.8s
[NODE-01] Block 133/500 | Index: 133 | Slot:  33 | Storage:  39.18 KB | Overwrites: Slot  33 | Hash Ops: 479235 | Time: 0.027s | ETA:  749.7s
[NODE-01] Block 134/500 | Index: 134 | Slot:  34 | Storage:  39.18 KB | Overwrites: Slot  34 | Hash Ops: 479740 | Time: 0.004s | ETA:  747.6s
[NODE-01] Block 135/500 | Index: 135 | Slot:  35 | Storage:  39.18 KB | Overwrites: Slot  35 | Hash Ops: 480319 | Time: 0.009s | ETA:  745.5s
[NODE-01] Block 136/500 | Index: 136 | Slot:  36 | Storage:  39.19 KB | Overwrites: Slot  36 | Hash Ops: 492615 | Time: 0.100s | ETA:  743.7s
[NODE-01] Block 137/500 | Index: 137 | Slot:  37 | Storage:  39.20 KB | Overwrites: Slot  37 | Hash Ops: 501799 | Time: 0.067s | ETA:  741.8s
[NODE-01] Block 138/500 | Index: 138 | Slot:  38 | Storage:  39.20 KB | Overwrites: Slot  38 | Hash Ops: 504303 | Time: 0.028s | ETA:  739.7s
[NODE-01] Block 139/500 | Index: 139 | Slot:  39 | Storage:  39.19 KB | Overwrites: Slot  39 | Hash Ops: 504393 | Time: 0.003s | ETA:  737.6s
[NODE-01] Block 140/500 | Index: 140 | Slot:  40 | Storage:  39.20 KB | Overwrites: Slot  40 | Hash Ops: 507182 | Time: 0.033s | ETA:  735.6s
[NODE-01] Block 141/500 | Index: 141 | Slot:  41 | Storage:  39.20 KB | Overwrites: Slot  41 | Hash Ops: 508352 | Time: 0.019s | ETA:  733.9s
[NODE-01] Block 142/500 | Index: 142 | Slot:  42 | Storage:  39.20 KB | Overwrites: Slot  42 | Hash Ops: 511869 | Time: 0.043s | ETA:  731.9s
[NODE-01] Block 143/500 | Index: 143 | Slot:  43 | Storage:  39.20 KB | Overwrites: Slot  43 | Hash Ops: 515282 | Time: 0.024s | ETA:  729.8s
[NODE-01] Block 144/500 | Index: 144 | Slot:  44 | Storage:  39.21 KB | Overwrites: Slot  44 | Hash Ops: 518420 | Time: 0.037s | ETA:  727.9s
[NODE-01] Block 145/500 | Index: 145 | Slot:  45 | Storage:  39.21 KB | Overwrites: Slot  45 | Hash Ops: 523843 | Time: 0.038s | ETA:  725.9s
[NODE-01] Block 146/500 | Index: 146 | Slot:  46 | Storage:  39.21 KB | Overwrites: Slot  46 | Hash Ops: 524629 | Time: 0.019s | ETA:  723.8s
[NODE-01] Block 147/500 | Index: 147 | Slot:  47 | Storage:  39.21 KB | Overwrites: Slot  47 | Hash Ops: 526151 | Time: 0.024s | ETA:  721.7s
[NODE-01] Block 148/500 | Index: 148 | Slot:  48 | Storage:  39.22 KB | Overwrites: Slot  48 | Hash Ops: 526334 | Time: 0.005s | ETA:  719.6s
[NODE-01] Block 149/500 | Index: 149 | Slot:  49 | Storage:  39.22 KB | Overwrites: Slot  49 | Hash Ops: 530149 | Time: 0.030s | ETA:  717.6s
[NODE-01] Block 150/500 | Index: 150 | Slot:  50 | Storage:  39.22 KB | Overwrites: Slot  50 | Hash Ops: 540944 | Time: 0.104s | ETA:  715.7s
[NODE-01] Block 151/500 | Index: 151 | Slot:  51 | Storage:  39.22 KB | Overwrites: Slot  51 | Hash Ops: 542484 | Time: 0.026s | ETA:  714.0s
[NODE-01] Block 152/500 | Index: 152 | Slot:  52 | Storage:  39.23 KB | Overwrites: Slot  52 | Hash Ops: 554878 | Time: 0.107s | ETA:  712.1s
[NODE-01] Block 153/500 | Index: 153 | Slot:  53 | Storage:  39.23 KB | Overwrites: Slot  53 | Hash Ops: 554999 | Time: 0.005s | ETA:  710.0s
[NODE-01] Block 154/500 | Index: 154 | Slot:  54 | Storage:  39.23 KB | Overwrites: Slot  54 | Hash Ops: 557489 | Time: 0.019s | ETA:  708.0s
[NODE-01] Block 155/500 | Index: 155 | Slot:  55 | Storage:  39.23 KB | Overwrites: Slot  55 | Hash Ops: 558623 | Time: 0.010s | ETA:  705.9s
[NODE-01] Block 156/500 | Index: 156 | Slot:  56 | Storage:  39.24 KB | Overwrites: Slot  56 | Hash Ops: 561714 | Time: 0.030s | ETA:  703.8s
[NODE-01] Block 157/500 | Index: 157 | Slot:  57 | Storage:  39.24 KB | Overwrites: Slot  57 | Hash Ops: 576639 | Time: 0.145s | ETA:  702.0s
[NODE-01] Block 158/500 | Index: 158 | Slot:  58 | Storage:  39.24 KB | Overwrites: Slot  58 | Hash Ops: 577582 | Time: 0.020s | ETA:  699.9s
[NODE-01] Block 159/500 | Index: 159 | Slot:  59 | Storage:  39.25 KB | Overwrites: Slot  59 | Hash Ops: 587378 | Time: 0.108s | ETA:  698.2s
[NODE-01] Block 160/500 | Index: 160 | Slot:  60 | Storage:  39.25 KB | Overwrites: Slot  60 | Hash Ops: 589043 | Time: 0.011s | ETA:  696.1s
[NODE-01] Block 161/500 | Index: 161 | Slot:  61 | Storage:  39.25 KB | Overwrites: Slot  61 | Hash Ops: 589479 | Time: 0.012s | ETA:  694.3s
[NODE-01] Block 162/500 | Index: 162 | Slot:  62 | Storage:  39.25 KB | Overwrites: Slot  62 | Hash Ops: 593803 | Time: 0.045s | ETA:  692.2s
[NODE-01] Block 163/500 | Index: 163 | Slot:  63 | Storage:  39.25 KB | Overwrites: Slot  63 | Hash Ops: 595938 | Time: 0.027s | ETA:  690.2s
[NODE-01] Block 164/500 | Index: 164 | Slot:  64 | Storage:  39.25 KB | Overwrites: Slot  64 | Hash Ops: 598306 | Time: 0.028s | ETA:  688.2s
[NODE-01] Block 165/500 | Index: 165 | Slot:  65 | Storage:  39.26 KB | Overwrites: Slot  65 | Hash Ops: 605218 | Time: 0.050s | ETA:  686.2s
[NODE-01] Block 166/500 | Index: 166 | Slot:  66 | Storage:  39.26 KB | Overwrites: Slot  66 | Hash Ops: 607705 | Time: 0.030s | ETA:  684.1s
[NODE-01] Block 167/500 | Index: 167 | Slot:  67 | Storage:  39.26 KB | Overwrites: Slot  67 | Hash Ops: 609320 | Time: 0.023s | ETA:  682.1s
[NODE-01] Block 168/500 | Index: 168 | Slot:  68 | Storage:  39.27 KB | Overwrites: Slot  68 | Hash Ops: 615817 | Time: 0.075s | ETA:  680.2s
[NODE-01] Block 169/500 | Index: 169 | Slot:  69 | Storage:  39.27 KB | Overwrites: Slot  69 | Hash Ops: 615878 | Time: 0.002s | ETA:  678.2s
[NODE-01] Block 170/500 | Index: 170 | Slot:  70 | Storage:  39.27 KB | Overwrites: Slot  70 | Hash Ops: 620076 | Time: 0.042s | ETA:  676.2s
[NODE-01] Block 171/500 | Index: 171 | Slot:  71 | Storage:  39.27 KB | Overwrites: Slot  71 | Hash Ops: 620275 | Time: 0.007s | ETA:  674.3s
[NODE-01] Block 172/500 | Index: 172 | Slot:  72 | Storage:  39.27 KB | Overwrites: Slot  72 | Hash Ops: 626468 | Time: 0.062s | ETA:  672.3s
[NODE-01] Block 173/500 | Index: 173 | Slot:  73 | Storage:  39.27 KB | Overwrites: Slot  73 | Hash Ops: 632841 | Time: 0.047s | ETA:  670.3s
[NODE-01] Block 174/500 | Index: 174 | Slot:  74 | Storage:  39.27 KB | Overwrites: Slot  74 | Hash Ops: 633513 | Time: 0.017s | ETA:  668.2s
[NODE-01] Block 175/500 | Index: 175 | Slot:  75 | Storage:  39.28 KB | Overwrites: Slot  75 | Hash Ops: 643156 | Time: 0.090s | ETA:  666.3s
[NODE-01] Block 176/500 | Index: 176 | Slot:  76 | Storage:  39.28 KB | Overwrites: Slot  76 | Hash Ops: 645587 | Time: 0.022s | ETA:  664.2s
[NODE-01] Block 177/500 | Index: 177 | Slot:  77 | Storage:  39.28 KB | Overwrites: Slot  77 | Hash Ops: 646018 | Time: 0.010s | ETA:  662.1s
[NODE-01] Block 178/500 | Index: 178 | Slot:  78 | Storage:  39.28 KB | Overwrites: Slot  78 | Hash Ops: 647511 | Time: 0.025s | ETA:  660.1s
[NODE-01] Block 179/500 | Index: 179 | Slot:  79 | Storage:  39.29 KB | Overwrites: Slot  79 | Hash Ops: 649590 | Time: 0.026s | ETA:  658.0s
[NODE-01] Block 180/500 | Index: 180 | Slot:  80 | Storage:  39.29 KB | Overwrites: Slot  80 | Hash Ops: 655319 | Time: 0.050s | ETA:  656.0s
[NODE-01] Block 181/500 | Index: 181 | Slot:  81 | Storage:  39.29 KB | Overwrites: Slot  81 | Hash Ops: 657223 | Time: 0.028s | ETA:  654.3s
[NODE-01] Block 182/500 | Index: 182 | Slot:  82 | Storage:  39.30 KB | Overwrites: Slot  82 | Hash Ops: 661691 | Time: 0.043s | ETA:  652.3s
[NODE-01] Block 183/500 | Index: 183 | Slot:  83 | Storage:  39.30 KB | Overwrites: Slot  83 | Hash Ops: 662377 | Time: 0.020s | ETA:  650.2s
[NODE-01] Block 184/500 | Index: 184 | Slot:  84 | Storage:  39.30 KB | Overwrites: Slot  84 | Hash Ops: 669732 | Time: 0.084s | ETA:  648.3s
[NODE-01] Block 185/500 | Index: 185 | Slot:  85 | Storage:  39.30 KB | Overwrites: Slot  85 | Hash Ops: 670081 | Time: 0.003s | ETA:  646.1s
[NODE-01] Block 186/500 | Index: 186 | Slot:  86 | Storage:  39.30 KB | Overwrites: Slot  86 | Hash Ops: 680926 | Time: 0.090s | ETA:  644.2s
[NODE-01] Block 187/500 | Index: 187 | Slot:  87 | Storage:  39.30 KB | Overwrites: Slot  87 | Hash Ops: 681463 | Time: 0.005s | ETA:  642.1s
[NODE-01] Block 188/500 | Index: 188 | Slot:  88 | Storage:  39.31 KB | Overwrites: Slot  88 | Hash Ops: 687587 | Time: 0.052s | ETA:  640.1s
[NODE-01] Block 189/500 | Index: 189 | Slot:  89 | Storage:  39.31 KB | Overwrites: Slot  89 | Hash Ops: 692121 | Time: 0.047s | ETA:  638.1s
[NODE-01] Block 190/500 | Index: 190 | Slot:  90 | Storage:  39.31 KB | Overwrites: Slot  90 | Hash Ops: 693078 | Time: 0.007s | ETA:  636.0s
[NODE-01] Block 191/500 | Index: 191 | Slot:  91 | Storage:  39.31 KB | Overwrites: Slot  91 | Hash Ops: 693428 | Time: 0.006s | ETA:  634.1s
[NODE-01] Block 192/500 | Index: 192 | Slot:  92 | Storage:  39.32 KB | Overwrites: Slot  92 | Hash Ops: 707738 | Time: 0.142s | ETA:  632.2s
[NODE-01] Block 193/500 | Index: 193 | Slot:  93 | Storage:  39.32 KB | Overwrites: Slot  93 | Hash Ops: 708176 | Time: 0.013s | ETA:  630.2s
[NODE-01] Block 194/500 | Index: 194 | Slot:  94 | Storage:  39.32 KB | Overwrites: Slot  94 | Hash Ops: 708226 | Time: 0.000s | ETA:  628.0s
[NODE-01] Block 195/500 | Index: 195 | Slot:  95 | Storage:  39.32 KB | Overwrites: Slot  95 | Hash Ops: 714199 | Time: 0.053s | ETA:  626.0s
[NODE-01] Block 196/500 | Index: 196 | Slot:  96 | Storage:  39.32 KB | Overwrites: Slot  96 | Hash Ops: 714487 | Time: 0.004s | ETA:  623.9s
[NODE-01] Block 197/500 | Index: 197 | Slot:  97 | Storage:  39.32 KB | Overwrites: Slot  97 | Hash Ops: 724806 | Time: 0.095s | ETA:  621.9s
[NODE-01] Block 198/500 | Index: 198 | Slot:  98 | Storage:  39.33 KB | Overwrites: Slot  98 | Hash Ops: 727102 | Time: 0.020s | ETA:  619.9s
[NODE-01] Block 199/500 | Index: 199 | Slot:  99 | Storage:  39.33 KB | Overwrites: Slot  99 | Hash Ops: 731746 | Time: 0.044s | ETA:  617.9s
[NODE-01] Block 200/500 | Index: 200 | Slot:   0 | Storage:  39.33 KB | Overwrites: Slot   0 | Hash Ops: 743883 | Time: 0.098s | ETA:  615.9s
[NODE-01] Block 201/500 | Index: 201 | Slot:   1 | Storage:  39.33 KB | Overwrites: Slot   1 | Hash Ops: 746843 | Time: 0.027s | ETA:  614.0s
[NODE-01] Block 202/500 | Index: 202 | Slot:   2 | Storage:  39.33 KB | Overwrites: Slot   2 | Hash Ops: 758103 | Time: 0.094s | ETA:  612.0s
[NODE-01] Block 203/500 | Index: 203 | Slot:   3 | Storage:  39.33 KB | Overwrites: Slot   3 | Hash Ops: 766732 | Time: 0.075s | ETA:  610.0s
[NODE-01] Block 204/500 | Index: 204 | Slot:   4 | Storage:  39.33 KB | Overwrites: Slot   4 | Hash Ops: 767703 | Time: 0.011s | ETA:  607.9s
[NODE-01] Block 205/500 | Index: 205 | Slot:   5 | Storage:  39.33 KB | Overwrites: Slot   5 | Hash Ops: 781360 | Time: 0.140s | ETA:  606.0s
[NODE-01] Block 206/500 | Index: 206 | Slot:   6 | Storage:  39.33 KB | Overwrites: Slot   6 | Hash Ops: 791860 | Time: 0.089s | ETA:  604.0s
[NODE-01] Block 207/500 | Index: 207 | Slot:   7 | Storage:  39.33 KB | Overwrites: Slot   7 | Hash Ops: 791925 | Time: 0.000s | ETA:  601.9s
[NODE-01] Block 208/500 | Index: 208 | Slot:   8 | Storage:  39.33 KB | Overwrites: Slot   8 | Hash Ops: 792029 | Time: 0.004s | ETA:  599.8s
[NODE-01] Block 209/500 | Index: 209 | Slot:   9 | Storage:  39.33 KB | Overwrites: Slot   9 | Hash Ops: 793420 | Time: 0.025s | ETA:  597.7s
[NODE-01] Block 210/500 | Index: 210 | Slot:  10 | Storage:  39.33 KB | Overwrites: Slot  10 | Hash Ops: 793917 | Time: 0.003s | ETA:  595.6s
[NODE-01] Block 211/500 | Index: 211 | Slot:  11 | Storage:  39.33 KB | Overwrites: Slot  11 | Hash Ops: 794661 | Time: 0.020s | ETA:  593.7s
[NODE-01] Block 212/500 | Index: 212 | Slot:  12 | Storage:  39.33 KB | Overwrites: Slot  12 | Hash Ops: 797978 | Time: 0.023s | ETA:  591.6s
[NODE-01] Block 213/500 | Index: 213 | Slot:  13 | Storage:  39.33 KB | Overwrites: Slot  13 | Hash Ops: 803377 | Time: 0.053s | ETA:  589.5s
[NODE-01] Block 214/500 | Index: 214 | Slot:  14 | Storage:  39.33 KB | Overwrites: Slot  14 | Hash Ops: 804377 | Time: 0.014s | ETA:  587.4s
[NODE-01] Block 215/500 | Index: 215 | Slot:  15 | Storage:  39.33 KB | Overwrites: Slot  15 | Hash Ops: 804675 | Time: 0.009s | ETA:  585.4s
[NODE-01] Block 216/500 | Index: 216 | Slot:  16 | Storage:  39.33 KB | Overwrites: Slot  16 | Hash Ops: 811069 | Time: 0.060s | ETA:  583.4s
[NODE-01] Block 217/500 | Index: 217 | Slot:  17 | Storage:  39.33 KB | Overwrites: Slot  17 | Hash Ops: 813472 | Time: 0.026s | ETA:  581.3s
[NODE-01] Block 218/500 | Index: 218 | Slot:  18 | Storage:  39.33 KB | Overwrites: Slot  18 | Hash Ops: 816380 | Time: 0.048s | ETA:  579.2s
[NODE-01] Block 219/500 | Index: 219 | Slot:  19 | Storage:  39.34 KB | Overwrites: Slot  19 | Hash Ops: 819532 | Time: 0.023s | ETA:  577.1s
[NODE-01] Block 220/500 | Index: 220 | Slot:  20 | Storage:  39.33 KB | Overwrites: Slot  20 | Hash Ops: 830104 | Time: 0.072s | ETA:  575.1s
[NODE-01] Block 221/500 | Index: 221 | Slot:  21 | Storage:  39.33 KB | Overwrites: Slot  21 | Hash Ops: 835483 | Time: 0.054s | ETA:  573.2s
[NODE-01] Block 222/500 | Index: 222 | Slot:  22 | Storage:  39.34 KB | Overwrites: Slot  22 | Hash Ops: 837916 | Time: 0.028s | ETA:  571.2s
[NODE-01] Block 223/500 | Index: 223 | Slot:  23 | Storage:  39.34 KB | Overwrites: Slot  23 | Hash Ops: 838811 | Time: 0.024s | ETA:  569.1s
[NODE-01] Block 224/500 | Index: 224 | Slot:  24 | Storage:  39.33 KB | Overwrites: Slot  24 | Hash Ops: 845513 | Time: 0.047s | ETA:  567.1s
[NODE-01] Block 225/500 | Index: 225 | Slot:  25 | Storage:  39.33 KB | Overwrites: Slot  25 | Hash Ops: 848703 | Time: 0.022s | ETA:  565.0s
[NODE-01] Block 226/500 | Index: 226 | Slot:  26 | Storage:  39.33 KB | Overwrites: Slot  26 | Hash Ops: 851726 | Time: 0.046s | ETA:  562.9s
[NODE-01] Block 227/500 | Index: 227 | Slot:  27 | Storage:  39.34 KB | Overwrites: Slot  27 | Hash Ops: 863838 | Time: 0.123s | ETA:  561.0s
[NODE-01] Block 228/500 | Index: 228 | Slot:  28 | Storage:  39.34 KB | Overwrites: Slot  28 | Hash Ops: 866219 | Time: 0.032s | ETA:  558.9s
[NODE-01] Block 229/500 | Index: 229 | Slot:  29 | Storage:  39.34 KB | Overwrites: Slot  29 | Hash Ops: 867247 | Time: 0.019s | ETA:  556.8s
[NODE-01] Block 230/500 | Index: 230 | Slot:  30 | Storage:  39.34 KB | Overwrites: Slot  30 | Hash Ops: 871343 | Time: 0.048s | ETA:  554.8s
[NODE-01] Block 231/500 | Index: 231 | Slot:  31 | Storage:  39.34 KB | Overwrites: Slot  31 | Hash Ops: 872576 | Time: 0.018s | ETA:  552.8s
[NODE-01] Block 232/500 | Index: 232 | Slot:  32 | Storage:  39.34 KB | Overwrites: Slot  32 | Hash Ops: 873505 | Time: 0.014s | ETA:  550.7s
[NODE-01] Block 233/500 | Index: 233 | Slot:  33 | Storage:  39.34 KB | Overwrites: Slot  33 | Hash Ops: 882494 | Time: 0.077s | ETA:  548.7s
[NODE-01] Block 234/500 | Index: 234 | Slot:  34 | Storage:  39.34 KB | Overwrites: Slot  34 | Hash Ops: 885833 | Time: 0.046s | ETA:  546.6s
[NODE-01] Block 235/500 | Index: 235 | Slot:  35 | Storage:  39.35 KB | Overwrites: Slot  35 | Hash Ops: 887549 | Time: 0.012s | ETA:  544.6s
[NODE-01] Block 236/500 | Index: 236 | Slot:  36 | Storage:  39.34 KB | Overwrites: Slot  36 | Hash Ops: 889703 | Time: 0.025s | ETA:  542.5s
[NODE-01] Block 237/500 | Index: 237 | Slot:  37 | Storage:  39.34 KB | Overwrites: Slot  37 | Hash Ops: 893259 | Time: 0.028s | ETA:  540.4s
[NODE-01] Block 238/500 | Index: 238 | Slot:  38 | Storage:  39.34 KB | Overwrites: Slot  38 | Hash Ops: 895080 | Time: 0.018s | ETA:  538.3s
[NODE-01] Block 239/500 | Index: 239 | Slot:  39 | Storage:  39.35 KB | Overwrites: Slot  39 | Hash Ops: 902331 | Time: 0.056s | ETA:  536.3s
[NODE-01] Block 240/500 | Index: 240 | Slot:  40 | Storage:  39.35 KB | Overwrites: Slot  40 | Hash Ops: 915793 | Time: 0.094s | ETA:  534.3s
[NODE-01] Block 241/500 | Index: 241 | Slot:  41 | Storage:  39.35 KB | Overwrites: Slot  41 | Hash Ops: 924027 | Time: 0.076s | ETA:  532.4s
[NODE-01] Block 242/500 | Index: 242 | Slot:  42 | Storage:  39.35 KB | Overwrites: Slot  42 | Hash Ops: 925018 | Time: 0.028s | ETA:  530.3s
[NODE-01] Block 243/500 | Index: 243 | Slot:  43 | Storage:  39.35 KB | Overwrites: Slot  43 | Hash Ops: 928649 | Time: 0.038s | ETA:  528.3s
[NODE-01] Block 244/500 | Index: 244 | Slot:  44 | Storage:  39.35 KB | Overwrites: Slot  44 | Hash Ops: 931399 | Time: 0.033s | ETA:  526.2s
[NODE-01] Block 245/500 | Index: 245 | Slot:  45 | Storage:  39.35 KB | Overwrites: Slot  45 | Hash Ops: 934864 | Time: 0.041s | ETA:  524.1s
[NODE-01] Block 246/500 | Index: 246 | Slot:  46 | Storage:  39.35 KB | Overwrites: Slot  46 | Hash Ops: 937749 | Time: 0.025s | ETA:  522.1s
[NODE-01] Block 247/500 | Index: 247 | Slot:  47 | Storage:  39.35 KB | Overwrites: Slot  47 | Hash Ops: 938519 | Time: 0.022s | ETA:  520.0s
[NODE-01] Block 248/500 | Index: 248 | Slot:  48 | Storage:  39.35 KB | Overwrites: Slot  48 | Hash Ops: 943800 | Time: 0.040s | ETA:  518.0s
[NODE-01] Block 249/500 | Index: 249 | Slot:  49 | Storage:  39.35 KB | Overwrites: Slot  49 | Hash Ops: 944464 | Time: 0.019s | ETA:  515.9s
[NODE-01] Block 250/500 | Index: 250 | Slot:  50 | Storage:  39.35 KB | Overwrites: Slot  50 | Hash Ops: 951887 | Time: 0.052s | ETA:  513.8s
[NODE-01] Block 251/500 | Index: 251 | Slot:  51 | Storage:  39.35 KB | Overwrites: Slot  51 | Hash Ops: 952468 | Time: 0.017s | ETA:  511.9s
[NODE-01] Block 252/500 | Index: 252 | Slot:  52 | Storage:  39.34 KB | Overwrites: Slot  52 | Hash Ops: 952490 | Time: 0.000s | ETA:  509.8s
[NODE-01] Block 253/500 | Index: 253 | Slot:  53 | Storage:  39.34 KB | Overwrites: Slot  53 | Hash Ops: 953571 | Time: 0.017s | ETA:  507.7s
[NODE-01] Block 254/500 | Index: 254 | Slot:  54 | Storage:  39.34 KB | Overwrites: Slot  54 | Hash Ops: 953703 | Time: 0.004s | ETA:  505.6s
[NODE-01] Block 255/500 | Index: 255 | Slot:  55 | Storage:  39.34 KB | Overwrites: Slot  55 | Hash Ops: 954180 | Time: 0.014s | ETA:  503.5s
[NODE-01] Block 256/500 | Index: 256 | Slot:  56 | Storage:  39.34 KB | Overwrites: Slot  56 | Hash Ops: 958300 | Time: 0.049s | ETA:  501.5s
[NODE-01] Block 257/500 | Index: 257 | Slot:  57 | Storage:  39.34 KB | Overwrites: Slot  57 | Hash Ops: 958791 | Time: 0.003s | ETA:  499.4s
[NODE-01] Block 258/500 | Index: 258 | Slot:  58 | Storage:  39.34 KB | Overwrites: Slot  58 | Hash Ops: 965228 | Time: 0.058s | ETA:  497.4s
[NODE-01] Block 259/500 | Index: 259 | Slot:  59 | Storage:  39.34 KB | Overwrites: Slot  59 | Hash Ops: 973144 | Time: 0.080s | ETA:  495.4s
[NODE-01] Block 260/500 | Index: 260 | Slot:  60 | Storage:  39.34 KB | Overwrites: Slot  60 | Hash Ops: 973517 | Time: 0.006s | ETA:  493.3s
[NODE-01] Block 261/500 | Index: 261 | Slot:  61 | Storage:  39.33 KB | Overwrites: Slot  61 | Hash Ops: 974130 | Time: 0.005s | ETA:  491.3s
[NODE-01] Block 262/500 | Index: 262 | Slot:  62 | Storage:  39.33 KB | Overwrites: Slot  62 | Hash Ops: 980628 | Time: 0.059s | ETA:  489.3s
[NODE-01] Block 263/500 | Index: 263 | Slot:  63 | Storage:  39.33 KB | Overwrites: Slot  63 | Hash Ops: 985218 | Time: 0.044s | ETA:  487.2s
[NODE-01] Block 264/500 | Index: 264 | Slot:  64 | Storage:  39.33 KB | Overwrites: Slot  64 | Hash Ops: 988434 | Time: 0.032s | ETA:  485.1s
[NODE-01] Block 265/500 | Index: 265 | Slot:  65 | Storage:  39.33 KB | Overwrites: Slot  65 | Hash Ops: 992211 | Time: 0.038s | ETA:  483.1s
[NODE-01] Block 266/500 | Index: 266 | Slot:  66 | Storage:  39.33 KB | Overwrites: Slot  66 | Hash Ops: 994327 | Time: 0.042s | ETA:  481.1s
[NODE-01] Block 267/500 | Index: 267 | Slot:  67 | Storage:  39.33 KB | Overwrites: Slot  67 | Hash Ops: 998362 | Time: 0.053s | ETA:  479.0s
[NODE-01] Block 268/500 | Index: 268 | Slot:  68 | Storage:  39.34 KB | Overwrites: Slot  68 | Hash Ops: 1008953 | Time: 0.091s | ETA:  477.0s
[NODE-01] Block 269/500 | Index: 269 | Slot:  69 | Storage:  39.34 KB | Overwrites: Slot  69 | Hash Ops: 1012860 | Time: 0.027s | ETA:  474.9s
[NODE-01] Block 270/500 | Index: 270 | Slot:  70 | Storage:  39.34 KB | Overwrites: Slot  70 | Hash Ops: 1013279 | Time: 0.003s | ETA:  472.8s
[NODE-01] Block 271/500 | Index: 271 | Slot:  71 | Storage:  39.34 KB | Overwrites: Slot  71 | Hash Ops: 1021185 | Time: 0.071s | ETA:  470.9s
[NODE-01] Block 272/500 | Index: 272 | Slot:  72 | Storage:  39.34 KB | Overwrites: Slot  72 | Hash Ops: 1024661 | Time: 0.074s | ETA:  468.9s
[NODE-01] Block 273/500 | Index: 273 | Slot:  73 | Storage:  39.34 KB | Overwrites: Slot  73 | Hash Ops: 1027393 | Time: 0.023s | ETA:  466.9s
[NODE-01] Block 274/500 | Index: 274 | Slot:  74 | Storage:  39.34 KB | Overwrites: Slot  74 | Hash Ops: 1030256 | Time: 0.032s | ETA:  464.8s
[NODE-01] Block 275/500 | Index: 275 | Slot:  75 | Storage:  39.34 KB | Overwrites: Slot  75 | Hash Ops: 1032583 | Time: 0.026s | ETA:  462.7s
[NODE-01] Block 276/500 | Index: 276 | Slot:  76 | Storage:  39.34 KB | Overwrites: Slot  76 | Hash Ops: 1036655 | Time: 0.036s | ETA:  460.7s
[NODE-01] Block 277/500 | Index: 277 | Slot:  77 | Storage:  39.34 KB | Overwrites: Slot  77 | Hash Ops: 1037028 | Time: 0.010s | ETA:  458.6s
[NODE-01] Block 278/500 | Index: 278 | Slot:  78 | Storage:  39.35 KB | Overwrites: Slot  78 | Hash Ops: 1053413 | Time: 0.128s | ETA:  456.6s
[NODE-01] Block 279/500 | Index: 279 | Slot:  79 | Storage:  39.35 KB | Overwrites: Slot  79 | Hash Ops: 1054524 | Time: 0.019s | ETA:  454.5s
[NODE-01] Block 280/500 | Index: 280 | Slot:  80 | Storage:  39.35 KB | Overwrites: Slot  80 | Hash Ops: 1056998 | Time: 0.028s | ETA:  452.4s
[NODE-01] Block 281/500 | Index: 281 | Slot:  81 | Storage:  39.35 KB | Overwrites: Slot  81 | Hash Ops: 1067386 | Time: 0.093s | ETA:  450.5s
[NODE-01] Block 282/500 | Index: 282 | Slot:  82 | Storage:  39.34 KB | Overwrites: Slot  82 | Hash Ops: 1067559 | Time: 0.005s | ETA:  448.4s
[NODE-01] Block 283/500 | Index: 283 | Slot:  83 | Storage:  39.35 KB | Overwrites: Slot  83 | Hash Ops: 1073122 | Time: 0.057s | ETA:  446.4s
[NODE-01] Block 284/500 | Index: 284 | Slot:  84 | Storage:  39.34 KB | Overwrites: Slot  84 | Hash Ops: 1078573 | Time: 0.040s | ETA:  444.3s
[NODE-01] Block 285/500 | Index: 285 | Slot:  85 | Storage:  39.35 KB | Overwrites: Slot  85 | Hash Ops: 1079093 | Time: 0.013s | ETA:  442.3s
[NODE-01] Block 286/500 | Index: 286 | Slot:  86 | Storage:  39.34 KB | Overwrites: Slot  86 | Hash Ops: 1085007 | Time: 0.053s | ETA:  440.2s
[NODE-01] Block 287/500 | Index: 287 | Slot:  87 | Storage:  39.34 KB | Overwrites: Slot  87 | Hash Ops: 1085105 | Time: 0.004s | ETA:  438.1s
[NODE-01] Block 288/500 | Index: 288 | Slot:  88 | Storage:  39.34 KB | Overwrites: Slot  88 | Hash Ops: 1085766 | Time: 0.005s | ETA:  436.1s
[NODE-01] Block 289/500 | Index: 289 | Slot:  89 | Storage:  39.34 KB | Overwrites: Slot  89 | Hash Ops: 1088741 | Time: 0.037s | ETA:  434.0s
[NODE-01] Block 290/500 | Index: 290 | Slot:  90 | Storage:  39.34 KB | Overwrites: Slot  90 | Hash Ops: 1096746 | Time: 0.070s | ETA:  432.0s
[NODE-01] Block 291/500 | Index: 291 | Slot:  91 | Storage:  39.34 KB | Overwrites: Slot  91 | Hash Ops: 1101241 | Time: 0.051s | ETA:  430.0s
[NODE-01] Block 292/500 | Index: 292 | Slot:  92 | Storage:  39.34 KB | Overwrites: Slot  92 | Hash Ops: 1104420 | Time: 0.045s | ETA:  428.0s
[NODE-01] Block 293/500 | Index: 293 | Slot:  93 | Storage:  39.34 KB | Overwrites: Slot  93 | Hash Ops: 1110341 | Time: 0.075s | ETA:  425.9s
[NODE-01] Block 294/500 | Index: 294 | Slot:  94 | Storage:  39.34 KB | Overwrites: Slot  94 | Hash Ops: 1115260 | Time: 0.050s | ETA:  423.9s
[NODE-01] Block 295/500 | Index: 295 | Slot:  95 | Storage:  39.34 KB | Overwrites: Slot  95 | Hash Ops: 1115693 | Time: 0.007s | ETA:  421.8s
[NODE-01] Block 296/500 | Index: 296 | Slot:  96 | Storage:  39.34 KB | Overwrites: Slot  96 | Hash Ops: 1118595 | Time: 0.029s | ETA:  419.7s
[NODE-01] Block 297/500 | Index: 297 | Slot:  97 | Storage:  39.34 KB | Overwrites: Slot  97 | Hash Ops: 1122666 | Time: 0.051s | ETA:  417.7s
[NODE-01] Block 298/500 | Index: 298 | Slot:  98 | Storage:  39.34 KB | Overwrites: Slot  98 | Hash Ops: 1123003 | Time: 0.008s | ETA:  415.6s
[NODE-01] Block 299/500 | Index: 299 | Slot:  99 | Storage:  39.34 KB | Overwrites: Slot  99 | Hash Ops: 1125054 | Time: 0.019s | ETA:  413.5s
[NODE-01] Block 300/500 | Index: 300 | Slot:   0 | Storage:  39.34 KB | Overwrites: Slot   0 | Hash Ops: 1125106 | Time: 0.001s | ETA:  411.4s
[NODE-01] Block 301/500 | Index: 301 | Slot:   1 | Storage:  39.34 KB | Overwrites: Slot   1 | Hash Ops: 1126785 | Time: 0.017s | ETA:  409.4s
[NODE-01] Block 302/500 | Index: 302 | Slot:   2 | Storage:  39.34 KB | Overwrites: Slot   2 | Hash Ops: 1131488 | Time: 0.037s | ETA:  407.4s
[NODE-01] Block 303/500 | Index: 303 | Slot:   3 | Storage:  39.34 KB | Overwrites: Slot   3 | Hash Ops: 1142527 | Time: 0.105s | ETA:  405.4s
[NODE-01] Block 304/500 | Index: 304 | Slot:   4 | Storage:  39.34 KB | Overwrites: Slot   4 | Hash Ops: 1143938 | Time: 0.025s | ETA:  403.3s
[NODE-01] Block 305/500 | Index: 305 | Slot:   5 | Storage:  39.34 KB | Overwrites: Slot   5 | Hash Ops: 1154181 | Time: 0.085s | ETA:  401.3s
[NODE-01] Block 306/500 | Index: 306 | Slot:   6 | Storage:  39.34 KB | Overwrites: Slot   6 | Hash Ops: 1155553 | Time: 0.010s | ETA:  399.2s
[NODE-01] Block 307/500 | Index: 307 | Slot:   7 | Storage:  39.34 KB | Overwrites: Slot   7 | Hash Ops: 1155750 | Time: 0.002s | ETA:  397.1s
[NODE-01] Block 308/500 | Index: 308 | Slot:   8 | Storage:  39.35 KB | Overwrites: Slot   8 | Hash Ops: 1158165 | Time: 0.031s | ETA:  395.1s
[NODE-01] Block 309/500 | Index: 309 | Slot:   9 | Storage:  39.35 KB | Overwrites: Slot   9 | Hash Ops: 1166567 | Time: 0.074s | ETA:  393.0s
[NODE-01] Block 310/500 | Index: 310 | Slot:  10 | Storage:  39.35 KB | Overwrites: Slot  10 | Hash Ops: 1166876 | Time: 0.010s | ETA:  391.0s
[NODE-01] Block 311/500 | Index: 311 | Slot:  11 | Storage:  39.35 KB | Overwrites: Slot  11 | Hash Ops: 1168145 | Time: 0.009s | ETA:  388.9s
[NODE-01] Block 312/500 | Index: 312 | Slot:  12 | Storage:  39.35 KB | Overwrites: Slot  12 | Hash Ops: 1168242 | Time: 0.005s | ETA:  386.9s
[NODE-01] Block 313/500 | Index: 313 | Slot:  13 | Storage:  39.35 KB | Overwrites: Slot  13 | Hash Ops: 1170941 | Time: 0.026s | ETA:  384.8s
[NODE-01] Block 314/500 | Index: 314 | Slot:  14 | Storage:  39.35 KB | Overwrites: Slot  14 | Hash Ops: 1172597 | Time: 0.015s | ETA:  382.7s
[NODE-01] Block 315/500 | Index: 315 | Slot:  15 | Storage:  39.35 KB | Overwrites: Slot  15 | Hash Ops: 1184067 | Time: 0.095s | ETA:  380.7s
[NODE-01] Block 316/500 | Index: 316 | Slot:  16 | Storage:  39.35 KB | Overwrites: Slot  16 | Hash Ops: 1193923 | Time: 0.087s | ETA:  378.7s
[NODE-01] Block 317/500 | Index: 317 | Slot:  17 | Storage:  39.35 KB | Overwrites: Slot  17 | Hash Ops: 1194886 | Time: 0.011s | ETA:  376.6s
[NODE-01] Block 318/500 | Index: 318 | Slot:  18 | Storage:  39.35 KB | Overwrites: Slot  18 | Hash Ops: 1198956 | Time: 0.037s | ETA:  374.6s
[NODE-01] Block 319/500 | Index: 319 | Slot:  19 | Storage:  39.35 KB | Overwrites: Slot  19 | Hash Ops: 1199377 | Time: 0.008s | ETA:  372.5s
[NODE-01] Block 320/500 | Index: 320 | Slot:  20 | Storage:  39.35 KB | Overwrites: Slot  20 | Hash Ops: 1200284 | Time: 0.017s | ETA:  370.4s
[NODE-01] Block 321/500 | Index: 321 | Slot:  21 | Storage:  39.35 KB | Overwrites: Slot  21 | Hash Ops: 1201570 | Time: 0.015s | ETA:  368.4s
[NODE-01] Block 322/500 | Index: 322 | Slot:  22 | Storage:  39.35 KB | Overwrites: Slot  22 | Hash Ops: 1215454 | Time: 0.110s | ETA:  366.4s
[NODE-01] Block 323/500 | Index: 323 | Slot:  23 | Storage:  39.35 KB | Overwrites: Slot  23 | Hash Ops: 1217735 | Time: 0.017s | ETA:  364.3s
[NODE-01] Block 324/500 | Index: 324 | Slot:  24 | Storage:  39.35 KB | Overwrites: Slot  24 | Hash Ops: 1220539 | Time: 0.028s | ETA:  362.3s
[NODE-01] Block 325/500 | Index: 325 | Slot:  25 | Storage:  39.35 KB | Overwrites: Slot  25 | Hash Ops: 1220615 | Time: 0.002s | ETA:  360.2s
[NODE-01] Block 326/500 | Index: 326 | Slot:  26 | Storage:  39.35 KB | Overwrites: Slot  26 | Hash Ops: 1222646 | Time: 0.017s | ETA:  358.1s
[NODE-01] Block 327/500 | Index: 327 | Slot:  27 | Storage:  39.35 KB | Overwrites: Slot  27 | Hash Ops: 1228286 | Time: 0.057s | ETA:  356.1s
[NODE-01] Block 328/500 | Index: 328 | Slot:  28 | Storage:  39.35 KB | Overwrites: Slot  28 | Hash Ops: 1231791 | Time: 0.035s | ETA:  354.0s
[NODE-01] Block 329/500 | Index: 329 | Slot:  29 | Storage:  39.35 KB | Overwrites: Slot  29 | Hash Ops: 1233978 | Time: 0.016s | ETA:  351.9s
[NODE-01] Block 330/500 | Index: 330 | Slot:  30 | Storage:  39.35 KB | Overwrites: Slot  30 | Hash Ops: 1241893 | Time: 0.078s | ETA:  349.9s
[NODE-01] Block 331/500 | Index: 331 | Slot:  31 | Storage:  39.35 KB | Overwrites: Slot  31 | Hash Ops: 1244439 | Time: 0.043s | ETA:  347.9s
[NODE-01] Block 332/500 | Index: 332 | Slot:  32 | Storage:  39.35 KB | Overwrites: Slot  32 | Hash Ops: 1248263 | Time: 0.026s | ETA:  345.8s
[NODE-01] Block 333/500 | Index: 333 | Slot:  33 | Storage:  39.35 KB | Overwrites: Slot  33 | Hash Ops: 1260806 | Time: 0.113s | ETA:  343.8s
[NODE-01] Block 334/500 | Index: 334 | Slot:  34 | Storage:  39.35 KB | Overwrites: Slot  34 | Hash Ops: 1261860 | Time: 0.007s | ETA:  341.7s
[NODE-01] Block 335/500 | Index: 335 | Slot:  35 | Storage:  39.35 KB | Overwrites: Slot  35 | Hash Ops: 1263104 | Time: 0.008s | ETA:  339.6s
[NODE-01] Block 336/500 | Index: 336 | Slot:  36 | Storage:  39.35 KB | Overwrites: Slot  36 | Hash Ops: 1265650 | Time: 0.031s | ETA:  337.6s
[NODE-01] Block 337/500 | Index: 337 | Slot:  37 | Storage:  39.35 KB | Overwrites: Slot  37 | Hash Ops: 1270046 | Time: 0.044s | ETA:  335.6s
[NODE-01] Block 338/500 | Index: 338 | Slot:  38 | Storage:  39.35 KB | Overwrites: Slot  38 | Hash Ops: 1273415 | Time: 0.025s | ETA:  333.5s
[NODE-01] Block 339/500 | Index: 339 | Slot:  39 | Storage:  39.35 KB | Overwrites: Slot  39 | Hash Ops: 1273630 | Time: 0.002s | ETA:  331.4s
[NODE-01] Block 340/500 | Index: 340 | Slot:  40 | Storage:  39.35 KB | Overwrites: Slot  40 | Hash Ops: 1278000 | Time: 0.035s | ETA:  329.3s
[NODE-01] Block 341/500 | Index: 341 | Slot:  41 | Storage:  39.35 KB | Overwrites: Slot  41 | Hash Ops: 1290907 | Time: 0.118s | ETA:  327.4s
[NODE-01] Block 342/500 | Index: 342 | Slot:  42 | Storage:  39.35 KB | Overwrites: Slot  42 | Hash Ops: 1290946 | Time: 0.002s | ETA:  325.3s
[NODE-01] Block 343/500 | Index: 343 | Slot:  43 | Storage:  39.35 KB | Overwrites: Slot  43 | Hash Ops: 1293290 | Time: 0.018s | ETA:  323.2s
[NODE-01] Block 344/500 | Index: 344 | Slot:  44 | Storage:  39.35 KB | Overwrites: Slot  44 | Hash Ops: 1293581 | Time: 0.011s | ETA:  321.1s
[NODE-01] Block 345/500 | Index: 345 | Slot:  45 | Storage:  39.35 KB | Overwrites: Slot  45 | Hash Ops: 1300529 | Time: 0.055s | ETA:  319.1s
[NODE-01] Block 346/500 | Index: 346 | Slot:  46 | Storage:  39.35 KB | Overwrites: Slot  46 | Hash Ops: 1307484 | Time: 0.062s | ETA:  317.0s
[NODE-01] Block 347/500 | Index: 347 | Slot:  47 | Storage:  39.35 KB | Overwrites: Slot  47 | Hash Ops: 1315078 | Time: 0.061s | ETA:  315.0s
[NODE-01] Block 348/500 | Index: 348 | Slot:  48 | Storage:  39.35 KB | Overwrites: Slot  48 | Hash Ops: 1324653 | Time: 0.083s | ETA:  313.0s
[NODE-01] Block 349/500 | Index: 349 | Slot:  49 | Storage:  39.35 KB | Overwrites: Slot  49 | Hash Ops: 1326382 | Time: 0.012s | ETA:  310.9s
[NODE-01] Block 350/500 | Index: 350 | Slot:  50 | Storage:  39.35 KB | Overwrites: Slot  50 | Hash Ops: 1327716 | Time: 0.026s | ETA:  308.8s
[NODE-01] Block 351/500 | Index: 351 | Slot:  51 | Storage:  39.35 KB | Overwrites: Slot  51 | Hash Ops: 1328416 | Time: 0.005s | ETA:  306.8s
[NODE-01] Block 352/500 | Index: 352 | Slot:  52 | Storage:  39.35 KB | Overwrites: Slot  52 | Hash Ops: 1334543 | Time: 0.065s | ETA:  304.7s
[NODE-01] Block 353/500 | Index: 353 | Slot:  53 | Storage:  39.35 KB | Overwrites: Slot  53 | Hash Ops: 1337655 | Time: 0.042s | ETA:  302.7s
[NODE-01] Block 354/500 | Index: 354 | Slot:  54 | Storage:  39.35 KB | Overwrites: Slot  54 | Hash Ops: 1339957 | Time: 0.019s | ETA:  300.6s
[NODE-01] Block 355/500 | Index: 355 | Slot:  55 | Storage:  39.35 KB | Overwrites: Slot  55 | Hash Ops: 1347824 | Time: 0.065s | ETA:  298.6s
[NODE-01] Block 356/500 | Index: 356 | Slot:  56 | Storage:  39.35 KB | Overwrites: Slot  56 | Hash Ops: 1348952 | Time: 0.011s | ETA:  296.5s
[NODE-01] Block 357/500 | Index: 357 | Slot:  57 | Storage:  39.35 KB | Overwrites: Slot  57 | Hash Ops: 1354777 | Time: 0.043s | ETA:  294.4s
[NODE-01] Block 358/500 | Index: 358 | Slot:  58 | Storage:  39.36 KB | Overwrites: Slot  58 | Hash Ops: 1356636 | Time: 0.027s | ETA:  292.4s
[NODE-01] Block 359/500 | Index: 359 | Slot:  59 | Storage:  39.36 KB | Overwrites: Slot  59 | Hash Ops: 1366004 | Time: 0.099s | ETA:  290.4s
[NODE-01] Block 360/500 | Index: 360 | Slot:  60 | Storage:  39.36 KB | Overwrites: Slot  60 | Hash Ops: 1367271 | Time: 0.020s | ETA:  288.3s
[NODE-01] Block 361/500 | Index: 361 | Slot:  61 | Storage:  39.36 KB | Overwrites: Slot  61 | Hash Ops: 1369342 | Time: 0.023s | ETA:  286.3s
[NODE-01] Block 362/500 | Index: 362 | Slot:  62 | Storage:  39.36 KB | Overwrites: Slot  62 | Hash Ops: 1374849 | Time: 0.043s | ETA:  284.2s
[NODE-01] Block 363/500 | Index: 363 | Slot:  63 | Storage:  39.36 KB | Overwrites: Slot  63 | Hash Ops: 1374902 | Time: 0.000s | ETA:  282.1s
[NODE-01] Block 364/500 | Index: 364 | Slot:  64 | Storage:  39.36 KB | Overwrites: Slot  64 | Hash Ops: 1375804 | Time: 0.020s | ETA:  280.1s
[NODE-01] Block 365/500 | Index: 365 | Slot:  65 | Storage:  39.36 KB | Overwrites: Slot  65 | Hash Ops: 1375933 | Time: 0.003s | ETA:  278.0s
[NODE-01] Block 366/500 | Index: 366 | Slot:  66 | Storage:  39.35 KB | Overwrites: Slot  66 | Hash Ops: 1376233 | Time: 0.006s | ETA:  275.9s
[NODE-01] Block 367/500 | Index: 367 | Slot:  67 | Storage:  39.36 KB | Overwrites: Slot  67 | Hash Ops: 1391817 | Time: 0.131s | ETA:  273.9s
[NODE-01] Block 368/500 | Index: 368 | Slot:  68 | Storage:  39.35 KB | Overwrites: Slot  68 | Hash Ops: 1392576 | Time: 0.008s | ETA:  271.8s
[NODE-01] Block 369/500 | Index: 369 | Slot:  69 | Storage:  39.35 KB | Overwrites: Slot  69 | Hash Ops: 1396704 | Time: 0.031s | ETA:  269.8s
[NODE-01] Block 370/500 | Index: 370 | Slot:  70 | Storage:  39.35 KB | Overwrites: Slot  70 | Hash Ops: 1397063 | Time: 0.005s | ETA:  267.7s
[NODE-01] Block 371/500 | Index: 371 | Slot:  71 | Storage:  39.35 KB | Overwrites: Slot  71 | Hash Ops: 1397078 | Time: 0.000s | ETA:  265.7s
[NODE-01] Block 372/500 | Index: 372 | Slot:  72 | Storage:  39.35 KB | Overwrites: Slot  72 | Hash Ops: 1398002 | Time: 0.010s | ETA:  263.6s
[NODE-01] Block 373/500 | Index: 373 | Slot:  73 | Storage:  39.35 KB | Overwrites: Slot  73 | Hash Ops: 1404553 | Time: 0.051s | ETA:  261.5s
[NODE-01] Block 374/500 | Index: 374 | Slot:  74 | Storage:  39.35 KB | Overwrites: Slot  74 | Hash Ops: 1405228 | Time: 0.005s | ETA:  259.5s
[NODE-01] Block 375/500 | Index: 375 | Slot:  75 | Storage:  39.35 KB | Overwrites: Slot  75 | Hash Ops: 1405374 | Time: 0.002s | ETA:  257.4s
[NODE-01] Block 376/500 | Index: 376 | Slot:  76 | Storage:  39.35 KB | Overwrites: Slot  76 | Hash Ops: 1407555 | Time: 0.017s | ETA:  255.3s
[NODE-01] Block 377/500 | Index: 377 | Slot:  77 | Storage:  39.35 KB | Overwrites: Slot  77 | Hash Ops: 1411832 | Time: 0.032s | ETA:  253.2s
[NODE-01] Block 378/500 | Index: 378 | Slot:  78 | Storage:  39.35 KB | Overwrites: Slot  78 | Hash Ops: 1416293 | Time: 0.042s | ETA:  251.2s
[NODE-01] Block 379/500 | Index: 379 | Slot:  79 | Storage:  39.35 KB | Overwrites: Slot  79 | Hash Ops: 1418654 | Time: 0.017s | ETA:  249.1s
[NODE-01] Block 380/500 | Index: 380 | Slot:  80 | Storage:  39.35 KB | Overwrites: Slot  80 | Hash Ops: 1419592 | Time: 0.013s | ETA:  247.1s
[NODE-01] Block 381/500 | Index: 381 | Slot:  81 | Storage:  39.35 KB | Overwrites: Slot  81 | Hash Ops: 1424649 | Time: 0.043s | ETA:  245.1s
[NODE-01] Block 382/500 | Index: 382 | Slot:  82 | Storage:  39.35 KB | Overwrites: Slot  82 | Hash Ops: 1428002 | Time: 0.042s | ETA:  243.0s
[NODE-01] Block 383/500 | Index: 383 | Slot:  83 | Storage:  39.35 KB | Overwrites: Slot  83 | Hash Ops: 1433704 | Time: 0.054s | ETA:  240.9s
[NODE-01] Block 384/500 | Index: 384 | Slot:  84 | Storage:  39.34 KB | Overwrites: Slot  84 | Hash Ops: 1434645 | Time: 0.024s | ETA:  238.9s
[NODE-01] Block 385/500 | Index: 385 | Slot:  85 | Storage:  39.34 KB | Overwrites: Slot  85 | Hash Ops: 1435107 | Time: 0.014s | ETA:  236.8s
[NODE-01] Block 386/500 | Index: 386 | Slot:  86 | Storage:  39.34 KB | Overwrites: Slot  86 | Hash Ops: 1435763 | Time: 0.016s | ETA:  234.7s
[NODE-01] Block 387/500 | Index: 387 | Slot:  87 | Storage:  39.35 KB | Overwrites: Slot  87 | Hash Ops: 1437217 | Time: 0.015s | ETA:  232.7s
[NODE-01] Block 388/500 | Index: 388 | Slot:  88 | Storage:  39.35 KB | Overwrites: Slot  88 | Hash Ops: 1451555 | Time: 0.119s | ETA:  230.6s
[NODE-01] Block 389/500 | Index: 389 | Slot:  89 | Storage:  39.35 KB | Overwrites: Slot  89 | Hash Ops: 1451902 | Time: 0.005s | ETA:  228.6s
[NODE-01] Block 390/500 | Index: 390 | Slot:  90 | Storage:  39.35 KB | Overwrites: Slot  90 | Hash Ops: 1462156 | Time: 0.075s | ETA:  226.5s
[NODE-01] Block 391/500 | Index: 391 | Slot:  91 | Storage:  39.35 KB | Overwrites: Slot  91 | Hash Ops: 1462821 | Time: 0.004s | ETA:  224.5s
[NODE-01] Block 392/500 | Index: 392 | Slot:  92 | Storage:  39.34 KB | Overwrites: Slot  92 | Hash Ops: 1465934 | Time: 0.043s | ETA:  222.4s
[NODE-01] Block 393/500 | Index: 393 | Slot:  93 | Storage:  39.35 KB | Overwrites: Slot  93 | Hash Ops: 1467123 | Time: 0.009s | ETA:  220.3s
[NODE-01] Block 394/500 | Index: 394 | Slot:  94 | Storage:  39.34 KB | Overwrites: Slot  94 | Hash Ops: 1467181 | Time: 0.003s | ETA:  218.3s
[NODE-01] Block 395/500 | Index: 395 | Slot:  95 | Storage:  39.35 KB | Overwrites: Slot  95 | Hash Ops: 1473744 | Time: 0.068s | ETA:  216.2s
[NODE-01] Block 396/500 | Index: 396 | Slot:  96 | Storage:  39.35 KB | Overwrites: Slot  96 | Hash Ops: 1477552 | Time: 0.051s | ETA:  214.2s
[NODE-01] Block 397/500 | Index: 397 | Slot:  97 | Storage:  39.35 KB | Overwrites: Slot  97 | Hash Ops: 1484596 | Time: 0.065s | ETA:  212.1s
[NODE-01] Block 398/500 | Index: 398 | Slot:  98 | Storage:  39.35 KB | Overwrites: Slot  98 | Hash Ops: 1486086 | Time: 0.024s | ETA:  210.0s
[NODE-01] Block 399/500 | Index: 399 | Slot:  99 | Storage:  39.35 KB | Overwrites: Slot  99 | Hash Ops: 1492798 | Time: 0.075s | ETA:  208.0s
[NODE-01] Block 400/500 | Index: 400 | Slot:   0 | Storage:  39.35 KB | Overwrites: Slot   0 | Hash Ops: 1494798 | Time: 0.029s | ETA:  205.9s
[NODE-01] Block 401/500 | Index: 401 | Slot:   1 | Storage:  39.35 KB | Overwrites: Slot   1 | Hash Ops: 1505916 | Time: 0.093s | ETA:  203.9s
[NODE-01] Block 402/500 | Index: 402 | Slot:   2 | Storage:  39.35 KB | Overwrites: Slot   2 | Hash Ops: 1511040 | Time: 0.035s | ETA:  201.8s
[NODE-01] Block 403/500 | Index: 403 | Slot:   3 | Storage:  39.34 KB | Overwrites: Slot   3 | Hash Ops: 1513547 | Time: 0.020s | ETA:  199.8s
[NODE-01] Block 404/500 | Index: 404 | Slot:   4 | Storage:  39.35 KB | Overwrites: Slot   4 | Hash Ops: 1515686 | Time: 0.019s | ETA:  197.8s
[NODE-01] Block 405/500 | Index: 405 | Slot:   5 | Storage:  39.34 KB | Overwrites: Slot   5 | Hash Ops: 1520177 | Time: 0.033s | ETA:  195.7s
[NODE-01] Block 406/500 | Index: 406 | Slot:   6 | Storage:  39.34 KB | Overwrites: Slot   6 | Hash Ops: 1527556 | Time: 0.063s | ETA:  193.6s
[NODE-01] Block 407/500 | Index: 407 | Slot:   7 | Storage:  39.35 KB | Overwrites: Slot   7 | Hash Ops: 1537698 | Time: 0.095s | ETA:  191.6s
[NODE-01] Block 408/500 | Index: 408 | Slot:   8 | Storage:  39.34 KB | Overwrites: Slot   8 | Hash Ops: 1541581 | Time: 0.043s | ETA:  189.5s
[NODE-01] Block 409/500 | Index: 409 | Slot:   9 | Storage:  39.34 KB | Overwrites: Slot   9 | Hash Ops: 1544708 | Time: 0.022s | ETA:  187.5s
[NODE-01] Block 410/500 | Index: 410 | Slot:  10 | Storage:  39.34 KB | Overwrites: Slot  10 | Hash Ops: 1544787 | Time: 0.001s | ETA:  185.4s
[NODE-01] Block 411/500 | Index: 411 | Slot:  11 | Storage:  39.34 KB | Overwrites: Slot  11 | Hash Ops: 1545442 | Time: 0.012s | ETA:  183.4s
[NODE-01] Block 412/500 | Index: 412 | Slot:  12 | Storage:  39.34 KB | Overwrites: Slot  12 | Hash Ops: 1548689 | Time: 0.058s | ETA:  181.3s
[NODE-01] Block 413/500 | Index: 413 | Slot:  13 | Storage:  39.34 KB | Overwrites: Slot  13 | Hash Ops: 1549302 | Time: 0.016s | ETA:  179.2s
[NODE-01] Block 414/500 | Index: 414 | Slot:  14 | Storage:  39.34 KB | Overwrites: Slot  14 | Hash Ops: 1558705 | Time: 0.064s | ETA:  177.2s
[NODE-01] Block 415/500 | Index: 415 | Slot:  15 | Storage:  39.34 KB | Overwrites: Slot  15 | Hash Ops: 1561501 | Time: 0.037s | ETA:  175.1s
[NODE-01] Block 416/500 | Index: 416 | Slot:  16 | Storage:  39.34 KB | Overwrites: Slot  16 | Hash Ops: 1561739 | Time: 0.003s | ETA:  173.1s
[NODE-01] Block 417/500 | Index: 417 | Slot:  17 | Storage:  39.34 KB | Overwrites: Slot  17 | Hash Ops: 1565372 | Time: 0.042s | ETA:  171.0s
[NODE-01] Block 418/500 | Index: 418 | Slot:  18 | Storage:  39.34 KB | Overwrites: Slot  18 | Hash Ops: 1575377 | Time: 0.077s | ETA:  168.9s
[NODE-01] Block 419/500 | Index: 419 | Slot:  19 | Storage:  39.34 KB | Overwrites: Slot  19 | Hash Ops: 1575690 | Time: 0.010s | ETA:  166.9s
[NODE-01] Block 420/500 | Index: 420 | Slot:  20 | Storage:  39.34 KB | Overwrites: Slot  20 | Hash Ops: 1576467 | Time: 0.017s | ETA:  164.8s
[NODE-01] Block 421/500 | Index: 421 | Slot:  21 | Storage:  39.34 KB | Overwrites: Slot  21 | Hash Ops: 1577929 | Time: 0.028s | ETA:  162.8s
[NODE-01] Block 422/500 | Index: 422 | Slot:  22 | Storage:  39.34 KB | Overwrites: Slot  22 | Hash Ops: 1578677 | Time: 0.017s | ETA:  160.7s
[NODE-01] Block 423/500 | Index: 423 | Slot:  23 | Storage:  39.34 KB | Overwrites: Slot  23 | Hash Ops: 1583233 | Time: 0.044s | ETA:  158.7s
[NODE-01] Block 424/500 | Index: 424 | Slot:  24 | Storage:  39.34 KB | Overwrites: Slot  24 | Hash Ops: 1584831 | Time: 0.036s | ETA:  156.6s
[NODE-01] Block 425/500 | Index: 425 | Slot:  25 | Storage:  39.34 KB | Overwrites: Slot  25 | Hash Ops: 1587985 | Time: 0.022s | ETA:  154.5s
[NODE-01] Block 426/500 | Index: 426 | Slot:  26 | Storage:  39.34 KB | Overwrites: Slot  26 | Hash Ops: 1598778 | Time: 0.089s | ETA:  152.5s
[NODE-01] Block 427/500 | Index: 427 | Slot:  27 | Storage:  39.34 KB | Overwrites: Slot  27 | Hash Ops: 1602208 | Time: 0.025s | ETA:  150.4s
[NODE-01] Block 428/500 | Index: 428 | Slot:  28 | Storage:  39.34 KB | Overwrites: Slot  28 | Hash Ops: 1603568 | Time: 0.035s | ETA:  148.4s
[NODE-01] Block 429/500 | Index: 429 | Slot:  29 | Storage:  39.34 KB | Overwrites: Slot  29 | Hash Ops: 1605631 | Time: 0.035s | ETA:  146.3s
[NODE-01] Block 430/500 | Index: 430 | Slot:  30 | Storage:  39.34 KB | Overwrites: Slot  30 | Hash Ops: 1607661 | Time: 0.020s | ETA:  144.2s
[NODE-01] Block 431/500 | Index: 431 | Slot:  31 | Storage:  39.34 KB | Overwrites: Slot  31 | Hash Ops: 1609192 | Time: 0.014s | ETA:  142.2s
[NODE-01] Block 432/500 | Index: 432 | Slot:  32 | Storage:  39.34 KB | Overwrites: Slot  32 | Hash Ops: 1616793 | Time: 0.058s | ETA:  140.1s
[NODE-01] Block 433/500 | Index: 433 | Slot:  33 | Storage:  39.34 KB | Overwrites: Slot  33 | Hash Ops: 1617454 | Time: 0.005s | ETA:  138.1s
[NODE-01] Block 434/500 | Index: 434 | Slot:  34 | Storage:  39.34 KB | Overwrites: Slot  34 | Hash Ops: 1619255 | Time: 0.016s | ETA:  136.0s
[NODE-01] Block 435/500 | Index: 435 | Slot:  35 | Storage:  39.34 KB | Overwrites: Slot  35 | Hash Ops: 1623030 | Time: 0.031s | ETA:  134.0s
[NODE-01] Block 436/500 | Index: 436 | Slot:  36 | Storage:  39.34 KB | Overwrites: Slot  36 | Hash Ops: 1623779 | Time: 0.015s | ETA:  131.9s
[NODE-01] Block 437/500 | Index: 437 | Slot:  37 | Storage:  39.34 KB | Overwrites: Slot  37 | Hash Ops: 1626708 | Time: 0.042s | ETA:  129.8s
[NODE-01] Block 438/500 | Index: 438 | Slot:  38 | Storage:  39.33 KB | Overwrites: Slot  38 | Hash Ops: 1628080 | Time: 0.020s | ETA:  127.8s
[NODE-01] Block 439/500 | Index: 439 | Slot:  39 | Storage:  39.34 KB | Overwrites: Slot  39 | Hash Ops: 1630051 | Time: 0.024s | ETA:  125.7s
[NODE-01] Block 440/500 | Index: 440 | Slot:  40 | Storage:  39.33 KB | Overwrites: Slot  40 | Hash Ops: 1631276 | Time: 0.021s | ETA:  123.6s
[NODE-01] Block 441/500 | Index: 441 | Slot:  41 | Storage:  39.33 KB | Overwrites: Slot  41 | Hash Ops: 1635339 | Time: 0.037s | ETA:  121.6s
[NODE-01] Block 442/500 | Index: 442 | Slot:  42 | Storage:  39.33 KB | Overwrites: Slot  42 | Hash Ops: 1643305 | Time: 0.059s | ETA:  119.5s
[NODE-01] Block 443/500 | Index: 443 | Slot:  43 | Storage:  39.33 KB | Overwrites: Slot  43 | Hash Ops: 1644937 | Time: 0.018s | ETA:  117.5s
[NODE-01] Block 444/500 | Index: 444 | Slot:  44 | Storage:  39.33 KB | Overwrites: Slot  44 | Hash Ops: 1645114 | Time: 0.005s | ETA:  115.4s
[NODE-01] Block 445/500 | Index: 445 | Slot:  45 | Storage:  39.33 KB | Overwrites: Slot  45 | Hash Ops: 1658443 | Time: 0.124s | ETA:  113.4s
[NODE-01] Block 446/500 | Index: 446 | Slot:  46 | Storage:  39.33 KB | Overwrites: Slot  46 | Hash Ops: 1659861 | Time: 0.021s | ETA:  111.3s
[NODE-01] Block 447/500 | Index: 447 | Slot:  47 | Storage:  39.33 KB | Overwrites: Slot  47 | Hash Ops: 1660710 | Time: 0.020s | ETA:  109.2s
[NODE-01] Block 448/500 | Index: 448 | Slot:  48 | Storage:  39.33 KB | Overwrites: Slot  48 | Hash Ops: 1665678 | Time: 0.038s | ETA:  107.2s
[NODE-01] Block 449/500 | Index: 449 | Slot:  49 | Storage:  39.33 KB | Overwrites: Slot  49 | Hash Ops: 1666703 | Time: 0.020s | ETA:  105.1s
[NODE-01] Block 450/500 | Index: 450 | Slot:  50 | Storage:  39.33 KB | Overwrites: Slot  50 | Hash Ops: 1669280 | Time: 0.025s | ETA:  103.1s
[NODE-01] Block 451/500 | Index: 451 | Slot:  51 | Storage:  39.33 KB | Overwrites: Slot  51 | Hash Ops: 1673830 | Time: 0.032s | ETA:  101.0s
[NODE-01] Block 452/500 | Index: 452 | Slot:  52 | Storage:  39.33 KB | Overwrites: Slot  52 | Hash Ops: 1675938 | Time: 0.018s | ETA:   98.9s
[NODE-01] Block 453/500 | Index: 453 | Slot:  53 | Storage:  39.33 KB | Overwrites: Slot  53 | Hash Ops: 1682768 | Time: 0.060s | ETA:   96.9s
[NODE-01] Block 454/500 | Index: 454 | Slot:  54 | Storage:  39.33 KB | Overwrites: Slot  54 | Hash Ops: 1697028 | Time: 0.117s | ETA:   94.8s
[NODE-01] Block 455/500 | Index: 455 | Slot:  55 | Storage:  39.34 KB | Overwrites: Slot  55 | Hash Ops: 1699550 | Time: 0.021s | ETA:   92.8s
[NODE-01] Block 456/500 | Index: 456 | Slot:  56 | Storage:  39.34 KB | Overwrites: Slot  56 | Hash Ops: 1701648 | Time: 0.015s | ETA:   90.7s
[NODE-01] Block 457/500 | Index: 457 | Slot:  57 | Storage:  39.34 KB | Overwrites: Slot  57 | Hash Ops: 1715017 | Time: 0.108s | ETA:   88.6s
[NODE-01] Block 458/500 | Index: 458 | Slot:  58 | Storage:  39.34 KB | Overwrites: Slot  58 | Hash Ops: 1716391 | Time: 0.024s | ETA:   86.6s
[NODE-01] Block 459/500 | Index: 459 | Slot:  59 | Storage:  39.34 KB | Overwrites: Slot  59 | Hash Ops: 1723242 | Time: 0.052s | ETA:   84.5s
[NODE-01] Block 460/500 | Index: 460 | Slot:  60 | Storage:  39.34 KB | Overwrites: Slot  60 | Hash Ops: 1729382 | Time: 0.058s | ETA:   82.5s
[NODE-01] Block 461/500 | Index: 461 | Slot:  61 | Storage:  39.34 KB | Overwrites: Slot  61 | Hash Ops: 1736319 | Time: 0.053s | ETA:   80.4s
[NODE-01] Block 462/500 | Index: 462 | Slot:  62 | Storage:  39.34 KB | Overwrites: Slot  62 | Hash Ops: 1741020 | Time: 0.055s | ETA:   78.3s
[NODE-01] Block 463/500 | Index: 463 | Slot:  63 | Storage:  39.34 KB | Overwrites: Slot  63 | Hash Ops: 1747149 | Time: 0.058s | ETA:   76.3s
[NODE-01] Block 464/500 | Index: 464 | Slot:  64 | Storage:  39.34 KB | Overwrites: Slot  64 | Hash Ops: 1748220 | Time: 0.011s | ETA:   74.2s
[NODE-01] Block 465/500 | Index: 465 | Slot:  65 | Storage:  39.34 KB | Overwrites: Slot  65 | Hash Ops: 1752947 | Time: 0.046s | ETA:   72.2s
[NODE-01] Block 466/500 | Index: 466 | Slot:  66 | Storage:  39.34 KB | Overwrites: Slot  66 | Hash Ops: 1759158 | Time: 0.069s | ETA:   70.1s
[NODE-01] Block 467/500 | Index: 467 | Slot:  67 | Storage:  39.34 KB | Overwrites: Slot  67 | Hash Ops: 1759492 | Time: 0.010s | ETA:   68.0s
[NODE-01] Block 468/500 | Index: 468 | Slot:  68 | Storage:  39.34 KB | Overwrites: Slot  68 | Hash Ops: 1761470 | Time: 0.017s | ETA:   66.0s
[NODE-01] Block 469/500 | Index: 469 | Slot:  69 | Storage:  39.34 KB | Overwrites: Slot  69 | Hash Ops: 1762731 | Time: 0.011s | ETA:   63.9s
[NODE-01] Block 470/500 | Index: 470 | Slot:  70 | Storage:  39.34 KB | Overwrites: Slot  70 | Hash Ops: 1767906 | Time: 0.048s | ETA:   61.8s
[NODE-01] Block 471/500 | Index: 471 | Slot:  71 | Storage:  39.34 KB | Overwrites: Slot  71 | Hash Ops: 1770399 | Time: 0.017s | ETA:   59.8s
[NODE-01] Block 472/500 | Index: 472 | Slot:  72 | Storage:  39.35 KB | Overwrites: Slot  72 | Hash Ops: 1783107 | Time: 0.090s | ETA:   57.7s
[NODE-01] Block 473/500 | Index: 473 | Slot:  73 | Storage:  39.35 KB | Overwrites: Slot  73 | Hash Ops: 1787793 | Time: 0.059s | ETA:   55.7s
[NODE-01] Block 474/500 | Index: 474 | Slot:  74 | Storage:  39.35 KB | Overwrites: Slot  74 | Hash Ops: 1791071 | Time: 0.051s | ETA:   53.6s
[NODE-01] Block 475/500 | Index: 475 | Slot:  75 | Storage:  39.35 KB | Overwrites: Slot  75 | Hash Ops: 1792020 | Time: 0.010s | ETA:   51.5s
[NODE-01] Block 476/500 | Index: 476 | Slot:  76 | Storage:  39.35 KB | Overwrites: Slot  76 | Hash Ops: 1792898 | Time: 0.017s | ETA:   49.5s
[NODE-01] Block 477/500 | Index: 477 | Slot:  77 | Storage:  39.35 KB | Overwrites: Slot  77 | Hash Ops: 1799181 | Time: 0.048s | ETA:   47.4s
[NODE-01] Block 478/500 | Index: 478 | Slot:  78 | Storage:  39.35 KB | Overwrites: Slot  78 | Hash Ops: 1801010 | Time: 0.021s | ETA:   45.4s
[NODE-01] Block 479/500 | Index: 479 | Slot:  79 | Storage:  39.35 KB | Overwrites: Slot  79 | Hash Ops: 1802679 | Time: 0.023s | ETA:   43.3s
[NODE-01] Block 480/500 | Index: 480 | Slot:  80 | Storage:  39.35 KB | Overwrites: Slot  80 | Hash Ops: 1806674 | Time: 0.032s | ETA:   41.2s
[NODE-01] Block 481/500 | Index: 481 | Slot:  81 | Storage:  39.34 KB | Overwrites: Slot  81 | Hash Ops: 1807300 | Time: 0.016s | ETA:   39.2s
[NODE-01] Block 482/500 | Index: 482 | Slot:  82 | Storage:  39.35 KB | Overwrites: Slot  82 | Hash Ops: 1808184 | Time: 0.017s | ETA:   37.1s
[NODE-01] Block 483/500 | Index: 483 | Slot:  83 | Storage:  39.35 KB | Overwrites: Slot  83 | Hash Ops: 1811533 | Time: 0.025s | ETA:   35.1s
[NODE-01] Block 484/500 | Index: 484 | Slot:  84 | Storage:  39.35 KB | Overwrites: Slot  84 | Hash Ops: 1813226 | Time: 0.024s | ETA:   33.0s
[NODE-01] Block 485/500 | Index: 485 | Slot:  85 | Storage:  39.35 KB | Overwrites: Slot  85 | Hash Ops: 1814674 | Time: 0.020s | ETA:   30.9s
[NODE-01] Block 486/500 | Index: 486 | Slot:  86 | Storage:  39.35 KB | Overwrites: Slot  86 | Hash Ops: 1824616 | Time: 0.089s | ETA:   28.9s
[NODE-01] Block 487/500 | Index: 487 | Slot:  87 | Storage:  39.35 KB | Overwrites: Slot  87 | Hash Ops: 1825522 | Time: 0.006s | ETA:   26.8s
[NODE-01] Block 488/500 | Index: 488 | Slot:  88 | Storage:  39.35 KB | Overwrites: Slot  88 | Hash Ops: 1830467 | Time: 0.035s | ETA:   24.7s
[NODE-01] Block 489/500 | Index: 489 | Slot:  89 | Storage:  39.35 KB | Overwrites: Slot  89 | Hash Ops: 1830871 | Time: 0.013s | ETA:   22.7s
[NODE-01] Block 490/500 | Index: 490 | Slot:  90 | Storage:  39.35 KB | Overwrites: Slot  90 | Hash Ops: 1833283 | Time: 0.020s | ETA:   20.6s
[NODE-01] Block 491/500 | Index: 491 | Slot:  91 | Storage:  39.36 KB | Overwrites: Slot  91 | Hash Ops: 1840781 | Time: 0.055s | ETA:   18.6s
[NODE-01] Block 492/500 | Index: 492 | Slot:  92 | Storage:  39.36 KB | Overwrites: Slot  92 | Hash Ops: 1842767 | Time: 0.022s | ETA:   16.5s
[NODE-01] Block 493/500 | Index: 493 | Slot:  93 | Storage:  39.36 KB | Overwrites: Slot  93 | Hash Ops: 1845056 | Time: 0.022s | ETA:   14.4s
[NODE-01] Block 494/500 | Index: 494 | Slot:  94 | Storage:  39.36 KB | Overwrites: Slot  94 | Hash Ops: 1845057 | Time: 0.000s | ETA:   12.4s
[NODE-01] Block 495/500 | Index: 495 | Slot:  95 | Storage:  39.36 KB | Overwrites: Slot  95 | Hash Ops: 1846177 | Time: 0.019s | ETA:   10.3s
[NODE-01] Block 496/500 | Index: 496 | Slot:  96 | Storage:  39.36 KB | Overwrites: Slot  96 | Hash Ops: 1847862 | Time: 0.013s | ETA:    8.2s
[NODE-01] Block 497/500 | Index: 497 | Slot:  97 | Storage:  39.36 KB | Overwrites: Slot  97 | Hash Ops: 1856119 | Time: 0.079s | ETA:    6.2s
[NODE-01] Block 498/500 | Index: 498 | Slot:  98 | Storage:  39.36 KB | Overwrites: Slot  98 | Hash Ops: 1861555 | Time: 0.073s | ETA:    4.1s
[NODE-01] Block 499/500 | Index: 499 | Slot:  99 | Storage:  39.36 KB | Overwrites: Slot  99 | Hash Ops: 1862592 | Time: 0.015s | ETA:    2.1s
[NODE-01] Block 500/500 | Index: 500 | Slot:   0 | Storage:  39.36 KB | Overwrites: Slot   0 | Hash Ops: 1865498 | Time: 0.025s | ETA:    0.0s
[NODE-01] Peer connections restored
[NODE-01] Completed in 1032.79 seconds

================================================================================
Resetting NODE-02 to genesis before its simulation
================================================================================
✓ NODE-02 reset to genesis (index=0)


[NODE-02] Starting block generation...
[NODE-02] Initial ledger state:
[NODE-02]   Last index: 0
[NODE-02]   Genesis hash: 000ac6d79f7c53bb...
[NODE-02] Target: 500 blocks
[NODE-02] Mode: Independent (no peer interaction)
[NODE-02] Peers temporarily disconnected for independent simulation
[NODE-02] Block   1/500 | Index:   1 | Slot:   1 | Storage:   0.70 KB | Overwrites:   - | Hash Ops:    970 | Time: 0.015s | ETA:   57.8s
[NODE-02] Block   2/500 | Index:   2 | Slot:   2 | Storage:   1.09 KB | Overwrites:   - | Hash Ops:   3285 | Time: 0.032s | ETA:  535.5s
[NODE-02] Block   3/500 | Index:   3 | Slot:   3 | Storage:   1.48 KB | Overwrites:   - | Hash Ops:   8308 | Time: 0.045s | ETA:  699.1s
[NODE-02] Block   4/500 | Index:   4 | Slot:   4 | Storage:   1.87 KB | Overwrites:   - | Hash Ops:   8765 | Time: 0.007s | ETA:  772.6s
[NODE-02] Block   5/500 | Index:   5 | Slot:   5 | Storage:   2.26 KB | Overwrites:   - | Hash Ops:  12290 | Time: 0.024s | ETA:  817.4s
[NODE-02] Block   6/500 | Index:   6 | Slot:   6 | Storage:   2.64 KB | Overwrites:   - | Hash Ops:  12656 | Time: 0.003s | ETA:  844.7s
[NODE-02] Block   7/500 | Index:   7 | Slot:   7 | Storage:   3.03 KB | Overwrites:   - | Hash Ops:  32157 | Time: 0.167s | ETA:  875.6s
[NODE-02] Block   8/500 | Index:   8 | Slot:   8 | Storage:   3.42 KB | Overwrites:   - | Hash Ops:  32420 | Time: 0.009s | ETA:  888.3s
[NODE-02] Block   9/500 | Index:   9 | Slot:   9 | Storage:   3.81 KB | Overwrites:   - | Hash Ops:  36471 | Time: 0.048s | ETA:  900.4s
[NODE-02] Block  10/500 | Index:  10 | Slot:  10 | Storage:   4.20 KB | Overwrites:   - | Hash Ops:  36960 | Time: 0.003s | ETA:  908.2s
[NODE-02] Block  11/500 | Index:  11 | Slot:  11 | Storage:   4.59 KB | Overwrites:   - | Hash Ops:  40358 | Time: 0.038s | ETA:  920.8s
[NODE-02] Block  12/500 | Index:  12 | Slot:  12 | Storage:   4.98 KB | Overwrites:   - | Hash Ops:  50531 | Time: 0.093s | ETA:  928.1s
[NODE-02] Block  13/500 | Index:  13 | Slot:  13 | Storage:   5.37 KB | Overwrites:   - | Hash Ops:  50592 | Time: 0.003s | ETA:  931.0s
[NODE-02] Block  14/500 | Index:  14 | Slot:  14 | Storage:   5.76 KB | Overwrites:   - | Hash Ops:  51087 | Time: 0.004s | ETA:  932.5s
[NODE-02] Block  15/500 | Index:  15 | Slot:  15 | Storage:   6.15 KB | Overwrites:   - | Hash Ops:  60379 | Time: 0.086s | ETA:  936.6s
[NODE-02] Block  16/500 | Index:  16 | Slot:  16 | Storage:   6.54 KB | Overwrites:   - | Hash Ops:  68740 | Time: 0.058s | ETA:  939.1s
[NODE-02] Block  17/500 | Index:  17 | Slot:  17 | Storage:   6.93 KB | Overwrites:   - | Hash Ops:  69195 | Time: 0.007s | ETA:  939.5s
[NODE-02] Block  18/500 | Index:  18 | Slot:  18 | Storage:   7.32 KB | Overwrites:   - | Hash Ops:  75581 | Time: 0.064s | ETA:  941.2s
[NODE-02] Block  19/500 | Index:  19 | Slot:  19 | Storage:   7.72 KB | Overwrites:   - | Hash Ops:  76384 | Time: 0.019s | ETA:  941.9s
[NODE-02] Block  20/500 | Index:  20 | Slot:  20 | Storage:   8.11 KB | Overwrites:   - | Hash Ops:  77642 | Time: 0.026s | ETA:  942.1s
[NODE-02] Block  21/500 | Index:  21 | Slot:  21 | Storage:   8.50 KB | Overwrites:   - | Hash Ops:  85378 | Time: 0.058s | ETA:  945.9s
[NODE-02] Block  22/500 | Index:  22 | Slot:  22 | Storage:   8.89 KB | Overwrites:   - | Hash Ops:  88328 | Time: 0.032s | ETA:  945.2s
[NODE-02] Block  23/500 | Index:  23 | Slot:  23 | Storage:   9.28 KB | Overwrites:   - | Hash Ops:  89023 | Time: 0.008s | ETA:  944.0s
[NODE-02] Block  24/500 | Index:  24 | Slot:  24 | Storage:   9.67 KB | Overwrites:   - | Hash Ops:  90502 | Time: 0.020s | ETA:  943.0s
[NODE-02] Block  25/500 | Index:  25 | Slot:  25 | Storage:  10.06 KB | Overwrites:   - | Hash Ops:  91014 | Time: 0.013s | ETA:  941.7s
[NODE-02] Block  26/500 | Index:  26 | Slot:  26 | Storage:  10.45 KB | Overwrites:   - | Hash Ops:  97110 | Time: 0.055s | ETA:  941.2s
[NODE-02] Block  27/500 | Index:  27 | Slot:  27 | Storage:  10.84 KB | Overwrites:   - | Hash Ops: 105880 | Time: 0.075s | ETA:  940.8s
[NODE-02] Block  28/500 | Index:  28 | Slot:  28 | Storage:  11.23 KB | Overwrites:   - | Hash Ops: 105910 | Time: 0.001s | ETA:  939.3s
[NODE-02] Block  29/500 | Index:  29 | Slot:  29 | Storage:  11.62 KB | Overwrites:   - | Hash Ops: 108391 | Time: 0.037s | ETA:  938.4s
[NODE-02] Block  30/500 | Index:  30 | Slot:  30 | Storage:  12.01 KB | Overwrites:   - | Hash Ops: 109764 | Time: 0.024s | ETA:  937.2s
[NODE-02] Block  31/500 | Index:  31 | Slot:  31 | Storage:  12.40 KB | Overwrites:   - | Hash Ops: 113129 | Time: 0.030s | ETA:  937.6s
[NODE-02] Block  32/500 | Index:  32 | Slot:  32 | Storage:  12.79 KB | Overwrites:   - | Hash Ops: 117059 | Time: 0.048s | ETA:  936.6s
[NODE-02] Block  33/500 | Index:  33 | Slot:  33 | Storage:  13.18 KB | Overwrites:   - | Hash Ops: 118562 | Time: 0.010s | ETA:  935.2s
[NODE-02] Block  34/500 | Index:  34 | Slot:  34 | Storage:  13.57 KB | Overwrites:   - | Hash Ops: 120587 | Time: 0.035s | ETA:  934.0s
[NODE-02] Block  35/500 | Index:  35 | Slot:  35 | Storage:  13.96 KB | Overwrites:   - | Hash Ops: 125233 | Time: 0.055s | ETA:  932.7s
[NODE-02] Block  36/500 | Index:  36 | Slot:  36 | Storage:  14.35 KB | Overwrites:   - | Hash Ops: 133432 | Time: 0.071s | ETA:  931.7s
[NODE-02] Block  37/500 | Index:  37 | Slot:  37 | Storage:  14.74 KB | Overwrites:   - | Hash Ops: 133679 | Time: 0.007s | ETA:  930.2s
[NODE-02] Block  38/500 | Index:  38 | Slot:  38 | Storage:  15.13 KB | Overwrites:   - | Hash Ops: 140449 | Time: 0.057s | ETA:  928.9s
[NODE-02] Block  39/500 | Index:  39 | Slot:  39 | Storage:  15.52 KB | Overwrites:   - | Hash Ops: 143330 | Time: 0.040s | ETA:  927.3s
[NODE-02] Block  40/500 | Index:  40 | Slot:  40 | Storage:  15.91 KB | Overwrites:   - | Hash Ops: 151848 | Time: 0.086s | ETA:  926.2s
[NODE-02] Block  41/500 | Index:  41 | Slot:  41 | Storage:  16.30 KB | Overwrites:   - | Hash Ops: 156171 | Time: 0.049s | ETA:  925.8s
[NODE-02] Block  42/500 | Index:  42 | Slot:  42 | Storage:  16.69 KB | Overwrites:   - | Hash Ops: 157089 | Time: 0.025s | ETA:  924.0s
[NODE-02] Block  43/500 | Index:  43 | Slot:  43 | Storage:  17.08 KB | Overwrites:   - | Hash Ops: 161092 | Time: 0.030s | ETA:  922.1s
[NODE-02] Block  44/500 | Index:  44 | Slot:  44 | Storage:  17.48 KB | Overwrites:   - | Hash Ops: 162486 | Time: 0.023s | ETA:  920.3s
[NODE-02] Block  45/500 | Index:  45 | Slot:  45 | Storage:  17.87 KB | Overwrites:   - | Hash Ops: 164274 | Time: 0.012s | ETA:  918.5s
[NODE-02] Block  46/500 | Index:  46 | Slot:  46 | Storage:  18.26 KB | Overwrites:   - | Hash Ops: 170323 | Time: 0.042s | ETA:  916.7s
[NODE-02] Block  47/500 | Index:  47 | Slot:  47 | Storage:  18.65 KB | Overwrites:   - | Hash Ops: 170564 | Time: 0.010s | ETA:  914.7s
[NODE-02] Block  48/500 | Index:  48 | Slot:  48 | Storage:  19.04 KB | Overwrites:   - | Hash Ops: 174256 | Time: 0.025s | ETA:  912.8s
[NODE-02] Block  49/500 | Index:  49 | Slot:  49 | Storage:  19.43 KB | Overwrites:   - | Hash Ops: 180933 | Time: 0.078s | ETA:  911.3s
[NODE-02] Block  50/500 | Index:  50 | Slot:  50 | Storage:  19.82 KB | Overwrites:   - | Hash Ops: 186282 | Time: 0.049s | ETA:  909.6s
[NODE-02] Block  51/500 | Index:  51 | Slot:  51 | Storage:  20.21 KB | Overwrites:   - | Hash Ops: 187618 | Time: 0.020s | ETA:  908.9s
[NODE-02] Block  52/500 | Index:  52 | Slot:  52 | Storage:  20.60 KB | Overwrites:   - | Hash Ops: 190320 | Time: 0.023s | ETA:  906.9s
[NODE-02] Block  53/500 | Index:  53 | Slot:  53 | Storage:  20.99 KB | Overwrites:   - | Hash Ops: 190650 | Time: 0.009s | ETA:  904.8s
[NODE-02] Block  54/500 | Index:  54 | Slot:  54 | Storage:  21.38 KB | Overwrites:   - | Hash Ops: 200187 | Time: 0.080s | ETA:  903.3s
[NODE-02] Block  55/500 | Index:  55 | Slot:  55 | Storage:  21.77 KB | Overwrites:   - | Hash Ops: 202974 | Time: 0.021s | ETA:  901.3s
[NODE-02] Block  56/500 | Index:  56 | Slot:  56 | Storage:  22.16 KB | Overwrites:   - | Hash Ops: 205003 | Time: 0.026s | ETA:  899.5s
[NODE-02] Block  57/500 | Index:  57 | Slot:  57 | Storage:  22.55 KB | Overwrites:   - | Hash Ops: 208306 | Time: 0.039s | ETA:  897.7s
[NODE-02] Block  58/500 | Index:  58 | Slot:  58 | Storage:  22.94 KB | Overwrites:   - | Hash Ops: 209190 | Time: 0.020s | ETA:  895.6s
[NODE-02] Block  59/500 | Index:  59 | Slot:  59 | Storage:  23.33 KB | Overwrites:   - | Hash Ops: 210391 | Time: 0.011s | ETA:  893.5s
[NODE-02] Block  60/500 | Index:  60 | Slot:  60 | Storage:  23.72 KB | Overwrites:   - | Hash Ops: 211228 | Time: 0.011s | ETA:  891.5s
[NODE-02] Block  61/500 | Index:  61 | Slot:  61 | Storage:  24.11 KB | Overwrites:   - | Hash Ops: 214017 | Time: 0.038s | ETA:  890.7s
[NODE-02] Block  62/500 | Index:  62 | Slot:  62 | Storage:  24.50 KB | Overwrites:   - | Hash Ops: 215793 | Time: 0.027s | ETA:  888.7s
[NODE-02] Block  63/500 | Index:  63 | Slot:  63 | Storage:  24.89 KB | Overwrites:   - | Hash Ops: 224052 | Time: 0.080s | ETA:  887.1s
[NODE-02] Block  64/500 | Index:  64 | Slot:  64 | Storage:  25.28 KB | Overwrites:   - | Hash Ops: 227616 | Time: 0.025s | ETA:  885.2s
[NODE-02] Block  65/500 | Index:  65 | Slot:  65 | Storage:  25.67 KB | Overwrites:   - | Hash Ops: 233021 | Time: 0.040s | ETA:  883.3s
[NODE-02] Block  66/500 | Index:  66 | Slot:  66 | Storage:  26.07 KB | Overwrites:   - | Hash Ops: 249455 | Time: 0.142s | ETA:  882.1s
[NODE-02] Block  67/500 | Index:  67 | Slot:  67 | Storage:  26.46 KB | Overwrites:   - | Hash Ops: 254971 | Time: 0.059s | ETA:  880.2s
[NODE-02] Block  68/500 | Index:  68 | Slot:  68 | Storage:  26.85 KB | Overwrites:   - | Hash Ops: 259492 | Time: 0.039s | ETA:  878.3s
[NODE-02] Block  69/500 | Index:  69 | Slot:  69 | Storage:  27.25 KB | Overwrites:   - | Hash Ops: 271338 | Time: 0.101s | ETA:  876.7s
[NODE-02] Block  70/500 | Index:  70 | Slot:  70 | Storage:  27.63 KB | Overwrites:   - | Hash Ops: 271636 | Time: 0.009s | ETA:  874.7s
[NODE-02] Block  71/500 | Index:  71 | Slot:  71 | Storage:  28.03 KB | Overwrites:   - | Hash Ops: 272216 | Time: 0.014s | ETA:  873.2s
[NODE-02] Block  72/500 | Index:  72 | Slot:  72 | Storage:  28.42 KB | Overwrites:   - | Hash Ops: 274237 | Time: 0.028s | ETA:  871.2s
[NODE-02] Block  73/500 | Index:  73 | Slot:  73 | Storage:  28.81 KB | Overwrites:   - | Hash Ops: 293316 | Time: 0.168s | ETA:  870.0s
[NODE-02] Block  74/500 | Index:  74 | Slot:  74 | Storage:  29.20 KB | Overwrites:   - | Hash Ops: 293972 | Time: 0.017s | ETA:  867.8s
[NODE-02] Block  75/500 | Index:  75 | Slot:  75 | Storage:  29.59 KB | Overwrites:   - | Hash Ops: 295475 | Time: 0.015s | ETA:  865.9s
[NODE-02] Block  76/500 | Index:  76 | Slot:  76 | Storage:  29.98 KB | Overwrites:   - | Hash Ops: 295816 | Time: 0.007s | ETA:  863.9s
[NODE-02] Block  77/500 | Index:  77 | Slot:  77 | Storage:  30.37 KB | Overwrites:   - | Hash Ops: 297698 | Time: 0.017s | ETA:  861.9s
[NODE-02] Block  78/500 | Index:  78 | Slot:  78 | Storage:  30.76 KB | Overwrites:   - | Hash Ops: 297736 | Time: 0.002s | ETA:  860.2s
[NODE-02] Block  79/500 | Index:  79 | Slot:  79 | Storage:  31.16 KB | Overwrites:   - | Hash Ops: 299185 | Time: 0.032s | ETA:  858.3s
[NODE-02] Block  80/500 | Index:  80 | Slot:  80 | Storage:  31.55 KB | Overwrites:   - | Hash Ops: 301333 | Time: 0.018s | ETA:  856.2s
[NODE-02] Block  81/500 | Index:  81 | Slot:  81 | Storage:  31.94 KB | Overwrites:   - | Hash Ops: 301598 | Time: 0.009s | ETA:  854.8s
[NODE-02] Block  82/500 | Index:  82 | Slot:  82 | Storage:  32.33 KB | Overwrites:   - | Hash Ops: 304333 | Time: 0.027s | ETA:  852.8s
[NODE-02] Block  83/500 | Index:  83 | Slot:  83 | Storage:  32.72 KB | Overwrites:   - | Hash Ops: 307144 | Time: 0.019s | ETA:  850.7s
[NODE-02] Block  84/500 | Index:  84 | Slot:  84 | Storage:  33.11 KB | Overwrites:   - | Hash Ops: 320816 | Time: 0.119s | ETA:  849.2s
[NODE-02] Block  85/500 | Index:  85 | Slot:  85 | Storage:  33.50 KB | Overwrites:   - | Hash Ops: 331793 | Time: 0.105s | ETA:  847.4s
[NODE-02] Block  86/500 | Index:  86 | Slot:  86 | Storage:  33.89 KB | Overwrites:   - | Hash Ops: 335278 | Time: 0.046s | ETA:  845.5s
[NODE-02] Block  87/500 | Index:  87 | Slot:  87 | Storage:  34.28 KB | Overwrites:   - | Hash Ops: 335492 | Time: 0.001s | ETA:  843.4s
[NODE-02] Block  88/500 | Index:  88 | Slot:  88 | Storage:  34.68 KB | Overwrites:   - | Hash Ops: 338688 | Time: 0.041s | ETA:  841.4s
[NODE-02] Block  89/500 | Index:  89 | Slot:  89 | Storage:  35.07 KB | Overwrites:   - | Hash Ops: 341875 | Time: 0.029s | ETA:  839.3s
[NODE-02] Block  90/500 | Index:  90 | Slot:  90 | Storage:  35.46 KB | Overwrites:   - | Hash Ops: 344517 | Time: 0.018s | ETA:  837.2s
[NODE-02] Block  91/500 | Index:  91 | Slot:  91 | Storage:  35.85 KB | Overwrites:   - | Hash Ops: 345041 | Time: 0.016s | ETA:  835.8s
[NODE-02] Block  92/500 | Index:  92 | Slot:  92 | Storage:  36.24 KB | Overwrites:   - | Hash Ops: 348361 | Time: 0.045s | ETA:  833.8s
[NODE-02] Block  93/500 | Index:  93 | Slot:  93 | Storage:  36.63 KB | Overwrites:   - | Hash Ops: 352564 | Time: 0.030s | ETA:  831.8s
[NODE-02] Block  94/500 | Index:  94 | Slot:  94 | Storage:  37.02 KB | Overwrites:   - | Hash Ops: 355852 | Time: 0.030s | ETA:  829.9s
[NODE-02] Block  95/500 | Index:  95 | Slot:  95 | Storage:  37.41 KB | Overwrites:   - | Hash Ops: 361719 | Time: 0.063s | ETA:  828.1s
[NODE-02] Block  96/500 | Index:  96 | Slot:  96 | Storage:  37.80 KB | Overwrites:   - | Hash Ops: 367363 | Time: 0.054s | ETA:  826.1s
[NODE-02] Block  97/500 | Index:  97 | Slot:  97 | Storage:  38.19 KB | Overwrites:   - | Hash Ops: 367442 | Time: 0.003s | ETA:  824.1s
[NODE-02] Block  98/500 | Index:  98 | Slot:  98 | Storage:  38.58 KB | Overwrites:   - | Hash Ops: 368324 | Time: 0.018s | ETA:  822.1s
[NODE-02] Block  99/500 | Index:  99 | Slot:  99 | Storage:  38.97 KB | Overwrites:   - | Hash Ops: 371616 | Time: 0.036s | ETA:  820.1s
[NODE-02] Block 100/500 | Index: 100 | Slot:   0 | Storage:  39.05 KB | Overwrites: Slot   0 | Hash Ops: 374127 | Time: 0.018s | ETA:  818.0s
[NODE-02] Block 101/500 | Index: 101 | Slot:   1 | Storage:  39.06 KB | Overwrites: Slot   1 | Hash Ops: 376729 | Time: 0.035s | ETA:  816.3s
[NODE-02] Block 102/500 | Index: 102 | Slot:   2 | Storage:  39.06 KB | Overwrites: Slot   2 | Hash Ops: 381187 | Time: 0.031s | ETA:  814.4s
[NODE-02] Block 103/500 | Index: 103 | Slot:   3 | Storage:  39.07 KB | Overwrites: Slot   3 | Hash Ops: 381350 | Time: 0.001s | ETA:  812.2s
[NODE-02] Block 104/500 | Index: 104 | Slot:   4 | Storage:  39.07 KB | Overwrites: Slot   4 | Hash Ops: 384176 | Time: 0.026s | ETA:  810.1s
[NODE-02] Block 105/500 | Index: 105 | Slot:   5 | Storage:  39.08 KB | Overwrites: Slot   5 | Hash Ops: 399526 | Time: 0.117s | ETA:  808.5s
[NODE-02] Block 106/500 | Index: 106 | Slot:   6 | Storage:  39.08 KB | Overwrites: Slot   6 | Hash Ops: 410707 | Time: 0.106s | ETA:  806.8s
[NODE-02] Block 107/500 | Index: 107 | Slot:   7 | Storage:  39.09 KB | Overwrites: Slot   7 | Hash Ops: 415643 | Time: 0.051s | ETA:  804.7s
[NODE-02] Block 108/500 | Index: 108 | Slot:   8 | Storage:  39.09 KB | Overwrites: Slot   8 | Hash Ops: 416648 | Time: 0.014s | ETA:  802.6s
[NODE-02] Block 109/500 | Index: 109 | Slot:   9 | Storage:  39.10 KB | Overwrites: Slot   9 | Hash Ops: 418801 | Time: 0.029s | ETA:  800.6s
[NODE-02] Block 110/500 | Index: 110 | Slot:  10 | Storage:  39.10 KB | Overwrites: Slot  10 | Hash Ops: 426124 | Time: 0.082s | ETA:  798.7s
[NODE-02] Block 111/500 | Index: 111 | Slot:  11 | Storage:  39.11 KB | Overwrites: Slot  11 | Hash Ops: 430830 | Time: 0.038s | ETA:  797.2s
[NODE-02] Block 112/500 | Index: 112 | Slot:  12 | Storage:  39.11 KB | Overwrites: Slot  12 | Hash Ops: 431515 | Time: 0.021s | ETA:  795.1s
[NODE-02] Block 113/500 | Index: 113 | Slot:  13 | Storage:  39.11 KB | Overwrites: Slot  13 | Hash Ops: 437392 | Time: 0.062s | ETA:  793.2s
[NODE-02] Block 114/500 | Index: 114 | Slot:  14 | Storage:  39.12 KB | Overwrites: Slot  14 | Hash Ops: 441857 | Time: 0.043s | ETA:  791.1s
[NODE-02] Block 115/500 | Index: 115 | Slot:  15 | Storage:  39.12 KB | Overwrites: Slot  15 | Hash Ops: 445965 | Time: 0.055s | ETA:  789.2s
[NODE-02] Block 116/500 | Index: 116 | Slot:  16 | Storage:  39.12 KB | Overwrites: Slot  16 | Hash Ops: 448225 | Time: 0.029s | ETA:  787.1s
[NODE-02] Block 117/500 | Index: 117 | Slot:  17 | Storage:  39.12 KB | Overwrites: Slot  17 | Hash Ops: 449813 | Time: 0.013s | ETA:  785.1s
[NODE-02] Block 118/500 | Index: 118 | Slot:  18 | Storage:  39.12 KB | Overwrites: Slot  18 | Hash Ops: 451004 | Time: 0.021s | ETA:  782.9s
[NODE-02] Block 119/500 | Index: 119 | Slot:  19 | Storage:  39.12 KB | Overwrites: Slot  19 | Hash Ops: 455101 | Time: 0.043s | ETA:  780.9s
[NODE-02] Block 120/500 | Index: 120 | Slot:  20 | Storage:  39.13 KB | Overwrites: Slot  20 | Hash Ops: 460362 | Time: 0.047s | ETA:  778.9s
[NODE-02] Block 121/500 | Index: 121 | Slot:  21 | Storage:  39.13 KB | Overwrites: Slot  21 | Hash Ops: 461680 | Time: 0.014s | ETA:  777.2s
[NODE-02] Block 122/500 | Index: 122 | Slot:  22 | Storage:  39.13 KB | Overwrites: Slot  22 | Hash Ops: 465226 | Time: 0.036s | ETA:  775.2s
[NODE-02] Block 123/500 | Index: 123 | Slot:  23 | Storage:  39.14 KB | Overwrites: Slot  23 | Hash Ops: 475631 | Time: 0.089s | ETA:  773.7s
[NODE-02] Block 124/500 | Index: 124 | Slot:  24 | Storage:  39.14 KB | Overwrites: Slot  24 | Hash Ops: 476799 | Time: 0.021s | ETA:  771.6s
[NODE-02] Block 125/500 | Index: 125 | Slot:  25 | Storage:  39.14 KB | Overwrites: Slot  25 | Hash Ops: 481745 | Time: 0.053s | ETA:  769.6s
[NODE-02] Block 126/500 | Index: 126 | Slot:  26 | Storage:  39.14 KB | Overwrites: Slot  26 | Hash Ops: 485946 | Time: 0.055s | ETA:  767.6s
[NODE-02] Block 127/500 | Index: 127 | Slot:  27 | Storage:  39.15 KB | Overwrites: Slot  27 | Hash Ops: 490282 | Time: 0.038s | ETA:  765.6s
[NODE-02] Block 128/500 | Index: 128 | Slot:  28 | Storage:  39.15 KB | Overwrites: Slot  28 | Hash Ops: 495098 | Time: 0.034s | ETA:  763.5s
[NODE-02] Block 129/500 | Index: 129 | Slot:  29 | Storage:  39.16 KB | Overwrites: Slot  29 | Hash Ops: 499843 | Time: 0.043s | ETA:  761.5s
[NODE-02] Block 130/500 | Index: 130 | Slot:  30 | Storage:  39.16 KB | Overwrites: Slot  30 | Hash Ops: 501810 | Time: 0.024s | ETA:  759.4s
[NODE-02] Block 131/500 | Index: 131 | Slot:  31 | Storage:  39.16 KB | Overwrites: Slot  31 | Hash Ops: 506544 | Time: 0.035s | ETA:  757.7s
[NODE-02] Block 132/500 | Index: 132 | Slot:  32 | Storage:  39.17 KB | Overwrites: Slot  32 | Hash Ops: 509650 | Time: 0.037s | ETA:  755.6s
[NODE-02] Block 133/500 | Index: 133 | Slot:  33 | Storage:  39.17 KB | Overwrites: Slot  33 | Hash Ops: 516230 | Time: 0.056s | ETA:  753.6s
[NODE-02] Block 134/500 | Index: 134 | Slot:  34 | Storage:  39.17 KB | Overwrites: Slot  34 | Hash Ops: 517013 | Time: 0.015s | ETA:  751.5s
[NODE-02] Block 135/500 | Index: 135 | Slot:  35 | Storage:  39.17 KB | Overwrites: Slot  35 | Hash Ops: 524014 | Time: 0.057s | ETA:  749.4s
[NODE-02] Block 136/500 | Index: 136 | Slot:  36 | Storage:  39.17 KB | Overwrites: Slot  36 | Hash Ops: 524082 | Time: 0.001s | ETA:  747.2s
[NODE-02] Block 137/500 | Index: 137 | Slot:  37 | Storage:  39.18 KB | Overwrites: Slot  37 | Hash Ops: 525853 | Time: 0.020s | ETA:  745.1s
[NODE-02] Block 138/500 | Index: 138 | Slot:  38 | Storage:  39.18 KB | Overwrites: Slot  38 | Hash Ops: 527196 | Time: 0.014s | ETA:  743.0s
[NODE-02] Block 139/500 | Index: 139 | Slot:  39 | Storage:  39.19 KB | Overwrites: Slot  39 | Hash Ops: 529856 | Time: 0.038s | ETA:  741.0s
[NODE-02] Block 140/500 | Index: 140 | Slot:  40 | Storage:  39.19 KB | Overwrites: Slot  40 | Hash Ops: 533839 | Time: 0.056s | ETA:  739.0s
[NODE-02] Block 141/500 | Index: 141 | Slot:  41 | Storage:  39.19 KB | Overwrites: Slot  41 | Hash Ops: 534136 | Time: 0.010s | ETA:  737.2s
[NODE-02] Block 142/500 | Index: 142 | Slot:  42 | Storage:  39.19 KB | Overwrites: Slot  42 | Hash Ops: 536491 | Time: 0.033s | ETA:  735.3s
[NODE-02] Block 143/500 | Index: 143 | Slot:  43 | Storage:  39.19 KB | Overwrites: Slot  43 | Hash Ops: 539543 | Time: 0.049s | ETA:  733.2s
[NODE-02] Block 144/500 | Index: 144 | Slot:  44 | Storage:  39.19 KB | Overwrites: Slot  44 | Hash Ops: 542983 | Time: 0.035s | ETA:  731.2s
[NODE-02] Block 145/500 | Index: 145 | Slot:  45 | Storage:  39.19 KB | Overwrites: Slot  45 | Hash Ops: 550761 | Time: 0.062s | ETA:  729.4s
[NODE-02] Block 146/500 | Index: 146 | Slot:  46 | Storage:  39.20 KB | Overwrites: Slot  46 | Hash Ops: 552053 | Time: 0.009s | ETA:  727.3s
[NODE-02] Block 147/500 | Index: 147 | Slot:  47 | Storage:  39.20 KB | Overwrites: Slot  47 | Hash Ops: 554708 | Time: 0.029s | ETA:  725.2s
[NODE-02] Block 148/500 | Index: 148 | Slot:  48 | Storage:  39.21 KB | Overwrites: Slot  48 | Hash Ops: 556100 | Time: 0.024s | ETA:  723.1s
[NODE-02] Block 149/500 | Index: 149 | Slot:  49 | Storage:  39.21 KB | Overwrites: Slot  49 | Hash Ops: 565413 | Time: 0.081s | ETA:  721.1s
[NODE-02] Block 150/500 | Index: 150 | Slot:  50 | Storage:  39.21 KB | Overwrites: Slot  50 | Hash Ops: 574479 | Time: 0.069s | ETA:  719.2s
[NODE-02] Block 151/500 | Index: 151 | Slot:  51 | Storage:  39.21 KB | Overwrites: Slot  51 | Hash Ops: 578935 | Time: 0.032s | ETA:  717.3s
[NODE-02] Block 152/500 | Index: 152 | Slot:  52 | Storage:  39.21 KB | Overwrites: Slot  52 | Hash Ops: 579471 | Time: 0.009s | ETA:  715.2s
[NODE-02] Block 153/500 | Index: 153 | Slot:  53 | Storage:  39.22 KB | Overwrites: Slot  53 | Hash Ops: 583516 | Time: 0.059s | ETA:  713.2s
[NODE-02] Block 154/500 | Index: 154 | Slot:  54 | Storage:  39.22 KB | Overwrites: Slot  54 | Hash Ops: 586195 | Time: 0.022s | ETA:  711.1s
[NODE-02] Block 155/500 | Index: 155 | Slot:  55 | Storage:  39.22 KB | Overwrites: Slot  55 | Hash Ops: 603142 | Time: 0.167s | ETA:  709.4s
[NODE-02] Block 156/500 | Index: 156 | Slot:  56 | Storage:  39.22 KB | Overwrites: Slot  56 | Hash Ops: 605807 | Time: 0.034s | ETA:  707.3s
[NODE-02] Block 157/500 | Index: 157 | Slot:  57 | Storage:  39.22 KB | Overwrites: Slot  57 | Hash Ops: 606703 | Time: 0.006s | ETA:  705.1s
[NODE-02] Block 158/500 | Index: 158 | Slot:  58 | Storage:  39.22 KB | Overwrites: Slot  58 | Hash Ops: 606790 | Time: 0.001s | ETA:  702.9s
[NODE-02] Block 159/500 | Index: 159 | Slot:  59 | Storage:  39.23 KB | Overwrites: Slot  59 | Hash Ops: 608409 | Time: 0.012s | ETA:  700.8s
[NODE-02] Block 160/500 | Index: 160 | Slot:  60 | Storage:  39.23 KB | Overwrites: Slot  60 | Hash Ops: 610561 | Time: 0.035s | ETA:  698.7s
[NODE-02] Block 161/500 | Index: 161 | Slot:  61 | Storage:  39.23 KB | Overwrites: Slot  61 | Hash Ops: 618696 | Time: 0.096s | ETA:  697.0s
[NODE-02] Block 162/500 | Index: 162 | Slot:  62 | Storage:  39.23 KB | Overwrites: Slot  62 | Hash Ops: 619204 | Time: 0.006s | ETA:  694.9s
[NODE-02] Block 163/500 | Index: 163 | Slot:  63 | Storage:  39.23 KB | Overwrites: Slot  63 | Hash Ops: 620195 | Time: 0.019s | ETA:  692.8s
[NODE-02] Block 164/500 | Index: 164 | Slot:  64 | Storage:  39.23 KB | Overwrites: Slot  64 | Hash Ops: 624313 | Time: 0.046s | ETA:  690.7s
[NODE-02] Block 165/500 | Index: 165 | Slot:  65 | Storage:  39.24 KB | Overwrites: Slot  65 | Hash Ops: 629535 | Time: 0.036s | ETA:  688.6s
[NODE-02] Block 166/500 | Index: 166 | Slot:  66 | Storage:  39.24 KB | Overwrites: Slot  66 | Hash Ops: 632272 | Time: 0.042s | ETA:  686.6s
[NODE-02] Block 167/500 | Index: 167 | Slot:  67 | Storage:  39.24 KB | Overwrites: Slot  67 | Hash Ops: 642822 | Time: 0.124s | ETA:  684.7s
[NODE-02] Block 168/500 | Index: 168 | Slot:  68 | Storage:  39.24 KB | Overwrites: Slot  68 | Hash Ops: 646765 | Time: 0.035s | ETA:  682.7s
[NODE-02] Block 169/500 | Index: 169 | Slot:  69 | Storage:  39.24 KB | Overwrites: Slot  69 | Hash Ops: 646896 | Time: 0.003s | ETA:  680.5s
[NODE-02] Block 170/500 | Index: 170 | Slot:  70 | Storage:  39.25 KB | Overwrites: Slot  70 | Hash Ops: 649250 | Time: 0.020s | ETA:  678.4s
[NODE-02] Block 171/500 | Index: 171 | Slot:  71 | Storage:  39.25 KB | Overwrites: Slot  71 | Hash Ops: 678338 | Time: 0.219s | ETA:  677.0s
[NODE-02] Block 172/500 | Index: 172 | Slot:  72 | Storage:  39.25 KB | Overwrites: Slot  72 | Hash Ops: 682226 | Time: 0.043s | ETA:  674.9s
[NODE-02] Block 173/500 | Index: 173 | Slot:  73 | Storage:  39.25 KB | Overwrites: Slot  73 | Hash Ops: 684123 | Time: 0.015s | ETA:  672.8s
[NODE-02] Block 174/500 | Index: 174 | Slot:  74 | Storage:  39.26 KB | Overwrites: Slot  74 | Hash Ops: 687371 | Time: 0.032s | ETA:  670.7s
[NODE-02] Block 175/500 | Index: 175 | Slot:  75 | Storage:  39.26 KB | Overwrites: Slot  75 | Hash Ops: 688817 | Time: 0.026s | ETA:  668.6s
[NODE-02] Block 176/500 | Index: 176 | Slot:  76 | Storage:  39.26 KB | Overwrites: Slot  76 | Hash Ops: 694309 | Time: 0.049s | ETA:  666.7s
[NODE-02] Block 177/500 | Index: 177 | Slot:  77 | Storage:  39.26 KB | Overwrites: Slot  77 | Hash Ops: 697278 | Time: 0.037s | ETA:  664.6s
[NODE-02] Block 178/500 | Index: 178 | Slot:  78 | Storage:  39.27 KB | Overwrites: Slot  78 | Hash Ops: 698725 | Time: 0.029s | ETA:  662.9s
[NODE-02] Block 179/500 | Index: 179 | Slot:  79 | Storage:  39.27 KB | Overwrites: Slot  79 | Hash Ops: 700325 | Time: 0.018s | ETA:  660.8s
[NODE-02] Block 180/500 | Index: 180 | Slot:  80 | Storage:  39.27 KB | Overwrites: Slot  80 | Hash Ops: 705305 | Time: 0.070s | ETA:  658.7s
[NODE-02] Block 181/500 | Index: 181 | Slot:  81 | Storage:  39.27 KB | Overwrites: Slot  81 | Hash Ops: 710858 | Time: 0.055s | ETA:  656.9s
[NODE-02] Block 182/500 | Index: 182 | Slot:  82 | Storage:  39.28 KB | Overwrites: Slot  82 | Hash Ops: 714359 | Time: 0.042s | ETA:  654.9s
[NODE-02] Block 183/500 | Index: 183 | Slot:  83 | Storage:  39.28 KB | Overwrites: Slot  83 | Hash Ops: 717064 | Time: 0.034s | ETA:  652.8s
[NODE-02] Block 184/500 | Index: 184 | Slot:  84 | Storage:  39.28 KB | Overwrites: Slot  84 | Hash Ops: 717241 | Time: 0.005s | ETA:  650.8s
[NODE-02] Block 185/500 | Index: 185 | Slot:  85 | Storage:  39.28 KB | Overwrites: Slot  85 | Hash Ops: 724498 | Time: 0.077s | ETA:  648.8s
[NODE-02] Block 186/500 | Index: 186 | Slot:  86 | Storage:  39.29 KB | Overwrites: Slot  86 | Hash Ops: 738977 | Time: 0.116s | ETA:  646.9s
[NODE-02] Block 187/500 | Index: 187 | Slot:  87 | Storage:  39.29 KB | Overwrites: Slot  87 | Hash Ops: 742422 | Time: 0.039s | ETA:  644.8s
[NODE-02] Block 188/500 | Index: 188 | Slot:  88 | Storage:  39.29 KB | Overwrites: Slot  88 | Hash Ops: 747767 | Time: 0.038s | ETA:  642.8s
[NODE-02] Block 189/500 | Index: 189 | Slot:  89 | Storage:  39.29 KB | Overwrites: Slot  89 | Hash Ops: 750235 | Time: 0.017s | ETA:  640.7s
[NODE-02] Block 190/500 | Index: 190 | Slot:  90 | Storage:  39.30 KB | Overwrites: Slot  90 | Hash Ops: 753606 | Time: 0.032s | ETA:  638.6s
[NODE-02] Block 191/500 | Index: 191 | Slot:  91 | Storage:  39.30 KB | Overwrites: Slot  91 | Hash Ops: 754914 | Time: 0.021s | ETA:  636.7s
[NODE-02] Block 192/500 | Index: 192 | Slot:  92 | Storage:  39.30 KB | Overwrites: Slot  92 | Hash Ops: 755098 | Time: 0.005s | ETA:  634.6s
[NODE-02] Block 193/500 | Index: 193 | Slot:  93 | Storage:  39.30 KB | Overwrites: Slot  93 | Hash Ops: 764165 | Time: 0.094s | ETA:  632.6s
[NODE-02] Block 194/500 | Index: 194 | Slot:  94 | Storage:  39.31 KB | Overwrites: Slot  94 | Hash Ops: 765522 | Time: 0.035s | ETA:  630.5s
[NODE-02] Block 195/500 | Index: 195 | Slot:  95 | Storage:  39.31 KB | Overwrites: Slot  95 | Hash Ops: 768137 | Time: 0.026s | ETA:  628.4s
[NODE-02] Block 196/500 | Index: 196 | Slot:  96 | Storage:  39.31 KB | Overwrites: Slot  96 | Hash Ops: 770330 | Time: 0.019s | ETA:  626.3s
[NODE-02] Block 197/500 | Index: 197 | Slot:  97 | Storage:  39.32 KB | Overwrites: Slot  97 | Hash Ops: 776412 | Time: 0.057s | ETA:  624.2s
[NODE-02] Block 198/500 | Index: 198 | Slot:  98 | Storage:  39.32 KB | Overwrites: Slot  98 | Hash Ops: 779473 | Time: 0.033s | ETA:  622.1s
[NODE-02] Block 199/500 | Index: 199 | Slot:  99 | Storage:  39.32 KB | Overwrites: Slot  99 | Hash Ops: 789909 | Time: 0.111s | ETA:  620.2s
[NODE-02] Block 200/500 | Index: 200 | Slot:   0 | Storage:  39.33 KB | Overwrites: Slot   0 | Hash Ops: 790907 | Time: 0.019s | ETA:  618.1s
[NODE-02] Block 201/500 | Index: 201 | Slot:   1 | Storage:  39.32 KB | Overwrites: Slot   1 | Hash Ops: 791521 | Time: 0.009s | ETA:  616.2s
[NODE-02] Block 202/500 | Index: 202 | Slot:   2 | Storage:  39.33 KB | Overwrites: Slot   2 | Hash Ops: 794674 | Time: 0.028s | ETA:  614.1s
[NODE-02] Block 203/500 | Index: 203 | Slot:   3 | Storage:  39.33 KB | Overwrites: Slot   3 | Hash Ops: 795990 | Time: 0.012s | ETA:  612.0s
[NODE-02] Block 204/500 | Index: 204 | Slot:   4 | Storage:  39.33 KB | Overwrites: Slot   4 | Hash Ops: 796248 | Time: 0.002s | ETA:  609.9s
[NODE-02] Block 205/500 | Index: 205 | Slot:   5 | Storage:  39.33 KB | Overwrites: Slot   5 | Hash Ops: 801761 | Time: 0.051s | ETA:  607.8s
[NODE-02] Block 206/500 | Index: 206 | Slot:   6 | Storage:  39.33 KB | Overwrites: Slot   6 | Hash Ops: 805842 | Time: 0.048s | ETA:  606.0s
[NODE-02] Block 207/500 | Index: 207 | Slot:   7 | Storage:  39.33 KB | Overwrites: Slot   7 | Hash Ops: 809111 | Time: 0.026s | ETA:  603.9s
[NODE-02] Block 208/500 | Index: 208 | Slot:   8 | Storage:  39.33 KB | Overwrites: Slot   8 | Hash Ops: 810845 | Time: 0.024s | ETA:  601.8s
[NODE-02] Block 209/500 | Index: 209 | Slot:   9 | Storage:  39.33 KB | Overwrites: Slot   9 | Hash Ops: 814929 | Time: 0.036s | ETA:  599.8s
[NODE-02] Block 210/500 | Index: 210 | Slot:  10 | Storage:  39.33 KB | Overwrites: Slot  10 | Hash Ops: 815064 | Time: 0.004s | ETA:  597.6s
[NODE-02] Block 211/500 | Index: 211 | Slot:  11 | Storage:  39.33 KB | Overwrites: Slot  11 | Hash Ops: 817046 | Time: 0.028s | ETA:  595.8s
[NODE-02] Block 212/500 | Index: 212 | Slot:  12 | Storage:  39.33 KB | Overwrites: Slot  12 | Hash Ops: 826550 | Time: 0.094s | ETA:  593.8s
[NODE-02] Block 213/500 | Index: 213 | Slot:  13 | Storage:  39.33 KB | Overwrites: Slot  13 | Hash Ops: 827565 | Time: 0.025s | ETA:  591.8s
[NODE-02] Block 214/500 | Index: 214 | Slot:  14 | Storage:  39.33 KB | Overwrites: Slot  14 | Hash Ops: 829276 | Time: 0.019s | ETA:  589.7s
[NODE-02] Block 215/500 | Index: 215 | Slot:  15 | Storage:  39.33 KB | Overwrites: Slot  15 | Hash Ops: 831444 | Time: 0.019s | ETA:  587.6s
[NODE-02] Block 216/500 | Index: 216 | Slot:  16 | Storage:  39.33 KB | Overwrites: Slot  16 | Hash Ops: 832346 | Time: 0.016s | ETA:  585.5s
[NODE-02] Block 217/500 | Index: 217 | Slot:  17 | Storage:  39.33 KB | Overwrites: Slot  17 | Hash Ops: 834645 | Time: 0.034s | ETA:  583.4s
[NODE-02] Block 218/500 | Index: 218 | Slot:  18 | Storage:  39.33 KB | Overwrites: Slot  18 | Hash Ops: 836800 | Time: 0.022s | ETA:  581.3s
[NODE-02] Block 219/500 | Index: 219 | Slot:  19 | Storage:  39.33 KB | Overwrites: Slot  19 | Hash Ops: 837056 | Time: 0.011s | ETA:  579.2s
[NODE-02] Block 220/500 | Index: 220 | Slot:  20 | Storage:  39.33 KB | Overwrites: Slot  20 | Hash Ops: 848624 | Time: 0.130s | ETA:  577.2s
[NODE-02] Block 221/500 | Index: 221 | Slot:  21 | Storage:  39.33 KB | Overwrites: Slot  21 | Hash Ops: 853596 | Time: 0.041s | ETA:  575.4s
[NODE-02] Block 222/500 | Index: 222 | Slot:  22 | Storage:  39.33 KB | Overwrites: Slot  22 | Hash Ops: 856081 | Time: 0.048s | ETA:  573.3s
[NODE-02] Block 223/500 | Index: 223 | Slot:  23 | Storage:  39.33 KB | Overwrites: Slot  23 | Hash Ops: 856758 | Time: 0.005s | ETA:  571.2s
[NODE-02] Block 224/500 | Index: 224 | Slot:  24 | Storage:  39.33 KB | Overwrites: Slot  24 | Hash Ops: 860367 | Time: 0.046s | ETA:  569.2s
[NODE-02] Block 225/500 | Index: 225 | Slot:  25 | Storage:  39.33 KB | Overwrites: Slot  25 | Hash Ops: 861150 | Time: 0.018s | ETA:  567.0s
[NODE-02] Block 226/500 | Index: 226 | Slot:  26 | Storage:  39.33 KB | Overwrites: Slot  26 | Hash Ops: 865671 | Time: 0.037s | ETA:  565.0s
[NODE-02] Block 227/500 | Index: 227 | Slot:  27 | Storage:  39.33 KB | Overwrites: Slot  27 | Hash Ops: 865891 | Time: 0.002s | ETA:  562.9s
[NODE-02] Block 228/500 | Index: 228 | Slot:  28 | Storage:  39.33 KB | Overwrites: Slot  28 | Hash Ops: 869212 | Time: 0.028s | ETA:  560.8s
[NODE-02] Block 229/500 | Index: 229 | Slot:  29 | Storage:  39.33 KB | Overwrites: Slot  29 | Hash Ops: 869932 | Time: 0.007s | ETA:  558.7s
[NODE-02] Block 230/500 | Index: 230 | Slot:  30 | Storage:  39.33 KB | Overwrites: Slot  30 | Hash Ops: 881077 | Time: 0.097s | ETA:  556.7s
[NODE-02] Block 231/500 | Index: 231 | Slot:  31 | Storage:  39.33 KB | Overwrites: Slot  31 | Hash Ops: 883105 | Time: 0.025s | ETA:  554.7s
[NODE-02] Block 232/500 | Index: 232 | Slot:  32 | Storage:  39.33 KB | Overwrites: Slot  32 | Hash Ops: 884626 | Time: 0.022s | ETA:  552.6s
[NODE-02] Block 233/500 | Index: 233 | Slot:  33 | Storage:  39.33 KB | Overwrites: Slot  33 | Hash Ops: 887625 | Time: 0.034s | ETA:  550.5s
[NODE-02] Block 234/500 | Index: 234 | Slot:  34 | Storage:  39.33 KB | Overwrites: Slot  34 | Hash Ops: 895697 | Time: 0.074s | ETA:  548.5s
[NODE-02] Block 235/500 | Index: 235 | Slot:  35 | Storage:  39.34 KB | Overwrites: Slot  35 | Hash Ops: 906443 | Time: 0.079s | ETA:  546.5s
[NODE-02] Block 236/500 | Index: 236 | Slot:  36 | Storage:  39.34 KB | Overwrites: Slot  36 | Hash Ops: 907399 | Time: 0.010s | ETA:  544.4s
[NODE-02] Block 237/500 | Index: 237 | Slot:  37 | Storage:  39.34 KB | Overwrites: Slot  37 | Hash Ops: 914828 | Time: 0.071s | ETA:  542.4s
[NODE-02] Block 238/500 | Index: 238 | Slot:  38 | Storage:  39.34 KB | Overwrites: Slot  38 | Hash Ops: 915050 | Time: 0.007s | ETA:  540.3s
[NODE-02] Block 239/500 | Index: 239 | Slot:  39 | Storage:  39.34 KB | Overwrites: Slot  39 | Hash Ops: 921736 | Time: 0.058s | ETA:  538.2s
[NODE-02] Block 240/500 | Index: 240 | Slot:  40 | Storage:  39.34 KB | Overwrites: Slot  40 | Hash Ops: 925208 | Time: 0.039s | ETA:  536.1s
[NODE-02] Block 241/500 | Index: 241 | Slot:  41 | Storage:  39.34 KB | Overwrites: Slot  41 | Hash Ops: 929962 | Time: 0.043s | ETA:  534.2s
[NODE-02] Block 242/500 | Index: 242 | Slot:  42 | Storage:  39.34 KB | Overwrites: Slot  42 | Hash Ops: 930554 | Time: 0.009s | ETA:  532.1s
[NODE-02] Block 243/500 | Index: 243 | Slot:  43 | Storage:  39.34 KB | Overwrites: Slot  43 | Hash Ops: 932001 | Time: 0.021s | ETA:  530.0s
[NODE-02] Block 244/500 | Index: 244 | Slot:  44 | Storage:  39.35 KB | Overwrites: Slot  44 | Hash Ops: 937252 | Time: 0.050s | ETA:  528.0s
[NODE-02] Block 245/500 | Index: 245 | Slot:  45 | Storage:  39.35 KB | Overwrites: Slot  45 | Hash Ops: 938723 | Time: 0.020s | ETA:  525.9s
[NODE-02] Block 246/500 | Index: 246 | Slot:  46 | Storage:  39.35 KB | Overwrites: Slot  46 | Hash Ops: 948973 | Time: 0.089s | ETA:  523.9s
[NODE-02] Block 247/500 | Index: 247 | Slot:  47 | Storage:  39.35 KB | Overwrites: Slot  47 | Hash Ops: 961033 | Time: 0.104s | ETA:  521.8s
[NODE-02] Block 248/500 | Index: 248 | Slot:  48 | Storage:  39.35 KB | Overwrites: Slot  48 | Hash Ops: 969690 | Time: 0.081s | ETA:  519.8s
[NODE-02] Block 249/500 | Index: 249 | Slot:  49 | Storage:  39.35 KB | Overwrites: Slot  49 | Hash Ops: 972901 | Time: 0.026s | ETA:  517.8s
[NODE-02] Block 250/500 | Index: 250 | Slot:  50 | Storage:  39.35 KB | Overwrites: Slot  50 | Hash Ops: 974384 | Time: 0.013s | ETA:  515.7s
[NODE-02] Block 251/500 | Index: 251 | Slot:  51 | Storage:  39.35 KB | Overwrites: Slot  51 | Hash Ops: 980955 | Time: 0.056s | ETA:  513.7s
[NODE-02] Block 252/500 | Index: 252 | Slot:  52 | Storage:  39.35 KB | Overwrites: Slot  52 | Hash Ops: 984388 | Time: 0.043s | ETA:  511.7s
[NODE-02] Block 253/500 | Index: 253 | Slot:  53 | Storage:  39.35 KB | Overwrites: Slot  53 | Hash Ops: 992094 | Time: 0.061s | ETA:  509.6s
[NODE-02] Block 254/500 | Index: 254 | Slot:  54 | Storage:  39.36 KB | Overwrites: Slot  54 | Hash Ops: 993950 | Time: 0.038s | ETA:  507.5s
[NODE-02] Block 255/500 | Index: 255 | Slot:  55 | Storage:  39.36 KB | Overwrites: Slot  55 | Hash Ops: 1009384 | Time: 0.127s | ETA:  505.6s
[NODE-02] Block 256/500 | Index: 256 | Slot:  56 | Storage:  39.36 KB | Overwrites: Slot  56 | Hash Ops: 1012788 | Time: 0.027s | ETA:  503.5s
[NODE-02] Block 257/500 | Index: 257 | Slot:  57 | Storage:  39.36 KB | Overwrites: Slot  57 | Hash Ops: 1013533 | Time: 0.007s | ETA:  501.4s
[NODE-02] Block 258/500 | Index: 258 | Slot:  58 | Storage:  39.36 KB | Overwrites: Slot  58 | Hash Ops: 1013995 | Time: 0.004s | ETA:  499.3s
[NODE-02] Block 259/500 | Index: 259 | Slot:  59 | Storage:  39.36 KB | Overwrites: Slot  59 | Hash Ops: 1025316 | Time: 0.111s | ETA:  497.3s
[NODE-02] Block 260/500 | Index: 260 | Slot:  60 | Storage:  39.36 KB | Overwrites: Slot  60 | Hash Ops: 1029671 | Time: 0.043s | ETA:  495.2s
[NODE-02] Block 261/500 | Index: 261 | Slot:  61 | Storage:  39.37 KB | Overwrites: Slot  61 | Hash Ops: 1030679 | Time: 0.022s | ETA:  493.3s
[NODE-02] Block 262/500 | Index: 262 | Slot:  62 | Storage:  39.37 KB | Overwrites: Slot  62 | Hash Ops: 1032793 | Time: 0.022s | ETA:  491.2s
[NODE-02] Block 263/500 | Index: 263 | Slot:  63 | Storage:  39.37 KB | Overwrites: Slot  63 | Hash Ops: 1033396 | Time: 0.009s | ETA:  489.1s
[NODE-02] Block 264/500 | Index: 264 | Slot:  64 | Storage:  39.37 KB | Overwrites: Slot  64 | Hash Ops: 1038664 | Time: 0.050s | ETA:  487.0s
[NODE-02] Block 265/500 | Index: 265 | Slot:  65 | Storage:  39.37 KB | Overwrites: Slot  65 | Hash Ops: 1041310 | Time: 0.047s | ETA:  484.9s
[NODE-02] Block 266/500 | Index: 266 | Slot:  66 | Storage:  39.37 KB | Overwrites: Slot  66 | Hash Ops: 1047931 | Time: 0.082s | ETA:  482.9s
[NODE-02] Block 267/500 | Index: 267 | Slot:  67 | Storage:  39.37 KB | Overwrites: Slot  67 | Hash Ops: 1047956 | Time: 0.000s | ETA:  480.8s
[NODE-02] Block 268/500 | Index: 268 | Slot:  68 | Storage:  39.37 KB | Overwrites: Slot  68 | Hash Ops: 1048162 | Time: 0.005s | ETA:  478.7s
[NODE-02] Block 269/500 | Index: 269 | Slot:  69 | Storage:  39.37 KB | Overwrites: Slot  69 | Hash Ops: 1055723 | Time: 0.079s | ETA:  476.7s
[NODE-02] Block 270/500 | Index: 270 | Slot:  70 | Storage:  39.37 KB | Overwrites: Slot  70 | Hash Ops: 1071854 | Time: 0.155s | ETA:  474.7s
[NODE-02] Block 271/500 | Index: 271 | Slot:  71 | Storage:  39.37 KB | Overwrites: Slot  71 | Hash Ops: 1072447 | Time: 0.007s | ETA:  472.7s
[NODE-02] Block 272/500 | Index: 272 | Slot:  72 | Storage:  39.37 KB | Overwrites: Slot  72 | Hash Ops: 1076389 | Time: 0.037s | ETA:  470.6s
[NODE-02] Block 273/500 | Index: 273 | Slot:  73 | Storage:  39.37 KB | Overwrites: Slot  73 | Hash Ops: 1082279 | Time: 0.041s | ETA:  468.5s
[NODE-02] Block 274/500 | Index: 274 | Slot:  74 | Storage:  39.36 KB | Overwrites: Slot  74 | Hash Ops: 1085063 | Time: 0.022s | ETA:  466.4s
[NODE-02] Block 275/500 | Index: 275 | Slot:  75 | Storage:  39.36 KB | Overwrites: Slot  75 | Hash Ops: 1098933 | Time: 0.113s | ETA:  464.4s
[NODE-02] Block 276/500 | Index: 276 | Slot:  76 | Storage:  39.37 KB | Overwrites: Slot  76 | Hash Ops: 1102608 | Time: 0.042s | ETA:  462.4s
[NODE-02] Block 277/500 | Index: 277 | Slot:  77 | Storage:  39.37 KB | Overwrites: Slot  77 | Hash Ops: 1112875 | Time: 0.070s | ETA:  460.3s
[NODE-02] Block 278/500 | Index: 278 | Slot:  78 | Storage:  39.36 KB | Overwrites: Slot  78 | Hash Ops: 1118574 | Time: 0.059s | ETA:  458.2s
[NODE-02] Block 279/500 | Index: 279 | Slot:  79 | Storage:  39.36 KB | Overwrites: Slot  79 | Hash Ops: 1126145 | Time: 0.062s | ETA:  456.2s
[NODE-02] Block 280/500 | Index: 280 | Slot:  80 | Storage:  39.36 KB | Overwrites: Slot  80 | Hash Ops: 1128405 | Time: 0.027s | ETA:  454.1s
[NODE-02] Block 281/500 | Index: 281 | Slot:  81 | Storage:  39.36 KB | Overwrites: Slot  81 | Hash Ops: 1131255 | Time: 0.043s | ETA:  452.1s
[NODE-02] Block 282/500 | Index: 282 | Slot:  82 | Storage:  39.36 KB | Overwrites: Slot  82 | Hash Ops: 1139992 | Time: 0.078s | ETA:  450.1s
[NODE-02] Block 283/500 | Index: 283 | Slot:  83 | Storage:  39.36 KB | Overwrites: Slot  83 | Hash Ops: 1149237 | Time: 0.083s | ETA:  448.0s
[NODE-02] Block 284/500 | Index: 284 | Slot:  84 | Storage:  39.36 KB | Overwrites: Slot  84 | Hash Ops: 1157022 | Time: 0.061s | ETA:  446.0s
[NODE-02] Block 285/500 | Index: 285 | Slot:  85 | Storage:  39.36 KB | Overwrites: Slot  85 | Hash Ops: 1157079 | Time: 0.002s | ETA:  443.9s
[NODE-02] Block 286/500 | Index: 286 | Slot:  86 | Storage:  39.36 KB | Overwrites: Slot  86 | Hash Ops: 1159805 | Time: 0.028s | ETA:  441.8s
[NODE-02] Block 287/500 | Index: 287 | Slot:  87 | Storage:  39.36 KB | Overwrites: Slot  87 | Hash Ops: 1169236 | Time: 0.098s | ETA:  439.8s
[NODE-02] Block 288/500 | Index: 288 | Slot:  88 | Storage:  39.36 KB | Overwrites: Slot  88 | Hash Ops: 1170891 | Time: 0.023s | ETA:  437.7s
[NODE-02] Block 289/500 | Index: 289 | Slot:  89 | Storage:  39.36 KB | Overwrites: Slot  89 | Hash Ops: 1180322 | Time: 0.081s | ETA:  435.6s
[NODE-02] Block 290/500 | Index: 290 | Slot:  90 | Storage:  39.37 KB | Overwrites: Slot  90 | Hash Ops: 1180607 | Time: 0.009s | ETA:  433.5s
[NODE-02] Block 291/500 | Index: 291 | Slot:  91 | Storage:  39.36 KB | Overwrites: Slot  91 | Hash Ops: 1185638 | Time: 0.069s | ETA:  431.5s
[NODE-02] Block 292/500 | Index: 292 | Slot:  92 | Storage:  39.36 KB | Overwrites: Slot  92 | Hash Ops: 1187800 | Time: 0.020s | ETA:  429.5s
[NODE-02] Block 293/500 | Index: 293 | Slot:  93 | Storage:  39.36 KB | Overwrites: Slot  93 | Hash Ops: 1188640 | Time: 0.019s | ETA:  427.4s
[NODE-02] Block 294/500 | Index: 294 | Slot:  94 | Storage:  39.36 KB | Overwrites: Slot  94 | Hash Ops: 1193462 | Time: 0.042s | ETA:  425.3s
[NODE-02] Block 295/500 | Index: 295 | Slot:  95 | Storage:  39.36 KB | Overwrites: Slot  95 | Hash Ops: 1195304 | Time: 0.023s | ETA:  423.2s
[NODE-02] Block 296/500 | Index: 296 | Slot:  96 | Storage:  39.36 KB | Overwrites: Slot  96 | Hash Ops: 1197422 | Time: 0.021s | ETA:  421.1s
[NODE-02] Block 297/500 | Index: 297 | Slot:  97 | Storage:  39.36 KB | Overwrites: Slot  97 | Hash Ops: 1199584 | Time: 0.018s | ETA:  419.0s
[NODE-02] Block 298/500 | Index: 298 | Slot:  98 | Storage:  39.36 KB | Overwrites: Slot  98 | Hash Ops: 1206463 | Time: 0.047s | ETA:  417.0s
[NODE-02] Block 299/500 | Index: 299 | Slot:  99 | Storage:  39.36 KB | Overwrites: Slot  99 | Hash Ops: 1239701 | Time: 0.271s | ETA:  415.1s
[NODE-02] Block 300/500 | Index: 300 | Slot:   0 | Storage:  39.36 KB | Overwrites: Slot   0 | Hash Ops: 1242599 | Time: 0.022s | ETA:  413.0s
[NODE-02] Block 301/500 | Index: 301 | Slot:   1 | Storage:  39.36 KB | Overwrites: Slot   1 | Hash Ops: 1249317 | Time: 0.061s | ETA:  411.0s
[NODE-02] Block 302/500 | Index: 302 | Slot:   2 | Storage:  39.36 KB | Overwrites: Slot   2 | Hash Ops: 1251466 | Time: 0.035s | ETA:  408.9s
[NODE-02] Block 303/500 | Index: 303 | Slot:   3 | Storage:  39.36 KB | Overwrites: Slot   3 | Hash Ops: 1258309 | Time: 0.069s | ETA:  406.9s
[NODE-02] Block 304/500 | Index: 304 | Slot:   4 | Storage:  39.36 KB | Overwrites: Slot   4 | Hash Ops: 1258449 | Time: 0.001s | ETA:  404.8s
[NODE-02] Block 305/500 | Index: 305 | Slot:   5 | Storage:  39.36 KB | Overwrites: Slot   5 | Hash Ops: 1265015 | Time: 0.059s | ETA:  402.7s
[NODE-02] Block 306/500 | Index: 306 | Slot:   6 | Storage:  39.35 KB | Overwrites: Slot   6 | Hash Ops: 1267320 | Time: 0.019s | ETA:  400.6s
[NODE-02] Block 307/500 | Index: 307 | Slot:   7 | Storage:  39.35 KB | Overwrites: Slot   7 | Hash Ops: 1267321 | Time: 0.000s | ETA:  398.5s
[NODE-02] Block 308/500 | Index: 308 | Slot:   8 | Storage:  39.35 KB | Overwrites: Slot   8 | Hash Ops: 1267724 | Time: 0.005s | ETA:  396.5s
[NODE-02] Block 309/500 | Index: 309 | Slot:   9 | Storage:  39.35 KB | Overwrites: Slot   9 | Hash Ops: 1267914 | Time: 0.005s | ETA:  394.4s
[NODE-02] Block 310/500 | Index: 310 | Slot:  10 | Storage:  39.35 KB | Overwrites: Slot  10 | Hash Ops: 1268732 | Time: 0.009s | ETA:  392.3s
[NODE-02] Block 311/500 | Index: 311 | Slot:  11 | Storage:  39.35 KB | Overwrites: Slot  11 | Hash Ops: 1268790 | Time: 0.002s | ETA:  390.2s
[NODE-02] Block 312/500 | Index: 312 | Slot:  12 | Storage:  39.35 KB | Overwrites: Slot  12 | Hash Ops: 1269786 | Time: 0.007s | ETA:  388.1s
[NODE-02] Block 313/500 | Index: 313 | Slot:  13 | Storage:  39.35 KB | Overwrites: Slot  13 | Hash Ops: 1287472 | Time: 0.146s | ETA:  386.1s
[NODE-02] Block 314/500 | Index: 314 | Slot:  14 | Storage:  39.35 KB | Overwrites: Slot  14 | Hash Ops: 1288086 | Time: 0.018s | ETA:  384.1s
[NODE-02] Block 315/500 | Index: 315 | Slot:  15 | Storage:  39.35 KB | Overwrites: Slot  15 | Hash Ops: 1291056 | Time: 0.031s | ETA:  382.0s
[NODE-02] Block 316/500 | Index: 316 | Slot:  16 | Storage:  39.35 KB | Overwrites: Slot  16 | Hash Ops: 1291771 | Time: 0.009s | ETA:  379.9s
[NODE-02] Block 317/500 | Index: 317 | Slot:  17 | Storage:  39.35 KB | Overwrites: Slot  17 | Hash Ops: 1297028 | Time: 0.056s | ETA:  377.9s
[NODE-02] Block 318/500 | Index: 318 | Slot:  18 | Storage:  39.35 KB | Overwrites: Slot  18 | Hash Ops: 1303965 | Time: 0.057s | ETA:  375.8s
[NODE-02] Block 319/500 | Index: 319 | Slot:  19 | Storage:  39.35 KB | Overwrites: Slot  19 | Hash Ops: 1311540 | Time: 0.062s | ETA:  373.8s
[NODE-02] Block 320/500 | Index: 320 | Slot:  20 | Storage:  39.35 KB | Overwrites: Slot  20 | Hash Ops: 1316840 | Time: 0.044s | ETA:  371.7s
[NODE-02] Block 321/500 | Index: 321 | Slot:  21 | Storage:  39.35 KB | Overwrites: Slot  21 | Hash Ops: 1319834 | Time: 0.036s | ETA:  369.7s
[NODE-02] Block 322/500 | Index: 322 | Slot:  22 | Storage:  39.35 KB | Overwrites: Slot  22 | Hash Ops: 1322552 | Time: 0.031s | ETA:  367.7s
[NODE-02] Block 323/500 | Index: 323 | Slot:  23 | Storage:  39.35 KB | Overwrites: Slot  23 | Hash Ops: 1332187 | Time: 0.080s | ETA:  365.6s
[NODE-02] Block 324/500 | Index: 324 | Slot:  24 | Storage:  39.35 KB | Overwrites: Slot  24 | Hash Ops: 1338023 | Time: 0.058s | ETA:  363.5s
[NODE-02] Block 325/500 | Index: 325 | Slot:  25 | Storage:  39.35 KB | Overwrites: Slot  25 | Hash Ops: 1339696 | Time: 0.019s | ETA:  361.5s
[NODE-02] Block 326/500 | Index: 326 | Slot:  26 | Storage:  39.35 KB | Overwrites: Slot  26 | Hash Ops: 1339773 | Time: 0.002s | ETA:  359.4s
[NODE-02] Block 327/500 | Index: 327 | Slot:  27 | Storage:  39.35 KB | Overwrites: Slot  27 | Hash Ops: 1343954 | Time: 0.044s | ETA:  357.3s
[NODE-02] Block 328/500 | Index: 328 | Slot:  28 | Storage:  39.35 KB | Overwrites: Slot  28 | Hash Ops: 1347257 | Time: 0.025s | ETA:  355.2s
[NODE-02] Block 329/500 | Index: 329 | Slot:  29 | Storage:  39.35 KB | Overwrites: Slot  29 | Hash Ops: 1349399 | Time: 0.027s | ETA:  353.1s
[NODE-02] Block 330/500 | Index: 330 | Slot:  30 | Storage:  39.35 KB | Overwrites: Slot  30 | Hash Ops: 1349504 | Time: 0.004s | ETA:  351.0s
[NODE-02] Block 331/500 | Index: 331 | Slot:  31 | Storage:  39.35 KB | Overwrites: Slot  31 | Hash Ops: 1350028 | Time: 0.004s | ETA:  349.0s
[NODE-02] Block 332/500 | Index: 332 | Slot:  32 | Storage:  39.35 KB | Overwrites: Slot  32 | Hash Ops: 1356856 | Time: 0.075s | ETA:  347.0s
[NODE-02] Block 333/500 | Index: 333 | Slot:  33 | Storage:  39.35 KB | Overwrites: Slot  33 | Hash Ops: 1356980 | Time: 0.001s | ETA:  344.9s
[NODE-02] Block 334/500 | Index: 334 | Slot:  34 | Storage:  39.35 KB | Overwrites: Slot  34 | Hash Ops: 1359514 | Time: 0.018s | ETA:  342.8s
[NODE-02] Block 335/500 | Index: 335 | Slot:  35 | Storage:  39.35 KB | Overwrites: Slot  35 | Hash Ops: 1360800 | Time: 0.010s | ETA:  340.7s
[NODE-02] Block 336/500 | Index: 336 | Slot:  36 | Storage:  39.35 KB | Overwrites: Slot  36 | Hash Ops: 1363272 | Time: 0.041s | ETA:  338.6s
[NODE-02] Block 337/500 | Index: 337 | Slot:  37 | Storage:  39.35 KB | Overwrites: Slot  37 | Hash Ops: 1369050 | Time: 0.063s | ETA:  336.6s
[NODE-02] Block 338/500 | Index: 338 | Slot:  38 | Storage:  39.35 KB | Overwrites: Slot  38 | Hash Ops: 1381082 | Time: 0.104s | ETA:  334.5s
[NODE-02] Block 339/500 | Index: 339 | Slot:  39 | Storage:  39.35 KB | Overwrites: Slot  39 | Hash Ops: 1394803 | Time: 0.097s | ETA:  332.5s
[NODE-02] Block 340/500 | Index: 340 | Slot:  40 | Storage:  39.35 KB | Overwrites: Slot  40 | Hash Ops: 1396831 | Time: 0.026s | ETA:  330.4s
[NODE-02] Block 341/500 | Index: 341 | Slot:  41 | Storage:  39.36 KB | Overwrites: Slot  41 | Hash Ops: 1401578 | Time: 0.044s | ETA:  328.4s
[NODE-02] Block 342/500 | Index: 342 | Slot:  42 | Storage:  39.36 KB | Overwrites: Slot  42 | Hash Ops: 1402268 | Time: 0.016s | ETA:  326.3s
[NODE-02] Block 343/500 | Index: 343 | Slot:  43 | Storage:  39.36 KB | Overwrites: Slot  43 | Hash Ops: 1404924 | Time: 0.035s | ETA:  324.2s
[NODE-02] Block 344/500 | Index: 344 | Slot:  44 | Storage:  39.36 KB | Overwrites: Slot  44 | Hash Ops: 1415042 | Time: 0.092s | ETA:  322.2s
[NODE-02] Block 345/500 | Index: 345 | Slot:  45 | Storage:  39.36 KB | Overwrites: Slot  45 | Hash Ops: 1424894 | Time: 0.100s | ETA:  320.2s
[NODE-02] Block 346/500 | Index: 346 | Slot:  46 | Storage:  39.36 KB | Overwrites: Slot  46 | Hash Ops: 1425334 | Time: 0.014s | ETA:  318.1s
[NODE-02] Block 347/500 | Index: 347 | Slot:  47 | Storage:  39.36 KB | Overwrites: Slot  47 | Hash Ops: 1429759 | Time: 0.045s | ETA:  316.0s
[NODE-02] Block 348/500 | Index: 348 | Slot:  48 | Storage:  39.36 KB | Overwrites: Slot  48 | Hash Ops: 1447151 | Time: 0.120s | ETA:  314.0s
[NODE-02] Block 349/500 | Index: 349 | Slot:  49 | Storage:  39.36 KB | Overwrites: Slot  49 | Hash Ops: 1448417 | Time: 0.012s | ETA:  311.9s
[NODE-02] Block 350/500 | Index: 350 | Slot:  50 | Storage:  39.35 KB | Overwrites: Slot  50 | Hash Ops: 1448728 | Time: 0.002s | ETA:  309.8s
[NODE-02] Block 351/500 | Index: 351 | Slot:  51 | Storage:  39.36 KB | Overwrites: Slot  51 | Hash Ops: 1452090 | Time: 0.026s | ETA:  307.7s
[NODE-02] Block 352/500 | Index: 352 | Slot:  52 | Storage:  39.36 KB | Overwrites: Slot  52 | Hash Ops: 1456163 | Time: 0.030s | ETA:  305.7s
[NODE-02] Block 353/500 | Index: 353 | Slot:  53 | Storage:  39.35 KB | Overwrites: Slot  53 | Hash Ops: 1460798 | Time: 0.030s | ETA:  303.6s
[NODE-02] Block 354/500 | Index: 354 | Slot:  54 | Storage:  39.35 KB | Overwrites: Slot  54 | Hash Ops: 1469559 | Time: 0.061s | ETA:  301.5s
[NODE-02] Block 355/500 | Index: 355 | Slot:  55 | Storage:  39.35 KB | Overwrites: Slot  55 | Hash Ops: 1473313 | Time: 0.037s | ETA:  299.5s
[NODE-02] Block 356/500 | Index: 356 | Slot:  56 | Storage:  39.35 KB | Overwrites: Slot  56 | Hash Ops: 1478181 | Time: 0.046s | ETA:  297.4s
[NODE-02] Block 357/500 | Index: 357 | Slot:  57 | Storage:  39.35 KB | Overwrites: Slot  57 | Hash Ops: 1483996 | Time: 0.038s | ETA:  295.3s
[NODE-02] Block 358/500 | Index: 358 | Slot:  58 | Storage:  39.35 KB | Overwrites: Slot  58 | Hash Ops: 1490361 | Time: 0.048s | ETA:  293.3s
[NODE-02] Block 359/500 | Index: 359 | Slot:  59 | Storage:  39.36 KB | Overwrites: Slot  59 | Hash Ops: 1493703 | Time: 0.024s | ETA:  291.2s
[NODE-02] Block 360/500 | Index: 360 | Slot:  60 | Storage:  39.36 KB | Overwrites: Slot  60 | Hash Ops: 1497650 | Time: 0.032s | ETA:  289.1s
[NODE-02] Block 361/500 | Index: 361 | Slot:  61 | Storage:  39.36 KB | Overwrites: Slot  61 | Hash Ops: 1497777 | Time: 0.001s | ETA:  287.1s
[NODE-02] Block 362/500 | Index: 362 | Slot:  62 | Storage:  39.36 KB | Overwrites: Slot  62 | Hash Ops: 1504206 | Time: 0.044s | ETA:  285.0s
[NODE-02] Block 363/500 | Index: 363 | Slot:  63 | Storage:  39.36 KB | Overwrites: Slot  63 | Hash Ops: 1506132 | Time: 0.021s | ETA:  282.9s
[NODE-02] Block 364/500 | Index: 364 | Slot:  64 | Storage:  39.36 KB | Overwrites: Slot  64 | Hash Ops: 1506400 | Time: 0.006s | ETA:  280.9s
[NODE-02] Block 365/500 | Index: 365 | Slot:  65 | Storage:  39.35 KB | Overwrites: Slot  65 | Hash Ops: 1506728 | Time: 0.006s | ETA:  278.8s
[NODE-02] Block 366/500 | Index: 366 | Slot:  66 | Storage:  39.35 KB | Overwrites: Slot  66 | Hash Ops: 1507369 | Time: 0.007s | ETA:  276.7s
[NODE-02] Block 367/500 | Index: 367 | Slot:  67 | Storage:  39.36 KB | Overwrites: Slot  67 | Hash Ops: 1517351 | Time: 0.069s | ETA:  274.6s
[NODE-02] Block 368/500 | Index: 368 | Slot:  68 | Storage:  39.36 KB | Overwrites: Slot  68 | Hash Ops: 1519744 | Time: 0.019s | ETA:  272.5s
[NODE-02] Block 369/500 | Index: 369 | Slot:  69 | Storage:  39.36 KB | Overwrites: Slot  69 | Hash Ops: 1522338 | Time: 0.021s | ETA:  270.5s
[NODE-02] Block 370/500 | Index: 370 | Slot:  70 | Storage:  39.36 KB | Overwrites: Slot  70 | Hash Ops: 1525588 | Time: 0.025s | ETA:  268.4s
[NODE-02] Block 371/500 | Index: 371 | Slot:  71 | Storage:  39.35 KB | Overwrites: Slot  71 | Hash Ops: 1525653 | Time: 0.002s | ETA:  266.3s
[NODE-02] Block 372/500 | Index: 372 | Slot:  72 | Storage:  39.35 KB | Overwrites: Slot  72 | Hash Ops: 1525833 | Time: 0.005s | ETA:  264.3s
[NODE-02] Block 373/500 | Index: 373 | Slot:  73 | Storage:  39.35 KB | Overwrites: Slot  73 | Hash Ops: 1526341 | Time: 0.009s | ETA:  262.2s
[NODE-02] Block 374/500 | Index: 374 | Slot:  74 | Storage:  39.36 KB | Overwrites: Slot  74 | Hash Ops: 1537034 | Time: 0.073s | ETA:  260.2s
[NODE-02] Block 375/500 | Index: 375 | Slot:  75 | Storage:  39.36 KB | Overwrites: Slot  75 | Hash Ops: 1544850 | Time: 0.064s | ETA:  258.1s
[NODE-02] Block 376/500 | Index: 376 | Slot:  76 | Storage:  39.36 KB | Overwrites: Slot  76 | Hash Ops: 1548188 | Time: 0.026s | ETA:  256.0s
[NODE-02] Block 377/500 | Index: 377 | Slot:  77 | Storage:  39.36 KB | Overwrites: Slot  77 | Hash Ops: 1551272 | Time: 0.021s | ETA:  253.9s
[NODE-02] Block 378/500 | Index: 378 | Slot:  78 | Storage:  39.36 KB | Overwrites: Slot  78 | Hash Ops: 1558062 | Time: 0.044s | ETA:  251.9s
[NODE-02] Block 379/500 | Index: 379 | Slot:  79 | Storage:  39.36 KB | Overwrites: Slot  79 | Hash Ops: 1572810 | Time: 0.099s | ETA:  249.8s
[NODE-02] Block 380/500 | Index: 380 | Slot:  80 | Storage:  39.36 KB | Overwrites: Slot  80 | Hash Ops: 1574000 | Time: 0.018s | ETA:  247.7s
[NODE-02] Block 381/500 | Index: 381 | Slot:  81 | Storage:  39.36 KB | Overwrites: Slot  81 | Hash Ops: 1577850 | Time: 0.029s | ETA:  245.7s
[NODE-02] Block 382/500 | Index: 382 | Slot:  82 | Storage:  39.36 KB | Overwrites: Slot  82 | Hash Ops: 1578185 | Time: 0.006s | ETA:  243.6s
[NODE-02] Block 383/500 | Index: 383 | Slot:  83 | Storage:  39.36 KB | Overwrites: Slot  83 | Hash Ops: 1580429 | Time: 0.019s | ETA:  241.6s
[NODE-02] Block 384/500 | Index: 384 | Slot:  84 | Storage:  39.36 KB | Overwrites: Slot  84 | Hash Ops: 1581640 | Time: 0.009s | ETA:  239.5s
[NODE-02] Block 385/500 | Index: 385 | Slot:  85 | Storage:  39.36 KB | Overwrites: Slot  85 | Hash Ops: 1584811 | Time: 0.026s | ETA:  237.4s
[NODE-02] Block 386/500 | Index: 386 | Slot:  86 | Storage:  39.36 KB | Overwrites: Slot  86 | Hash Ops: 1587921 | Time: 0.025s | ETA:  235.3s
[NODE-02] Block 387/500 | Index: 387 | Slot:  87 | Storage:  39.36 KB | Overwrites: Slot  87 | Hash Ops: 1591653 | Time: 0.025s | ETA:  233.3s
[NODE-02] Block 388/500 | Index: 388 | Slot:  88 | Storage:  39.36 KB | Overwrites: Slot  88 | Hash Ops: 1597177 | Time: 0.041s | ETA:  231.2s
[NODE-02] Block 389/500 | Index: 389 | Slot:  89 | Storage:  39.36 KB | Overwrites: Slot  89 | Hash Ops: 1600471 | Time: 0.028s | ETA:  229.1s
[NODE-02] Block 390/500 | Index: 390 | Slot:  90 | Storage:  39.36 KB | Overwrites: Slot  90 | Hash Ops: 1604265 | Time: 0.029s | ETA:  227.0s
[NODE-02] Block 391/500 | Index: 391 | Slot:  91 | Storage:  39.36 KB | Overwrites: Slot  91 | Hash Ops: 1606546 | Time: 0.017s | ETA:  225.0s
[NODE-02] Block 392/500 | Index: 392 | Slot:  92 | Storage:  39.36 KB | Overwrites: Slot  92 | Hash Ops: 1612408 | Time: 0.041s | ETA:  222.9s
[NODE-02] Block 393/500 | Index: 393 | Slot:  93 | Storage:  39.36 KB | Overwrites: Slot  93 | Hash Ops: 1613005 | Time: 0.004s | ETA:  220.9s
[NODE-02] Block 394/500 | Index: 394 | Slot:  94 | Storage:  39.36 KB | Overwrites: Slot  94 | Hash Ops: 1616172 | Time: 0.031s | ETA:  218.8s
[NODE-02] Block 395/500 | Index: 395 | Slot:  95 | Storage:  39.37 KB | Overwrites: Slot  95 | Hash Ops: 1619003 | Time: 0.019s | ETA:  216.7s
[NODE-02] Block 396/500 | Index: 396 | Slot:  96 | Storage:  39.36 KB | Overwrites: Slot  96 | Hash Ops: 1619281 | Time: 0.003s | ETA:  214.7s
[NODE-02] Block 397/500 | Index: 397 | Slot:  97 | Storage:  39.37 KB | Overwrites: Slot  97 | Hash Ops: 1624045 | Time: 0.033s | ETA:  212.6s
[NODE-02] Block 398/500 | Index: 398 | Slot:  98 | Storage:  39.37 KB | Overwrites: Slot  98 | Hash Ops: 1627646 | Time: 0.024s | ETA:  210.5s
[NODE-02] Block 399/500 | Index: 399 | Slot:  99 | Storage:  39.37 KB | Overwrites: Slot  99 | Hash Ops: 1633977 | Time: 0.044s | ETA:  208.5s
[NODE-02] Block 400/500 | Index: 400 | Slot:   0 | Storage:  39.37 KB | Overwrites: Slot   0 | Hash Ops: 1639449 | Time: 0.044s | ETA:  206.4s
[NODE-02] Block 401/500 | Index: 401 | Slot:   1 | Storage:  39.37 KB | Overwrites: Slot   1 | Hash Ops: 1654888 | Time: 0.108s | ETA:  204.4s
[NODE-02] Block 402/500 | Index: 402 | Slot:   2 | Storage:  39.37 KB | Overwrites: Slot   2 | Hash Ops: 1656267 | Time: 0.014s | ETA:  202.3s
[NODE-02] Block 403/500 | Index: 403 | Slot:   3 | Storage:  39.37 KB | Overwrites: Slot   3 | Hash Ops: 1659431 | Time: 0.025s | ETA:  200.2s
[NODE-02] Block 404/500 | Index: 404 | Slot:   4 | Storage:  39.37 KB | Overwrites: Slot   4 | Hash Ops: 1664557 | Time: 0.038s | ETA:  198.2s
[NODE-02] Block 405/500 | Index: 405 | Slot:   5 | Storage:  39.37 KB | Overwrites: Slot   5 | Hash Ops: 1669000 | Time: 0.030s | ETA:  196.1s
[NODE-02] Block 406/500 | Index: 406 | Slot:   6 | Storage:  39.37 KB | Overwrites: Slot   6 | Hash Ops: 1671213 | Time: 0.018s | ETA:  194.0s
[NODE-02] Block 407/500 | Index: 407 | Slot:   7 | Storage:  39.38 KB | Overwrites: Slot   7 | Hash Ops: 1673935 | Time: 0.027s | ETA:  191.9s
[NODE-02] Block 408/500 | Index: 408 | Slot:   8 | Storage:  39.38 KB | Overwrites: Slot   8 | Hash Ops: 1676288 | Time: 0.020s | ETA:  189.9s
[NODE-02] Block 409/500 | Index: 409 | Slot:   9 | Storage:  39.38 KB | Overwrites: Slot   9 | Hash Ops: 1676357 | Time: 0.002s | ETA:  187.8s
[NODE-02] Block 410/500 | Index: 410 | Slot:  10 | Storage:  39.37 KB | Overwrites: Slot  10 | Hash Ops: 1676980 | Time: 0.007s | ETA:  185.7s
[NODE-02] Block 411/500 | Index: 411 | Slot:  11 | Storage:  39.38 KB | Overwrites: Slot  11 | Hash Ops: 1688461 | Time: 0.080s | ETA:  183.7s
[NODE-02] Block 412/500 | Index: 412 | Slot:  12 | Storage:  39.37 KB | Overwrites: Slot  12 | Hash Ops: 1692990 | Time: 0.039s | ETA:  181.6s
[NODE-02] Block 413/500 | Index: 413 | Slot:  13 | Storage:  39.38 KB | Overwrites: Slot  13 | Hash Ops: 1694581 | Time: 0.011s | ETA:  179.6s
[NODE-02] Block 414/500 | Index: 414 | Slot:  14 | Storage:  39.38 KB | Overwrites: Slot  14 | Hash Ops: 1696992 | Time: 0.017s | ETA:  177.5s
[NODE-02] Block 415/500 | Index: 415 | Slot:  15 | Storage:  39.38 KB | Overwrites: Slot  15 | Hash Ops: 1703471 | Time: 0.046s | ETA:  175.4s
[NODE-02] Block 416/500 | Index: 416 | Slot:  16 | Storage:  39.38 KB | Overwrites: Slot  16 | Hash Ops: 1705853 | Time: 0.020s | ETA:  173.4s
[NODE-02] Block 417/500 | Index: 417 | Slot:  17 | Storage:  39.38 KB | Overwrites: Slot  17 | Hash Ops: 1709257 | Time: 0.022s | ETA:  171.3s
[NODE-02] Block 418/500 | Index: 418 | Slot:  18 | Storage:  39.38 KB | Overwrites: Slot  18 | Hash Ops: 1723564 | Time: 0.098s | ETA:  169.2s
[NODE-02] Block 419/500 | Index: 419 | Slot:  19 | Storage:  39.38 KB | Overwrites: Slot  19 | Hash Ops: 1724353 | Time: 0.010s | ETA:  167.2s
[NODE-02] Block 420/500 | Index: 420 | Slot:  20 | Storage:  39.38 KB | Overwrites: Slot  20 | Hash Ops: 1725907 | Time: 0.014s | ETA:  165.1s
[NODE-02] Block 421/500 | Index: 421 | Slot:  21 | Storage:  39.38 KB | Overwrites: Slot  21 | Hash Ops: 1726711 | Time: 0.013s | ETA:  163.0s
[NODE-02] Block 422/500 | Index: 422 | Slot:  22 | Storage:  39.38 KB | Overwrites: Slot  22 | Hash Ops: 1731427 | Time: 0.037s | ETA:  161.0s
[NODE-02] Block 423/500 | Index: 423 | Slot:  23 | Storage:  39.38 KB | Overwrites: Slot  23 | Hash Ops: 1732483 | Time: 0.010s | ETA:  158.9s
[NODE-02] Block 424/500 | Index: 424 | Slot:  24 | Storage:  39.38 KB | Overwrites: Slot  24 | Hash Ops: 1735439 | Time: 0.024s | ETA:  156.8s
[NODE-02] Block 425/500 | Index: 425 | Slot:  25 | Storage:  39.38 KB | Overwrites: Slot  25 | Hash Ops: 1735651 | Time: 0.005s | ETA:  154.8s
[NODE-02] Block 426/500 | Index: 426 | Slot:  26 | Storage:  39.38 KB | Overwrites: Slot  26 | Hash Ops: 1736603 | Time: 0.010s | ETA:  152.7s
[NODE-02] Block 427/500 | Index: 427 | Slot:  27 | Storage:  39.38 KB | Overwrites: Slot  27 | Hash Ops: 1739877 | Time: 0.023s | ETA:  150.6s
[NODE-02] Block 428/500 | Index: 428 | Slot:  28 | Storage:  39.38 KB | Overwrites: Slot  28 | Hash Ops: 1752333 | Time: 0.087s | ETA:  148.6s
[NODE-02] Block 429/500 | Index: 429 | Slot:  29 | Storage:  39.38 KB | Overwrites: Slot  29 | Hash Ops: 1760037 | Time: 0.053s | ETA:  146.5s
[NODE-02] Block 430/500 | Index: 430 | Slot:  30 | Storage:  39.38 KB | Overwrites: Slot  30 | Hash Ops: 1762567 | Time: 0.021s | ETA:  144.4s
[NODE-02] Block 431/500 | Index: 431 | Slot:  31 | Storage:  39.38 KB | Overwrites: Slot  31 | Hash Ops: 1763507 | Time: 0.014s | ETA:  142.4s
[NODE-02] Block 432/500 | Index: 432 | Slot:  32 | Storage:  39.38 KB | Overwrites: Slot  32 | Hash Ops: 1766677 | Time: 0.029s | ETA:  140.3s
[NODE-02] Block 433/500 | Index: 433 | Slot:  33 | Storage:  39.38 KB | Overwrites: Slot  33 | Hash Ops: 1766708 | Time: 0.001s | ETA:  138.3s
[NODE-02] Block 434/500 | Index: 434 | Slot:  34 | Storage:  39.38 KB | Overwrites: Slot  34 | Hash Ops: 1767830 | Time: 0.016s | ETA:  136.2s
[NODE-02] Block 435/500 | Index: 435 | Slot:  35 | Storage:  39.38 KB | Overwrites: Slot  35 | Hash Ops: 1769665 | Time: 0.013s | ETA:  134.1s
[NODE-02] Block 436/500 | Index: 436 | Slot:  36 | Storage:  39.38 KB | Overwrites: Slot  36 | Hash Ops: 1770518 | Time: 0.006s | ETA:  132.1s
[NODE-02] Block 437/500 | Index: 437 | Slot:  37 | Storage:  39.37 KB | Overwrites: Slot  37 | Hash Ops: 1771186 | Time: 0.013s | ETA:  130.0s
[NODE-02] Block 438/500 | Index: 438 | Slot:  38 | Storage:  39.37 KB | Overwrites: Slot  38 | Hash Ops: 1773529 | Time: 0.018s | ETA:  127.9s
[NODE-02] Block 439/500 | Index: 439 | Slot:  39 | Storage:  39.37 KB | Overwrites: Slot  39 | Hash Ops: 1775758 | Time: 0.015s | ETA:  125.9s
[NODE-02] Block 440/500 | Index: 440 | Slot:  40 | Storage:  39.37 KB | Overwrites: Slot  40 | Hash Ops: 1781246 | Time: 0.038s | ETA:  123.8s
[NODE-02] Block 441/500 | Index: 441 | Slot:  41 | Storage:  39.37 KB | Overwrites: Slot  41 | Hash Ops: 1790924 | Time: 0.072s | ETA:  121.7s
[NODE-02] Block 442/500 | Index: 442 | Slot:  42 | Storage:  39.37 KB | Overwrites: Slot  42 | Hash Ops: 1791769 | Time: 0.013s | ETA:  119.7s
[NODE-02] Block 443/500 | Index: 443 | Slot:  43 | Storage:  39.37 KB | Overwrites: Slot  43 | Hash Ops: 1794297 | Time: 0.024s | ETA:  117.6s
[NODE-02] Block 444/500 | Index: 444 | Slot:  44 | Storage:  39.37 KB | Overwrites: Slot  44 | Hash Ops: 1796015 | Time: 0.016s | ETA:  115.6s
[NODE-02] Block 445/500 | Index: 445 | Slot:  45 | Storage:  39.37 KB | Overwrites: Slot  45 | Hash Ops: 1796919 | Time: 0.006s | ETA:  113.5s
[NODE-02] Block 446/500 | Index: 446 | Slot:  46 | Storage:  39.37 KB | Overwrites: Slot  46 | Hash Ops: 1798345 | Time: 0.013s | ETA:  111.4s
[NODE-02] Block 447/500 | Index: 447 | Slot:  47 | Storage:  39.37 KB | Overwrites: Slot  47 | Hash Ops: 1801537 | Time: 0.026s | ETA:  109.4s
[NODE-02] Block 448/500 | Index: 448 | Slot:  48 | Storage:  39.37 KB | Overwrites: Slot  48 | Hash Ops: 1801743 | Time: 0.005s | ETA:  107.3s
[NODE-02] Block 449/500 | Index: 449 | Slot:  49 | Storage:  39.37 KB | Overwrites: Slot  49 | Hash Ops: 1804282 | Time: 0.019s | ETA:  105.2s
[NODE-02] Block 450/500 | Index: 450 | Slot:  50 | Storage:  39.37 KB | Overwrites: Slot  50 | Hash Ops: 1806382 | Time: 0.021s | ETA:  103.2s
[NODE-02] Block 451/500 | Index: 451 | Slot:  51 | Storage:  39.37 KB | Overwrites: Slot  51 | Hash Ops: 1813206 | Time: 0.049s | ETA:  101.1s
[NODE-02] Block 452/500 | Index: 452 | Slot:  52 | Storage:  39.37 KB | Overwrites: Slot  52 | Hash Ops: 1817910 | Time: 0.034s | ETA:   99.0s
[NODE-02] Block 453/500 | Index: 453 | Slot:  53 | Storage:  39.37 KB | Overwrites: Slot  53 | Hash Ops: 1819732 | Time: 0.022s | ETA:   97.0s
[NODE-02] Block 454/500 | Index: 454 | Slot:  54 | Storage:  39.37 KB | Overwrites: Slot  54 | Hash Ops: 1823751 | Time: 0.031s | ETA:   94.9s
[NODE-02] Block 455/500 | Index: 455 | Slot:  55 | Storage:  39.37 KB | Overwrites: Slot  55 | Hash Ops: 1831690 | Time: 0.057s | ETA:   92.8s
[NODE-02] Block 456/500 | Index: 456 | Slot:  56 | Storage:  39.37 KB | Overwrites: Slot  56 | Hash Ops: 1835837 | Time: 0.032s | ETA:   90.8s
[NODE-02] Block 457/500 | Index: 457 | Slot:  57 | Storage:  39.37 KB | Overwrites: Slot  57 | Hash Ops: 1835869 | Time: 0.001s | ETA:   88.7s
[NODE-02] Block 458/500 | Index: 458 | Slot:  58 | Storage:  39.37 KB | Overwrites: Slot  58 | Hash Ops: 1841343 | Time: 0.037s | ETA:   86.6s
[NODE-02] Block 459/500 | Index: 459 | Slot:  59 | Storage:  39.37 KB | Overwrites: Slot  59 | Hash Ops: 1853987 | Time: 0.089s | ETA:   84.6s
[NODE-02] Block 460/500 | Index: 460 | Slot:  60 | Storage:  39.37 KB | Overwrites: Slot  60 | Hash Ops: 1864172 | Time: 0.071s | ETA:   82.5s
[NODE-02] Block 461/500 | Index: 461 | Slot:  61 | Storage:  39.37 KB | Overwrites: Slot  61 | Hash Ops: 1878311 | Time: 0.097s | ETA:   80.5s
[NODE-02] Block 462/500 | Index: 462 | Slot:  62 | Storage:  39.37 KB | Overwrites: Slot  62 | Hash Ops: 1881665 | Time: 0.030s | ETA:   78.4s
[NODE-02] Block 463/500 | Index: 463 | Slot:  63 | Storage:  39.37 KB | Overwrites: Slot  63 | Hash Ops: 1881723 | Time: 0.002s | ETA:   76.3s
[NODE-02] Block 464/500 | Index: 464 | Slot:  64 | Storage:  39.37 KB | Overwrites: Slot  64 | Hash Ops: 1884698 | Time: 0.020s | ETA:   74.3s
[NODE-02] Block 465/500 | Index: 465 | Slot:  65 | Storage:  39.37 KB | Overwrites: Slot  65 | Hash Ops: 1886535 | Time: 0.021s | ETA:   72.2s
[NODE-02] Block 466/500 | Index: 466 | Slot:  66 | Storage:  39.37 KB | Overwrites: Slot  66 | Hash Ops: 1897668 | Time: 0.078s | ETA:   70.2s
[NODE-02] Block 467/500 | Index: 467 | Slot:  67 | Storage:  39.37 KB | Overwrites: Slot  67 | Hash Ops: 1907461 | Time: 0.074s | ETA:   68.1s
[NODE-02] Block 468/500 | Index: 468 | Slot:  68 | Storage:  39.37 KB | Overwrites: Slot  68 | Hash Ops: 1907583 | Time: 0.003s | ETA:   66.0s
[NODE-02] Block 469/500 | Index: 469 | Slot:  69 | Storage:  39.37 KB | Overwrites: Slot  69 | Hash Ops: 1909237 | Time: 0.017s | ETA:   64.0s
[NODE-02] Block 470/500 | Index: 470 | Slot:  70 | Storage:  39.37 KB | Overwrites: Slot  70 | Hash Ops: 1913092 | Time: 0.026s | ETA:   61.9s
[NODE-02] Block 471/500 | Index: 471 | Slot:  71 | Storage:  39.37 KB | Overwrites: Slot  71 | Hash Ops: 1915669 | Time: 0.021s | ETA:   59.8s
[NODE-02] Block 472/500 | Index: 472 | Slot:  72 | Storage:  39.37 KB | Overwrites: Slot  72 | Hash Ops: 1918730 | Time: 0.026s | ETA:   57.8s
[NODE-02] Block 473/500 | Index: 473 | Slot:  73 | Storage:  39.37 KB | Overwrites: Slot  73 | Hash Ops: 1922897 | Time: 0.032s | ETA:   55.7s
[NODE-02] Block 474/500 | Index: 474 | Slot:  74 | Storage:  39.37 KB | Overwrites: Slot  74 | Hash Ops: 1923783 | Time: 0.008s | ETA:   53.6s
[NODE-02] Block 475/500 | Index: 475 | Slot:  75 | Storage:  39.37 KB | Overwrites: Slot  75 | Hash Ops: 1924764 | Time: 0.011s | ETA:   51.6s
[NODE-02] Block 476/500 | Index: 476 | Slot:  76 | Storage:  39.37 KB | Overwrites: Slot  76 | Hash Ops: 1925073 | Time: 0.006s | ETA:   49.5s
[NODE-02] Block 477/500 | Index: 477 | Slot:  77 | Storage:  39.37 KB | Overwrites: Slot  77 | Hash Ops: 1926691 | Time: 0.015s | ETA:   47.4s
[NODE-02] Block 478/500 | Index: 478 | Slot:  78 | Storage:  39.37 KB | Overwrites: Slot  78 | Hash Ops: 1927633 | Time: 0.011s | ETA:   45.4s
[NODE-02] Block 479/500 | Index: 479 | Slot:  79 | Storage:  39.37 KB | Overwrites: Slot  79 | Hash Ops: 1933343 | Time: 0.046s | ETA:   43.3s
[NODE-02] Block 480/500 | Index: 480 | Slot:  80 | Storage:  39.36 KB | Overwrites: Slot  80 | Hash Ops: 1934072 | Time: 0.014s | ETA:   41.3s
[NODE-02] Block 481/500 | Index: 481 | Slot:  81 | Storage:  39.37 KB | Overwrites: Slot  81 | Hash Ops: 1935864 | Time: 0.012s | ETA:   39.2s
[NODE-02] Block 482/500 | Index: 482 | Slot:  82 | Storage:  39.37 KB | Overwrites: Slot  82 | Hash Ops: 1940513 | Time: 0.033s | ETA:   37.1s
[NODE-02] Block 483/500 | Index: 483 | Slot:  83 | Storage:  39.37 KB | Overwrites: Slot  83 | Hash Ops: 1948300 | Time: 0.059s | ETA:   35.1s
[NODE-02] Block 484/500 | Index: 484 | Slot:  84 | Storage:  39.37 KB | Overwrites: Slot  84 | Hash Ops: 1956035 | Time: 0.054s | ETA:   33.0s
[NODE-02] Block 485/500 | Index: 485 | Slot:  85 | Storage:  39.37 KB | Overwrites: Slot  85 | Hash Ops: 1960259 | Time: 0.029s | ETA:   30.9s
[NODE-02] Block 486/500 | Index: 486 | Slot:  86 | Storage:  39.37 KB | Overwrites: Slot  86 | Hash Ops: 1974570 | Time: 0.100s | ETA:   28.9s
[NODE-02] Block 487/500 | Index: 487 | Slot:  87 | Storage:  39.37 KB | Overwrites: Slot  87 | Hash Ops: 1978969 | Time: 0.029s | ETA:   26.8s
[NODE-02] Block 488/500 | Index: 488 | Slot:  88 | Storage:  39.37 KB | Overwrites: Slot  88 | Hash Ops: 1987760 | Time: 0.059s | ETA:   24.8s
[NODE-02] Block 489/500 | Index: 489 | Slot:  89 | Storage:  39.36 KB | Overwrites: Slot  89 | Hash Ops: 1988760 | Time: 0.011s | ETA:   22.7s
[NODE-02] Block 490/500 | Index: 490 | Slot:  90 | Storage:  39.36 KB | Overwrites: Slot  90 | Hash Ops: 1995023 | Time: 0.041s | ETA:   20.6s
[NODE-02] Block 491/500 | Index: 491 | Slot:  91 | Storage:  39.36 KB | Overwrites: Slot  91 | Hash Ops: 1999567 | Time: 0.032s | ETA:   18.6s
[NODE-02] Block 492/500 | Index: 492 | Slot:  92 | Storage:  39.36 KB | Overwrites: Slot  92 | Hash Ops: 2005599 | Time: 0.041s | ETA:   16.5s
[NODE-02] Block 493/500 | Index: 493 | Slot:  93 | Storage:  39.36 KB | Overwrites: Slot  93 | Hash Ops: 2006295 | Time: 0.005s | ETA:   14.4s
[NODE-02] Block 494/500 | Index: 494 | Slot:  94 | Storage:  39.36 KB | Overwrites: Slot  94 | Hash Ops: 2008145 | Time: 0.018s | ETA:   12.4s
[NODE-02] Block 495/500 | Index: 495 | Slot:  95 | Storage:  39.36 KB | Overwrites: Slot  95 | Hash Ops: 2008263 | Time: 0.002s | ETA:   10.3s
[NODE-02] Block 496/500 | Index: 496 | Slot:  96 | Storage:  39.36 KB | Overwrites: Slot  96 | Hash Ops: 2008542 | Time: 0.005s | ETA:    8.3s
[NODE-02] Block 497/500 | Index: 497 | Slot:  97 | Storage:  39.36 KB | Overwrites: Slot  97 | Hash Ops: 2008968 | Time: 0.005s | ETA:    6.2s
[NODE-02] Block 498/500 | Index: 498 | Slot:  98 | Storage:  39.36 KB | Overwrites: Slot  98 | Hash Ops: 2009121 | Time: 0.004s | ETA:    4.1s
[NODE-02] Block 499/500 | Index: 499 | Slot:  99 | Storage:  39.36 KB | Overwrites: Slot  99 | Hash Ops: 2015946 | Time: 0.049s | ETA:    2.1s
[NODE-02] Block 500/500 | Index: 500 | Slot:   0 | Storage:  39.36 KB | Overwrites: Slot   0 | Hash Ops: 2024201 | Time: 0.055s | ETA:    0.0s
[NODE-02] Peer connections restored
[NODE-02] Completed in 1033.29 seconds

================================================================================
Resetting NODE-03 to genesis before its simulation
================================================================================
✓ NODE-03 reset to genesis (index=0)


[NODE-03] Starting block generation...
[NODE-03] Initial ledger state:
[NODE-03]   Last index: 0
[NODE-03]   Genesis hash: 000ac6d79f7c53bb...
[NODE-03] Target: 500 blocks
[NODE-03] Mode: Independent (no peer interaction)
[NODE-03] Peers temporarily disconnected for independent simulation
[NODE-03] Block   1/500 | Index:   1 | Slot:   1 | Storage:   0.70 KB | Overwrites:   - | Hash Ops:   5022 | Time: 0.038s | ETA:   69.0s
[NODE-03] Block   2/500 | Index:   2 | Slot:   2 | Storage:   1.09 KB | Overwrites:   - | Hash Ops:  16980 | Time: 0.106s | ETA:  559.5s
[NODE-03] Block   3/500 | Index:   3 | Slot:   3 | Storage:   1.47 KB | Overwrites:   - | Hash Ops:  19835 | Time: 0.033s | ETA:  723.1s
[NODE-03] Block   4/500 | Index:   4 | Slot:   4 | Storage:   1.86 KB | Overwrites:   - | Hash Ops:  21362 | Time: 0.022s | ETA:  796.1s
[NODE-03] Block   5/500 | Index:   5 | Slot:   5 | Storage:   2.25 KB | Overwrites:   - | Hash Ops:  23664 | Time: 0.029s | ETA:  837.6s
[NODE-03] Block   6/500 | Index:   6 | Slot:   6 | Storage:   2.64 KB | Overwrites:   - | Hash Ops:  27062 | Time: 0.027s | ETA:  866.3s
[NODE-03] Block   7/500 | Index:   7 | Slot:   7 | Storage:   3.03 KB | Overwrites:   - | Hash Ops:  27483 | Time: 0.003s | ETA:  882.8s
[NODE-03] Block   8/500 | Index:   8 | Slot:   8 | Storage:   3.42 KB | Overwrites:   - | Hash Ops:  28012 | Time: 0.006s | ETA:  894.9s
[NODE-03] Block   9/500 | Index:   9 | Slot:   9 | Storage:   3.81 KB | Overwrites:   - | Hash Ops:  29916 | Time: 0.020s | ETA:  904.5s
[NODE-03] Block  10/500 | Index:  10 | Slot:  10 | Storage:   4.20 KB | Overwrites:   - | Hash Ops:  31659 | Time: 0.016s | ETA:  913.0s
[NODE-03] Block  11/500 | Index:  11 | Slot:  11 | Storage:   4.59 KB | Overwrites:   - | Hash Ops:  33364 | Time: 0.019s | ETA:  924.7s
[NODE-03] Block  12/500 | Index:  12 | Slot:  12 | Storage:   4.98 KB | Overwrites:   - | Hash Ops:  34232 | Time: 0.016s | ETA:  928.7s
[NODE-03] Block  13/500 | Index:  13 | Slot:  13 | Storage:   5.37 KB | Overwrites:   - | Hash Ops:  34369 | Time: 0.001s | ETA:  930.9s
[NODE-03] Block  14/500 | Index:  14 | Slot:  14 | Storage:   5.76 KB | Overwrites:   - | Hash Ops:  42140 | Time: 0.056s | ETA:  934.5s
[NODE-03] Block  15/500 | Index:  15 | Slot:  15 | Storage:   6.15 KB | Overwrites:   - | Hash Ops:  42775 | Time: 0.005s | ETA:  935.8s
[NODE-03] Block  16/500 | Index:  16 | Slot:  16 | Storage:   6.54 KB | Overwrites:   - | Hash Ops:  43242 | Time: 0.003s | ETA:  937.6s
[NODE-03] Block  17/500 | Index:  17 | Slot:  17 | Storage:   6.93 KB | Overwrites:   - | Hash Ops:  43377 | Time: 0.001s | ETA:  938.9s
[NODE-03] Block  18/500 | Index:  18 | Slot:  18 | Storage:   7.32 KB | Overwrites:   - | Hash Ops:  45882 | Time: 0.046s | ETA:  939.8s
[NODE-03] Block  19/500 | Index:  19 | Slot:  19 | Storage:   7.71 KB | Overwrites:   - | Hash Ops:  53999 | Time: 0.084s | ETA:  941.8s
[NODE-03] Block  20/500 | Index:  20 | Slot:  20 | Storage:   8.10 KB | Overwrites:   - | Hash Ops:  57408 | Time: 0.027s | ETA:  942.1s
[NODE-03] Block  21/500 | Index:  21 | Slot:  21 | Storage:   8.49 KB | Overwrites:   - | Hash Ops:  58932 | Time: 0.015s | ETA:  944.7s
[NODE-03] Block  22/500 | Index:  22 | Slot:  22 | Storage:   8.88 KB | Overwrites:   - | Hash Ops:  84777 | Time: 0.229s | ETA:  949.0s
[NODE-03] Block  23/500 | Index:  23 | Slot:  23 | Storage:   9.27 KB | Overwrites:   - | Hash Ops:  86685 | Time: 0.017s | ETA:  947.9s
[NODE-03] Block  24/500 | Index:  24 | Slot:  24 | Storage:   9.67 KB | Overwrites:   - | Hash Ops:  87789 | Time: 0.008s | ETA:  946.6s
[NODE-03] Block  25/500 | Index:  25 | Slot:  25 | Storage:  10.06 KB | Overwrites:   - | Hash Ops:  93813 | Time: 0.044s | ETA:  946.4s
[NODE-03] Block  26/500 | Index:  26 | Slot:  26 | Storage:  10.45 KB | Overwrites:   - | Hash Ops: 104772 | Time: 0.089s | ETA:  946.3s
[NODE-03] Block  27/500 | Index:  27 | Slot:  27 | Storage:  10.84 KB | Overwrites:   - | Hash Ops: 116726 | Time: 0.095s | ETA:  946.1s
[NODE-03] Block  28/500 | Index:  28 | Slot:  28 | Storage:  11.23 KB | Overwrites:   - | Hash Ops: 119707 | Time: 0.039s | ETA:  945.4s
[NODE-03] Block  29/500 | Index:  29 | Slot:  29 | Storage:  11.62 KB | Overwrites:   - | Hash Ops: 124046 | Time: 0.040s | ETA:  944.2s
[NODE-03] Block  30/500 | Index:  30 | Slot:  30 | Storage:  12.02 KB | Overwrites:   - | Hash Ops: 133786 | Time: 0.093s | ETA:  943.6s
[NODE-03] Block  31/500 | Index:  31 | Slot:  31 | Storage:  12.41 KB | Overwrites:   - | Hash Ops: 141535 | Time: 0.054s | ETA:  944.6s
[NODE-03] Block  32/500 | Index:  32 | Slot:  32 | Storage:  12.80 KB | Overwrites:   - | Hash Ops: 142331 | Time: 0.008s | ETA:  942.7s
[NODE-03] Block  33/500 | Index:  33 | Slot:  33 | Storage:  13.19 KB | Overwrites:   - | Hash Ops: 147586 | Time: 0.049s | ETA:  941.6s
[NODE-03] Block  34/500 | Index:  34 | Slot:  34 | Storage:  13.58 KB | Overwrites:   - | Hash Ops: 151439 | Time: 0.037s | ETA:  939.9s
[NODE-03] Block  35/500 | Index:  35 | Slot:  35 | Storage:  13.97 KB | Overwrites:   - | Hash Ops: 151989 | Time: 0.007s | ETA:  938.0s
[NODE-03] Block  36/500 | Index:  36 | Slot:  36 | Storage:  14.36 KB | Overwrites:   - | Hash Ops: 153766 | Time: 0.029s | ETA:  936.2s
[NODE-03] Block  37/500 | Index:  37 | Slot:  37 | Storage:  14.75 KB | Overwrites:   - | Hash Ops: 157822 | Time: 0.042s | ETA:  934.6s
[NODE-03] Block  38/500 | Index:  38 | Slot:  38 | Storage:  15.15 KB | Overwrites:   - | Hash Ops: 161696 | Time: 0.039s | ETA:  933.0s
[NODE-03] Block  39/500 | Index:  39 | Slot:  39 | Storage:  15.54 KB | Overwrites:   - | Hash Ops: 177953 | Time: 0.130s | ETA:  932.3s
[NODE-03] Block  40/500 | Index:  40 | Slot:  40 | Storage:  15.93 KB | Overwrites:   - | Hash Ops: 185145 | Time: 0.055s | ETA:  930.8s
[NODE-03] Block  41/500 | Index:  41 | Slot:  41 | Storage:  16.32 KB | Overwrites:   - | Hash Ops: 186732 | Time: 0.022s | ETA:  930.0s
[NODE-03] Block  42/500 | Index:  42 | Slot:  42 | Storage:  16.71 KB | Overwrites:   - | Hash Ops: 194921 | Time: 0.069s | ETA:  928.7s
[NODE-03] Block  43/500 | Index:  43 | Slot:  43 | Storage:  17.10 KB | Overwrites:   - | Hash Ops: 197519 | Time: 0.030s | ETA:  926.9s
[NODE-03] Block  44/500 | Index:  44 | Slot:  44 | Storage:  17.49 KB | Overwrites:   - | Hash Ops: 198016 | Time: 0.010s | ETA:  924.8s
[NODE-03] Block  45/500 | Index:  45 | Slot:  45 | Storage:  17.88 KB | Overwrites:   - | Hash Ops: 202091 | Time: 0.039s | ETA:  923.0s
[NODE-03] Block  46/500 | Index:  46 | Slot:  46 | Storage:  18.27 KB | Overwrites:   - | Hash Ops: 206370 | Time: 0.044s | ETA:  921.5s
[NODE-03] Block  47/500 | Index:  47 | Slot:  47 | Storage:  18.66 KB | Overwrites:   - | Hash Ops: 208446 | Time: 0.026s | ETA:  919.6s
[NODE-03] Block  48/500 | Index:  48 | Slot:  48 | Storage:  19.05 KB | Overwrites:   - | Hash Ops: 209095 | Time: 0.009s | ETA:  917.5s
[NODE-03] Block  49/500 | Index:  49 | Slot:  49 | Storage:  19.44 KB | Overwrites:   - | Hash Ops: 214693 | Time: 0.057s | ETA:  915.8s
[NODE-03] Block  50/500 | Index:  50 | Slot:  50 | Storage:  19.83 KB | Overwrites:   - | Hash Ops: 217351 | Time: 0.036s | ETA:  913.9s
[NODE-03] Block  51/500 | Index:  51 | Slot:  51 | Storage:  20.23 KB | Overwrites:   - | Hash Ops: 218709 | Time: 0.021s | ETA:  912.8s
[NODE-03] Block  52/500 | Index:  52 | Slot:  52 | Storage:  20.62 KB | Overwrites:   - | Hash Ops: 220265 | Time: 0.028s | ETA:  911.1s
[NODE-03] Block  53/500 | Index:  53 | Slot:  53 | Storage:  21.01 KB | Overwrites:   - | Hash Ops: 229379 | Time: 0.092s | ETA:  909.6s
[NODE-03] Block  54/500 | Index:  54 | Slot:  54 | Storage:  21.40 KB | Overwrites:   - | Hash Ops: 241432 | Time: 0.094s | ETA:  908.1s
[NODE-03] Block  55/500 | Index:  55 | Slot:  55 | Storage:  21.79 KB | Overwrites:   - | Hash Ops: 245890 | Time: 0.050s | ETA:  906.4s
[NODE-03] Block  56/500 | Index:  56 | Slot:  56 | Storage:  22.18 KB | Overwrites:   - | Hash Ops: 248446 | Time: 0.034s | ETA:  904.4s
[NODE-03] Block  57/500 | Index:  57 | Slot:  57 | Storage:  22.58 KB | Overwrites:   - | Hash Ops: 252924 | Time: 0.051s | ETA:  902.5s
[NODE-03] Block  58/500 | Index:  58 | Slot:  58 | Storage:  22.97 KB | Overwrites:   - | Hash Ops: 256463 | Time: 0.036s | ETA:  900.8s
[NODE-03] Block  59/500 | Index:  59 | Slot:  59 | Storage:  23.36 KB | Overwrites:   - | Hash Ops: 263880 | Time: 0.072s | ETA:  899.5s
[NODE-03] Block  60/500 | Index:  60 | Slot:  60 | Storage:  23.75 KB | Overwrites:   - | Hash Ops: 266113 | Time: 0.019s | ETA:  897.5s
[NODE-03] Block  61/500 | Index:  61 | Slot:  61 | Storage:  24.14 KB | Overwrites:   - | Hash Ops: 279696 | Time: 0.122s | ETA:  897.1s
[NODE-03] Block  62/500 | Index:  62 | Slot:  62 | Storage:  24.53 KB | Overwrites:   - | Hash Ops: 283010 | Time: 0.042s | ETA:  895.4s
[NODE-03] Block  63/500 | Index:  63 | Slot:  63 | Storage:  24.92 KB | Overwrites:   - | Hash Ops: 288939 | Time: 0.063s | ETA:  893.5s
[NODE-03] Block  64/500 | Index:  64 | Slot:  64 | Storage:  25.31 KB | Overwrites:   - | Hash Ops: 289717 | Time: 0.008s | ETA:  891.3s
[NODE-03] Block  65/500 | Index:  65 | Slot:  65 | Storage:  25.70 KB | Overwrites:   - | Hash Ops: 289972 | Time: 0.004s | ETA:  889.1s
[NODE-03] Block  66/500 | Index:  66 | Slot:  66 | Storage:  26.09 KB | Overwrites:   - | Hash Ops: 294059 | Time: 0.050s | ETA:  887.2s
[NODE-03] Block  67/500 | Index:  67 | Slot:  67 | Storage:  26.48 KB | Overwrites:   - | Hash Ops: 295186 | Time: 0.028s | ETA:  885.2s
[NODE-03] Block  68/500 | Index:  68 | Slot:  68 | Storage:  26.88 KB | Overwrites:   - | Hash Ops: 296973 | Time: 0.031s | ETA:  883.4s
[NODE-03] Block  69/500 | Index:  69 | Slot:  69 | Storage:  27.27 KB | Overwrites:   - | Hash Ops: 317494 | Time: 0.184s | ETA:  882.5s
[NODE-03] Block  70/500 | Index:  70 | Slot:  70 | Storage:  27.66 KB | Overwrites:   - | Hash Ops: 324414 | Time: 0.056s | ETA:  880.7s
[NODE-03] Block  71/500 | Index:  71 | Slot:  71 | Storage:  28.05 KB | Overwrites:   - | Hash Ops: 328177 | Time: 0.044s | ETA:  879.3s
[NODE-03] Block  72/500 | Index:  72 | Slot:  72 | Storage:  28.44 KB | Overwrites:   - | Hash Ops: 328800 | Time: 0.004s | ETA:  877.0s
[NODE-03] Block  73/500 | Index:  73 | Slot:  73 | Storage:  28.83 KB | Overwrites:   - | Hash Ops: 328854 | Time: 0.002s | ETA:  874.8s
[NODE-03] Block  74/500 | Index:  74 | Slot:  74 | Storage:  29.22 KB | Overwrites:   - | Hash Ops: 329535 | Time: 0.015s | ETA:  872.7s
[NODE-03] Block  75/500 | Index:  75 | Slot:  75 | Storage:  29.61 KB | Overwrites:   - | Hash Ops: 331147 | Time: 0.024s | ETA:  870.6s
[NODE-03] Block  76/500 | Index:  76 | Slot:  76 | Storage:  30.00 KB | Overwrites:   - | Hash Ops: 331158 | Time: 0.000s | ETA:  868.3s
[NODE-03] Block  77/500 | Index:  77 | Slot:  77 | Storage:  30.39 KB | Overwrites:   - | Hash Ops: 343922 | Time: 0.112s | ETA:  866.6s
[NODE-03] Block  78/500 | Index:  78 | Slot:  78 | Storage:  30.78 KB | Overwrites:   - | Hash Ops: 344714 | Time: 0.019s | ETA:  864.4s
[NODE-03] Block  79/500 | Index:  79 | Slot:  79 | Storage:  31.17 KB | Overwrites:   - | Hash Ops: 352090 | Time: 0.051s | ETA:  862.4s
[NODE-03] Block  80/500 | Index:  80 | Slot:  80 | Storage:  31.56 KB | Overwrites:   - | Hash Ops: 357287 | Time: 0.060s | ETA:  860.7s
[NODE-03] Block  81/500 | Index:  81 | Slot:  81 | Storage:  31.95 KB | Overwrites:   - | Hash Ops: 358270 | Time: 0.018s | ETA:  859.3s
[NODE-03] Block  82/500 | Index:  82 | Slot:  82 | Storage:  32.34 KB | Overwrites:   - | Hash Ops: 358680 | Time: 0.003s | ETA:  857.0s
[NODE-03] Block  83/500 | Index:  83 | Slot:  83 | Storage:  32.73 KB | Overwrites:   - | Hash Ops: 364464 | Time: 0.051s | ETA:  855.0s
[NODE-03] Block  84/500 | Index:  84 | Slot:  84 | Storage:  33.12 KB | Overwrites:   - | Hash Ops: 367137 | Time: 0.029s | ETA:  852.9s
[NODE-03] Block  85/500 | Index:  85 | Slot:  85 | Storage:  33.51 KB | Overwrites:   - | Hash Ops: 369315 | Time: 0.025s | ETA:  850.8s
[NODE-03] Block  86/500 | Index:  86 | Slot:  86 | Storage:  33.90 KB | Overwrites:   - | Hash Ops: 369522 | Time: 0.007s | ETA:  848.7s
[NODE-03] Block  87/500 | Index:  87 | Slot:  87 | Storage:  34.29 KB | Overwrites:   - | Hash Ops: 387650 | Time: 0.147s | ETA:  847.2s
[NODE-03] Block  88/500 | Index:  88 | Slot:  88 | Storage:  34.68 KB | Overwrites:   - | Hash Ops: 393070 | Time: 0.052s | ETA:  845.2s
[NODE-03] Block  89/500 | Index:  89 | Slot:  89 | Storage:  35.07 KB | Overwrites:   - | Hash Ops: 394811 | Time: 0.026s | ETA:  843.1s
[NODE-03] Block  90/500 | Index:  90 | Slot:  90 | Storage:  35.46 KB | Overwrites:   - | Hash Ops: 405591 | Time: 0.082s | ETA:  841.2s
[NODE-03] Block  91/500 | Index:  91 | Slot:  91 | Storage:  35.86 KB | Overwrites:   - | Hash Ops: 409577 | Time: 0.032s | ETA:  839.6s
[NODE-03] Block  92/500 | Index:  92 | Slot:  92 | Storage:  36.25 KB | Overwrites:   - | Hash Ops: 419052 | Time: 0.080s | ETA:  837.7s
[NODE-03] Block  93/500 | Index:  93 | Slot:  93 | Storage:  36.64 KB | Overwrites:   - | Hash Ops: 419812 | Time: 0.010s | ETA:  835.6s
[NODE-03] Block  94/500 | Index:  94 | Slot:  94 | Storage:  37.03 KB | Overwrites:   - | Hash Ops: 424047 | Time: 0.029s | ETA:  833.4s
[NODE-03] Block  95/500 | Index:  95 | Slot:  95 | Storage:  37.42 KB | Overwrites:   - | Hash Ops: 427431 | Time: 0.035s | ETA:  831.4s
[NODE-03] Block  96/500 | Index:  96 | Slot:  96 | Storage:  37.81 KB | Overwrites:   - | Hash Ops: 430622 | Time: 0.032s | ETA:  829.3s
[NODE-03] Block  97/500 | Index:  97 | Slot:  97 | Storage:  38.20 KB | Overwrites:   - | Hash Ops: 448106 | Time: 0.164s | ETA:  827.8s
[NODE-03] Block  98/500 | Index:  98 | Slot:  98 | Storage:  38.59 KB | Overwrites:   - | Hash Ops: 455458 | Time: 0.055s | ETA:  825.8s
[NODE-03] Block  99/500 | Index:  99 | Slot:  99 | Storage:  38.98 KB | Overwrites:   - | Hash Ops: 461568 | Time: 0.067s | ETA:  824.0s
[NODE-03] Block 100/500 | Index: 100 | Slot:   0 | Storage:  39.06 KB | Overwrites: Slot   0 | Hash Ops: 463410 | Time: 0.025s | ETA:  821.8s
[NODE-03] Block 101/500 | Index: 101 | Slot:   1 | Storage:  39.07 KB | Overwrites: Slot   1 | Hash Ops: 465477 | Time: 0.034s | ETA:  820.2s
[NODE-03] Block 102/500 | Index: 102 | Slot:   2 | Storage:  39.07 KB | Overwrites: Slot   2 | Hash Ops: 468182 | Time: 0.030s | ETA:  818.1s
[NODE-03] Block 103/500 | Index: 103 | Slot:   3 | Storage:  39.08 KB | Overwrites: Slot   3 | Hash Ops: 475190 | Time: 0.065s | ETA:  816.1s
[NODE-03] Block 104/500 | Index: 104 | Slot:   4 | Storage:  39.08 KB | Overwrites: Slot   4 | Hash Ops: 476785 | Time: 0.033s | ETA:  814.0s
[NODE-03] Block 105/500 | Index: 105 | Slot:   5 | Storage:  39.09 KB | Overwrites: Slot   5 | Hash Ops: 479243 | Time: 0.032s | ETA:  811.9s
[NODE-03] Block 106/500 | Index: 106 | Slot:   6 | Storage:  39.09 KB | Overwrites: Slot   6 | Hash Ops: 480434 | Time: 0.017s | ETA:  809.8s
[NODE-03] Block 107/500 | Index: 107 | Slot:   7 | Storage:  39.10 KB | Overwrites: Slot   7 | Hash Ops: 487850 | Time: 0.079s | ETA:  807.8s
[NODE-03] Block 108/500 | Index: 108 | Slot:   8 | Storage:  39.11 KB | Overwrites: Slot   8 | Hash Ops: 490176 | Time: 0.031s | ETA:  805.7s
[NODE-03] Block 109/500 | Index: 109 | Slot:   9 | Storage:  39.11 KB | Overwrites: Slot   9 | Hash Ops: 501220 | Time: 0.093s | ETA:  803.8s
[NODE-03] Block 110/500 | Index: 110 | Slot:  10 | Storage:  39.12 KB | Overwrites: Slot  10 | Hash Ops: 511279 | Time: 0.081s | ETA:  801.9s
[NODE-03] Block 111/500 | Index: 111 | Slot:  11 | Storage:  39.12 KB | Overwrites: Slot  11 | Hash Ops: 527715 | Time: 0.127s | ETA:  800.6s
[NODE-03] Block 112/500 | Index: 112 | Slot:  12 | Storage:  39.12 KB | Overwrites: Slot  12 | Hash Ops: 534360 | Time: 0.078s | ETA:  798.6s
[NODE-03] Block 113/500 | Index: 113 | Slot:  13 | Storage:  39.12 KB | Overwrites: Slot  13 | Hash Ops: 537709 | Time: 0.050s | ETA:  796.6s
[NODE-03] Block 114/500 | Index: 114 | Slot:  14 | Storage:  39.13 KB | Overwrites: Slot  14 | Hash Ops: 539560 | Time: 0.033s | ETA:  794.5s
[NODE-03] Block 115/500 | Index: 115 | Slot:  15 | Storage:  39.13 KB | Overwrites: Slot  15 | Hash Ops: 543258 | Time: 0.044s | ETA:  792.4s
[NODE-03] Block 116/500 | Index: 116 | Slot:  16 | Storage:  39.13 KB | Overwrites: Slot  16 | Hash Ops: 566428 | Time: 0.179s | ETA:  790.8s
[NODE-03] Block 117/500 | Index: 117 | Slot:  17 | Storage:  39.14 KB | Overwrites: Slot  17 | Hash Ops: 566458 | Time: 0.001s | ETA:  788.7s
[NODE-03] Block 118/500 | Index: 118 | Slot:  18 | Storage:  39.14 KB | Overwrites: Slot  18 | Hash Ops: 567702 | Time: 0.020s | ETA:  786.7s
[NODE-03] Block 119/500 | Index: 119 | Slot:  19 | Storage:  39.14 KB | Overwrites: Slot  19 | Hash Ops: 569056 | Time: 0.024s | ETA:  784.5s
[NODE-03] Block 120/500 | Index: 120 | Slot:  20 | Storage:  39.15 KB | Overwrites: Slot  20 | Hash Ops: 583937 | Time: 0.121s | ETA:  782.7s
[NODE-03] Block 121/500 | Index: 121 | Slot:  21 | Storage:  39.15 KB | Overwrites: Slot  21 | Hash Ops: 587459 | Time: 0.027s | ETA:  781.2s
[NODE-03] Block 122/500 | Index: 122 | Slot:  22 | Storage:  39.15 KB | Overwrites: Slot  22 | Hash Ops: 592755 | Time: 0.120s | ETA:  779.3s
[NODE-03] Block 123/500 | Index: 123 | Slot:  23 | Storage:  39.15 KB | Overwrites: Slot  23 | Hash Ops: 593491 | Time: 0.022s | ETA:  777.2s
[NODE-03] Block 124/500 | Index: 124 | Slot:  24 | Storage:  39.15 KB | Overwrites: Slot  24 | Hash Ops: 596542 | Time: 0.035s | ETA:  775.1s
[NODE-03] Block 125/500 | Index: 125 | Slot:  25 | Storage:  39.16 KB | Overwrites: Slot  25 | Hash Ops: 601371 | Time: 0.053s | ETA:  773.0s
[NODE-03] Block 126/500 | Index: 126 | Slot:  26 | Storage:  39.16 KB | Overwrites: Slot  26 | Hash Ops: 602290 | Time: 0.006s | ETA:  770.8s
[NODE-03] Block 127/500 | Index: 127 | Slot:  27 | Storage:  39.16 KB | Overwrites: Slot  27 | Hash Ops: 602964 | Time: 0.014s | ETA:  768.7s
[NODE-03] Block 128/500 | Index: 128 | Slot:  28 | Storage:  39.16 KB | Overwrites: Slot  28 | Hash Ops: 618240 | Time: 0.139s | ETA:  766.9s
[NODE-03] Block 129/500 | Index: 129 | Slot:  29 | Storage:  39.17 KB | Overwrites: Slot  29 | Hash Ops: 622977 | Time: 0.037s | ETA:  764.9s
[NODE-03] Block 130/500 | Index: 130 | Slot:  30 | Storage:  39.17 KB | Overwrites: Slot  30 | Hash Ops: 629709 | Time: 0.056s | ETA:  762.9s
[NODE-03] Block 131/500 | Index: 131 | Slot:  31 | Storage:  39.17 KB | Overwrites: Slot  31 | Hash Ops: 630584 | Time: 0.006s | ETA:  761.0s
[NODE-03] Block 132/500 | Index: 132 | Slot:  32 | Storage:  39.17 KB | Overwrites: Slot  32 | Hash Ops: 634589 | Time: 0.028s | ETA:  758.9s
[NODE-03] Block 133/500 | Index: 133 | Slot:  33 | Storage:  39.18 KB | Overwrites: Slot  33 | Hash Ops: 636475 | Time: 0.018s | ETA:  756.8s
[NODE-03] Block 134/500 | Index: 134 | Slot:  34 | Storage:  39.18 KB | Overwrites: Slot  34 | Hash Ops: 636747 | Time: 0.009s | ETA:  754.7s
[NODE-03] Block 135/500 | Index: 135 | Slot:  35 | Storage:  39.18 KB | Overwrites: Slot  35 | Hash Ops: 648118 | Time: 0.084s | ETA:  752.7s
[NODE-03] Block 136/500 | Index: 136 | Slot:  36 | Storage:  39.19 KB | Overwrites: Slot  36 | Hash Ops: 667391 | Time: 0.156s | ETA:  750.9s
[NODE-03] Block 137/500 | Index: 137 | Slot:  37 | Storage:  39.19 KB | Overwrites: Slot  37 | Hash Ops: 669555 | Time: 0.032s | ETA:  748.8s
[NODE-03] Block 138/500 | Index: 138 | Slot:  38 | Storage:  39.19 KB | Overwrites: Slot  38 | Hash Ops: 670320 | Time: 0.014s | ETA:  746.6s
[NODE-03] Block 139/500 | Index: 139 | Slot:  39 | Storage:  39.19 KB | Overwrites: Slot  39 | Hash Ops: 670421 | Time: 0.003s | ETA:  744.4s
[NODE-03] Block 140/500 | Index: 140 | Slot:  40 | Storage:  39.19 KB | Overwrites: Slot  40 | Hash Ops: 671530 | Time: 0.019s | ETA:  742.2s
[NODE-03] Block 141/500 | Index: 141 | Slot:  41 | Storage:  39.19 KB | Overwrites: Slot  41 | Hash Ops: 677256 | Time: 0.055s | ETA:  740.6s
[NODE-03] Block 142/500 | Index: 142 | Slot:  42 | Storage:  39.20 KB | Overwrites: Slot  42 | Hash Ops: 678738 | Time: 0.027s | ETA:  738.6s
[NODE-03] Block 143/500 | Index: 143 | Slot:  43 | Storage:  39.20 KB | Overwrites: Slot  43 | Hash Ops: 681728 | Time: 0.032s | ETA:  736.5s
[NODE-03] Block 144/500 | Index: 144 | Slot:  44 | Storage:  39.20 KB | Overwrites: Slot  44 | Hash Ops: 685300 | Time: 0.026s | ETA:  734.4s
[NODE-03] Block 145/500 | Index: 145 | Slot:  45 | Storage:  39.21 KB | Overwrites: Slot  45 | Hash Ops: 686332 | Time: 0.018s | ETA:  732.3s
[NODE-03] Block 146/500 | Index: 146 | Slot:  46 | Storage:  39.21 KB | Overwrites: Slot  46 | Hash Ops: 693154 | Time: 0.046s | ETA:  730.2s
[NODE-03] Block 147/500 | Index: 147 | Slot:  47 | Storage:  39.22 KB | Overwrites: Slot  47 | Hash Ops: 702650 | Time: 0.068s | ETA:  728.1s
[NODE-03] Block 148/500 | Index: 148 | Slot:  48 | Storage:  39.22 KB | Overwrites: Slot  48 | Hash Ops: 716949 | Time: 0.101s | ETA:  726.2s
[NODE-03] Block 149/500 | Index: 149 | Slot:  49 | Storage:  39.22 KB | Overwrites: Slot  49 | Hash Ops: 718859 | Time: 0.026s | ETA:  724.1s
[NODE-03] Block 150/500 | Index: 150 | Slot:  50 | Storage:  39.22 KB | Overwrites: Slot  50 | Hash Ops: 721535 | Time: 0.022s | ETA:  722.0s
[NODE-03] Block 151/500 | Index: 151 | Slot:  51 | Storage:  39.23 KB | Overwrites: Slot  51 | Hash Ops: 724640 | Time: 0.026s | ETA:  720.1s
[NODE-03] Block 152/500 | Index: 152 | Slot:  52 | Storage:  39.23 KB | Overwrites: Slot  52 | Hash Ops: 727226 | Time: 0.020s | ETA:  718.0s
[NODE-03] Block 153/500 | Index: 153 | Slot:  53 | Storage:  39.23 KB | Overwrites: Slot  53 | Hash Ops: 734698 | Time: 0.061s | ETA:  715.9s
[NODE-03] Block 154/500 | Index: 154 | Slot:  54 | Storage:  39.23 KB | Overwrites: Slot  54 | Hash Ops: 738897 | Time: 0.045s | ETA:  713.8s
[NODE-03] Block 155/500 | Index: 155 | Slot:  55 | Storage:  39.23 KB | Overwrites: Slot  55 | Hash Ops: 738969 | Time: 0.004s | ETA:  711.7s
[NODE-03] Block 156/500 | Index: 156 | Slot:  56 | Storage:  39.23 KB | Overwrites: Slot  56 | Hash Ops: 739565 | Time: 0.015s | ETA:  709.5s
[NODE-03] Block 157/500 | Index: 157 | Slot:  57 | Storage:  39.23 KB | Overwrites: Slot  57 | Hash Ops: 739587 | Time: 0.000s | ETA:  707.4s
[NODE-03] Block 158/500 | Index: 158 | Slot:  58 | Storage:  39.23 KB | Overwrites: Slot  58 | Hash Ops: 741328 | Time: 0.014s | ETA:  705.3s
[NODE-03] Block 159/500 | Index: 159 | Slot:  59 | Storage:  39.24 KB | Overwrites: Slot  59 | Hash Ops: 746202 | Time: 0.070s | ETA:  703.3s
[NODE-03] Block 160/500 | Index: 160 | Slot:  60 | Storage:  39.24 KB | Overwrites: Slot  60 | Hash Ops: 749876 | Time: 0.029s | ETA:  701.2s
[NODE-03] Block 161/500 | Index: 161 | Slot:  61 | Storage:  39.24 KB | Overwrites: Slot  61 | Hash Ops: 763425 | Time: 0.109s | ETA:  699.5s
[NODE-03] Block 162/500 | Index: 162 | Slot:  62 | Storage:  39.25 KB | Overwrites: Slot  62 | Hash Ops: 765148 | Time: 0.028s | ETA:  697.4s
[NODE-03] Block 163/500 | Index: 163 | Slot:  63 | Storage:  39.25 KB | Overwrites: Slot  63 | Hash Ops: 772506 | Time: 0.064s | ETA:  695.4s
[NODE-03] Block 164/500 | Index: 164 | Slot:  64 | Storage:  39.25 KB | Overwrites: Slot  64 | Hash Ops: 775714 | Time: 0.032s | ETA:  693.3s
[NODE-03] Block 165/500 | Index: 165 | Slot:  65 | Storage:  39.26 KB | Overwrites: Slot  65 | Hash Ops: 777303 | Time: 0.031s | ETA:  691.2s
[NODE-03] Block 166/500 | Index: 166 | Slot:  66 | Storage:  39.26 KB | Overwrites: Slot  66 | Hash Ops: 778085 | Time: 0.015s | ETA:  689.1s
[NODE-03] Block 167/500 | Index: 167 | Slot:  67 | Storage:  39.25 KB | Overwrites: Slot  67 | Hash Ops: 779030 | Time: 0.025s | ETA:  687.0s
[NODE-03] Block 168/500 | Index: 168 | Slot:  68 | Storage:  39.25 KB | Overwrites: Slot  68 | Hash Ops: 779317 | Time: 0.009s | ETA:  684.9s
[NODE-03] Block 169/500 | Index: 169 | Slot:  69 | Storage:  39.25 KB | Overwrites: Slot  69 | Hash Ops: 779956 | Time: 0.019s | ETA:  682.8s
[NODE-03] Block 170/500 | Index: 170 | Slot:  70 | Storage:  39.26 KB | Overwrites: Slot  70 | Hash Ops: 782298 | Time: 0.040s | ETA:  680.7s
[NODE-03] Block 171/500 | Index: 171 | Slot:  71 | Storage:  39.26 KB | Overwrites: Slot  71 | Hash Ops: 783368 | Time: 0.018s | ETA:  678.8s
[NODE-03] Block 172/500 | Index: 172 | Slot:  72 | Storage:  39.27 KB | Overwrites: Slot  72 | Hash Ops: 783588 | Time: 0.002s | ETA:  676.6s
[NODE-03] Block 173/500 | Index: 173 | Slot:  73 | Storage:  39.27 KB | Overwrites: Slot  73 | Hash Ops: 791446 | Time: 0.064s | ETA:  674.6s
[NODE-03] Block 174/500 | Index: 174 | Slot:  74 | Storage:  39.27 KB | Overwrites: Slot  74 | Hash Ops: 798062 | Time: 0.076s | ETA:  672.6s
[NODE-03] Block 175/500 | Index: 175 | Slot:  75 | Storage:  39.27 KB | Overwrites: Slot  75 | Hash Ops: 802448 | Time: 0.052s | ETA:  670.5s
[NODE-03] Block 176/500 | Index: 176 | Slot:  76 | Storage:  39.28 KB | Overwrites: Slot  76 | Hash Ops: 803889 | Time: 0.015s | ETA:  668.3s
[NODE-03] Block 177/500 | Index: 177 | Slot:  77 | Storage:  39.28 KB | Overwrites: Slot  77 | Hash Ops: 805754 | Time: 0.024s | ETA:  666.3s
[NODE-03] Block 178/500 | Index: 178 | Slot:  78 | Storage:  39.28 KB | Overwrites: Slot  78 | Hash Ops: 806477 | Time: 0.018s | ETA:  664.2s
[NODE-03] Block 179/500 | Index: 179 | Slot:  79 | Storage:  39.29 KB | Overwrites: Slot  79 | Hash Ops: 821072 | Time: 0.126s | ETA:  662.3s
[NODE-03] Block 180/500 | Index: 180 | Slot:  80 | Storage:  39.29 KB | Overwrites: Slot  80 | Hash Ops: 824077 | Time: 0.030s | ETA:  660.2s
[NODE-03] Block 181/500 | Index: 181 | Slot:  81 | Storage:  39.29 KB | Overwrites: Slot  81 | Hash Ops: 833774 | Time: 0.084s | ETA:  658.4s
[NODE-03] Block 182/500 | Index: 182 | Slot:  82 | Storage:  39.30 KB | Overwrites: Slot  82 | Hash Ops: 833887 | Time: 0.001s | ETA:  656.3s
[NODE-03] Block 183/500 | Index: 183 | Slot:  83 | Storage:  39.30 KB | Overwrites: Slot  83 | Hash Ops: 838321 | Time: 0.043s | ETA:  654.2s
[NODE-03] Block 184/500 | Index: 184 | Slot:  84 | Storage:  39.30 KB | Overwrites: Slot  84 | Hash Ops: 846936 | Time: 0.059s | ETA:  652.2s
[NODE-03] Block 185/500 | Index: 185 | Slot:  85 | Storage:  39.30 KB | Overwrites: Slot  85 | Hash Ops: 852249 | Time: 0.064s | ETA:  650.1s
[NODE-03] Block 186/500 | Index: 186 | Slot:  86 | Storage:  39.31 KB | Overwrites: Slot  86 | Hash Ops: 853978 | Time: 0.023s | ETA:  648.0s
[NODE-03] Block 187/500 | Index: 187 | Slot:  87 | Storage:  39.31 KB | Overwrites: Slot  87 | Hash Ops: 854386 | Time: 0.006s | ETA:  645.9s
[NODE-03] Block 188/500 | Index: 188 | Slot:  88 | Storage:  39.31 KB | Overwrites: Slot  88 | Hash Ops: 860900 | Time: 0.045s | ETA:  643.8s
[NODE-03] Block 189/500 | Index: 189 | Slot:  89 | Storage:  39.31 KB | Overwrites: Slot  89 | Hash Ops: 866009 | Time: 0.068s | ETA:  641.8s
[NODE-03] Block 190/500 | Index: 190 | Slot:  90 | Storage:  39.32 KB | Overwrites: Slot  90 | Hash Ops: 867114 | Time: 0.023s | ETA:  639.7s
[NODE-03] Block 191/500 | Index: 191 | Slot:  91 | Storage:  39.32 KB | Overwrites: Slot  91 | Hash Ops: 869575 | Time: 0.033s | ETA:  637.7s
[NODE-03] Block 192/500 | Index: 192 | Slot:  92 | Storage:  39.32 KB | Overwrites: Slot  92 | Hash Ops: 871214 | Time: 0.025s | ETA:  635.6s
[NODE-03] Block 193/500 | Index: 193 | Slot:  93 | Storage:  39.33 KB | Overwrites: Slot  93 | Hash Ops: 873938 | Time: 0.024s | ETA:  633.5s
[NODE-03] Block 194/500 | Index: 194 | Slot:  94 | Storage:  39.33 KB | Overwrites: Slot  94 | Hash Ops: 879998 | Time: 0.048s | ETA:  631.6s
[NODE-03] Block 195/500 | Index: 195 | Slot:  95 | Storage:  39.33 KB | Overwrites: Slot  95 | Hash Ops: 885384 | Time: 0.049s | ETA:  629.5s
[NODE-03] Block 196/500 | Index: 196 | Slot:  96 | Storage:  39.34 KB | Overwrites: Slot  96 | Hash Ops: 886461 | Time: 0.021s | ETA:  627.4s
[NODE-03] Block 197/500 | Index: 197 | Slot:  97 | Storage:  39.34 KB | Overwrites: Slot  97 | Hash Ops: 889160 | Time: 0.033s | ETA:  625.3s
[NODE-03] Block 198/500 | Index: 198 | Slot:  98 | Storage:  39.34 KB | Overwrites: Slot  98 | Hash Ops: 890347 | Time: 0.021s | ETA:  623.2s
[NODE-03] Block 199/500 | Index: 199 | Slot:  99 | Storage:  39.34 KB | Overwrites: Slot  99 | Hash Ops: 892077 | Time: 0.026s | ETA:  621.1s
[NODE-03] Block 200/500 | Index: 200 | Slot:   0 | Storage:  39.34 KB | Overwrites: Slot   0 | Hash Ops: 892620 | Time: 0.015s | ETA:  619.0s
[NODE-03] Block 201/500 | Index: 201 | Slot:   1 | Storage:  39.34 KB | Overwrites: Slot   1 | Hash Ops: 893433 | Time: 0.019s | ETA:  617.1s
[NODE-03] Block 202/500 | Index: 202 | Slot:   2 | Storage:  39.34 KB | Overwrites: Slot   2 | Hash Ops: 897398 | Time: 0.028s | ETA:  615.0s
[NODE-03] Block 203/500 | Index: 203 | Slot:   3 | Storage:  39.34 KB | Overwrites: Slot   3 | Hash Ops: 898000 | Time: 0.007s | ETA:  612.9s
[NODE-03] Block 204/500 | Index: 204 | Slot:   4 | Storage:  39.34 KB | Overwrites: Slot   4 | Hash Ops: 899757 | Time: 0.032s | ETA:  610.8s
[NODE-03] Block 205/500 | Index: 205 | Slot:   5 | Storage:  39.34 KB | Overwrites: Slot   5 | Hash Ops: 900095 | Time: 0.005s | ETA:  608.7s
[NODE-03] Block 206/500 | Index: 206 | Slot:   6 | Storage:  39.34 KB | Overwrites: Slot   6 | Hash Ops: 902272 | Time: 0.015s | ETA:  606.6s
[NODE-03] Block 207/500 | Index: 207 | Slot:   7 | Storage:  39.34 KB | Overwrites: Slot   7 | Hash Ops: 904025 | Time: 0.017s | ETA:  604.5s
[NODE-03] Block 208/500 | Index: 208 | Slot:   8 | Storage:  39.34 KB | Overwrites: Slot   8 | Hash Ops: 905592 | Time: 0.012s | ETA:  602.4s
[NODE-03] Block 209/500 | Index: 209 | Slot:   9 | Storage:  39.34 KB | Overwrites: Slot   9 | Hash Ops: 910860 | Time: 0.053s | ETA:  600.4s
[NODE-03] Block 210/500 | Index: 210 | Slot:  10 | Storage:  39.34 KB | Overwrites: Slot  10 | Hash Ops: 918001 | Time: 0.066s | ETA:  598.3s
[NODE-03] Block 211/500 | Index: 211 | Slot:  11 | Storage:  39.33 KB | Overwrites: Slot  11 | Hash Ops: 921604 | Time: 0.040s | ETA:  596.4s
[NODE-03] Block 212/500 | Index: 212 | Slot:  12 | Storage:  39.34 KB | Overwrites: Slot  12 | Hash Ops: 923389 | Time: 0.016s | ETA:  594.3s
[NODE-03] Block 213/500 | Index: 213 | Slot:  13 | Storage:  39.34 KB | Overwrites: Slot  13 | Hash Ops: 933164 | Time: 0.084s | ETA:  592.3s
[NODE-03] Block 214/500 | Index: 214 | Slot:  14 | Storage:  39.34 KB | Overwrites: Slot  14 | Hash Ops: 937360 | Time: 0.065s | ETA:  590.3s
[NODE-03] Block 215/500 | Index: 215 | Slot:  15 | Storage:  39.34 KB | Overwrites: Slot  15 | Hash Ops: 937696 | Time: 0.013s | ETA:  588.2s
[NODE-03] Block 216/500 | Index: 216 | Slot:  16 | Storage:  39.34 KB | Overwrites: Slot  16 | Hash Ops: 945008 | Time: 0.068s | ETA:  586.1s
[NODE-03] Block 217/500 | Index: 217 | Slot:  17 | Storage:  39.34 KB | Overwrites: Slot  17 | Hash Ops: 945399 | Time: 0.006s | ETA:  584.0s
[NODE-03] Block 218/500 | Index: 218 | Slot:  18 | Storage:  39.34 KB | Overwrites: Slot  18 | Hash Ops: 947297 | Time: 0.032s | ETA:  581.9s
[NODE-03] Block 219/500 | Index: 219 | Slot:  19 | Storage:  39.34 KB | Overwrites: Slot  19 | Hash Ops: 953997 | Time: 0.075s | ETA:  579.9s
[NODE-03] Block 220/500 | Index: 220 | Slot:  20 | Storage:  39.33 KB | Overwrites: Slot  20 | Hash Ops: 960789 | Time: 0.064s | ETA:  577.8s
[NODE-03] Block 221/500 | Index: 221 | Slot:  21 | Storage:  39.34 KB | Overwrites: Slot  21 | Hash Ops: 962505 | Time: 0.012s | ETA:  575.8s
[NODE-03] Block 222/500 | Index: 222 | Slot:  22 | Storage:  39.34 KB | Overwrites: Slot  22 | Hash Ops: 970031 | Time: 0.065s | ETA:  573.8s
[NODE-03] Block 223/500 | Index: 223 | Slot:  23 | Storage:  39.34 KB | Overwrites: Slot  23 | Hash Ops: 974748 | Time: 0.041s | ETA:  571.7s
[NODE-03] Block 224/500 | Index: 224 | Slot:  24 | Storage:  39.34 KB | Overwrites: Slot  24 | Hash Ops: 976077 | Time: 0.009s | ETA:  569.6s
[NODE-03] Block 225/500 | Index: 225 | Slot:  25 | Storage:  39.34 KB | Overwrites: Slot  25 | Hash Ops: 976936 | Time: 0.017s | ETA:  567.5s
[NODE-03] Block 226/500 | Index: 226 | Slot:  26 | Storage:  39.34 KB | Overwrites: Slot  26 | Hash Ops: 977483 | Time: 0.019s | ETA:  565.4s
[NODE-03] Block 227/500 | Index: 227 | Slot:  27 | Storage:  39.34 KB | Overwrites: Slot  27 | Hash Ops: 980652 | Time: 0.039s | ETA:  563.4s
[NODE-03] Block 228/500 | Index: 228 | Slot:  28 | Storage:  39.34 KB | Overwrites: Slot  28 | Hash Ops: 987422 | Time: 0.092s | ETA:  561.4s
[NODE-03] Block 229/500 | Index: 229 | Slot:  29 | Storage:  39.34 KB | Overwrites: Slot  29 | Hash Ops: 992111 | Time: 0.077s | ETA:  559.3s
[NODE-03] Block 230/500 | Index: 230 | Slot:  30 | Storage:  39.34 KB | Overwrites: Slot  30 | Hash Ops: 999331 | Time: 0.051s | ETA:  557.2s
[NODE-03] Block 231/500 | Index: 231 | Slot:  31 | Storage:  39.34 KB | Overwrites: Slot  31 | Hash Ops: 1012016 | Time: 0.115s | ETA:  555.5s
[NODE-03] Block 232/500 | Index: 232 | Slot:  32 | Storage:  39.35 KB | Overwrites: Slot  32 | Hash Ops: 1019466 | Time: 0.069s | ETA:  553.4s
[NODE-03] Block 233/500 | Index: 233 | Slot:  33 | Storage:  39.35 KB | Overwrites: Slot  33 | Hash Ops: 1019942 | Time: 0.015s | ETA:  551.3s
[NODE-03] Block 234/500 | Index: 234 | Slot:  34 | Storage:  39.35 KB | Overwrites: Slot  34 | Hash Ops: 1026345 | Time: 0.067s | ETA:  549.3s
[NODE-03] Block 235/500 | Index: 235 | Slot:  35 | Storage:  39.35 KB | Overwrites: Slot  35 | Hash Ops: 1028622 | Time: 0.043s | ETA:  547.2s
[NODE-03] Block 236/500 | Index: 236 | Slot:  36 | Storage:  39.35 KB | Overwrites: Slot  36 | Hash Ops: 1030668 | Time: 0.033s | ETA:  545.2s
[NODE-03] Block 237/500 | Index: 237 | Slot:  37 | Storage:  39.35 KB | Overwrites: Slot  37 | Hash Ops: 1039432 | Time: 0.076s | ETA:  543.1s
[NODE-03] Block 238/500 | Index: 238 | Slot:  38 | Storage:  39.35 KB | Overwrites: Slot  38 | Hash Ops: 1047881 | Time: 0.073s | ETA:  541.1s
[NODE-03] Block 239/500 | Index: 239 | Slot:  39 | Storage:  39.35 KB | Overwrites: Slot  39 | Hash Ops: 1050612 | Time: 0.031s | ETA:  539.0s
[NODE-03] Block 240/500 | Index: 240 | Slot:  40 | Storage:  39.35 KB | Overwrites: Slot  40 | Hash Ops: 1050651 | Time: 0.000s | ETA:  536.8s
[NODE-03] Block 241/500 | Index: 241 | Slot:  41 | Storage:  39.35 KB | Overwrites: Slot  41 | Hash Ops: 1052685 | Time: 0.018s | ETA:  534.9s
[NODE-03] Block 242/500 | Index: 242 | Slot:  42 | Storage:  39.35 KB | Overwrites: Slot  42 | Hash Ops: 1055101 | Time: 0.024s | ETA:  532.8s
[NODE-03] Block 243/500 | Index: 243 | Slot:  43 | Storage:  39.35 KB | Overwrites: Slot  43 | Hash Ops: 1060227 | Time: 0.042s | ETA:  530.7s
[NODE-03] Block 244/500 | Index: 244 | Slot:  44 | Storage:  39.35 KB | Overwrites: Slot  44 | Hash Ops: 1072902 | Time: 0.101s | ETA:  528.7s
[NODE-03] Block 245/500 | Index: 245 | Slot:  45 | Storage:  39.35 KB | Overwrites: Slot  45 | Hash Ops: 1074764 | Time: 0.024s | ETA:  526.6s
[NODE-03] Block 246/500 | Index: 246 | Slot:  46 | Storage:  39.35 KB | Overwrites: Slot  46 | Hash Ops: 1077400 | Time: 0.030s | ETA:  524.5s
[NODE-03] Block 247/500 | Index: 247 | Slot:  47 | Storage:  39.35 KB | Overwrites: Slot  47 | Hash Ops: 1079611 | Time: 0.019s | ETA:  522.4s
[NODE-03] Block 248/500 | Index: 248 | Slot:  48 | Storage:  39.35 KB | Overwrites: Slot  48 | Hash Ops: 1082315 | Time: 0.019s | ETA:  520.3s
[NODE-03] Block 249/500 | Index: 249 | Slot:  49 | Storage:  39.35 KB | Overwrites: Slot  49 | Hash Ops: 1084016 | Time: 0.044s | ETA:  518.3s
[NODE-03] Block 250/500 | Index: 250 | Slot:  50 | Storage:  39.34 KB | Overwrites: Slot  50 | Hash Ops: 1086508 | Time: 0.024s | ETA:  516.2s
[NODE-03] Block 251/500 | Index: 251 | Slot:  51 | Storage:  39.34 KB | Overwrites: Slot  51 | Hash Ops: 1088186 | Time: 0.024s | ETA:  514.2s
[NODE-03] Block 252/500 | Index: 252 | Slot:  52 | Storage:  39.34 KB | Overwrites: Slot  52 | Hash Ops: 1092758 | Time: 0.043s | ETA:  512.1s
[NODE-03] Block 253/500 | Index: 253 | Slot:  53 | Storage:  39.34 KB | Overwrites: Slot  53 | Hash Ops: 1098046 | Time: 0.048s | ETA:  510.0s
[NODE-03] Block 254/500 | Index: 254 | Slot:  54 | Storage:  39.35 KB | Overwrites: Slot  54 | Hash Ops: 1100100 | Time: 0.018s | ETA:  508.0s
[NODE-03] Block 255/500 | Index: 255 | Slot:  55 | Storage:  39.35 KB | Overwrites: Slot  55 | Hash Ops: 1100194 | Time: 0.002s | ETA:  505.8s
[NODE-03] Block 256/500 | Index: 256 | Slot:  56 | Storage:  39.35 KB | Overwrites: Slot  56 | Hash Ops: 1100663 | Time: 0.011s | ETA:  503.8s
[NODE-03] Block 257/500 | Index: 257 | Slot:  57 | Storage:  39.35 KB | Overwrites: Slot  57 | Hash Ops: 1105241 | Time: 0.032s | ETA:  501.7s
[NODE-03] Block 258/500 | Index: 258 | Slot:  58 | Storage:  39.35 KB | Overwrites: Slot  58 | Hash Ops: 1107086 | Time: 0.026s | ETA:  499.6s
[NODE-03] Block 259/500 | Index: 259 | Slot:  59 | Storage:  39.35 KB | Overwrites: Slot  59 | Hash Ops: 1111792 | Time: 0.036s | ETA:  497.5s
[NODE-03] Block 260/500 | Index: 260 | Slot:  60 | Storage:  39.35 KB | Overwrites: Slot  60 | Hash Ops: 1114131 | Time: 0.034s | ETA:  495.4s
[NODE-03] Block 261/500 | Index: 261 | Slot:  61 | Storage:  39.35 KB | Overwrites: Slot  61 | Hash Ops: 1116932 | Time: 0.030s | ETA:  493.5s
[NODE-03] Block 262/500 | Index: 262 | Slot:  62 | Storage:  39.34 KB | Overwrites: Slot  62 | Hash Ops: 1117165 | Time: 0.010s | ETA:  491.4s
[NODE-03] Block 263/500 | Index: 263 | Slot:  63 | Storage:  39.34 KB | Overwrites: Slot  63 | Hash Ops: 1119598 | Time: 0.018s | ETA:  489.3s
[NODE-03] Block 264/500 | Index: 264 | Slot:  64 | Storage:  39.35 KB | Overwrites: Slot  64 | Hash Ops: 1132534 | Time: 0.093s | ETA:  487.3s
[NODE-03] Block 265/500 | Index: 265 | Slot:  65 | Storage:  39.35 KB | Overwrites: Slot  65 | Hash Ops: 1133618 | Time: 0.025s | ETA:  485.2s
[NODE-03] Block 266/500 | Index: 266 | Slot:  66 | Storage:  39.35 KB | Overwrites: Slot  66 | Hash Ops: 1139739 | Time: 0.058s | ETA:  483.1s
[NODE-03] Block 267/500 | Index: 267 | Slot:  67 | Storage:  39.35 KB | Overwrites: Slot  67 | Hash Ops: 1141769 | Time: 0.024s | ETA:  481.0s
[NODE-03] Block 268/500 | Index: 268 | Slot:  68 | Storage:  39.35 KB | Overwrites: Slot  68 | Hash Ops: 1148242 | Time: 0.085s | ETA:  479.0s
[NODE-03] Block 269/500 | Index: 269 | Slot:  69 | Storage:  39.35 KB | Overwrites: Slot  69 | Hash Ops: 1151490 | Time: 0.045s | ETA:  476.9s
[NODE-03] Block 270/500 | Index: 270 | Slot:  70 | Storage:  39.35 KB | Overwrites: Slot  70 | Hash Ops: 1157207 | Time: 0.073s | ETA:  474.9s
[NODE-03] Block 271/500 | Index: 271 | Slot:  71 | Storage:  39.35 KB | Overwrites: Slot  71 | Hash Ops: 1159999 | Time: 0.020s | ETA:  472.9s
[NODE-03] Block 272/500 | Index: 272 | Slot:  72 | Storage:  39.35 KB | Overwrites: Slot  72 | Hash Ops: 1179331 | Time: 0.149s | ETA:  470.9s
[NODE-03] Block 273/500 | Index: 273 | Slot:  73 | Storage:  39.35 KB | Overwrites: Slot  73 | Hash Ops: 1184417 | Time: 0.066s | ETA:  468.9s
[NODE-03] Block 274/500 | Index: 274 | Slot:  74 | Storage:  39.35 KB | Overwrites: Slot  74 | Hash Ops: 1187107 | Time: 0.034s | ETA:  466.8s
[NODE-03] Block 275/500 | Index: 275 | Slot:  75 | Storage:  39.35 KB | Overwrites: Slot  75 | Hash Ops: 1189181 | Time: 0.025s | ETA:  464.7s
[NODE-03] Block 276/500 | Index: 276 | Slot:  76 | Storage:  39.35 KB | Overwrites: Slot  76 | Hash Ops: 1195036 | Time: 0.047s | ETA:  462.6s
[NODE-03] Block 277/500 | Index: 277 | Slot:  77 | Storage:  39.35 KB | Overwrites: Slot  77 | Hash Ops: 1205166 | Time: 0.100s | ETA:  460.6s
[NODE-03] Block 278/500 | Index: 278 | Slot:  78 | Storage:  39.36 KB | Overwrites: Slot  78 | Hash Ops: 1206489 | Time: 0.020s | ETA:  458.5s
[NODE-03] Block 279/500 | Index: 279 | Slot:  79 | Storage:  39.35 KB | Overwrites: Slot  79 | Hash Ops: 1208953 | Time: 0.021s | ETA:  456.4s
[NODE-03] Block 280/500 | Index: 280 | Slot:  80 | Storage:  39.36 KB | Overwrites: Slot  80 | Hash Ops: 1210561 | Time: 0.022s | ETA:  454.4s
[NODE-03] Block 281/500 | Index: 281 | Slot:  81 | Storage:  39.36 KB | Overwrites: Slot  81 | Hash Ops: 1211723 | Time: 0.024s | ETA:  452.4s
[NODE-03] Block 282/500 | Index: 282 | Slot:  82 | Storage:  39.36 KB | Overwrites: Slot  82 | Hash Ops: 1218990 | Time: 0.067s | ETA:  450.4s
[NODE-03] Block 283/500 | Index: 283 | Slot:  83 | Storage:  39.36 KB | Overwrites: Slot  83 | Hash Ops: 1223678 | Time: 0.033s | ETA:  448.3s
[NODE-03] Block 284/500 | Index: 284 | Slot:  84 | Storage:  39.36 KB | Overwrites: Slot  84 | Hash Ops: 1231562 | Time: 0.067s | ETA:  446.2s
[NODE-03] Block 285/500 | Index: 285 | Slot:  85 | Storage:  39.36 KB | Overwrites: Slot  85 | Hash Ops: 1232161 | Time: 0.014s | ETA:  444.1s
[NODE-03] Block 286/500 | Index: 286 | Slot:  86 | Storage:  39.36 KB | Overwrites: Slot  86 | Hash Ops: 1245110 | Time: 0.119s | ETA:  442.1s
[NODE-03] Block 287/500 | Index: 287 | Slot:  87 | Storage:  39.36 KB | Overwrites: Slot  87 | Hash Ops: 1247197 | Time: 0.026s | ETA:  440.0s
[NODE-03] Block 288/500 | Index: 288 | Slot:  88 | Storage:  39.36 KB | Overwrites: Slot  88 | Hash Ops: 1250526 | Time: 0.023s | ETA:  438.0s
[NODE-03] Block 289/500 | Index: 289 | Slot:  89 | Storage:  39.36 KB | Overwrites: Slot  89 | Hash Ops: 1251897 | Time: 0.009s | ETA:  435.9s
[NODE-03] Block 290/500 | Index: 290 | Slot:  90 | Storage:  39.37 KB | Overwrites: Slot  90 | Hash Ops: 1255333 | Time: 0.042s | ETA:  433.9s
[NODE-03] Block 291/500 | Index: 291 | Slot:  91 | Storage:  39.36 KB | Overwrites: Slot  91 | Hash Ops: 1264988 | Time: 0.083s | ETA:  431.9s
[NODE-03] Block 292/500 | Index: 292 | Slot:  92 | Storage:  39.36 KB | Overwrites: Slot  92 | Hash Ops: 1266063 | Time: 0.033s | ETA:  429.8s
[NODE-03] Block 293/500 | Index: 293 | Slot:  93 | Storage:  39.36 KB | Overwrites: Slot  93 | Hash Ops: 1269770 | Time: 0.040s | ETA:  427.8s
[NODE-03] Block 294/500 | Index: 294 | Slot:  94 | Storage:  39.36 KB | Overwrites: Slot  94 | Hash Ops: 1278177 | Time: 0.069s | ETA:  425.7s
[NODE-03] Block 295/500 | Index: 295 | Slot:  95 | Storage:  39.37 KB | Overwrites: Slot  95 | Hash Ops: 1293185 | Time: 0.136s | ETA:  423.7s
[NODE-03] Block 296/500 | Index: 296 | Slot:  96 | Storage:  39.37 KB | Overwrites: Slot  96 | Hash Ops: 1296268 | Time: 0.021s | ETA:  421.6s
[NODE-03] Block 297/500 | Index: 297 | Slot:  97 | Storage:  39.36 KB | Overwrites: Slot  97 | Hash Ops: 1296348 | Time: 0.003s | ETA:  419.5s
[NODE-03] Block 298/500 | Index: 298 | Slot:  98 | Storage:  39.36 KB | Overwrites: Slot  98 | Hash Ops: 1296665 | Time: 0.011s | ETA:  417.4s
[NODE-03] Block 299/500 | Index: 299 | Slot:  99 | Storage:  39.36 KB | Overwrites: Slot  99 | Hash Ops: 1296957 | Time: 0.002s | ETA:  415.3s
[NODE-03] Block 300/500 | Index: 300 | Slot:   0 | Storage:  39.36 KB | Overwrites: Slot   0 | Hash Ops: 1298586 | Time: 0.015s | ETA:  413.2s
[NODE-03] Block 301/500 | Index: 301 | Slot:   1 | Storage:  39.36 KB | Overwrites: Slot   1 | Hash Ops: 1298869 | Time: 0.008s | ETA:  411.3s
[NODE-03] Block 302/500 | Index: 302 | Slot:   2 | Storage:  39.36 KB | Overwrites: Slot   2 | Hash Ops: 1304963 | Time: 0.052s | ETA:  409.2s
[NODE-03] Block 303/500 | Index: 303 | Slot:   3 | Storage:  39.36 KB | Overwrites: Slot   3 | Hash Ops: 1309415 | Time: 0.045s | ETA:  407.1s
[NODE-03] Block 304/500 | Index: 304 | Slot:   4 | Storage:  39.36 KB | Overwrites: Slot   4 | Hash Ops: 1310390 | Time: 0.019s | ETA:  405.2s
[NODE-03] Block 305/500 | Index: 305 | Slot:   5 | Storage:  39.36 KB | Overwrites: Slot   5 | Hash Ops: 1317522 | Time: 0.067s | ETA:  403.2s
[NODE-03] Block 306/500 | Index: 306 | Slot:   6 | Storage:  39.36 KB | Overwrites: Slot   6 | Hash Ops: 1321205 | Time: 0.037s | ETA:  401.1s
[NODE-03] Block 307/500 | Index: 307 | Slot:   7 | Storage:  39.36 KB | Overwrites: Slot   7 | Hash Ops: 1325760 | Time: 0.052s | ETA:  399.0s
[NODE-03] Block 308/500 | Index: 308 | Slot:   8 | Storage:  39.36 KB | Overwrites: Slot   8 | Hash Ops: 1325989 | Time: 0.007s | ETA:  396.9s
[NODE-03] Block 309/500 | Index: 309 | Slot:   9 | Storage:  39.36 KB | Overwrites: Slot   9 | Hash Ops: 1328132 | Time: 0.032s | ETA:  394.8s
[NODE-03] Block 310/500 | Index: 310 | Slot:  10 | Storage:  39.36 KB | Overwrites: Slot  10 | Hash Ops: 1332808 | Time: 0.049s | ETA:  392.8s
[NODE-03] Block 311/500 | Index: 311 | Slot:  11 | Storage:  39.36 KB | Overwrites: Slot  11 | Hash Ops: 1334158 | Time: 0.016s | ETA:  390.8s
[NODE-03] Block 312/500 | Index: 312 | Slot:  12 | Storage:  39.36 KB | Overwrites: Slot  12 | Hash Ops: 1334989 | Time: 0.017s | ETA:  388.7s
[NODE-03] Block 313/500 | Index: 313 | Slot:  13 | Storage:  39.36 KB | Overwrites: Slot  13 | Hash Ops: 1348462 | Time: 0.116s | ETA:  386.7s
[NODE-03] Block 314/500 | Index: 314 | Slot:  14 | Storage:  39.36 KB | Overwrites: Slot  14 | Hash Ops: 1349605 | Time: 0.008s | ETA:  384.6s
[NODE-03] Block 315/500 | Index: 315 | Slot:  15 | Storage:  39.36 KB | Overwrites: Slot  15 | Hash Ops: 1351305 | Time: 0.013s | ETA:  382.5s
[NODE-03] Block 316/500 | Index: 316 | Slot:  16 | Storage:  39.36 KB | Overwrites: Slot  16 | Hash Ops: 1358786 | Time: 0.063s | ETA:  380.5s
[NODE-03] Block 317/500 | Index: 317 | Slot:  17 | Storage:  39.36 KB | Overwrites: Slot  17 | Hash Ops: 1360473 | Time: 0.035s | ETA:  378.4s
[NODE-03] Block 318/500 | Index: 318 | Slot:  18 | Storage:  39.36 KB | Overwrites: Slot  18 | Hash Ops: 1360881 | Time: 0.006s | ETA:  376.3s
[NODE-03] Block 319/500 | Index: 319 | Slot:  19 | Storage:  39.36 KB | Overwrites: Slot  19 | Hash Ops: 1361176 | Time: 0.005s | ETA:  374.2s
[NODE-03] Block 320/500 | Index: 320 | Slot:  20 | Storage:  39.36 KB | Overwrites: Slot  20 | Hash Ops: 1363151 | Time: 0.015s | ETA:  372.1s
[NODE-03] Block 321/500 | Index: 321 | Slot:  21 | Storage:  39.36 KB | Overwrites: Slot  21 | Hash Ops: 1366266 | Time: 0.040s | ETA:  370.1s
[NODE-03] Block 322/500 | Index: 322 | Slot:  22 | Storage:  39.36 KB | Overwrites: Slot  22 | Hash Ops: 1371126 | Time: 0.034s | ETA:  368.0s
[NODE-03] Block 323/500 | Index: 323 | Slot:  23 | Storage:  39.36 KB | Overwrites: Slot  23 | Hash Ops: 1378979 | Time: 0.070s | ETA:  366.0s
[NODE-03] Block 324/500 | Index: 324 | Slot:  24 | Storage:  39.36 KB | Overwrites: Slot  24 | Hash Ops: 1383185 | Time: 0.030s | ETA:  363.9s
[NODE-03] Block 325/500 | Index: 325 | Slot:  25 | Storage:  39.36 KB | Overwrites: Slot  25 | Hash Ops: 1388564 | Time: 0.042s | ETA:  361.8s
[NODE-03] Block 326/500 | Index: 326 | Slot:  26 | Storage:  39.36 KB | Overwrites: Slot  26 | Hash Ops: 1390310 | Time: 0.023s | ETA:  359.7s
[NODE-03] Block 327/500 | Index: 327 | Slot:  27 | Storage:  39.36 KB | Overwrites: Slot  27 | Hash Ops: 1395828 | Time: 0.048s | ETA:  357.7s
[NODE-03] Block 328/500 | Index: 328 | Slot:  28 | Storage:  39.36 KB | Overwrites: Slot  28 | Hash Ops: 1396554 | Time: 0.024s | ETA:  355.6s
[NODE-03] Block 329/500 | Index: 329 | Slot:  29 | Storage:  39.36 KB | Overwrites: Slot  29 | Hash Ops: 1405328 | Time: 0.072s | ETA:  353.5s
[NODE-03] Block 330/500 | Index: 330 | Slot:  30 | Storage:  39.35 KB | Overwrites: Slot  30 | Hash Ops: 1405364 | Time: 0.001s | ETA:  351.4s
[NODE-03] Block 331/500 | Index: 331 | Slot:  31 | Storage:  39.35 KB | Overwrites: Slot  31 | Hash Ops: 1417999 | Time: 0.134s | ETA:  349.5s
[NODE-03] Block 332/500 | Index: 332 | Slot:  32 | Storage:  39.35 KB | Overwrites: Slot  32 | Hash Ops: 1418152 | Time: 0.001s | ETA:  347.4s
[NODE-03] Block 333/500 | Index: 333 | Slot:  33 | Storage:  39.35 KB | Overwrites: Slot  33 | Hash Ops: 1419595 | Time: 0.010s | ETA:  345.3s
[NODE-03] Block 334/500 | Index: 334 | Slot:  34 | Storage:  39.35 KB | Overwrites: Slot  34 | Hash Ops: 1422751 | Time: 0.027s | ETA:  343.2s
[NODE-03] Block 335/500 | Index: 335 | Slot:  35 | Storage:  39.35 KB | Overwrites: Slot  35 | Hash Ops: 1422815 | Time: 0.001s | ETA:  341.1s
[NODE-03] Block 336/500 | Index: 336 | Slot:  36 | Storage:  39.34 KB | Overwrites: Slot  36 | Hash Ops: 1427136 | Time: 0.032s | ETA:  339.1s
[NODE-03] Block 337/500 | Index: 337 | Slot:  37 | Storage:  39.35 KB | Overwrites: Slot  37 | Hash Ops: 1431357 | Time: 0.043s | ETA:  337.0s
[NODE-03] Block 338/500 | Index: 338 | Slot:  38 | Storage:  39.34 KB | Overwrites: Slot  38 | Hash Ops: 1433434 | Time: 0.030s | ETA:  334.9s
[NODE-03] Block 339/500 | Index: 339 | Slot:  39 | Storage:  39.34 KB | Overwrites: Slot  39 | Hash Ops: 1436669 | Time: 0.043s | ETA:  332.8s
[NODE-03] Block 340/500 | Index: 340 | Slot:  40 | Storage:  39.35 KB | Overwrites: Slot  40 | Hash Ops: 1438200 | Time: 0.018s | ETA:  330.8s
[NODE-03] Block 341/500 | Index: 341 | Slot:  41 | Storage:  39.35 KB | Overwrites: Slot  41 | Hash Ops: 1440262 | Time: 0.030s | ETA:  328.7s
[NODE-03] Block 342/500 | Index: 342 | Slot:  42 | Storage:  39.35 KB | Overwrites: Slot  42 | Hash Ops: 1441021 | Time: 0.006s | ETA:  326.6s
[NODE-03] Block 343/500 | Index: 343 | Slot:  43 | Storage:  39.35 KB | Overwrites: Slot  43 | Hash Ops: 1442007 | Time: 0.007s | ETA:  324.6s
[NODE-03] Block 344/500 | Index: 344 | Slot:  44 | Storage:  39.34 KB | Overwrites: Slot  44 | Hash Ops: 1442842 | Time: 0.012s | ETA:  322.5s
[NODE-03] Block 345/500 | Index: 345 | Slot:  45 | Storage:  39.34 KB | Overwrites: Slot  45 | Hash Ops: 1447487 | Time: 0.038s | ETA:  320.4s
[NODE-03] Block 346/500 | Index: 346 | Slot:  46 | Storage:  39.34 KB | Overwrites: Slot  46 | Hash Ops: 1455545 | Time: 0.056s | ETA:  318.3s
[NODE-03] Block 347/500 | Index: 347 | Slot:  47 | Storage:  39.34 KB | Overwrites: Slot  47 | Hash Ops: 1456497 | Time: 0.011s | ETA:  316.3s
[NODE-03] Block 348/500 | Index: 348 | Slot:  48 | Storage:  39.34 KB | Overwrites: Slot  48 | Hash Ops: 1461782 | Time: 0.039s | ETA:  314.2s
[NODE-03] Block 349/500 | Index: 349 | Slot:  49 | Storage:  39.34 KB | Overwrites: Slot  49 | Hash Ops: 1464590 | Time: 0.019s | ETA:  312.1s
[NODE-03] Block 350/500 | Index: 350 | Slot:  50 | Storage:  39.34 KB | Overwrites: Slot  50 | Hash Ops: 1473588 | Time: 0.060s | ETA:  310.0s
[NODE-03] Block 351/500 | Index: 351 | Slot:  51 | Storage:  39.34 KB | Overwrites: Slot  51 | Hash Ops: 1480821 | Time: 0.048s | ETA:  308.0s
[NODE-03] Block 352/500 | Index: 352 | Slot:  52 | Storage:  39.34 KB | Overwrites: Slot  52 | Hash Ops: 1481368 | Time: 0.004s | ETA:  305.9s
[NODE-03] Block 353/500 | Index: 353 | Slot:  53 | Storage:  39.34 KB | Overwrites: Slot  53 | Hash Ops: 1485930 | Time: 0.035s | ETA:  303.9s
[NODE-03] Block 354/500 | Index: 354 | Slot:  54 | Storage:  39.33 KB | Overwrites: Slot  54 | Hash Ops: 1487894 | Time: 0.017s | ETA:  301.8s
[NODE-03] Block 355/500 | Index: 355 | Slot:  55 | Storage:  39.34 KB | Overwrites: Slot  55 | Hash Ops: 1490770 | Time: 0.019s | ETA:  299.7s
[NODE-03] Block 356/500 | Index: 356 | Slot:  56 | Storage:  39.34 KB | Overwrites: Slot  56 | Hash Ops: 1501070 | Time: 0.067s | ETA:  297.6s
[NODE-03] Block 357/500 | Index: 357 | Slot:  57 | Storage:  39.33 KB | Overwrites: Slot  57 | Hash Ops: 1501949 | Time: 0.014s | ETA:  295.6s
[NODE-03] Block 358/500 | Index: 358 | Slot:  58 | Storage:  39.33 KB | Overwrites: Slot  58 | Hash Ops: 1506555 | Time: 0.036s | ETA:  293.5s
[NODE-03] Block 359/500 | Index: 359 | Slot:  59 | Storage:  39.33 KB | Overwrites: Slot  59 | Hash Ops: 1508869 | Time: 0.020s | ETA:  291.4s
[NODE-03] Block 360/500 | Index: 360 | Slot:  60 | Storage:  39.33 KB | Overwrites: Slot  60 | Hash Ops: 1526197 | Time: 0.119s | ETA:  289.4s
[NODE-03] Block 361/500 | Index: 361 | Slot:  61 | Storage:  39.33 KB | Overwrites: Slot  61 | Hash Ops: 1528694 | Time: 0.017s | ETA:  287.3s
[NODE-03] Block 362/500 | Index: 362 | Slot:  62 | Storage:  39.34 KB | Overwrites: Slot  62 | Hash Ops: 1529947 | Time: 0.011s | ETA:  285.2s
[NODE-03] Block 363/500 | Index: 363 | Slot:  63 | Storage:  39.34 KB | Overwrites: Slot  63 | Hash Ops: 1532987 | Time: 0.023s | ETA:  283.1s
[NODE-03] Block 364/500 | Index: 364 | Slot:  64 | Storage:  39.34 KB | Overwrites: Slot  64 | Hash Ops: 1541998 | Time: 0.060s | ETA:  281.1s
[NODE-03] Block 365/500 | Index: 365 | Slot:  65 | Storage:  39.34 KB | Overwrites: Slot  65 | Hash Ops: 1545456 | Time: 0.026s | ETA:  279.0s
[NODE-03] Block 366/500 | Index: 366 | Slot:  66 | Storage:  39.34 KB | Overwrites: Slot  66 | Hash Ops: 1556831 | Time: 0.073s | ETA:  276.9s
[NODE-03] Block 367/500 | Index: 367 | Slot:  67 | Storage:  39.34 KB | Overwrites: Slot  67 | Hash Ops: 1559139 | Time: 0.020s | ETA:  274.9s
[NODE-03] Block 368/500 | Index: 368 | Slot:  68 | Storage:  39.34 KB | Overwrites: Slot  68 | Hash Ops: 1562470 | Time: 0.027s | ETA:  272.8s
[NODE-03] Block 369/500 | Index: 369 | Slot:  69 | Storage:  39.34 KB | Overwrites: Slot  69 | Hash Ops: 1566168 | Time: 0.024s | ETA:  270.7s
[NODE-03] Block 370/500 | Index: 370 | Slot:  70 | Storage:  39.34 KB | Overwrites: Slot  70 | Hash Ops: 1567173 | Time: 0.007s | ETA:  268.6s
[NODE-03] Block 371/500 | Index: 371 | Slot:  71 | Storage:  39.34 KB | Overwrites: Slot  71 | Hash Ops: 1568084 | Time: 0.006s | ETA:  266.6s
[NODE-03] Block 372/500 | Index: 372 | Slot:  72 | Storage:  39.34 KB | Overwrites: Slot  72 | Hash Ops: 1572476 | Time: 0.038s | ETA:  264.5s
[NODE-03] Block 373/500 | Index: 373 | Slot:  73 | Storage:  39.34 KB | Overwrites: Slot  73 | Hash Ops: 1573705 | Time: 0.009s | ETA:  262.5s
[NODE-03] Block 374/500 | Index: 374 | Slot:  74 | Storage:  39.34 KB | Overwrites: Slot  74 | Hash Ops: 1574505 | Time: 0.010s | ETA:  260.4s
[NODE-03] Block 375/500 | Index: 375 | Slot:  75 | Storage:  39.34 KB | Overwrites: Slot  75 | Hash Ops: 1581411 | Time: 0.054s | ETA:  258.3s
[NODE-03] Block 376/500 | Index: 376 | Slot:  76 | Storage:  39.34 KB | Overwrites: Slot  76 | Hash Ops: 1583373 | Time: 0.017s | ETA:  256.3s
[NODE-03] Block 377/500 | Index: 377 | Slot:  77 | Storage:  39.34 KB | Overwrites: Slot  77 | Hash Ops: 1585109 | Time: 0.015s | ETA:  254.2s
[NODE-03] Block 378/500 | Index: 378 | Slot:  78 | Storage:  39.34 KB | Overwrites: Slot  78 | Hash Ops: 1587170 | Time: 0.018s | ETA:  252.1s
[NODE-03] Block 379/500 | Index: 379 | Slot:  79 | Storage:  39.34 KB | Overwrites: Slot  79 | Hash Ops: 1590946 | Time: 0.027s | ETA:  250.0s
[NODE-03] Block 380/500 | Index: 380 | Slot:  80 | Storage:  39.34 KB | Overwrites: Slot  80 | Hash Ops: 1598243 | Time: 0.051s | ETA:  248.0s
[NODE-03] Block 381/500 | Index: 381 | Slot:  81 | Storage:  39.33 KB | Overwrites: Slot  81 | Hash Ops: 1598350 | Time: 0.003s | ETA:  245.9s
[NODE-03] Block 382/500 | Index: 382 | Slot:  82 | Storage:  39.33 KB | Overwrites: Slot  82 | Hash Ops: 1605363 | Time: 0.050s | ETA:  243.9s
[NODE-03] Block 383/500 | Index: 383 | Slot:  83 | Storage:  39.33 KB | Overwrites: Slot  83 | Hash Ops: 1607147 | Time: 0.015s | ETA:  241.8s
[NODE-03] Block 384/500 | Index: 384 | Slot:  84 | Storage:  39.33 KB | Overwrites: Slot  84 | Hash Ops: 1614027 | Time: 0.050s | ETA:  239.7s
[NODE-03] Block 385/500 | Index: 385 | Slot:  85 | Storage:  39.33 KB | Overwrites: Slot  85 | Hash Ops: 1614914 | Time: 0.010s | ETA:  237.6s
[NODE-03] Block 386/500 | Index: 386 | Slot:  86 | Storage:  39.34 KB | Overwrites: Slot  86 | Hash Ops: 1636308 | Time: 0.144s | ETA:  235.6s
[NODE-03] Block 387/500 | Index: 387 | Slot:  87 | Storage:  39.33 KB | Overwrites: Slot  87 | Hash Ops: 1636409 | Time: 0.003s | ETA:  233.6s
[NODE-03] Block 388/500 | Index: 388 | Slot:  88 | Storage:  39.33 KB | Overwrites: Slot  88 | Hash Ops: 1639597 | Time: 0.022s | ETA:  231.5s
[NODE-03] Block 389/500 | Index: 389 | Slot:  89 | Storage:  39.33 KB | Overwrites: Slot  89 | Hash Ops: 1643185 | Time: 0.024s | ETA:  229.4s
[NODE-03] Block 390/500 | Index: 390 | Slot:  90 | Storage:  39.33 KB | Overwrites: Slot  90 | Hash Ops: 1645209 | Time: 0.015s | ETA:  227.4s
[NODE-03] Block 391/500 | Index: 391 | Slot:  91 | Storage:  39.33 KB | Overwrites: Slot  91 | Hash Ops: 1653685 | Time: 0.058s | ETA:  225.3s
[NODE-03] Block 392/500 | Index: 392 | Slot:  92 | Storage:  39.33 KB | Overwrites: Slot  92 | Hash Ops: 1658793 | Time: 0.038s | ETA:  223.3s
[NODE-03] Block 393/500 | Index: 393 | Slot:  93 | Storage:  39.33 KB | Overwrites: Slot  93 | Hash Ops: 1665406 | Time: 0.052s | ETA:  221.2s
[NODE-03] Block 394/500 | Index: 394 | Slot:  94 | Storage:  39.33 KB | Overwrites: Slot  94 | Hash Ops: 1666855 | Time: 0.013s | ETA:  219.1s
[NODE-03] Block 395/500 | Index: 395 | Slot:  95 | Storage:  39.33 KB | Overwrites: Slot  95 | Hash Ops: 1677318 | Time: 0.075s | ETA:  217.1s
[NODE-03] Block 396/500 | Index: 396 | Slot:  96 | Storage:  39.33 KB | Overwrites: Slot  96 | Hash Ops: 1679737 | Time: 0.016s | ETA:  215.0s
[NODE-03] Block 397/500 | Index: 397 | Slot:  97 | Storage:  39.33 KB | Overwrites: Slot  97 | Hash Ops: 1688771 | Time: 0.063s | ETA:  212.9s
[NODE-03] Block 398/500 | Index: 398 | Slot:  98 | Storage:  39.33 KB | Overwrites: Slot  98 | Hash Ops: 1690876 | Time: 0.022s | ETA:  210.9s
[NODE-03] Block 399/500 | Index: 399 | Slot:  99 | Storage:  39.33 KB | Overwrites: Slot  99 | Hash Ops: 1692548 | Time: 0.015s | ETA:  208.8s
[NODE-03] Block 400/500 | Index: 400 | Slot:   0 | Storage:  39.33 KB | Overwrites: Slot   0 | Hash Ops: 1702103 | Time: 0.066s | ETA:  206.7s
[NODE-03] Block 401/500 | Index: 401 | Slot:   1 | Storage:  39.33 KB | Overwrites: Slot   1 | Hash Ops: 1702837 | Time: 0.005s | ETA:  204.7s
[NODE-03] Block 402/500 | Index: 402 | Slot:   2 | Storage:  39.33 KB | Overwrites: Slot   2 | Hash Ops: 1705172 | Time: 0.016s | ETA:  202.6s
[NODE-03] Block 403/500 | Index: 403 | Slot:   3 | Storage:  39.33 KB | Overwrites: Slot   3 | Hash Ops: 1711057 | Time: 0.047s | ETA:  200.5s
[NODE-03] Block 404/500 | Index: 404 | Slot:   4 | Storage:  39.34 KB | Overwrites: Slot   4 | Hash Ops: 1713399 | Time: 0.021s | ETA:  198.4s
[NODE-03] Block 405/500 | Index: 405 | Slot:   5 | Storage:  39.34 KB | Overwrites: Slot   5 | Hash Ops: 1723855 | Time: 0.072s | ETA:  196.4s
[NODE-03] Block 406/500 | Index: 406 | Slot:   6 | Storage:  39.34 KB | Overwrites: Slot   6 | Hash Ops: 1726426 | Time: 0.023s | ETA:  194.3s
[NODE-03] Block 407/500 | Index: 407 | Slot:   7 | Storage:  39.34 KB | Overwrites: Slot   7 | Hash Ops: 1733036 | Time: 0.048s | ETA:  192.2s
[NODE-03] Block 408/500 | Index: 408 | Slot:   8 | Storage:  39.34 KB | Overwrites: Slot   8 | Hash Ops: 1735823 | Time: 0.019s | ETA:  190.2s
[NODE-03] Block 409/500 | Index: 409 | Slot:   9 | Storage:  39.34 KB | Overwrites: Slot   9 | Hash Ops: 1740192 | Time: 0.032s | ETA:  188.1s
[NODE-03] Block 410/500 | Index: 410 | Slot:  10 | Storage:  39.34 KB | Overwrites: Slot  10 | Hash Ops: 1741521 | Time: 0.013s | ETA:  186.0s
[NODE-03] Block 411/500 | Index: 411 | Slot:  11 | Storage:  39.34 KB | Overwrites: Slot  11 | Hash Ops: 1744635 | Time: 0.023s | ETA:  184.0s
[NODE-03] Block 412/500 | Index: 412 | Slot:  12 | Storage:  39.34 KB | Overwrites: Slot  12 | Hash Ops: 1746859 | Time: 0.019s | ETA:  181.9s
[NODE-03] Block 413/500 | Index: 413 | Slot:  13 | Storage:  39.34 KB | Overwrites: Slot  13 | Hash Ops: 1758108 | Time: 0.076s | ETA:  179.8s
[NODE-03] Block 414/500 | Index: 414 | Slot:  14 | Storage:  39.34 KB | Overwrites: Slot  14 | Hash Ops: 1762459 | Time: 0.029s | ETA:  177.8s
[NODE-03] Block 415/500 | Index: 415 | Slot:  15 | Storage:  39.34 KB | Overwrites: Slot  15 | Hash Ops: 1771323 | Time: 0.058s | ETA:  175.7s
[NODE-03] Block 416/500 | Index: 416 | Slot:  16 | Storage:  39.34 KB | Overwrites: Slot  16 | Hash Ops: 1771501 | Time: 0.005s | ETA:  173.6s
[NODE-03] Block 417/500 | Index: 417 | Slot:  17 | Storage:  39.34 KB | Overwrites: Slot  17 | Hash Ops: 1774083 | Time: 0.017s | ETA:  171.5s
[NODE-03] Block 418/500 | Index: 418 | Slot:  18 | Storage:  39.34 KB | Overwrites: Slot  18 | Hash Ops: 1774442 | Time: 0.007s | ETA:  169.5s
[NODE-03] Block 419/500 | Index: 419 | Slot:  19 | Storage:  39.34 KB | Overwrites: Slot  19 | Hash Ops: 1775451 | Time: 0.010s | ETA:  167.4s
[NODE-03] Block 420/500 | Index: 420 | Slot:  20 | Storage:  39.34 KB | Overwrites: Slot  20 | Hash Ops: 1779528 | Time: 0.027s | ETA:  165.3s
[NODE-03] Block 421/500 | Index: 421 | Slot:  21 | Storage:  39.34 KB | Overwrites: Slot  21 | Hash Ops: 1780797 | Time: 0.011s | ETA:  163.3s
[NODE-03] Block 422/500 | Index: 422 | Slot:  22 | Storage:  39.34 KB | Overwrites: Slot  22 | Hash Ops: 1783686 | Time: 0.023s | ETA:  161.2s
[NODE-03] Block 423/500 | Index: 423 | Slot:  23 | Storage:  39.34 KB | Overwrites: Slot  23 | Hash Ops: 1784572 | Time: 0.013s | ETA:  159.1s
[NODE-03] Block 424/500 | Index: 424 | Slot:  24 | Storage:  39.34 KB | Overwrites: Slot  24 | Hash Ops: 1786131 | Time: 0.011s | ETA:  157.0s
[NODE-03] Block 425/500 | Index: 425 | Slot:  25 | Storage:  39.34 KB | Overwrites: Slot  25 | Hash Ops: 1789399 | Time: 0.029s | ETA:  155.0s
[NODE-03] Block 426/500 | Index: 426 | Slot:  26 | Storage:  39.34 KB | Overwrites: Slot  26 | Hash Ops: 1791022 | Time: 0.011s | ETA:  152.9s
[NODE-03] Block 427/500 | Index: 427 | Slot:  27 | Storage:  39.34 KB | Overwrites: Slot  27 | Hash Ops: 1791714 | Time: 0.005s | ETA:  150.8s
[NODE-03] Block 428/500 | Index: 428 | Slot:  28 | Storage:  39.34 KB | Overwrites: Slot  28 | Hash Ops: 1800422 | Time: 0.062s | ETA:  148.8s
[NODE-03] Block 429/500 | Index: 429 | Slot:  29 | Storage:  39.34 KB | Overwrites: Slot  29 | Hash Ops: 1802654 | Time: 0.023s | ETA:  146.7s
[NODE-03] Block 430/500 | Index: 430 | Slot:  30 | Storage:  39.34 KB | Overwrites: Slot  30 | Hash Ops: 1803026 | Time: 0.003s | ETA:  144.6s
[NODE-03] Block 431/500 | Index: 431 | Slot:  31 | Storage:  39.34 KB | Overwrites: Slot  31 | Hash Ops: 1805803 | Time: 0.020s | ETA:  142.6s
[NODE-03] Block 432/500 | Index: 432 | Slot:  32 | Storage:  39.34 KB | Overwrites: Slot  32 | Hash Ops: 1807375 | Time: 0.013s | ETA:  140.5s
[NODE-03] Block 433/500 | Index: 433 | Slot:  33 | Storage:  39.35 KB | Overwrites: Slot  33 | Hash Ops: 1812771 | Time: 0.039s | ETA:  138.4s
[NODE-03] Block 434/500 | Index: 434 | Slot:  34 | Storage:  39.35 KB | Overwrites: Slot  34 | Hash Ops: 1824800 | Time: 0.080s | ETA:  136.4s
[NODE-03] Block 435/500 | Index: 435 | Slot:  35 | Storage:  39.35 KB | Overwrites: Slot  35 | Hash Ops: 1825998 | Time: 0.012s | ETA:  134.3s
[NODE-03] Block 436/500 | Index: 436 | Slot:  36 | Storage:  39.35 KB | Overwrites: Slot  36 | Hash Ops: 1826140 | Time: 0.001s | ETA:  132.2s
[NODE-03] Block 437/500 | Index: 437 | Slot:  37 | Storage:  39.35 KB | Overwrites: Slot  37 | Hash Ops: 1827779 | Time: 0.014s | ETA:  130.1s
[NODE-03] Block 438/500 | Index: 438 | Slot:  38 | Storage:  39.35 KB | Overwrites: Slot  38 | Hash Ops: 1829607 | Time: 0.017s | ETA:  128.1s
[NODE-03] Block 439/500 | Index: 439 | Slot:  39 | Storage:  39.35 KB | Overwrites: Slot  39 | Hash Ops: 1836287 | Time: 0.048s | ETA:  126.0s
[NODE-03] Block 440/500 | Index: 440 | Slot:  40 | Storage:  39.35 KB | Overwrites: Slot  40 | Hash Ops: 1842436 | Time: 0.051s | ETA:  123.9s
[NODE-03] Block 441/500 | Index: 441 | Slot:  41 | Storage:  39.35 KB | Overwrites: Slot  41 | Hash Ops: 1844458 | Time: 0.017s | ETA:  121.9s
[NODE-03] Block 442/500 | Index: 442 | Slot:  42 | Storage:  39.35 KB | Overwrites: Slot  42 | Hash Ops: 1845249 | Time: 0.006s | ETA:  119.8s
[NODE-03] Block 443/500 | Index: 443 | Slot:  43 | Storage:  39.35 KB | Overwrites: Slot  43 | Hash Ops: 1845601 | Time: 0.006s | ETA:  117.8s
[NODE-03] Block 444/500 | Index: 444 | Slot:  44 | Storage:  39.35 KB | Overwrites: Slot  44 | Hash Ops: 1850887 | Time: 0.044s | ETA:  115.7s
[NODE-03] Block 445/500 | Index: 445 | Slot:  45 | Storage:  39.35 KB | Overwrites: Slot  45 | Hash Ops: 1853016 | Time: 0.023s | ETA:  113.6s
[NODE-03] Block 446/500 | Index: 446 | Slot:  46 | Storage:  39.35 KB | Overwrites: Slot  46 | Hash Ops: 1854987 | Time: 0.016s | ETA:  111.6s
[NODE-03] Block 447/500 | Index: 447 | Slot:  47 | Storage:  39.35 KB | Overwrites: Slot  47 | Hash Ops: 1860720 | Time: 0.042s | ETA:  109.5s
[NODE-03] Block 448/500 | Index: 448 | Slot:  48 | Storage:  39.35 KB | Overwrites: Slot  48 | Hash Ops: 1861565 | Time: 0.006s | ETA:  107.4s
[NODE-03] Block 449/500 | Index: 449 | Slot:  49 | Storage:  39.35 KB | Overwrites: Slot  49 | Hash Ops: 1862612 | Time: 0.010s | ETA:  105.4s
[NODE-03] Block 450/500 | Index: 450 | Slot:  50 | Storage:  39.35 KB | Overwrites: Slot  50 | Hash Ops: 1863406 | Time: 0.012s | ETA:  103.3s
[NODE-03] Block 451/500 | Index: 451 | Slot:  51 | Storage:  39.35 KB | Overwrites: Slot  51 | Hash Ops: 1863729 | Time: 0.007s | ETA:  101.2s
[NODE-03] Block 452/500 | Index: 452 | Slot:  52 | Storage:  39.35 KB | Overwrites: Slot  52 | Hash Ops: 1868227 | Time: 0.033s | ETA:   99.2s
[NODE-03] Block 453/500 | Index: 453 | Slot:  53 | Storage:  39.35 KB | Overwrites: Slot  53 | Hash Ops: 1868929 | Time: 0.009s | ETA:   97.1s
[NODE-03] Block 454/500 | Index: 454 | Slot:  54 | Storage:  39.35 KB | Overwrites: Slot  54 | Hash Ops: 1888468 | Time: 0.134s | ETA:   95.0s
[NODE-03] Block 455/500 | Index: 455 | Slot:  55 | Storage:  39.35 KB | Overwrites: Slot  55 | Hash Ops: 1890523 | Time: 0.015s | ETA:   93.0s
[NODE-03] Block 456/500 | Index: 456 | Slot:  56 | Storage:  39.35 KB | Overwrites: Slot  56 | Hash Ops: 1890678 | Time: 0.001s | ETA:   90.9s
[NODE-03] Block 457/500 | Index: 457 | Slot:  57 | Storage:  39.35 KB | Overwrites: Slot  57 | Hash Ops: 1895580 | Time: 0.041s | ETA:   88.8s
[NODE-03] Block 458/500 | Index: 458 | Slot:  58 | Storage:  39.35 KB | Overwrites: Slot  58 | Hash Ops: 1901195 | Time: 0.044s | ETA:   86.8s
[NODE-03] Block 459/500 | Index: 459 | Slot:  59 | Storage:  39.35 KB | Overwrites: Slot  59 | Hash Ops: 1916925 | Time: 0.107s | ETA:   84.7s
[NODE-03] Block 460/500 | Index: 460 | Slot:  60 | Storage:  39.35 KB | Overwrites: Slot  60 | Hash Ops: 1918270 | Time: 0.026s | ETA:   82.6s
[NODE-03] Block 461/500 | Index: 461 | Slot:  61 | Storage:  39.35 KB | Overwrites: Slot  61 | Hash Ops: 1920590 | Time: 0.016s | ETA:   80.6s
[NODE-03] Block 462/500 | Index: 462 | Slot:  62 | Storage:  39.35 KB | Overwrites: Slot  62 | Hash Ops: 1922209 | Time: 0.018s | ETA:   78.5s
[NODE-03] Block 463/500 | Index: 463 | Slot:  63 | Storage:  39.35 KB | Overwrites: Slot  63 | Hash Ops: 1923179 | Time: 0.007s | ETA:   76.4s
[NODE-03] Block 464/500 | Index: 464 | Slot:  64 | Storage:  39.35 KB | Overwrites: Slot  64 | Hash Ops: 1928494 | Time: 0.049s | ETA:   74.4s
[NODE-03] Block 465/500 | Index: 465 | Slot:  65 | Storage:  39.35 KB | Overwrites: Slot  65 | Hash Ops: 1932370 | Time: 0.030s | ETA:   72.3s
[NODE-03] Block 466/500 | Index: 466 | Slot:  66 | Storage:  39.35 KB | Overwrites: Slot  66 | Hash Ops: 1936223 | Time: 0.043s | ETA:   70.2s
[NODE-03] Block 467/500 | Index: 467 | Slot:  67 | Storage:  39.35 KB | Overwrites: Slot  67 | Hash Ops: 1940177 | Time: 0.035s | ETA:   68.2s
[NODE-03] Block 468/500 | Index: 468 | Slot:  68 | Storage:  39.35 KB | Overwrites: Slot  68 | Hash Ops: 1944066 | Time: 0.051s | ETA:   66.1s
[NODE-03] Block 469/500 | Index: 469 | Slot:  69 | Storage:  39.35 KB | Overwrites: Slot  69 | Hash Ops: 1948929 | Time: 0.046s | ETA:   64.0s
[NODE-03] Block 470/500 | Index: 470 | Slot:  70 | Storage:  39.35 KB | Overwrites: Slot  70 | Hash Ops: 1954508 | Time: 0.052s | ETA:   62.0s
[NODE-03] Block 471/500 | Index: 471 | Slot:  71 | Storage:  39.35 KB | Overwrites: Slot  71 | Hash Ops: 1963173 | Time: 0.089s | ETA:   59.9s
[NODE-03] Block 472/500 | Index: 472 | Slot:  72 | Storage:  39.35 KB | Overwrites: Slot  72 | Hash Ops: 1968644 | Time: 0.056s | ETA:   57.8s
[NODE-03] Block 473/500 | Index: 473 | Slot:  73 | Storage:  39.35 KB | Overwrites: Slot  73 | Hash Ops: 1971322 | Time: 0.030s | ETA:   55.8s
[NODE-03] Block 474/500 | Index: 474 | Slot:  74 | Storage:  39.35 KB | Overwrites: Slot  74 | Hash Ops: 1975160 | Time: 0.026s | ETA:   53.7s
[NODE-03] Block 475/500 | Index: 475 | Slot:  75 | Storage:  39.35 KB | Overwrites: Slot  75 | Hash Ops: 1977305 | Time: 0.032s | ETA:   51.6s
[NODE-03] Block 476/500 | Index: 476 | Slot:  76 | Storage:  39.35 KB | Overwrites: Slot  76 | Hash Ops: 1978774 | Time: 0.015s | ETA:   49.6s
[NODE-03] Block 477/500 | Index: 477 | Slot:  77 | Storage:  39.35 KB | Overwrites: Slot  77 | Hash Ops: 1981184 | Time: 0.019s | ETA:   47.5s
[NODE-03] Block 478/500 | Index: 478 | Slot:  78 | Storage:  39.35 KB | Overwrites: Slot  78 | Hash Ops: 1984061 | Time: 0.029s | ETA:   45.4s
[NODE-03] Block 479/500 | Index: 479 | Slot:  79 | Storage:  39.35 KB | Overwrites: Slot  79 | Hash Ops: 1986835 | Time: 0.020s | ETA:   43.4s
[NODE-03] Block 480/500 | Index: 480 | Slot:  80 | Storage:  39.35 KB | Overwrites: Slot  80 | Hash Ops: 1989276 | Time: 0.025s | ETA:   41.3s
[NODE-03] Block 481/500 | Index: 481 | Slot:  81 | Storage:  39.35 KB | Overwrites: Slot  81 | Hash Ops: 1993311 | Time: 0.042s | ETA:   39.3s
[NODE-03] Block 482/500 | Index: 482 | Slot:  82 | Storage:  39.35 KB | Overwrites: Slot  82 | Hash Ops: 1996887 | Time: 0.031s | ETA:   37.2s
[NODE-03] Block 483/500 | Index: 483 | Slot:  83 | Storage:  39.35 KB | Overwrites: Slot  83 | Hash Ops: 2000232 | Time: 0.038s | ETA:   35.1s
[NODE-03] Block 484/500 | Index: 484 | Slot:  84 | Storage:  39.35 KB | Overwrites: Slot  84 | Hash Ops: 2004413 | Time: 0.052s | ETA:   33.1s
[NODE-03] Block 485/500 | Index: 485 | Slot:  85 | Storage:  39.35 KB | Overwrites: Slot  85 | Hash Ops: 2006750 | Time: 0.038s | ETA:   31.0s
[NODE-03] Block 486/500 | Index: 486 | Slot:  86 | Storage:  39.35 KB | Overwrites: Slot  86 | Hash Ops: 2009653 | Time: 0.021s | ETA:   28.9s
[NODE-03] Block 487/500 | Index: 487 | Slot:  87 | Storage:  39.35 KB | Overwrites: Slot  87 | Hash Ops: 2013771 | Time: 0.038s | ETA:   26.9s
[NODE-03] Block 488/500 | Index: 488 | Slot:  88 | Storage:  39.35 KB | Overwrites: Slot  88 | Hash Ops: 2016765 | Time: 0.024s | ETA:   24.8s
[NODE-03] Block 489/500 | Index: 489 | Slot:  89 | Storage:  39.36 KB | Overwrites: Slot  89 | Hash Ops: 2023116 | Time: 0.049s | ETA:   22.7s
[NODE-03] Block 490/500 | Index: 490 | Slot:  90 | Storage:  39.36 KB | Overwrites: Slot  90 | Hash Ops: 2027835 | Time: 0.045s | ETA:   20.7s
[NODE-03] Block 491/500 | Index: 491 | Slot:  91 | Storage:  39.35 KB | Overwrites: Slot  91 | Hash Ops: 2028923 | Time: 0.013s | ETA:   18.6s
[NODE-03] Block 492/500 | Index: 492 | Slot:  92 | Storage:  39.35 KB | Overwrites: Slot  92 | Hash Ops: 2037096 | Time: 0.066s | ETA:   16.5s
[NODE-03] Block 493/500 | Index: 493 | Slot:  93 | Storage:  39.35 KB | Overwrites: Slot  93 | Hash Ops: 2039749 | Time: 0.018s | ETA:   14.5s
[NODE-03] Block 494/500 | Index: 494 | Slot:  94 | Storage:  39.35 KB | Overwrites: Slot  94 | Hash Ops: 2040686 | Time: 0.007s | ETA:   12.4s
[NODE-03] Block 495/500 | Index: 495 | Slot:  95 | Storage:  39.35 KB | Overwrites: Slot  95 | Hash Ops: 2045672 | Time: 0.041s | ETA:   10.3s
[NODE-03] Block 496/500 | Index: 496 | Slot:  96 | Storage:  39.35 KB | Overwrites: Slot  96 | Hash Ops: 2048130 | Time: 0.020s | ETA:    8.3s
[NODE-03] Block 497/500 | Index: 497 | Slot:  97 | Storage:  39.35 KB | Overwrites: Slot  97 | Hash Ops: 2054000 | Time: 0.044s | ETA:    6.2s
[NODE-03] Block 498/500 | Index: 498 | Slot:  98 | Storage:  39.35 KB | Overwrites: Slot  98 | Hash Ops: 2054008 | Time: 0.000s | ETA:    4.1s
[NODE-03] Block 499/500 | Index: 499 | Slot:  99 | Storage:  39.35 KB | Overwrites: Slot  99 | Hash Ops: 2056654 | Time: 0.018s | ETA:    2.1s
[NODE-03] Block 500/500 | Index: 500 | Slot:   0 | Storage:  39.35 KB | Overwrites: Slot   0 | Hash Ops: 2059184 | Time: 0.021s | ETA:    0.0s
[NODE-03] Peer connections restored
[NODE-03] Completed in 1034.68 seconds

================================================================================
Resetting NODE-04 to genesis before its simulation
================================================================================
✓ NODE-04 reset to genesis (index=0)


[NODE-04] Starting block generation...
[NODE-04] Initial ledger state:
[NODE-04]   Last index: 0
[NODE-04]   Genesis hash: 000ac6d79f7c53bb...
[NODE-04] Target: 500 blocks
[NODE-04] Mode: Independent (no peer interaction)
[NODE-04] Peers temporarily disconnected for independent simulation
[NODE-04] Block   1/500 | Index:   1 | Slot:   1 | Storage:   0.70 KB | Overwrites:   - | Hash Ops:   2739 | Time: 0.022s | ETA:   67.3s
[NODE-04] Block   2/500 | Index:   2 | Slot:   2 | Storage:   1.09 KB | Overwrites:   - | Hash Ops:   9316 | Time: 0.047s | ETA:  545.1s
[NODE-04] Block   3/500 | Index:   3 | Slot:   3 | Storage:   1.48 KB | Overwrites:   - | Hash Ops:  12996 | Time: 0.027s | ETA:  706.3s
[NODE-04] Block   4/500 | Index:   4 | Slot:   4 | Storage:   1.87 KB | Overwrites:   - | Hash Ops:  21229 | Time: 0.054s | ETA:  783.6s
[NODE-04] Block   5/500 | Index:   5 | Slot:   5 | Storage:   2.26 KB | Overwrites:   - | Hash Ops:  21289 | Time: 0.002s | ETA:  827.7s
[NODE-04] Block   6/500 | Index:   6 | Slot:   6 | Storage:   2.64 KB | Overwrites:   - | Hash Ops:  22853 | Time: 0.012s | ETA:  855.2s
[NODE-04] Block   7/500 | Index:   7 | Slot:   7 | Storage:   3.04 KB | Overwrites:   - | Hash Ops:  25567 | Time: 0.027s | ETA:  874.6s
[NODE-04] Block   8/500 | Index:   8 | Slot:   8 | Storage:   3.42 KB | Overwrites:   - | Hash Ops:  27564 | Time: 0.017s | ETA:  887.8s
[NODE-04] Block   9/500 | Index:   9 | Slot:   9 | Storage:   3.81 KB | Overwrites:   - | Hash Ops:  27765 | Time: 0.006s | ETA:  897.1s
[NODE-04] Block  10/500 | Index:  10 | Slot:  10 | Storage:   4.20 KB | Overwrites:   - | Hash Ops:  30044 | Time: 0.020s | ETA:  904.8s
[NODE-04] Block  11/500 | Index:  11 | Slot:  11 | Storage:   4.59 KB | Overwrites:   - | Hash Ops:  35983 | Time: 0.043s | ETA:  919.2s
[NODE-04] Block  12/500 | Index:  12 | Slot:  12 | Storage:   4.98 KB | Overwrites:   - | Hash Ops:  39858 | Time: 0.031s | ETA:  924.3s
[NODE-04] Block  13/500 | Index:  13 | Slot:  13 | Storage:   5.37 KB | Overwrites:   - | Hash Ops:  43940 | Time: 0.027s | ETA:  927.4s
[NODE-04] Block  14/500 | Index:  14 | Slot:  14 | Storage:   5.76 KB | Overwrites:   - | Hash Ops:  44045 | Time: 0.001s | ETA:  929.0s
[NODE-04] Block  15/500 | Index:  15 | Slot:  15 | Storage:   6.15 KB | Overwrites:   - | Hash Ops:  50088 | Time: 0.042s | ETA:  931.4s
[NODE-04] Block  16/500 | Index:  16 | Slot:  16 | Storage:   6.54 KB | Overwrites:   - | Hash Ops:  51380 | Time: 0.012s | ETA:  932.9s
[NODE-04] Block  17/500 | Index:  17 | Slot:  17 | Storage:   6.93 KB | Overwrites:   - | Hash Ops:  55483 | Time: 0.034s | ETA:  936.2s
[NODE-04] Block  18/500 | Index:  18 | Slot:  18 | Storage:   7.32 KB | Overwrites:   - | Hash Ops:  57877 | Time: 0.016s | ETA:  936.6s
[NODE-04] Block  19/500 | Index:  19 | Slot:  19 | Storage:   7.71 KB | Overwrites:   - | Hash Ops:  57986 | Time: 0.003s | ETA:  936.2s
[NODE-04] Block  20/500 | Index:  20 | Slot:  20 | Storage:   8.10 KB | Overwrites:   - | Hash Ops:  65880 | Time: 0.057s | ETA:  937.0s
[NODE-04] Block  21/500 | Index:  21 | Slot:  21 | Storage:   8.49 KB | Overwrites:   - | Hash Ops:  66111 | Time: 0.005s | ETA:  938.7s
[NODE-04] Block  22/500 | Index:  22 | Slot:  22 | Storage:   8.88 KB | Overwrites:   - | Hash Ops:  66565 | Time: 0.007s | ETA:  938.1s
[NODE-04] Block  23/500 | Index:  23 | Slot:  23 | Storage:   9.27 KB | Overwrites:   - | Hash Ops:  70230 | Time: 0.027s | ETA:  938.0s
[NODE-04] Block  24/500 | Index:  24 | Slot:  24 | Storage:   9.66 KB | Overwrites:   - | Hash Ops:  71649 | Time: 0.010s | ETA:  937.2s
[NODE-04] Block  25/500 | Index:  25 | Slot:  25 | Storage:  10.05 KB | Overwrites:   - | Hash Ops:  72332 | Time: 0.013s | ETA:  936.2s
[NODE-04] Block  26/500 | Index:  26 | Slot:  26 | Storage:  10.44 KB | Overwrites:   - | Hash Ops:  78244 | Time: 0.042s | ETA:  935.8s
[NODE-04] Block  27/500 | Index:  27 | Slot:  27 | Storage:  10.83 KB | Overwrites:   - | Hash Ops:  85110 | Time: 0.050s | ETA:  935.4s
[NODE-04] Block  28/500 | Index:  28 | Slot:  28 | Storage:  11.22 KB | Overwrites:   - | Hash Ops:  87393 | Time: 0.019s | ETA:  934.5s
[NODE-04] Block  29/500 | Index:  29 | Slot:  29 | Storage:  11.61 KB | Overwrites:   - | Hash Ops:  88517 | Time: 0.011s | ETA:  935.5s
[NODE-04] Block  30/500 | Index:  30 | Slot:  30 | Storage:  12.00 KB | Overwrites:   - | Hash Ops:  90028 | Time: 0.011s | ETA:  934.6s
[NODE-04] Block  31/500 | Index:  31 | Slot:  31 | Storage:  12.39 KB | Overwrites:   - | Hash Ops:  90733 | Time: 0.008s | ETA:  934.5s
[NODE-04] Block  32/500 | Index:  32 | Slot:  32 | Storage:  12.78 KB | Overwrites:   - | Hash Ops:  99202 | Time: 0.059s | ETA:  933.8s
[NODE-04] Block  33/500 | Index:  33 | Slot:  33 | Storage:  13.17 KB | Overwrites:   - | Hash Ops:  99498 | Time: 0.002s | ETA:  931.9s
[NODE-04] Block  34/500 | Index:  34 | Slot:  34 | Storage:  13.56 KB | Overwrites:   - | Hash Ops:  99530 | Time: 0.000s | ETA:  930.1s
[NODE-04] Block  35/500 | Index:  35 | Slot:  35 | Storage:  13.96 KB | Overwrites:   - | Hash Ops: 104643 | Time: 0.035s | ETA:  928.8s
[NODE-04] Block  36/500 | Index:  36 | Slot:  36 | Storage:  14.35 KB | Overwrites:   - | Hash Ops: 105919 | Time: 0.013s | ETA:  927.1s
[NODE-04] Block  37/500 | Index:  37 | Slot:  37 | Storage:  14.74 KB | Overwrites:   - | Hash Ops: 106979 | Time: 0.010s | ETA:  925.4s
[NODE-04] Block  38/500 | Index:  38 | Slot:  38 | Storage:  15.13 KB | Overwrites:   - | Hash Ops: 111583 | Time: 0.033s | ETA:  924.1s
[NODE-04] Block  39/500 | Index:  39 | Slot:  39 | Storage:  15.52 KB | Overwrites:   - | Hash Ops: 113733 | Time: 0.014s | ETA:  922.4s
[NODE-04] Block  40/500 | Index:  40 | Slot:  40 | Storage:  15.91 KB | Overwrites:   - | Hash Ops: 114151 | Time: 0.009s | ETA:  920.6s
[NODE-04] Block  41/500 | Index:  41 | Slot:  41 | Storage:  16.30 KB | Overwrites:   - | Hash Ops: 116443 | Time: 0.019s | ETA:  920.3s
[NODE-04] Block  42/500 | Index:  42 | Slot:  42 | Storage:  16.70 KB | Overwrites:   - | Hash Ops: 132484 | Time: 0.114s | ETA:  919.6s
[NODE-04] Block  43/500 | Index:  43 | Slot:  43 | Storage:  17.09 KB | Overwrites:   - | Hash Ops: 132926 | Time: 0.006s | ETA:  917.7s
[NODE-04] Block  44/500 | Index:  44 | Slot:  44 | Storage:  17.48 KB | Overwrites:   - | Hash Ops: 136236 | Time: 0.023s | ETA:  915.9s
[NODE-04] Block  45/500 | Index:  45 | Slot:  45 | Storage:  17.86 KB | Overwrites:   - | Hash Ops: 137083 | Time: 0.007s | ETA:  914.3s
[NODE-04] Block  46/500 | Index:  46 | Slot:  46 | Storage:  18.26 KB | Overwrites:   - | Hash Ops: 140063 | Time: 0.028s | ETA:  912.5s
[NODE-04] Block  47/500 | Index:  47 | Slot:  47 | Storage:  18.65 KB | Overwrites:   - | Hash Ops: 141530 | Time: 0.017s | ETA:  910.7s
[NODE-04] Block  48/500 | Index:  48 | Slot:  48 | Storage:  19.04 KB | Overwrites:   - | Hash Ops: 146188 | Time: 0.032s | ETA:  908.9s
[NODE-04] Block  49/500 | Index:  49 | Slot:  49 | Storage:  19.43 KB | Overwrites:   - | Hash Ops: 150027 | Time: 0.027s | ETA:  907.1s
[NODE-04] Block  50/500 | Index:  50 | Slot:  50 | Storage:  19.82 KB | Overwrites:   - | Hash Ops: 152157 | Time: 0.021s | ETA:  905.2s
[NODE-04] Block  51/500 | Index:  51 | Slot:  51 | Storage:  20.21 KB | Overwrites:   - | Hash Ops: 155787 | Time: 0.031s | ETA:  904.6s
[NODE-04] Block  52/500 | Index:  52 | Slot:  52 | Storage:  20.61 KB | Overwrites:   - | Hash Ops: 157708 | Time: 0.018s | ETA:  902.9s
[NODE-04] Block  53/500 | Index:  53 | Slot:  53 | Storage:  21.00 KB | Overwrites:   - | Hash Ops: 165035 | Time: 0.051s | ETA:  901.4s
[NODE-04] Block  54/500 | Index:  54 | Slot:  54 | Storage:  21.39 KB | Overwrites:   - | Hash Ops: 173475 | Time: 0.063s | ETA:  899.9s
[NODE-04] Block  55/500 | Index:  55 | Slot:  55 | Storage:  21.78 KB | Overwrites:   - | Hash Ops: 175232 | Time: 0.017s | ETA:  898.0s
[NODE-04] Block  56/500 | Index:  56 | Slot:  56 | Storage:  22.17 KB | Overwrites:   - | Hash Ops: 182486 | Time: 0.049s | ETA:  896.3s
[NODE-04] Block  57/500 | Index:  57 | Slot:  57 | Storage:  22.56 KB | Overwrites:   - | Hash Ops: 189178 | Time: 0.049s | ETA:  894.5s
[NODE-04] Block  58/500 | Index:  58 | Slot:  58 | Storage:  22.95 KB | Overwrites:   - | Hash Ops: 189275 | Time: 0.002s | ETA:  892.6s
[NODE-04] Block  59/500 | Index:  59 | Slot:  59 | Storage:  23.34 KB | Overwrites:   - | Hash Ops: 190382 | Time: 0.013s | ETA:  890.9s
[NODE-04] Block  60/500 | Index:  60 | Slot:  60 | Storage:  23.73 KB | Overwrites:   - | Hash Ops: 195591 | Time: 0.043s | ETA:  889.2s
[NODE-04] Block  61/500 | Index:  61 | Slot:  61 | Storage:  24.12 KB | Overwrites:   - | Hash Ops: 201734 | Time: 0.041s | ETA:  888.1s
[NODE-04] Block  62/500 | Index:  62 | Slot:  62 | Storage:  24.51 KB | Overwrites:   - | Hash Ops: 204000 | Time: 0.015s | ETA:  886.0s
[NODE-04] Block  63/500 | Index:  63 | Slot:  63 | Storage:  24.90 KB | Overwrites:   - | Hash Ops: 206769 | Time: 0.018s | ETA:  884.0s
[NODE-04] Block  64/500 | Index:  64 | Slot:  64 | Storage:  25.30 KB | Overwrites:   - | Hash Ops: 208787 | Time: 0.022s | ETA:  882.0s
[NODE-04] Block  65/500 | Index:  65 | Slot:  65 | Storage:  25.69 KB | Overwrites:   - | Hash Ops: 210050 | Time: 0.012s | ETA:  879.9s
[NODE-04] Block  66/500 | Index:  66 | Slot:  66 | Storage:  26.08 KB | Overwrites:   - | Hash Ops: 214925 | Time: 0.041s | ETA:  878.0s
[NODE-04] Block  67/500 | Index:  67 | Slot:  67 | Storage:  26.47 KB | Overwrites:   - | Hash Ops: 226089 | Time: 0.076s | ETA:  876.4s
[NODE-04] Block  68/500 | Index:  68 | Slot:  68 | Storage:  26.86 KB | Overwrites:   - | Hash Ops: 228552 | Time: 0.021s | ETA:  874.4s
[NODE-04] Block  69/500 | Index:  69 | Slot:  69 | Storage:  27.25 KB | Overwrites:   - | Hash Ops: 236473 | Time: 0.061s | ETA:  872.9s
[NODE-04] Block  70/500 | Index:  70 | Slot:  70 | Storage:  27.64 KB | Overwrites:   - | Hash Ops: 237557 | Time: 0.011s | ETA:  870.8s
[NODE-04] Block  71/500 | Index:  71 | Slot:  71 | Storage:  28.03 KB | Overwrites:   - | Hash Ops: 246526 | Time: 0.061s | ETA:  869.6s
[NODE-04] Block  72/500 | Index:  72 | Slot:  72 | Storage:  28.42 KB | Overwrites:   - | Hash Ops: 248688 | Time: 0.018s | ETA:  867.7s
[NODE-04] Block  73/500 | Index:  73 | Slot:  73 | Storage:  28.81 KB | Overwrites:   - | Hash Ops: 252615 | Time: 0.026s | ETA:  865.7s
[NODE-04] Block  74/500 | Index:  74 | Slot:  74 | Storage:  29.20 KB | Overwrites:   - | Hash Ops: 257756 | Time: 0.035s | ETA:  863.9s
[NODE-04] Block  75/500 | Index:  75 | Slot:  75 | Storage:  29.59 KB | Overwrites:   - | Hash Ops: 264381 | Time: 0.048s | ETA:  862.0s
[NODE-04] Block  76/500 | Index:  76 | Slot:  76 | Storage:  29.98 KB | Overwrites:   - | Hash Ops: 265772 | Time: 0.013s | ETA:  859.9s
[NODE-04] Block  77/500 | Index:  77 | Slot:  77 | Storage:  30.38 KB | Overwrites:   - | Hash Ops: 266473 | Time: 0.009s | ETA:  857.9s
[NODE-04] Block  78/500 | Index:  78 | Slot:  78 | Storage:  30.76 KB | Overwrites:   - | Hash Ops: 266712 | Time: 0.002s | ETA:  855.9s
[NODE-04] Block  79/500 | Index:  79 | Slot:  79 | Storage:  31.15 KB | Overwrites:   - | Hash Ops: 268566 | Time: 0.024s | ETA:  853.9s
[NODE-04] Block  80/500 | Index:  80 | Slot:  80 | Storage:  31.55 KB | Overwrites:   - | Hash Ops: 268719 | Time: 0.001s | ETA:  851.8s
[NODE-04] Block  81/500 | Index:  81 | Slot:  81 | Storage:  31.94 KB | Overwrites:   - | Hash Ops: 272211 | Time: 0.026s | ETA:  850.3s
[NODE-04] Block  82/500 | Index:  82 | Slot:  82 | Storage:  32.33 KB | Overwrites:   - | Hash Ops: 283219 | Time: 0.073s | ETA:  848.7s
[NODE-04] Block  83/500 | Index:  83 | Slot:  83 | Storage:  32.72 KB | Overwrites:   - | Hash Ops: 284008 | Time: 0.009s | ETA:  847.0s
[NODE-04] Block  84/500 | Index:  84 | Slot:  84 | Storage:  33.11 KB | Overwrites:   - | Hash Ops: 288956 | Time: 0.040s | ETA:  845.0s
[NODE-04] Block  85/500 | Index:  85 | Slot:  85 | Storage:  33.50 KB | Overwrites:   - | Hash Ops: 290197 | Time: 0.014s | ETA:  843.1s
[NODE-04] Block  86/500 | Index:  86 | Slot:  86 | Storage:  33.89 KB | Overwrites:   - | Hash Ops: 293336 | Time: 0.021s | ETA:  841.0s
[NODE-04] Block  87/500 | Index:  87 | Slot:  87 | Storage:  34.28 KB | Overwrites:   - | Hash Ops: 300490 | Time: 0.052s | ETA:  839.1s
[NODE-04] Block  88/500 | Index:  88 | Slot:  88 | Storage:  34.67 KB | Overwrites:   - | Hash Ops: 314983 | Time: 0.100s | ETA:  837.4s
[NODE-04] Block  89/500 | Index:  89 | Slot:  89 | Storage:  35.06 KB | Overwrites:   - | Hash Ops: 318326 | Time: 0.026s | ETA:  835.3s
[NODE-04] Block  90/500 | Index:  90 | Slot:  90 | Storage:  35.45 KB | Overwrites:   - | Hash Ops: 331806 | Time: 0.088s | ETA:  833.6s
[NODE-04] Block  91/500 | Index:  91 | Slot:  91 | Storage:  35.84 KB | Overwrites:   - | Hash Ops: 335398 | Time: 0.027s | ETA:  832.1s
[NODE-04] Block  92/500 | Index:  92 | Slot:  92 | Storage:  36.23 KB | Overwrites:   - | Hash Ops: 336458 | Time: 0.015s | ETA:  830.0s
[NODE-04] Block  93/500 | Index:  93 | Slot:  93 | Storage:  36.62 KB | Overwrites:   - | Hash Ops: 337188 | Time: 0.005s | ETA:  827.9s
[NODE-04] Block  94/500 | Index:  94 | Slot:  94 | Storage:  37.01 KB | Overwrites:   - | Hash Ops: 345200 | Time: 0.063s | ETA:  826.0s
[NODE-04] Block  95/500 | Index:  95 | Slot:  95 | Storage:  37.41 KB | Overwrites:   - | Hash Ops: 348129 | Time: 0.020s | ETA:  824.0s
[NODE-04] Block  96/500 | Index:  96 | Slot:  96 | Storage:  37.80 KB | Overwrites:   - | Hash Ops: 354123 | Time: 0.043s | ETA:  822.0s
[NODE-04] Block  97/500 | Index:  97 | Slot:  97 | Storage:  38.19 KB | Overwrites:   - | Hash Ops: 360059 | Time: 0.045s | ETA:  820.2s
[NODE-04] Block  98/500 | Index:  98 | Slot:  98 | Storage:  38.58 KB | Overwrites:   - | Hash Ops: 368689 | Time: 0.061s | ETA:  818.3s
[NODE-04] Block  99/500 | Index:  99 | Slot:  99 | Storage:  38.97 KB | Overwrites:   - | Hash Ops: 376620 | Time: 0.056s | ETA:  816.4s
[NODE-04] Block 100/500 | Index: 100 | Slot:   0 | Storage:  39.05 KB | Overwrites: Slot   0 | Hash Ops: 382662 | Time: 0.044s | ETA:  814.5s
[NODE-04] Block 101/500 | Index: 101 | Slot:   1 | Storage:  39.06 KB | Overwrites: Slot   1 | Hash Ops: 385407 | Time: 0.019s | ETA:  813.0s
[NODE-04] Block 102/500 | Index: 102 | Slot:   2 | Storage:  39.06 KB | Overwrites: Slot   2 | Hash Ops: 387157 | Time: 0.018s | ETA:  810.9s
[NODE-04] Block 103/500 | Index: 103 | Slot:   3 | Storage:  39.07 KB | Overwrites: Slot   3 | Hash Ops: 397485 | Time: 0.076s | ETA:  809.1s
[NODE-04] Block 104/500 | Index: 104 | Slot:   4 | Storage:  39.07 KB | Overwrites: Slot   4 | Hash Ops: 398060 | Time: 0.008s | ETA:  806.9s
[NODE-04] Block 105/500 | Index: 105 | Slot:   5 | Storage:  39.07 KB | Overwrites: Slot   5 | Hash Ops: 398644 | Time: 0.008s | ETA:  804.9s
[NODE-04] Block 106/500 | Index: 106 | Slot:   6 | Storage:  39.08 KB | Overwrites: Slot   6 | Hash Ops: 399077 | Time: 0.003s | ETA:  802.8s
[NODE-04] Block 107/500 | Index: 107 | Slot:   7 | Storage:  39.08 KB | Overwrites: Slot   7 | Hash Ops: 402165 | Time: 0.021s | ETA:  800.7s
[NODE-04] Block 108/500 | Index: 108 | Slot:   8 | Storage:  39.09 KB | Overwrites: Slot   8 | Hash Ops: 408217 | Time: 0.041s | ETA:  798.7s
[NODE-04] Block 109/500 | Index: 109 | Slot:   9 | Storage:  39.09 KB | Overwrites: Slot   9 | Hash Ops: 413992 | Time: 0.039s | ETA:  796.8s
[NODE-04] Block 110/500 | Index: 110 | Slot:  10 | Storage:  39.10 KB | Overwrites: Slot  10 | Hash Ops: 424418 | Time: 0.071s | ETA:  794.9s
[NODE-04] Block 111/500 | Index: 111 | Slot:  11 | Storage:  39.10 KB | Overwrites: Slot  11 | Hash Ops: 428215 | Time: 0.029s | ETA:  793.2s
[NODE-04] Block 112/500 | Index: 112 | Slot:  12 | Storage:  39.11 KB | Overwrites: Slot  12 | Hash Ops: 435067 | Time: 0.050s | ETA:  791.4s
[NODE-04] Block 113/500 | Index: 113 | Slot:  13 | Storage:  39.11 KB | Overwrites: Slot  13 | Hash Ops: 437087 | Time: 0.025s | ETA:  789.4s
[NODE-04] Block 114/500 | Index: 114 | Slot:  14 | Storage:  39.11 KB | Overwrites: Slot  14 | Hash Ops: 448484 | Time: 0.080s | ETA:  787.5s
[NODE-04] Block 115/500 | Index: 115 | Slot:  15 | Storage:  39.12 KB | Overwrites: Slot  15 | Hash Ops: 453419 | Time: 0.036s | ETA:  785.5s
[NODE-04] Block 116/500 | Index: 116 | Slot:  16 | Storage:  39.12 KB | Overwrites: Slot  16 | Hash Ops: 455859 | Time: 0.020s | ETA:  783.4s
[NODE-04] Block 117/500 | Index: 117 | Slot:  17 | Storage:  39.12 KB | Overwrites: Slot  17 | Hash Ops: 457630 | Time: 0.012s | ETA:  781.3s
[NODE-04] Block 118/500 | Index: 118 | Slot:  18 | Storage:  39.12 KB | Overwrites: Slot  18 | Hash Ops: 457971 | Time: 0.005s | ETA:  779.2s
[NODE-04] Block 119/500 | Index: 119 | Slot:  19 | Storage:  39.12 KB | Overwrites: Slot  19 | Hash Ops: 462771 | Time: 0.035s | ETA:  777.3s
[NODE-04] Block 120/500 | Index: 120 | Slot:  20 | Storage:  39.12 KB | Overwrites: Slot  20 | Hash Ops: 463622 | Time: 0.011s | ETA:  775.2s
[NODE-04] Block 121/500 | Index: 121 | Slot:  21 | Storage:  39.13 KB | Overwrites: Slot  21 | Hash Ops: 465874 | Time: 0.018s | ETA:  773.4s
[NODE-04] Block 122/500 | Index: 122 | Slot:  22 | Storage:  39.13 KB | Overwrites: Slot  22 | Hash Ops: 466181 | Time: 0.008s | ETA:  771.3s
[NODE-04] Block 123/500 | Index: 123 | Slot:  23 | Storage:  39.13 KB | Overwrites: Slot  23 | Hash Ops: 469256 | Time: 0.025s | ETA:  769.3s
[NODE-04] Block 124/500 | Index: 124 | Slot:  24 | Storage:  39.14 KB | Overwrites: Slot  24 | Hash Ops: 470145 | Time: 0.007s | ETA:  767.1s
[NODE-04] Block 125/500 | Index: 125 | Slot:  25 | Storage:  39.14 KB | Overwrites: Slot  25 | Hash Ops: 473557 | Time: 0.026s | ETA:  765.1s
[NODE-04] Block 126/500 | Index: 126 | Slot:  26 | Storage:  39.14 KB | Overwrites: Slot  26 | Hash Ops: 480066 | Time: 0.047s | ETA:  763.1s
[NODE-04] Block 127/500 | Index: 127 | Slot:  27 | Storage:  39.15 KB | Overwrites: Slot  27 | Hash Ops: 483519 | Time: 0.027s | ETA:  761.0s
[NODE-04] Block 128/500 | Index: 128 | Slot:  28 | Storage:  39.15 KB | Overwrites: Slot  28 | Hash Ops: 490716 | Time: 0.051s | ETA:  759.0s
[NODE-04] Block 129/500 | Index: 129 | Slot:  29 | Storage:  39.15 KB | Overwrites: Slot  29 | Hash Ops: 493222 | Time: 0.020s | ETA:  757.0s
[NODE-04] Block 130/500 | Index: 130 | Slot:  30 | Storage:  39.16 KB | Overwrites: Slot  30 | Hash Ops: 499190 | Time: 0.039s | ETA:  755.0s
[NODE-04] Block 131/500 | Index: 131 | Slot:  31 | Storage:  39.16 KB | Overwrites: Slot  31 | Hash Ops: 501961 | Time: 0.024s | ETA:  753.3s
[NODE-04] Block 132/500 | Index: 132 | Slot:  32 | Storage:  39.16 KB | Overwrites: Slot  32 | Hash Ops: 505100 | Time: 0.023s | ETA:  751.2s
[NODE-04] Block 133/500 | Index: 133 | Slot:  33 | Storage:  39.16 KB | Overwrites: Slot  33 | Hash Ops: 506316 | Time: 0.011s | ETA:  749.1s
[NODE-04] Block 134/500 | Index: 134 | Slot:  34 | Storage:  39.17 KB | Overwrites: Slot  34 | Hash Ops: 507553 | Time: 0.015s | ETA:  747.0s
[NODE-04] Block 135/500 | Index: 135 | Slot:  35 | Storage:  39.17 KB | Overwrites: Slot  35 | Hash Ops: 516038 | Time: 0.060s | ETA:  745.1s
[NODE-04] Block 136/500 | Index: 136 | Slot:  36 | Storage:  39.17 KB | Overwrites: Slot  36 | Hash Ops: 520485 | Time: 0.039s | ETA:  743.1s
[NODE-04] Block 137/500 | Index: 137 | Slot:  37 | Storage:  39.18 KB | Overwrites: Slot  37 | Hash Ops: 523004 | Time: 0.021s | ETA:  741.5s
[NODE-04] Block 138/500 | Index: 138 | Slot:  38 | Storage:  39.18 KB | Overwrites: Slot  38 | Hash Ops: 541208 | Time: 0.126s | ETA:  739.7s
[NODE-04] Block 139/500 | Index: 139 | Slot:  39 | Storage:  39.18 KB | Overwrites: Slot  39 | Hash Ops: 544190 | Time: 0.026s | ETA:  737.7s
[NODE-04] Block 140/500 | Index: 140 | Slot:  40 | Storage:  39.19 KB | Overwrites: Slot  40 | Hash Ops: 558356 | Time: 0.096s | ETA:  735.8s
[NODE-04] Block 141/500 | Index: 141 | Slot:  41 | Storage:  39.19 KB | Overwrites: Slot  41 | Hash Ops: 564448 | Time: 0.051s | ETA:  734.2s
[NODE-04] Block 142/500 | Index: 142 | Slot:  42 | Storage:  39.19 KB | Overwrites: Slot  42 | Hash Ops: 567487 | Time: 0.026s | ETA:  732.2s
[NODE-04] Block 143/500 | Index: 143 | Slot:  43 | Storage:  39.19 KB | Overwrites: Slot  43 | Hash Ops: 569932 | Time: 0.018s | ETA:  730.1s
[NODE-04] Block 144/500 | Index: 144 | Slot:  44 | Storage:  39.19 KB | Overwrites: Slot  44 | Hash Ops: 576878 | Time: 0.047s | ETA:  728.0s
[NODE-04] Block 145/500 | Index: 145 | Slot:  45 | Storage:  39.20 KB | Overwrites: Slot  45 | Hash Ops: 577961 | Time: 0.015s | ETA:  726.0s
[NODE-04] Block 146/500 | Index: 146 | Slot:  46 | Storage:  39.20 KB | Overwrites: Slot  46 | Hash Ops: 582904 | Time: 0.040s | ETA:  724.0s
[NODE-04] Block 147/500 | Index: 147 | Slot:  47 | Storage:  39.20 KB | Overwrites: Slot  47 | Hash Ops: 586956 | Time: 0.031s | ETA:  722.0s
[NODE-04] Block 148/500 | Index: 148 | Slot:  48 | Storage:  39.20 KB | Overwrites: Slot  48 | Hash Ops: 589966 | Time: 0.024s | ETA:  719.9s
[NODE-04] Block 149/500 | Index: 149 | Slot:  49 | Storage:  39.20 KB | Overwrites: Slot  49 | Hash Ops: 595290 | Time: 0.037s | ETA:  717.8s
[NODE-04] Block 150/500 | Index: 150 | Slot:  50 | Storage:  39.21 KB | Overwrites: Slot  50 | Hash Ops: 597458 | Time: 0.019s | ETA:  715.7s
[NODE-04] Block 151/500 | Index: 151 | Slot:  51 | Storage:  39.21 KB | Overwrites: Slot  51 | Hash Ops: 598336 | Time: 0.006s | ETA:  713.9s
[NODE-04] Block 152/500 | Index: 152 | Slot:  52 | Storage:  39.21 KB | Overwrites: Slot  52 | Hash Ops: 601635 | Time: 0.024s | ETA:  711.8s
[NODE-04] Block 153/500 | Index: 153 | Slot:  53 | Storage:  39.21 KB | Overwrites: Slot  53 | Hash Ops: 610021 | Time: 0.060s | ETA:  709.8s
[NODE-04] Block 154/500 | Index: 154 | Slot:  54 | Storage:  39.21 KB | Overwrites: Slot  54 | Hash Ops: 616455 | Time: 0.046s | ETA:  707.8s
[NODE-04] Block 155/500 | Index: 155 | Slot:  55 | Storage:  39.22 KB | Overwrites: Slot  55 | Hash Ops: 617740 | Time: 0.009s | ETA:  705.7s
[NODE-04] Block 156/500 | Index: 156 | Slot:  56 | Storage:  39.22 KB | Overwrites: Slot  56 | Hash Ops: 619715 | Time: 0.013s | ETA:  703.6s
[NODE-04] Block 157/500 | Index: 157 | Slot:  57 | Storage:  39.22 KB | Overwrites: Slot  57 | Hash Ops: 619937 | Time: 0.006s | ETA:  701.6s
[NODE-04] Block 158/500 | Index: 158 | Slot:  58 | Storage:  39.22 KB | Overwrites: Slot  58 | Hash Ops: 620082 | Time: 0.004s | ETA:  699.5s
[NODE-04] Block 159/500 | Index: 159 | Slot:  59 | Storage:  39.22 KB | Overwrites: Slot  59 | Hash Ops: 620594 | Time: 0.011s | ETA:  697.4s
[NODE-04] Block 160/500 | Index: 160 | Slot:  60 | Storage:  39.22 KB | Overwrites: Slot  60 | Hash Ops: 632112 | Time: 0.076s | ETA:  695.5s
[NODE-04] Block 161/500 | Index: 161 | Slot:  61 | Storage:  39.23 KB | Overwrites: Slot  61 | Hash Ops: 634609 | Time: 0.021s | ETA:  693.7s
[NODE-04] Block 162/500 | Index: 162 | Slot:  62 | Storage:  39.23 KB | Overwrites: Slot  62 | Hash Ops: 634813 | Time: 0.004s | ETA:  691.6s
[NODE-04] Block 163/500 | Index: 163 | Slot:  63 | Storage:  39.23 KB | Overwrites: Slot  63 | Hash Ops: 634958 | Time: 0.004s | ETA:  689.4s
[NODE-04] Block 164/500 | Index: 164 | Slot:  64 | Storage:  39.24 KB | Overwrites: Slot  64 | Hash Ops: 636501 | Time: 0.014s | ETA:  687.4s
[NODE-04] Block 165/500 | Index: 165 | Slot:  65 | Storage:  39.24 KB | Overwrites: Slot  65 | Hash Ops: 637428 | Time: 0.010s | ETA:  685.3s
[NODE-04] Block 166/500 | Index: 166 | Slot:  66 | Storage:  39.24 KB | Overwrites: Slot  66 | Hash Ops: 641442 | Time: 0.027s | ETA:  683.2s
[NODE-04] Block 167/500 | Index: 167 | Slot:  67 | Storage:  39.24 KB | Overwrites: Slot  67 | Hash Ops: 648910 | Time: 0.055s | ETA:  681.2s
[NODE-04] Block 168/500 | Index: 168 | Slot:  68 | Storage:  39.24 KB | Overwrites: Slot  68 | Hash Ops: 654012 | Time: 0.034s | ETA:  679.1s
[NODE-04] Block 169/500 | Index: 169 | Slot:  69 | Storage:  39.25 KB | Overwrites: Slot  69 | Hash Ops: 658444 | Time: 0.033s | ETA:  677.1s
[NODE-04] Block 170/500 | Index: 170 | Slot:  70 | Storage:  39.25 KB | Overwrites: Slot  70 | Hash Ops: 662235 | Time: 0.025s | ETA:  675.0s
[NODE-04] Block 171/500 | Index: 171 | Slot:  71 | Storage:  39.26 KB | Overwrites: Slot  71 | Hash Ops: 663718 | Time: 0.014s | ETA:  673.1s
[NODE-04] Block 172/500 | Index: 172 | Slot:  72 | Storage:  39.26 KB | Overwrites: Slot  72 | Hash Ops: 664698 | Time: 0.007s | ETA:  671.1s
[NODE-04] Block 173/500 | Index: 173 | Slot:  73 | Storage:  39.26 KB | Overwrites: Slot  73 | Hash Ops: 668635 | Time: 0.026s | ETA:  669.0s
[NODE-04] Block 174/500 | Index: 174 | Slot:  74 | Storage:  39.26 KB | Overwrites: Slot  74 | Hash Ops: 676183 | Time: 0.057s | ETA:  667.0s
[NODE-04] Block 175/500 | Index: 175 | Slot:  75 | Storage:  39.27 KB | Overwrites: Slot  75 | Hash Ops: 678570 | Time: 0.024s | ETA:  664.9s
[NODE-04] Block 176/500 | Index: 176 | Slot:  76 | Storage:  39.27 KB | Overwrites: Slot  76 | Hash Ops: 679155 | Time: 0.004s | ETA:  662.8s
[NODE-04] Block 177/500 | Index: 177 | Slot:  77 | Storage:  39.27 KB | Overwrites: Slot  77 | Hash Ops: 682190 | Time: 0.029s | ETA:  660.7s
[NODE-04] Block 178/500 | Index: 178 | Slot:  78 | Storage:  39.28 KB | Overwrites: Slot  78 | Hash Ops: 683266 | Time: 0.012s | ETA:  658.7s
[NODE-04] Block 179/500 | Index: 179 | Slot:  79 | Storage:  39.28 KB | Overwrites: Slot  79 | Hash Ops: 685208 | Time: 0.021s | ETA:  656.6s
[NODE-04] Block 180/500 | Index: 180 | Slot:  80 | Storage:  39.28 KB | Overwrites: Slot  80 | Hash Ops: 685769 | Time: 0.012s | ETA:  654.5s
[NODE-04] Block 181/500 | Index: 181 | Slot:  81 | Storage:  39.28 KB | Overwrites: Slot  81 | Hash Ops: 686438 | Time: 0.006s | ETA:  652.6s
[NODE-04] Block 182/500 | Index: 182 | Slot:  82 | Storage:  39.28 KB | Overwrites: Slot  82 | Hash Ops: 686905 | Time: 0.003s | ETA:  650.5s
[NODE-04] Block 183/500 | Index: 183 | Slot:  83 | Storage:  39.29 KB | Overwrites: Slot  83 | Hash Ops: 693446 | Time: 0.051s | ETA:  648.5s
[NODE-04] Block 184/500 | Index: 184 | Slot:  84 | Storage:  39.29 KB | Overwrites: Slot  84 | Hash Ops: 696588 | Time: 0.030s | ETA:  646.5s
[NODE-04] Block 185/500 | Index: 185 | Slot:  85 | Storage:  39.30 KB | Overwrites: Slot  85 | Hash Ops: 698052 | Time: 0.016s | ETA:  644.4s
[NODE-04] Block 186/500 | Index: 186 | Slot:  86 | Storage:  39.30 KB | Overwrites: Slot  86 | Hash Ops: 703005 | Time: 0.036s | ETA:  642.4s
[NODE-04] Block 187/500 | Index: 187 | Slot:  87 | Storage:  39.30 KB | Overwrites: Slot  87 | Hash Ops: 703207 | Time: 0.005s | ETA:  640.3s
[NODE-04] Block 188/500 | Index: 188 | Slot:  88 | Storage:  39.30 KB | Overwrites: Slot  88 | Hash Ops: 704778 | Time: 0.011s | ETA:  638.3s
[NODE-04] Block 189/500 | Index: 189 | Slot:  89 | Storage:  39.31 KB | Overwrites: Slot  89 | Hash Ops: 705757 | Time: 0.007s | ETA:  636.2s
[NODE-04] Block 190/500 | Index: 190 | Slot:  90 | Storage:  39.31 KB | Overwrites: Slot  90 | Hash Ops: 706967 | Time: 0.013s | ETA:  634.1s
[NODE-04] Block 191/500 | Index: 191 | Slot:  91 | Storage:  39.31 KB | Overwrites: Slot  91 | Hash Ops: 709086 | Time: 0.018s | ETA:  632.2s
[NODE-04] Block 192/500 | Index: 192 | Slot:  92 | Storage:  39.31 KB | Overwrites: Slot  92 | Hash Ops: 710992 | Time: 0.015s | ETA:  630.1s
[NODE-04] Block 193/500 | Index: 193 | Slot:  93 | Storage:  39.32 KB | Overwrites: Slot  93 | Hash Ops: 715346 | Time: 0.032s | ETA:  628.1s
[NODE-04] Block 194/500 | Index: 194 | Slot:  94 | Storage:  39.32 KB | Overwrites: Slot  94 | Hash Ops: 716371 | Time: 0.011s | ETA:  626.0s
[NODE-04] Block 195/500 | Index: 195 | Slot:  95 | Storage:  39.32 KB | Overwrites: Slot  95 | Hash Ops: 717044 | Time: 0.005s | ETA:  623.9s
[NODE-04] Block 196/500 | Index: 196 | Slot:  96 | Storage:  39.32 KB | Overwrites: Slot  96 | Hash Ops: 717970 | Time: 0.009s | ETA:  621.8s
[NODE-04] Block 197/500 | Index: 197 | Slot:  97 | Storage:  39.32 KB | Overwrites: Slot  97 | Hash Ops: 718934 | Time: 0.006s | ETA:  619.8s
[NODE-04] Block 198/500 | Index: 198 | Slot:  98 | Storage:  39.33 KB | Overwrites: Slot  98 | Hash Ops: 719069 | Time: 0.004s | ETA:  617.7s
[NODE-04] Block 199/500 | Index: 199 | Slot:  99 | Storage:  39.33 KB | Overwrites: Slot  99 | Hash Ops: 725608 | Time: 0.049s | ETA:  615.7s
[NODE-04] Block 200/500 | Index: 200 | Slot:   0 | Storage:  39.33 KB | Overwrites: Slot   0 | Hash Ops: 728094 | Time: 0.020s | ETA:  613.6s
[NODE-04] Block 201/500 | Index: 201 | Slot:   1 | Storage:  39.33 KB | Overwrites: Slot   1 | Hash Ops: 732237 | Time: 0.029s | ETA:  611.7s
[NODE-04] Block 202/500 | Index: 202 | Slot:   2 | Storage:  39.33 KB | Overwrites: Slot   2 | Hash Ops: 734107 | Time: 0.012s | ETA:  609.7s
[NODE-04] Block 203/500 | Index: 203 | Slot:   3 | Storage:  39.32 KB | Overwrites: Slot   3 | Hash Ops: 735307 | Time: 0.016s | ETA:  607.6s
[NODE-04] Block 204/500 | Index: 204 | Slot:   4 | Storage:  39.33 KB | Overwrites: Slot   4 | Hash Ops: 743782 | Time: 0.062s | ETA:  605.6s
[NODE-04] Block 205/500 | Index: 205 | Slot:   5 | Storage:  39.33 KB | Overwrites: Slot   5 | Hash Ops: 745051 | Time: 0.020s | ETA:  603.5s
[NODE-04] Block 206/500 | Index: 206 | Slot:   6 | Storage:  39.33 KB | Overwrites: Slot   6 | Hash Ops: 745261 | Time: 0.005s | ETA:  601.4s
[NODE-04] Block 207/500 | Index: 207 | Slot:   7 | Storage:  39.32 KB | Overwrites: Slot   7 | Hash Ops: 746454 | Time: 0.008s | ETA:  599.3s
[NODE-04] Block 208/500 | Index: 208 | Slot:   8 | Storage:  39.32 KB | Overwrites: Slot   8 | Hash Ops: 747032 | Time: 0.004s | ETA:  597.2s
[NODE-04] Block 209/500 | Index: 209 | Slot:   9 | Storage:  39.32 KB | Overwrites: Slot   9 | Hash Ops: 748026 | Time: 0.007s | ETA:  595.2s
[NODE-04] Block 210/500 | Index: 210 | Slot:  10 | Storage:  39.32 KB | Overwrites: Slot  10 | Hash Ops: 750506 | Time: 0.021s | ETA:  593.1s
[NODE-04] Block 211/500 | Index: 211 | Slot:  11 | Storage:  39.32 KB | Overwrites: Slot  11 | Hash Ops: 753347 | Time: 0.026s | ETA:  591.2s
[NODE-04] Block 212/500 | Index: 212 | Slot:  12 | Storage:  39.33 KB | Overwrites: Slot  12 | Hash Ops: 761475 | Time: 0.062s | ETA:  589.2s
[NODE-04] Block 213/500 | Index: 213 | Slot:  13 | Storage:  39.33 KB | Overwrites: Slot  13 | Hash Ops: 764315 | Time: 0.022s | ETA:  587.1s
[NODE-04] Block 214/500 | Index: 214 | Slot:  14 | Storage:  39.33 KB | Overwrites: Slot  14 | Hash Ops: 769087 | Time: 0.035s | ETA:  585.1s
[NODE-04] Block 215/500 | Index: 215 | Slot:  15 | Storage:  39.32 KB | Overwrites: Slot  15 | Hash Ops: 769386 | Time: 0.006s | ETA:  583.0s
[NODE-04] Block 216/500 | Index: 216 | Slot:  16 | Storage:  39.32 KB | Overwrites: Slot  16 | Hash Ops: 775877 | Time: 0.051s | ETA:  581.0s
[NODE-04] Block 217/500 | Index: 217 | Slot:  17 | Storage:  39.32 KB | Overwrites: Slot  17 | Hash Ops: 779062 | Time: 0.024s | ETA:  579.0s
[NODE-04] Block 218/500 | Index: 218 | Slot:  18 | Storage:  39.32 KB | Overwrites: Slot  18 | Hash Ops: 782436 | Time: 0.027s | ETA:  576.9s
[NODE-04] Block 219/500 | Index: 219 | Slot:  19 | Storage:  39.33 KB | Overwrites: Slot  19 | Hash Ops: 790058 | Time: 0.054s | ETA:  574.9s
[NODE-04] Block 220/500 | Index: 220 | Slot:  20 | Storage:  39.32 KB | Overwrites: Slot  20 | Hash Ops: 790239 | Time: 0.004s | ETA:  572.8s
[NODE-04] Block 221/500 | Index: 221 | Slot:  21 | Storage:  39.32 KB | Overwrites: Slot  21 | Hash Ops: 798744 | Time: 0.058s | ETA:  570.9s
[NODE-04] Block 222/500 | Index: 222 | Slot:  22 | Storage:  39.33 KB | Overwrites: Slot  22 | Hash Ops: 805228 | Time: 0.047s | ETA:  569.0s
[NODE-04] Block 223/500 | Index: 223 | Slot:  23 | Storage:  39.33 KB | Overwrites: Slot  23 | Hash Ops: 806786 | Time: 0.015s | ETA:  566.9s
[NODE-04] Block 224/500 | Index: 224 | Slot:  24 | Storage:  39.33 KB | Overwrites: Slot  24 | Hash Ops: 813521 | Time: 0.050s | ETA:  564.9s
[NODE-04] Block 225/500 | Index: 225 | Slot:  25 | Storage:  39.33 KB | Overwrites: Slot  25 | Hash Ops: 820741 | Time: 0.053s | ETA:  562.8s
[NODE-04] Block 226/500 | Index: 226 | Slot:  26 | Storage:  39.33 KB | Overwrites: Slot  26 | Hash Ops: 829011 | Time: 0.060s | ETA:  560.8s
[NODE-04] Block 227/500 | Index: 227 | Slot:  27 | Storage:  39.33 KB | Overwrites: Slot  27 | Hash Ops: 832482 | Time: 0.031s | ETA:  558.8s
[NODE-04] Block 228/500 | Index: 228 | Slot:  28 | Storage:  39.33 KB | Overwrites: Slot  28 | Hash Ops: 838187 | Time: 0.038s | ETA:  556.7s
[NODE-04] Block 229/500 | Index: 229 | Slot:  29 | Storage:  39.33 KB | Overwrites: Slot  29 | Hash Ops: 841757 | Time: 0.026s | ETA:  554.7s
[NODE-04] Block 230/500 | Index: 230 | Slot:  30 | Storage:  39.33 KB | Overwrites: Slot  30 | Hash Ops: 843152 | Time: 0.019s | ETA:  552.6s
[NODE-04] Block 231/500 | Index: 231 | Slot:  31 | Storage:  39.33 KB | Overwrites: Slot  31 | Hash Ops: 843751 | Time: 0.007s | ETA:  550.7s
[NODE-04] Block 232/500 | Index: 232 | Slot:  32 | Storage:  39.33 KB | Overwrites: Slot  32 | Hash Ops: 854831 | Time: 0.083s | ETA:  548.7s
[NODE-04] Block 233/500 | Index: 233 | Slot:  33 | Storage:  39.33 KB | Overwrites: Slot  33 | Hash Ops: 860203 | Time: 0.040s | ETA:  546.7s
[NODE-04] Block 234/500 | Index: 234 | Slot:  34 | Storage:  39.33 KB | Overwrites: Slot  34 | Hash Ops: 862532 | Time: 0.016s | ETA:  544.6s
[NODE-04] Block 235/500 | Index: 235 | Slot:  35 | Storage:  39.33 KB | Overwrites: Slot  35 | Hash Ops: 863306 | Time: 0.009s | ETA:  542.5s
[NODE-04] Block 236/500 | Index: 236 | Slot:  36 | Storage:  39.33 KB | Overwrites: Slot  36 | Hash Ops: 864776 | Time: 0.015s | ETA:  540.5s
[NODE-04] Block 237/500 | Index: 237 | Slot:  37 | Storage:  39.33 KB | Overwrites: Slot  37 | Hash Ops: 867527 | Time: 0.028s | ETA:  538.5s
[NODE-04] Block 238/500 | Index: 238 | Slot:  38 | Storage:  39.33 KB | Overwrites: Slot  38 | Hash Ops: 869150 | Time: 0.016s | ETA:  536.4s
[NODE-04] Block 239/500 | Index: 239 | Slot:  39 | Storage:  39.33 KB | Overwrites: Slot  39 | Hash Ops: 870053 | Time: 0.014s | ETA:  534.3s
[NODE-04] Block 240/500 | Index: 240 | Slot:  40 | Storage:  39.32 KB | Overwrites: Slot  40 | Hash Ops: 870068 | Time: 0.001s | ETA:  532.3s
[NODE-04] Block 241/500 | Index: 241 | Slot:  41 | Storage:  39.33 KB | Overwrites: Slot  41 | Hash Ops: 876527 | Time: 0.047s | ETA:  530.3s
[NODE-04] Block 242/500 | Index: 242 | Slot:  42 | Storage:  39.32 KB | Overwrites: Slot  42 | Hash Ops: 882304 | Time: 0.046s | ETA:  528.3s
[NODE-04] Block 243/500 | Index: 243 | Slot:  43 | Storage:  39.32 KB | Overwrites: Slot  43 | Hash Ops: 882654 | Time: 0.009s | ETA:  526.2s
[NODE-04] Block 244/500 | Index: 244 | Slot:  44 | Storage:  39.32 KB | Overwrites: Slot  44 | Hash Ops: 884492 | Time: 0.016s | ETA:  524.1s
[NODE-04] Block 245/500 | Index: 245 | Slot:  45 | Storage:  39.32 KB | Overwrites: Slot  45 | Hash Ops: 885570 | Time: 0.011s | ETA:  522.1s
[NODE-04] Block 246/500 | Index: 246 | Slot:  46 | Storage:  39.32 KB | Overwrites: Slot  46 | Hash Ops: 887437 | Time: 0.016s | ETA:  520.0s
[NODE-04] Block 247/500 | Index: 247 | Slot:  47 | Storage:  39.32 KB | Overwrites: Slot  47 | Hash Ops: 891520 | Time: 0.028s | ETA:  517.9s
[NODE-04] Block 248/500 | Index: 248 | Slot:  48 | Storage:  39.32 KB | Overwrites: Slot  48 | Hash Ops: 893335 | Time: 0.016s | ETA:  515.9s
[NODE-04] Block 249/500 | Index: 249 | Slot:  49 | Storage:  39.32 KB | Overwrites: Slot  49 | Hash Ops: 896565 | Time: 0.025s | ETA:  513.8s
[NODE-04] Block 250/500 | Index: 250 | Slot:  50 | Storage:  39.32 KB | Overwrites: Slot  50 | Hash Ops: 902226 | Time: 0.038s | ETA:  511.8s
[NODE-04] Block 251/500 | Index: 251 | Slot:  51 | Storage:  39.33 KB | Overwrites: Slot  51 | Hash Ops: 903951 | Time: 0.012s | ETA:  509.8s
[NODE-04] Block 252/500 | Index: 252 | Slot:  52 | Storage:  39.33 KB | Overwrites: Slot  52 | Hash Ops: 906428 | Time: 0.017s | ETA:  507.7s
[NODE-04] Block 253/500 | Index: 253 | Slot:  53 | Storage:  39.33 KB | Overwrites: Slot  53 | Hash Ops: 909258 | Time: 0.019s | ETA:  505.7s
[NODE-04] Block 254/500 | Index: 254 | Slot:  54 | Storage:  39.33 KB | Overwrites: Slot  54 | Hash Ops: 911914 | Time: 0.018s | ETA:  503.6s
[NODE-04] Block 255/500 | Index: 255 | Slot:  55 | Storage:  39.33 KB | Overwrites: Slot  55 | Hash Ops: 913921 | Time: 0.019s | ETA:  501.6s
[NODE-04] Block 256/500 | Index: 256 | Slot:  56 | Storage:  39.33 KB | Overwrites: Slot  56 | Hash Ops: 917215 | Time: 0.028s | ETA:  499.5s
[NODE-04] Block 257/500 | Index: 257 | Slot:  57 | Storage:  39.33 KB | Overwrites: Slot  57 | Hash Ops: 919192 | Time: 0.017s | ETA:  497.5s
[NODE-04] Block 258/500 | Index: 258 | Slot:  58 | Storage:  39.33 KB | Overwrites: Slot  58 | Hash Ops: 926768 | Time: 0.054s | ETA:  495.5s
[NODE-04] Block 259/500 | Index: 259 | Slot:  59 | Storage:  39.33 KB | Overwrites: Slot  59 | Hash Ops: 927220 | Time: 0.010s | ETA:  493.7s
[NODE-04] Block 260/500 | Index: 260 | Slot:  60 | Storage:  39.33 KB | Overwrites: Slot  60 | Hash Ops: 928712 | Time: 0.011s | ETA:  491.6s
[NODE-04] Block 261/500 | Index: 261 | Slot:  61 | Storage:  39.33 KB | Overwrites: Slot  61 | Hash Ops: 934540 | Time: 0.043s | ETA:  489.6s
[NODE-04] Block 262/500 | Index: 262 | Slot:  62 | Storage:  39.33 KB | Overwrites: Slot  62 | Hash Ops: 934781 | Time: 0.003s | ETA:  487.5s
[NODE-04] Block 263/500 | Index: 263 | Slot:  63 | Storage:  39.33 KB | Overwrites: Slot  63 | Hash Ops: 935089 | Time: 0.002s | ETA:  485.5s
[NODE-04] Block 264/500 | Index: 264 | Slot:  64 | Storage:  39.33 KB | Overwrites: Slot  64 | Hash Ops: 938307 | Time: 0.022s | ETA:  483.4s
[NODE-04] Block 265/500 | Index: 265 | Slot:  65 | Storage:  39.33 KB | Overwrites: Slot  65 | Hash Ops: 939607 | Time: 0.011s | ETA:  481.3s
[NODE-04] Block 266/500 | Index: 266 | Slot:  66 | Storage:  39.34 KB | Overwrites: Slot  66 | Hash Ops: 943121 | Time: 0.024s | ETA:  479.3s
[NODE-04] Block 267/500 | Index: 267 | Slot:  67 | Storage:  39.34 KB | Overwrites: Slot  67 | Hash Ops: 943401 | Time: 0.002s | ETA:  477.2s
[NODE-04] Block 268/500 | Index: 268 | Slot:  68 | Storage:  39.34 KB | Overwrites: Slot  68 | Hash Ops: 946625 | Time: 0.029s | ETA:  475.2s
[NODE-04] Block 269/500 | Index: 269 | Slot:  69 | Storage:  39.34 KB | Overwrites: Slot  69 | Hash Ops: 947129 | Time: 0.009s | ETA:  473.1s
[NODE-04] Block 270/500 | Index: 270 | Slot:  70 | Storage:  39.33 KB | Overwrites: Slot  70 | Hash Ops: 947743 | Time: 0.006s | ETA:  471.0s
[NODE-04] Block 271/500 | Index: 271 | Slot:  71 | Storage:  39.33 KB | Overwrites: Slot  71 | Hash Ops: 966210 | Time: 0.128s | ETA:  469.2s
[NODE-04] Block 272/500 | Index: 272 | Slot:  72 | Storage:  39.34 KB | Overwrites: Slot  72 | Hash Ops: 980170 | Time: 0.097s | ETA:  467.3s
[NODE-04] Block 273/500 | Index: 273 | Slot:  73 | Storage:  39.33 KB | Overwrites: Slot  73 | Hash Ops: 984331 | Time: 0.027s | ETA:  465.2s
[NODE-04] Block 274/500 | Index: 274 | Slot:  74 | Storage:  39.33 KB | Overwrites: Slot  74 | Hash Ops: 987298 | Time: 0.023s | ETA:  463.1s
[NODE-04] Block 275/500 | Index: 275 | Slot:  75 | Storage:  39.33 KB | Overwrites: Slot  75 | Hash Ops: 988729 | Time: 0.013s | ETA:  461.1s
[NODE-04] Block 276/500 | Index: 276 | Slot:  76 | Storage:  39.33 KB | Overwrites: Slot  76 | Hash Ops: 993480 | Time: 0.032s | ETA:  459.0s
[NODE-04] Block 277/500 | Index: 277 | Slot:  77 | Storage:  39.33 KB | Overwrites: Slot  77 | Hash Ops: 994926 | Time: 0.013s | ETA:  456.9s
[NODE-04] Block 278/500 | Index: 278 | Slot:  78 | Storage:  39.33 KB | Overwrites: Slot  78 | Hash Ops: 1004476 | Time: 0.066s | ETA:  454.9s
[NODE-04] Block 279/500 | Index: 279 | Slot:  79 | Storage:  39.33 KB | Overwrites: Slot  79 | Hash Ops: 1004842 | Time: 0.003s | ETA:  452.9s
[NODE-04] Block 280/500 | Index: 280 | Slot:  80 | Storage:  39.33 KB | Overwrites: Slot  80 | Hash Ops: 1004880 | Time: 0.002s | ETA:  450.8s
[NODE-04] Block 281/500 | Index: 281 | Slot:  81 | Storage:  39.33 KB | Overwrites: Slot  81 | Hash Ops: 1006090 | Time: 0.015s | ETA:  448.9s
[NODE-04] Block 282/500 | Index: 282 | Slot:  82 | Storage:  39.34 KB | Overwrites: Slot  82 | Hash Ops: 1018693 | Time: 0.084s | ETA:  446.9s
[NODE-04] Block 283/500 | Index: 283 | Slot:  83 | Storage:  39.34 KB | Overwrites: Slot  83 | Hash Ops: 1019796 | Time: 0.011s | ETA:  444.8s
[NODE-04] Block 284/500 | Index: 284 | Slot:  84 | Storage:  39.34 KB | Overwrites: Slot  84 | Hash Ops: 1041328 | Time: 0.153s | ETA:  442.8s
[NODE-04] Block 285/500 | Index: 285 | Slot:  85 | Storage:  39.34 KB | Overwrites: Slot  85 | Hash Ops: 1044930 | Time: 0.027s | ETA:  440.8s
[NODE-04] Block 286/500 | Index: 286 | Slot:  86 | Storage:  39.34 KB | Overwrites: Slot  86 | Hash Ops: 1051573 | Time: 0.048s | ETA:  438.7s
[NODE-04] Block 287/500 | Index: 287 | Slot:  87 | Storage:  39.34 KB | Overwrites: Slot  87 | Hash Ops: 1053768 | Time: 0.019s | ETA:  436.7s
[NODE-04] Block 288/500 | Index: 288 | Slot:  88 | Storage:  39.34 KB | Overwrites: Slot  88 | Hash Ops: 1061317 | Time: 0.055s | ETA:  434.6s
[NODE-04] Block 289/500 | Index: 289 | Slot:  89 | Storage:  39.34 KB | Overwrites: Slot  89 | Hash Ops: 1090199 | Time: 0.191s | ETA:  432.7s
[NODE-04] Block 290/500 | Index: 290 | Slot:  90 | Storage:  39.34 KB | Overwrites: Slot  90 | Hash Ops: 1101736 | Time: 0.080s | ETA:  430.7s
[NODE-04] Block 291/500 | Index: 291 | Slot:  91 | Storage:  39.34 KB | Overwrites: Slot  91 | Hash Ops: 1107583 | Time: 0.044s | ETA:  428.7s
[NODE-04] Block 292/500 | Index: 292 | Slot:  92 | Storage:  39.34 KB | Overwrites: Slot  92 | Hash Ops: 1111788 | Time: 0.029s | ETA:  426.7s
[NODE-04] Block 293/500 | Index: 293 | Slot:  93 | Storage:  39.34 KB | Overwrites: Slot  93 | Hash Ops: 1118806 | Time: 0.051s | ETA:  424.6s
[NODE-04] Block 294/500 | Index: 294 | Slot:  94 | Storage:  39.34 KB | Overwrites: Slot  94 | Hash Ops: 1124908 | Time: 0.041s | ETA:  422.6s
[NODE-04] Block 295/500 | Index: 295 | Slot:  95 | Storage:  39.34 KB | Overwrites: Slot  95 | Hash Ops: 1125794 | Time: 0.010s | ETA:  420.5s
[NODE-04] Block 296/500 | Index: 296 | Slot:  96 | Storage:  39.34 KB | Overwrites: Slot  96 | Hash Ops: 1126088 | Time: 0.003s | ETA:  418.4s
[NODE-04] Block 297/500 | Index: 297 | Slot:  97 | Storage:  39.34 KB | Overwrites: Slot  97 | Hash Ops: 1129911 | Time: 0.030s | ETA:  416.4s
[NODE-04] Block 298/500 | Index: 298 | Slot:  98 | Storage:  39.34 KB | Overwrites: Slot  98 | Hash Ops: 1133756 | Time: 0.026s | ETA:  414.3s
[NODE-04] Block 299/500 | Index: 299 | Slot:  99 | Storage:  39.34 KB | Overwrites: Slot  99 | Hash Ops: 1139201 | Time: 0.040s | ETA:  412.2s
[NODE-04] Block 300/500 | Index: 300 | Slot:   0 | Storage:  39.34 KB | Overwrites: Slot   0 | Hash Ops: 1140773 | Time: 0.011s | ETA:  410.2s
[NODE-04] Block 301/500 | Index: 301 | Slot:   1 | Storage:  39.34 KB | Overwrites: Slot   1 | Hash Ops: 1147380 | Time: 0.046s | ETA:  408.2s
[NODE-04] Block 302/500 | Index: 302 | Slot:   2 | Storage:  39.34 KB | Overwrites: Slot   2 | Hash Ops: 1147457 | Time: 0.001s | ETA:  406.2s
[NODE-04] Block 303/500 | Index: 303 | Slot:   3 | Storage:  39.34 KB | Overwrites: Slot   3 | Hash Ops: 1150837 | Time: 0.056s | ETA:  404.1s
[NODE-04] Block 304/500 | Index: 304 | Slot:   4 | Storage:  39.34 KB | Overwrites: Slot   4 | Hash Ops: 1151386 | Time: 0.004s | ETA:  402.1s
[NODE-04] Block 305/500 | Index: 305 | Slot:   5 | Storage:  39.34 KB | Overwrites: Slot   5 | Hash Ops: 1153059 | Time: 0.017s | ETA:  400.0s
[NODE-04] Block 306/500 | Index: 306 | Slot:   6 | Storage:  39.34 KB | Overwrites: Slot   6 | Hash Ops: 1159936 | Time: 0.065s | ETA:  398.0s
[NODE-04] Block 307/500 | Index: 307 | Slot:   7 | Storage:  39.34 KB | Overwrites: Slot   7 | Hash Ops: 1160417 | Time: 0.013s | ETA:  395.9s
[NODE-04] Block 308/500 | Index: 308 | Slot:   8 | Storage:  39.34 KB | Overwrites: Slot   8 | Hash Ops: 1178446 | Time: 0.162s | ETA:  393.9s
[NODE-04] Block 309/500 | Index: 309 | Slot:   9 | Storage:  39.34 KB | Overwrites: Slot   9 | Hash Ops: 1183008 | Time: 0.033s | ETA:  391.9s
[NODE-04] Block 310/500 | Index: 310 | Slot:  10 | Storage:  39.34 KB | Overwrites: Slot  10 | Hash Ops: 1183587 | Time: 0.015s | ETA:  389.8s
[NODE-04] Block 311/500 | Index: 311 | Slot:  11 | Storage:  39.34 KB | Overwrites: Slot  11 | Hash Ops: 1187199 | Time: 0.054s | ETA:  387.9s
[NODE-04] Block 312/500 | Index: 312 | Slot:  12 | Storage:  39.34 KB | Overwrites: Slot  12 | Hash Ops: 1194535 | Time: 0.063s | ETA:  385.9s
[NODE-04] Block 313/500 | Index: 313 | Slot:  13 | Storage:  39.34 KB | Overwrites: Slot  13 | Hash Ops: 1197915 | Time: 0.035s | ETA:  383.8s
[NODE-04] Block 314/500 | Index: 314 | Slot:  14 | Storage:  39.34 KB | Overwrites: Slot  14 | Hash Ops: 1203404 | Time: 0.039s | ETA:  381.8s
[NODE-04] Block 315/500 | Index: 315 | Slot:  15 | Storage:  39.34 KB | Overwrites: Slot  15 | Hash Ops: 1212212 | Time: 0.084s | ETA:  379.7s
[NODE-04] Block 316/500 | Index: 316 | Slot:  16 | Storage:  39.34 KB | Overwrites: Slot  16 | Hash Ops: 1215750 | Time: 0.025s | ETA:  377.7s
[NODE-04] Block 317/500 | Index: 317 | Slot:  17 | Storage:  39.34 KB | Overwrites: Slot  17 | Hash Ops: 1218418 | Time: 0.029s | ETA:  375.6s
[NODE-04] Block 318/500 | Index: 318 | Slot:  18 | Storage:  39.34 KB | Overwrites: Slot  18 | Hash Ops: 1220296 | Time: 0.016s | ETA:  373.5s
[NODE-04] Block 319/500 | Index: 319 | Slot:  19 | Storage:  39.35 KB | Overwrites: Slot  19 | Hash Ops: 1224882 | Time: 0.034s | ETA:  371.5s
[NODE-04] Block 320/500 | Index: 320 | Slot:  20 | Storage:  39.35 KB | Overwrites: Slot  20 | Hash Ops: 1226783 | Time: 0.022s | ETA:  369.4s
[NODE-04] Block 321/500 | Index: 321 | Slot:  21 | Storage:  39.35 KB | Overwrites: Slot  21 | Hash Ops: 1231736 | Time: 0.058s | ETA:  367.5s
[NODE-04] Block 322/500 | Index: 322 | Slot:  22 | Storage:  39.35 KB | Overwrites: Slot  22 | Hash Ops: 1237124 | Time: 0.056s | ETA:  365.4s
[NODE-04] Block 323/500 | Index: 323 | Slot:  23 | Storage:  39.35 KB | Overwrites: Slot  23 | Hash Ops: 1241593 | Time: 0.039s | ETA:  363.4s
[NODE-04] Block 324/500 | Index: 324 | Slot:  24 | Storage:  39.35 KB | Overwrites: Slot  24 | Hash Ops: 1245163 | Time: 0.044s | ETA:  361.3s
[NODE-04] Block 325/500 | Index: 325 | Slot:  25 | Storage:  39.35 KB | Overwrites: Slot  25 | Hash Ops: 1246407 | Time: 0.011s | ETA:  359.2s
[NODE-04] Block 326/500 | Index: 326 | Slot:  26 | Storage:  39.35 KB | Overwrites: Slot  26 | Hash Ops: 1246680 | Time: 0.003s | ETA:  357.2s
[NODE-04] Block 327/500 | Index: 327 | Slot:  27 | Storage:  39.35 KB | Overwrites: Slot  27 | Hash Ops: 1247979 | Time: 0.019s | ETA:  355.1s
[NODE-04] Block 328/500 | Index: 328 | Slot:  28 | Storage:  39.35 KB | Overwrites: Slot  28 | Hash Ops: 1249962 | Time: 0.027s | ETA:  353.0s
[NODE-04] Block 329/500 | Index: 329 | Slot:  29 | Storage:  39.35 KB | Overwrites: Slot  29 | Hash Ops: 1250229 | Time: 0.009s | ETA:  351.0s
[NODE-04] Block 330/500 | Index: 330 | Slot:  30 | Storage:  39.35 KB | Overwrites: Slot  30 | Hash Ops: 1253235 | Time: 0.022s | ETA:  348.9s
[NODE-04] Block 331/500 | Index: 331 | Slot:  31 | Storage:  39.34 KB | Overwrites: Slot  31 | Hash Ops: 1253644 | Time: 0.010s | ETA:  346.9s
[NODE-04] Block 332/500 | Index: 332 | Slot:  32 | Storage:  39.34 KB | Overwrites: Slot  32 | Hash Ops: 1253685 | Time: 0.001s | ETA:  344.8s
[NODE-04] Block 333/500 | Index: 333 | Slot:  33 | Storage:  39.34 KB | Overwrites: Slot  33 | Hash Ops: 1258190 | Time: 0.046s | ETA:  342.8s
[NODE-04] Block 334/500 | Index: 334 | Slot:  34 | Storage:  39.34 KB | Overwrites: Slot  34 | Hash Ops: 1264760 | Time: 0.075s | ETA:  340.8s
[NODE-04] Block 335/500 | Index: 335 | Slot:  35 | Storage:  39.34 KB | Overwrites: Slot  35 | Hash Ops: 1264940 | Time: 0.006s | ETA:  338.7s
[NODE-04] Block 336/500 | Index: 336 | Slot:  36 | Storage:  39.34 KB | Overwrites: Slot  36 | Hash Ops: 1267050 | Time: 0.042s | ETA:  336.7s
[NODE-04] Block 337/500 | Index: 337 | Slot:  37 | Storage:  39.34 KB | Overwrites: Slot  37 | Hash Ops: 1268626 | Time: 0.029s | ETA:  334.6s
[NODE-04] Block 338/500 | Index: 338 | Slot:  38 | Storage:  39.34 KB | Overwrites: Slot  38 | Hash Ops: 1270641 | Time: 0.033s | ETA:  332.5s
[NODE-04] Block 339/500 | Index: 339 | Slot:  39 | Storage:  39.34 KB | Overwrites: Slot  39 | Hash Ops: 1273470 | Time: 0.030s | ETA:  330.5s
[NODE-04] Block 340/500 | Index: 340 | Slot:  40 | Storage:  39.34 KB | Overwrites: Slot  40 | Hash Ops: 1278556 | Time: 0.057s | ETA:  328.4s
[NODE-04] Block 341/500 | Index: 341 | Slot:  41 | Storage:  39.34 KB | Overwrites: Slot  41 | Hash Ops: 1280492 | Time: 0.020s | ETA:  326.4s
[NODE-04] Block 342/500 | Index: 342 | Slot:  42 | Storage:  39.35 KB | Overwrites: Slot  42 | Hash Ops: 1286505 | Time: 0.049s | ETA:  324.4s
[NODE-04] Block 343/500 | Index: 343 | Slot:  43 | Storage:  39.35 KB | Overwrites: Slot  43 | Hash Ops: 1297606 | Time: 0.093s | ETA:  322.4s
[NODE-04] Block 344/500 | Index: 344 | Slot:  44 | Storage:  39.35 KB | Overwrites: Slot  44 | Hash Ops: 1299511 | Time: 0.016s | ETA:  320.3s
[NODE-04] Block 345/500 | Index: 345 | Slot:  45 | Storage:  39.35 KB | Overwrites: Slot  45 | Hash Ops: 1300519 | Time: 0.031s | ETA:  318.2s
[NODE-04] Block 346/500 | Index: 346 | Slot:  46 | Storage:  39.35 KB | Overwrites: Slot  46 | Hash Ops: 1303502 | Time: 0.045s | ETA:  316.2s
[NODE-04] Block 347/500 | Index: 347 | Slot:  47 | Storage:  39.35 KB | Overwrites: Slot  47 | Hash Ops: 1305622 | Time: 0.021s | ETA:  314.1s
[NODE-04] Block 348/500 | Index: 348 | Slot:  48 | Storage:  39.35 KB | Overwrites: Slot  48 | Hash Ops: 1305828 | Time: 0.007s | ETA:  312.0s
[NODE-04] Block 349/500 | Index: 349 | Slot:  49 | Storage:  39.35 KB | Overwrites: Slot  49 | Hash Ops: 1309139 | Time: 0.039s | ETA:  310.0s
[NODE-04] Block 350/500 | Index: 350 | Slot:  50 | Storage:  39.35 KB | Overwrites: Slot  50 | Hash Ops: 1314960 | Time: 0.062s | ETA:  307.9s
[NODE-04] Block 351/500 | Index: 351 | Slot:  51 | Storage:  39.35 KB | Overwrites: Slot  51 | Hash Ops: 1315124 | Time: 0.005s | ETA:  305.9s
[NODE-04] Block 352/500 | Index: 352 | Slot:  52 | Storage:  39.35 KB | Overwrites: Slot  52 | Hash Ops: 1317640 | Time: 0.032s | ETA:  303.8s
[NODE-04] Block 353/500 | Index: 353 | Slot:  53 | Storage:  39.35 KB | Overwrites: Slot  53 | Hash Ops: 1318438 | Time: 0.008s | ETA:  301.8s
[NODE-04] Block 354/500 | Index: 354 | Slot:  54 | Storage:  39.35 KB | Overwrites: Slot  54 | Hash Ops: 1319222 | Time: 0.016s | ETA:  299.7s
[NODE-04] Block 355/500 | Index: 355 | Slot:  55 | Storage:  39.35 KB | Overwrites: Slot  55 | Hash Ops: 1320930 | Time: 0.019s | ETA:  297.7s
[NODE-04] Block 356/500 | Index: 356 | Slot:  56 | Storage:  39.35 KB | Overwrites: Slot  56 | Hash Ops: 1334846 | Time: 0.118s | ETA:  295.6s
[NODE-04] Block 357/500 | Index: 357 | Slot:  57 | Storage:  39.35 KB | Overwrites: Slot  57 | Hash Ops: 1336170 | Time: 0.022s | ETA:  293.6s
[NODE-04] Block 358/500 | Index: 358 | Slot:  58 | Storage:  39.35 KB | Overwrites: Slot  58 | Hash Ops: 1340613 | Time: 0.037s | ETA:  291.5s
[NODE-04] Block 359/500 | Index: 359 | Slot:  59 | Storage:  39.35 KB | Overwrites: Slot  59 | Hash Ops: 1342777 | Time: 0.043s | ETA:  289.5s
[NODE-04] Block 360/500 | Index: 360 | Slot:  60 | Storage:  39.35 KB | Overwrites: Slot  60 | Hash Ops: 1348562 | Time: 0.041s | ETA:  287.4s
[NODE-04] Block 361/500 | Index: 361 | Slot:  61 | Storage:  39.35 KB | Overwrites: Slot  61 | Hash Ops: 1356363 | Time: 0.085s | ETA:  285.4s
[NODE-04] Block 362/500 | Index: 362 | Slot:  62 | Storage:  39.35 KB | Overwrites: Slot  62 | Hash Ops: 1366570 | Time: 0.090s | ETA:  283.4s
[NODE-04] Block 363/500 | Index: 363 | Slot:  63 | Storage:  39.35 KB | Overwrites: Slot  63 | Hash Ops: 1372024 | Time: 0.052s | ETA:  281.4s
[NODE-04] Block 364/500 | Index: 364 | Slot:  64 | Storage:  39.35 KB | Overwrites: Slot  64 | Hash Ops: 1385019 | Time: 0.120s | ETA:  279.3s
[NODE-04] Block 365/500 | Index: 365 | Slot:  65 | Storage:  39.35 KB | Overwrites: Slot  65 | Hash Ops: 1388269 | Time: 0.038s | ETA:  277.3s
[NODE-04] Block 366/500 | Index: 366 | Slot:  66 | Storage:  39.35 KB | Overwrites: Slot  66 | Hash Ops: 1393977 | Time: 0.054s | ETA:  275.2s
[NODE-04] Block 367/500 | Index: 367 | Slot:  67 | Storage:  39.35 KB | Overwrites: Slot  67 | Hash Ops: 1395311 | Time: 0.013s | ETA:  273.2s
[NODE-04] Block 368/500 | Index: 368 | Slot:  68 | Storage:  39.35 KB | Overwrites: Slot  68 | Hash Ops: 1403985 | Time: 0.062s | ETA:  271.1s
[NODE-04] Block 369/500 | Index: 369 | Slot:  69 | Storage:  39.35 KB | Overwrites: Slot  69 | Hash Ops: 1404198 | Time: 0.007s | ETA:  269.1s
[NODE-04] Block 370/500 | Index: 370 | Slot:  70 | Storage:  39.35 KB | Overwrites: Slot  70 | Hash Ops: 1404970 | Time: 0.020s | ETA:  267.0s
[NODE-04] Block 371/500 | Index: 371 | Slot:  71 | Storage:  39.35 KB | Overwrites: Slot  71 | Hash Ops: 1413159 | Time: 0.080s | ETA:  265.0s
[NODE-04] Block 372/500 | Index: 372 | Slot:  72 | Storage:  39.35 KB | Overwrites: Slot  72 | Hash Ops: 1416646 | Time: 0.036s | ETA:  262.9s
[NODE-04] Block 373/500 | Index: 373 | Slot:  73 | Storage:  39.35 KB | Overwrites: Slot  73 | Hash Ops: 1418765 | Time: 0.027s | ETA:  260.9s
[NODE-04] Block 374/500 | Index: 374 | Slot:  74 | Storage:  39.35 KB | Overwrites: Slot  74 | Hash Ops: 1427753 | Time: 0.082s | ETA:  258.9s
[NODE-04] Block 375/500 | Index: 375 | Slot:  75 | Storage:  39.35 KB | Overwrites: Slot  75 | Hash Ops: 1431050 | Time: 0.029s | ETA:  256.8s
[NODE-04] Block 376/500 | Index: 376 | Slot:  76 | Storage:  39.35 KB | Overwrites: Slot  76 | Hash Ops: 1437986 | Time: 0.060s | ETA:  254.8s
[NODE-04] Block 377/500 | Index: 377 | Slot:  77 | Storage:  39.35 KB | Overwrites: Slot  77 | Hash Ops: 1438269 | Time: 0.006s | ETA:  252.7s
[NODE-04] Block 378/500 | Index: 378 | Slot:  78 | Storage:  39.35 KB | Overwrites: Slot  78 | Hash Ops: 1440720 | Time: 0.022s | ETA:  250.6s
[NODE-04] Block 379/500 | Index: 379 | Slot:  79 | Storage:  39.35 KB | Overwrites: Slot  79 | Hash Ops: 1444603 | Time: 0.030s | ETA:  248.6s
[NODE-04] Block 380/500 | Index: 380 | Slot:  80 | Storage:  39.36 KB | Overwrites: Slot  80 | Hash Ops: 1454722 | Time: 0.073s | ETA:  246.6s
[NODE-04] Block 381/500 | Index: 381 | Slot:  81 | Storage:  39.35 KB | Overwrites: Slot  81 | Hash Ops: 1454875 | Time: 0.001s | ETA:  244.5s
[NODE-04] Block 382/500 | Index: 382 | Slot:  82 | Storage:  39.35 KB | Overwrites: Slot  82 | Hash Ops: 1457432 | Time: 0.041s | ETA:  242.5s
[NODE-04] Block 383/500 | Index: 383 | Slot:  83 | Storage:  39.35 KB | Overwrites: Slot  83 | Hash Ops: 1472592 | Time: 0.133s | ETA:  240.4s
[NODE-04] Block 384/500 | Index: 384 | Slot:  84 | Storage:  39.35 KB | Overwrites: Slot  84 | Hash Ops: 1474674 | Time: 0.020s | ETA:  238.4s
[NODE-04] Block 385/500 | Index: 385 | Slot:  85 | Storage:  39.35 KB | Overwrites: Slot  85 | Hash Ops: 1480661 | Time: 0.057s | ETA:  236.3s
[NODE-04] Block 386/500 | Index: 386 | Slot:  86 | Storage:  39.35 KB | Overwrites: Slot  86 | Hash Ops: 1485432 | Time: 0.056s | ETA:  234.3s
[NODE-04] Block 387/500 | Index: 387 | Slot:  87 | Storage:  39.35 KB | Overwrites: Slot  87 | Hash Ops: 1487386 | Time: 0.029s | ETA:  232.2s
[NODE-04] Block 388/500 | Index: 388 | Slot:  88 | Storage:  39.35 KB | Overwrites: Slot  88 | Hash Ops: 1488916 | Time: 0.015s | ETA:  230.2s
[NODE-04] Block 389/500 | Index: 389 | Slot:  89 | Storage:  39.35 KB | Overwrites: Slot  89 | Hash Ops: 1505196 | Time: 0.143s | ETA:  228.1s
[NODE-04] Block 390/500 | Index: 390 | Slot:  90 | Storage:  39.35 KB | Overwrites: Slot  90 | Hash Ops: 1511212 | Time: 0.052s | ETA:  226.1s
[NODE-04] Block 391/500 | Index: 391 | Slot:  91 | Storage:  39.35 KB | Overwrites: Slot  91 | Hash Ops: 1511785 | Time: 0.013s | ETA:  224.1s
[NODE-04] Block 392/500 | Index: 392 | Slot:  92 | Storage:  39.35 KB | Overwrites: Slot  92 | Hash Ops: 1514106 | Time: 0.033s | ETA:  222.0s
[NODE-04] Block 393/500 | Index: 393 | Slot:  93 | Storage:  39.35 KB | Overwrites: Slot  93 | Hash Ops: 1516160 | Time: 0.016s | ETA:  219.9s
[NODE-04] Block 394/500 | Index: 394 | Slot:  94 | Storage:  39.35 KB | Overwrites: Slot  94 | Hash Ops: 1525573 | Time: 0.081s | ETA:  217.9s
[NODE-04] Block 395/500 | Index: 395 | Slot:  95 | Storage:  39.35 KB | Overwrites: Slot  95 | Hash Ops: 1529762 | Time: 0.029s | ETA:  215.8s
[NODE-04] Block 396/500 | Index: 396 | Slot:  96 | Storage:  39.35 KB | Overwrites: Slot  96 | Hash Ops: 1534029 | Time: 0.044s | ETA:  213.8s
[NODE-04] Block 397/500 | Index: 397 | Slot:  97 | Storage:  39.35 KB | Overwrites: Slot  97 | Hash Ops: 1536494 | Time: 0.023s | ETA:  211.7s
[NODE-04] Block 398/500 | Index: 398 | Slot:  98 | Storage:  39.35 KB | Overwrites: Slot  98 | Hash Ops: 1543878 | Time: 0.081s | ETA:  209.7s
[NODE-04] Block 399/500 | Index: 399 | Slot:  99 | Storage:  39.36 KB | Overwrites: Slot  99 | Hash Ops: 1544546 | Time: 0.015s | ETA:  207.6s
[NODE-04] Block 400/500 | Index: 400 | Slot:   0 | Storage:  39.36 KB | Overwrites: Slot   0 | Hash Ops: 1554272 | Time: 0.086s | ETA:  205.6s
[NODE-04] Block 401/500 | Index: 401 | Slot:   1 | Storage:  39.35 KB | Overwrites: Slot   1 | Hash Ops: 1558666 | Time: 0.049s | ETA:  203.5s
[NODE-04] Block 402/500 | Index: 402 | Slot:   2 | Storage:  39.36 KB | Overwrites: Slot   2 | Hash Ops: 1563480 | Time: 0.055s | ETA:  201.5s
[NODE-04] Block 403/500 | Index: 403 | Slot:   3 | Storage:  39.36 KB | Overwrites: Slot   3 | Hash Ops: 1563560 | Time: 0.003s | ETA:  199.4s
[NODE-04] Block 404/500 | Index: 404 | Slot:   4 | Storage:  39.36 KB | Overwrites: Slot   4 | Hash Ops: 1564416 | Time: 0.016s | ETA:  197.3s
[NODE-04] Block 405/500 | Index: 405 | Slot:   5 | Storage:  39.36 KB | Overwrites: Slot   5 | Hash Ops: 1564688 | Time: 0.007s | ETA:  195.3s
[NODE-04] Block 406/500 | Index: 406 | Slot:   6 | Storage:  39.36 KB | Overwrites: Slot   6 | Hash Ops: 1569367 | Time: 0.043s | ETA:  193.2s
[NODE-04] Block 407/500 | Index: 407 | Slot:   7 | Storage:  39.36 KB | Overwrites: Slot   7 | Hash Ops: 1575801 | Time: 0.060s | ETA:  191.2s
[NODE-04] Block 408/500 | Index: 408 | Slot:   8 | Storage:  39.36 KB | Overwrites: Slot   8 | Hash Ops: 1579162 | Time: 0.050s | ETA:  189.1s
[NODE-04] Block 409/500 | Index: 409 | Slot:   9 | Storage:  39.36 KB | Overwrites: Slot   9 | Hash Ops: 1584148 | Time: 0.051s | ETA:  187.1s
[NODE-04] Block 410/500 | Index: 410 | Slot:  10 | Storage:  39.36 KB | Overwrites: Slot  10 | Hash Ops: 1591487 | Time: 0.063s | ETA:  185.0s
[NODE-04] Block 411/500 | Index: 411 | Slot:  11 | Storage:  39.36 KB | Overwrites: Slot  11 | Hash Ops: 1595304 | Time: 0.037s | ETA:  183.0s
[NODE-04] Block 412/500 | Index: 412 | Slot:  12 | Storage:  39.36 KB | Overwrites: Slot  12 | Hash Ops: 1598404 | Time: 0.024s | ETA:  180.9s
[NODE-04] Block 413/500 | Index: 413 | Slot:  13 | Storage:  39.36 KB | Overwrites: Slot  13 | Hash Ops: 1598876 | Time: 0.015s | ETA:  178.9s
[NODE-04] Block 414/500 | Index: 414 | Slot:  14 | Storage:  39.36 KB | Overwrites: Slot  14 | Hash Ops: 1600575 | Time: 0.025s | ETA:  176.8s
[NODE-04] Block 415/500 | Index: 415 | Slot:  15 | Storage:  39.36 KB | Overwrites: Slot  15 | Hash Ops: 1603034 | Time: 0.021s | ETA:  174.8s
[NODE-04] Block 416/500 | Index: 416 | Slot:  16 | Storage:  39.35 KB | Overwrites: Slot  16 | Hash Ops: 1603491 | Time: 0.003s | ETA:  172.7s
[NODE-04] Block 417/500 | Index: 417 | Slot:  17 | Storage:  39.35 KB | Overwrites: Slot  17 | Hash Ops: 1610611 | Time: 0.074s | ETA:  170.7s
[NODE-04] Block 418/500 | Index: 418 | Slot:  18 | Storage:  39.35 KB | Overwrites: Slot  18 | Hash Ops: 1612338 | Time: 0.023s | ETA:  168.6s
[NODE-04] Block 419/500 | Index: 419 | Slot:  19 | Storage:  39.35 KB | Overwrites: Slot  19 | Hash Ops: 1621573 | Time: 0.096s | ETA:  166.6s
[NODE-04] Block 420/500 | Index: 420 | Slot:  20 | Storage:  39.35 KB | Overwrites: Slot  20 | Hash Ops: 1629252 | Time: 0.066s | ETA:  164.5s
[NODE-04] Block 421/500 | Index: 421 | Slot:  21 | Storage:  39.35 KB | Overwrites: Slot  21 | Hash Ops: 1632211 | Time: 0.027s | ETA:  162.5s
[NODE-04] Block 422/500 | Index: 422 | Slot:  22 | Storage:  39.35 KB | Overwrites: Slot  22 | Hash Ops: 1639907 | Time: 0.072s | ETA:  160.4s
[NODE-04] Block 423/500 | Index: 423 | Slot:  23 | Storage:  39.35 KB | Overwrites: Slot  23 | Hash Ops: 1640432 | Time: 0.015s | ETA:  158.4s
[NODE-04] Block 424/500 | Index: 424 | Slot:  24 | Storage:  39.35 KB | Overwrites: Slot  24 | Hash Ops: 1641184 | Time: 0.012s | ETA:  156.3s
[NODE-04] Block 425/500 | Index: 425 | Slot:  25 | Storage:  39.35 KB | Overwrites: Slot  25 | Hash Ops: 1643219 | Time: 0.027s | ETA:  154.3s
[NODE-04] Block 426/500 | Index: 426 | Slot:  26 | Storage:  39.35 KB | Overwrites: Slot  26 | Hash Ops: 1643433 | Time: 0.006s | ETA:  152.2s
[NODE-04] Block 427/500 | Index: 427 | Slot:  27 | Storage:  39.35 KB | Overwrites: Slot  27 | Hash Ops: 1651925 | Time: 0.058s | ETA:  150.1s
[NODE-04] Block 428/500 | Index: 428 | Slot:  28 | Storage:  39.35 KB | Overwrites: Slot  28 | Hash Ops: 1652976 | Time: 0.007s | ETA:  148.1s
[NODE-04] Block 429/500 | Index: 429 | Slot:  29 | Storage:  39.35 KB | Overwrites: Slot  29 | Hash Ops: 1668696 | Time: 0.139s | ETA:  146.0s
[NODE-04] Block 430/500 | Index: 430 | Slot:  30 | Storage:  39.35 KB | Overwrites: Slot  30 | Hash Ops: 1677076 | Time: 0.085s | ETA:  144.0s
[NODE-04] Block 431/500 | Index: 431 | Slot:  31 | Storage:  39.35 KB | Overwrites: Slot  31 | Hash Ops: 1678413 | Time: 0.010s | ETA:  141.9s
[NODE-04] Block 432/500 | Index: 432 | Slot:  32 | Storage:  39.35 KB | Overwrites: Slot  32 | Hash Ops: 1680140 | Time: 0.032s | ETA:  139.9s
[NODE-04] Block 433/500 | Index: 433 | Slot:  33 | Storage:  39.35 KB | Overwrites: Slot  33 | Hash Ops: 1684792 | Time: 0.033s | ETA:  137.8s
[NODE-04] Block 434/500 | Index: 434 | Slot:  34 | Storage:  39.35 KB | Overwrites: Slot  34 | Hash Ops: 1685563 | Time: 0.005s | ETA:  135.8s
[NODE-04] Block 435/500 | Index: 435 | Slot:  35 | Storage:  39.35 KB | Overwrites: Slot  35 | Hash Ops: 1686023 | Time: 0.004s | ETA:  133.7s
[NODE-04] Block 436/500 | Index: 436 | Slot:  36 | Storage:  39.35 KB | Overwrites: Slot  36 | Hash Ops: 1686546 | Time: 0.014s | ETA:  131.6s
[NODE-04] Block 437/500 | Index: 437 | Slot:  37 | Storage:  39.35 KB | Overwrites: Slot  37 | Hash Ops: 1691181 | Time: 0.042s | ETA:  129.6s
[NODE-04] Block 438/500 | Index: 438 | Slot:  38 | Storage:  39.35 KB | Overwrites: Slot  38 | Hash Ops: 1692744 | Time: 0.036s | ETA:  127.5s
[NODE-04] Block 439/500 | Index: 439 | Slot:  39 | Storage:  39.35 KB | Overwrites: Slot  39 | Hash Ops: 1706606 | Time: 0.098s | ETA:  125.5s
[NODE-04] Block 440/500 | Index: 440 | Slot:  40 | Storage:  39.35 KB | Overwrites: Slot  40 | Hash Ops: 1707849 | Time: 0.019s | ETA:  123.4s
[NODE-04] Block 441/500 | Index: 441 | Slot:  41 | Storage:  39.35 KB | Overwrites: Slot  41 | Hash Ops: 1711271 | Time: 0.029s | ETA:  121.4s
[NODE-04] Block 442/500 | Index: 442 | Slot:  42 | Storage:  39.35 KB | Overwrites: Slot  42 | Hash Ops: 1711527 | Time: 0.008s | ETA:  119.3s
[NODE-04] Block 443/500 | Index: 443 | Slot:  43 | Storage:  39.35 KB | Overwrites: Slot  43 | Hash Ops: 1712889 | Time: 0.010s | ETA:  117.3s
[NODE-04] Block 444/500 | Index: 444 | Slot:  44 | Storage:  39.35 KB | Overwrites: Slot  44 | Hash Ops: 1714110 | Time: 0.009s | ETA:  115.2s
[NODE-04] Block 445/500 | Index: 445 | Slot:  45 | Storage:  39.35 KB | Overwrites: Slot  45 | Hash Ops: 1715193 | Time: 0.024s | ETA:  113.1s
[NODE-04] Block 446/500 | Index: 446 | Slot:  46 | Storage:  39.35 KB | Overwrites: Slot  46 | Hash Ops: 1719929 | Time: 0.044s | ETA:  111.1s
[NODE-04] Block 447/500 | Index: 447 | Slot:  47 | Storage:  39.35 KB | Overwrites: Slot  47 | Hash Ops: 1720918 | Time: 0.009s | ETA:  109.0s
[NODE-04] Block 448/500 | Index: 448 | Slot:  48 | Storage:  39.35 KB | Overwrites: Slot  48 | Hash Ops: 1728476 | Time: 0.066s | ETA:  107.0s
[NODE-04] Block 449/500 | Index: 449 | Slot:  49 | Storage:  39.35 KB | Overwrites: Slot  49 | Hash Ops: 1728725 | Time: 0.008s | ETA:  104.9s
[NODE-04] Block 450/500 | Index: 450 | Slot:  50 | Storage:  39.35 KB | Overwrites: Slot  50 | Hash Ops: 1730868 | Time: 0.035s | ETA:  102.9s
[NODE-04] Block 451/500 | Index: 451 | Slot:  51 | Storage:  39.35 KB | Overwrites: Slot  51 | Hash Ops: 1734169 | Time: 0.037s | ETA:  100.8s
[NODE-04] Block 452/500 | Index: 452 | Slot:  52 | Storage:  39.35 KB | Overwrites: Slot  52 | Hash Ops: 1739336 | Time: 0.053s | ETA:   98.8s
[NODE-04] Block 453/500 | Index: 453 | Slot:  53 | Storage:  39.35 KB | Overwrites: Slot  53 | Hash Ops: 1739470 | Time: 0.003s | ETA:   96.7s
[NODE-04] Block 454/500 | Index: 454 | Slot:  54 | Storage:  39.35 KB | Overwrites: Slot  54 | Hash Ops: 1739818 | Time: 0.010s | ETA:   94.6s
[NODE-04] Block 455/500 | Index: 455 | Slot:  55 | Storage:  39.35 KB | Overwrites: Slot  55 | Hash Ops: 1740464 | Time: 0.012s | ETA:   92.6s
[NODE-04] Block 456/500 | Index: 456 | Slot:  56 | Storage:  39.35 KB | Overwrites: Slot  56 | Hash Ops: 1751291 | Time: 0.095s | ETA:   90.5s
[NODE-04] Block 457/500 | Index: 457 | Slot:  57 | Storage:  39.35 KB | Overwrites: Slot  57 | Hash Ops: 1758460 | Time: 0.075s | ETA:   88.5s
[NODE-04] Block 458/500 | Index: 458 | Slot:  58 | Storage:  39.35 KB | Overwrites: Slot  58 | Hash Ops: 1763252 | Time: 0.050s | ETA:   86.4s
[NODE-04] Block 459/500 | Index: 459 | Slot:  59 | Storage:  39.34 KB | Overwrites: Slot  59 | Hash Ops: 1763400 | Time: 0.004s | ETA:   84.3s
[NODE-04] Block 460/500 | Index: 460 | Slot:  60 | Storage:  39.34 KB | Overwrites: Slot  60 | Hash Ops: 1764976 | Time: 0.036s | ETA:   82.3s
[NODE-04] Block 461/500 | Index: 461 | Slot:  61 | Storage:  39.35 KB | Overwrites: Slot  61 | Hash Ops: 1766692 | Time: 0.033s | ETA:   80.2s
[NODE-04] Block 462/500 | Index: 462 | Slot:  62 | Storage:  39.34 KB | Overwrites: Slot  62 | Hash Ops: 1768486 | Time: 0.035s | ETA:   78.2s
[NODE-04] Block 463/500 | Index: 463 | Slot:  63 | Storage:  39.34 KB | Overwrites: Slot  63 | Hash Ops: 1768507 | Time: 0.001s | ETA:   76.1s
[NODE-04] Block 464/500 | Index: 464 | Slot:  64 | Storage:  39.34 KB | Overwrites: Slot  64 | Hash Ops: 1771443 | Time: 0.040s | ETA:   74.1s
[NODE-04] Block 465/500 | Index: 465 | Slot:  65 | Storage:  39.34 KB | Overwrites: Slot  65 | Hash Ops: 1771917 | Time: 0.013s | ETA:   72.0s
[NODE-04] Block 466/500 | Index: 466 | Slot:  66 | Storage:  39.35 KB | Overwrites: Slot  66 | Hash Ops: 1782125 | Time: 0.099s | ETA:   70.0s
[NODE-04] Block 467/500 | Index: 467 | Slot:  67 | Storage:  39.35 KB | Overwrites: Slot  67 | Hash Ops: 1788741 | Time: 0.056s | ETA:   67.9s
[NODE-04] Block 468/500 | Index: 468 | Slot:  68 | Storage:  39.35 KB | Overwrites: Slot  68 | Hash Ops: 1792162 | Time: 0.040s | ETA:   65.9s
[NODE-04] Block 469/500 | Index: 469 | Slot:  69 | Storage:  39.35 KB | Overwrites: Slot  69 | Hash Ops: 1794895 | Time: 0.046s | ETA:   63.8s
[NODE-04] Block 470/500 | Index: 470 | Slot:  70 | Storage:  39.35 KB | Overwrites: Slot  70 | Hash Ops: 1813571 | Time: 0.144s | ETA:   61.8s
[NODE-04] Block 471/500 | Index: 471 | Slot:  71 | Storage:  39.35 KB | Overwrites: Slot  71 | Hash Ops: 1822384 | Time: 0.091s | ETA:   59.7s
[NODE-04] Block 472/500 | Index: 472 | Slot:  72 | Storage:  39.34 KB | Overwrites: Slot  72 | Hash Ops: 1827593 | Time: 0.054s | ETA:   57.6s
[NODE-04] Block 473/500 | Index: 473 | Slot:  73 | Storage:  39.34 KB | Overwrites: Slot  73 | Hash Ops: 1828686 | Time: 0.011s | ETA:   55.6s
[NODE-04] Block 474/500 | Index: 474 | Slot:  74 | Storage:  39.34 KB | Overwrites: Slot  74 | Hash Ops: 1830684 | Time: 0.018s | ETA:   53.5s
[NODE-04] Block 475/500 | Index: 475 | Slot:  75 | Storage:  39.34 KB | Overwrites: Slot  75 | Hash Ops: 1832396 | Time: 0.019s | ETA:   51.5s
[NODE-04] Block 476/500 | Index: 476 | Slot:  76 | Storage:  39.34 KB | Overwrites: Slot  76 | Hash Ops: 1833134 | Time: 0.008s | ETA:   49.4s
[NODE-04] Block 477/500 | Index: 477 | Slot:  77 | Storage:  39.34 KB | Overwrites: Slot  77 | Hash Ops: 1835150 | Time: 0.015s | ETA:   47.3s
[NODE-04] Block 478/500 | Index: 478 | Slot:  78 | Storage:  39.34 KB | Overwrites: Slot  78 | Hash Ops: 1842057 | Time: 0.068s | ETA:   45.3s
[NODE-04] Block 479/500 | Index: 479 | Slot:  79 | Storage:  39.34 KB | Overwrites: Slot  79 | Hash Ops: 1846159 | Time: 0.047s | ETA:   43.2s
[NODE-04] Block 480/500 | Index: 480 | Slot:  80 | Storage:  39.34 KB | Overwrites: Slot  80 | Hash Ops: 1847465 | Time: 0.028s | ETA:   41.2s
[NODE-04] Block 481/500 | Index: 481 | Slot:  81 | Storage:  39.34 KB | Overwrites: Slot  81 | Hash Ops: 1852432 | Time: 0.040s | ETA:   39.1s
[NODE-04] Block 482/500 | Index: 482 | Slot:  82 | Storage:  39.34 KB | Overwrites: Slot  82 | Hash Ops: 1854209 | Time: 0.020s | ETA:   37.1s
[NODE-04] Block 483/500 | Index: 483 | Slot:  83 | Storage:  39.34 KB | Overwrites: Slot  83 | Hash Ops: 1857400 | Time: 0.049s | ETA:   35.0s
[NODE-04] Block 484/500 | Index: 484 | Slot:  84 | Storage:  39.34 KB | Overwrites: Slot  84 | Hash Ops: 1859687 | Time: 0.029s | ETA:   32.9s
[NODE-04] Block 485/500 | Index: 485 | Slot:  85 | Storage:  39.34 KB | Overwrites: Slot  85 | Hash Ops: 1861185 | Time: 0.024s | ETA:   30.9s
[NODE-04] Block 486/500 | Index: 486 | Slot:  86 | Storage:  39.34 KB | Overwrites: Slot  86 | Hash Ops: 1863282 | Time: 0.019s | ETA:   28.8s
[NODE-04] Block 487/500 | Index: 487 | Slot:  87 | Storage:  39.34 KB | Overwrites: Slot  87 | Hash Ops: 1864862 | Time: 0.018s | ETA:   26.8s
[NODE-04] Block 488/500 | Index: 488 | Slot:  88 | Storage:  39.34 KB | Overwrites: Slot  88 | Hash Ops: 1877331 | Time: 0.135s | ETA:   24.7s
[NODE-04] Block 489/500 | Index: 489 | Slot:  89 | Storage:  39.34 KB | Overwrites: Slot  89 | Hash Ops: 1883174 | Time: 0.061s | ETA:   22.6s
[NODE-04] Block 490/500 | Index: 490 | Slot:  90 | Storage:  39.34 KB | Overwrites: Slot  90 | Hash Ops: 1886044 | Time: 0.020s | ETA:   20.6s
[NODE-04] Block 491/500 | Index: 491 | Slot:  91 | Storage:  39.34 KB | Overwrites: Slot  91 | Hash Ops: 1886159 | Time: 0.004s | ETA:   18.5s
[NODE-04] Block 492/500 | Index: 492 | Slot:  92 | Storage:  39.34 KB | Overwrites: Slot  92 | Hash Ops: 1890145 | Time: 0.029s | ETA:   16.5s
[NODE-04] Block 493/500 | Index: 493 | Slot:  93 | Storage:  39.34 KB | Overwrites: Slot  93 | Hash Ops: 1891702 | Time: 0.030s | ETA:   14.4s
[NODE-04] Block 494/500 | Index: 494 | Slot:  94 | Storage:  39.34 KB | Overwrites: Slot  94 | Hash Ops: 1902793 | Time: 0.119s | ETA:   12.4s
[NODE-04] Block 495/500 | Index: 495 | Slot:  95 | Storage:  39.35 KB | Overwrites: Slot  95 | Hash Ops: 1904438 | Time: 0.019s | ETA:   10.3s
[NODE-04] Block 496/500 | Index: 496 | Slot:  96 | Storage:  39.35 KB | Overwrites: Slot  96 | Hash Ops: 1910841 | Time: 0.048s | ETA:    8.2s
[NODE-04] Block 497/500 | Index: 497 | Slot:  97 | Storage:  39.35 KB | Overwrites: Slot  97 | Hash Ops: 1911420 | Time: 0.006s | ETA:    6.2s
[NODE-04] Block 498/500 | Index: 498 | Slot:  98 | Storage:  39.35 KB | Overwrites: Slot  98 | Hash Ops: 1925477 | Time: 0.118s | ETA:    4.1s
[NODE-04] Block 499/500 | Index: 499 | Slot:  99 | Storage:  39.35 KB | Overwrites: Slot  99 | Hash Ops: 1933769 | Time: 0.058s | ETA:    2.1s
[NODE-04] Block 500/500 | Index: 500 | Slot:   0 | Storage:  39.35 KB | Overwrites: Slot   0 | Hash Ops: 1952728 | Time: 0.176s | ETA:    0.0s
[NODE-04] Peer connections restored
[NODE-04] Completed in 1031.83 seconds

================================================================================
Resetting NODE-05 to genesis before its simulation
================================================================================
✓ NODE-05 reset to genesis (index=0)


[NODE-05] Starting block generation...
[NODE-05] Initial ledger state:
[NODE-05]   Last index: 0
[NODE-05]   Genesis hash: 000ac6d79f7c53bb...
[NODE-05] Target: 500 blocks
[NODE-05] Mode: Independent (no peer interaction)
[NODE-05] Peers temporarily disconnected for independent simulation
[NODE-05] Block   1/500 | Index:   1 | Slot:   1 | Storage:   0.70 KB | Overwrites:   - | Hash Ops:    500 | Time: 0.006s | ETA:   66.8s
[NODE-05] Block   2/500 | Index:   2 | Slot:   2 | Storage:   1.09 KB | Overwrites:   - | Hash Ops:   6882 | Time: 0.045s | ETA:  544.3s
[NODE-05] Block   3/500 | Index:   3 | Slot:   3 | Storage:   1.48 KB | Overwrites:   - | Hash Ops:  10839 | Time: 0.035s | ETA:  699.7s
[NODE-05] Block   4/500 | Index:   4 | Slot:   4 | Storage:   1.86 KB | Overwrites:   - | Hash Ops:  12166 | Time: 0.022s | ETA:  779.6s
[NODE-05] Block   5/500 | Index:   5 | Slot:   5 | Storage:   2.25 KB | Overwrites:   - | Hash Ops:  14163 | Time: 0.018s | ETA:  822.4s
[NODE-05] Block   6/500 | Index:   6 | Slot:   6 | Storage:   2.64 KB | Overwrites:   - | Hash Ops:  15517 | Time: 0.012s | ETA:  850.4s
[NODE-05] Block   7/500 | Index:   7 | Slot:   7 | Storage:   3.03 KB | Overwrites:   - | Hash Ops:  16679 | Time: 0.012s | ETA:  869.8s
[NODE-05] Block   8/500 | Index:   8 | Slot:   8 | Storage:   3.41 KB | Overwrites:   - | Hash Ops:  17260 | Time: 0.005s | ETA:  883.1s
[NODE-05] Block   9/500 | Index:   9 | Slot:   9 | Storage:   3.80 KB | Overwrites:   - | Hash Ops:  17694 | Time: 0.006s | ETA:  893.0s
[NODE-05] Block  10/500 | Index:  10 | Slot:  10 | Storage:   4.20 KB | Overwrites:   - | Hash Ops:  19582 | Time: 0.016s | ETA:  902.5s
[NODE-05] Block  11/500 | Index:  11 | Slot:  11 | Storage:   4.58 KB | Overwrites:   - | Hash Ops:  19908 | Time: 0.003s | ETA:  913.5s
[NODE-05] Block  12/500 | Index:  12 | Slot:  12 | Storage:   4.97 KB | Overwrites:   - | Hash Ops:  27978 | Time: 0.060s | ETA:  920.4s
[NODE-05] Block  13/500 | Index:  13 | Slot:  13 | Storage:   5.36 KB | Overwrites:   - | Hash Ops:  29222 | Time: 0.013s | ETA:  923.4s
[NODE-05] Block  14/500 | Index:  14 | Slot:  14 | Storage:   5.76 KB | Overwrites:   - | Hash Ops:  37765 | Time: 0.062s | ETA:  928.1s
[NODE-05] Block  15/500 | Index:  15 | Slot:  15 | Storage:   6.15 KB | Overwrites:   - | Hash Ops:  39178 | Time: 0.015s | ETA:  929.9s
[NODE-05] Block  16/500 | Index:  16 | Slot:  16 | Storage:   6.54 KB | Overwrites:   - | Hash Ops:  39346 | Time: 0.005s | ETA:  930.9s
[NODE-05] Block  17/500 | Index:  17 | Slot:  17 | Storage:   6.93 KB | Overwrites:   - | Hash Ops:  41395 | Time: 0.020s | ETA:  931.9s
[NODE-05] Block  18/500 | Index:  18 | Slot:  18 | Storage:   7.32 KB | Overwrites:   - | Hash Ops:  47635 | Time: 0.045s | ETA:  933.1s
[NODE-05] Block  19/500 | Index:  19 | Slot:  19 | Storage:   7.71 KB | Overwrites:   - | Hash Ops:  47922 | Time: 0.007s | ETA:  933.7s
[NODE-05] Block  20/500 | Index:  20 | Slot:  20 | Storage:   8.10 KB | Overwrites:   - | Hash Ops:  54930 | Time: 0.046s | ETA:  934.4s
[NODE-05] Block  21/500 | Index:  21 | Slot:  21 | Storage:   8.50 KB | Overwrites:   - | Hash Ops:  67793 | Time: 0.091s | ETA:  938.4s
[NODE-05] Block  22/500 | Index:  22 | Slot:  22 | Storage:   8.89 KB | Overwrites:   - | Hash Ops:  72088 | Time: 0.032s | ETA:  938.2s
[NODE-05] Block  23/500 | Index:  23 | Slot:  23 | Storage:   9.28 KB | Overwrites:   - | Hash Ops:  76420 | Time: 0.032s | ETA:  938.3s
[NODE-05] Block  24/500 | Index:  24 | Slot:  24 | Storage:   9.67 KB | Overwrites:   - | Hash Ops:  81328 | Time: 0.032s | ETA:  937.8s
[NODE-05] Block  25/500 | Index:  25 | Slot:  25 | Storage:  10.06 KB | Overwrites:   - | Hash Ops:  83382 | Time: 0.014s | ETA:  936.9s
[NODE-05] Block  26/500 | Index:  26 | Slot:  26 | Storage:  10.45 KB | Overwrites:   - | Hash Ops:  85911 | Time: 0.024s | ETA:  935.9s
[NODE-05] Block  27/500 | Index:  27 | Slot:  27 | Storage:  10.84 KB | Overwrites:   - | Hash Ops:  87330 | Time: 0.013s | ETA:  935.0s
[NODE-05] Block  28/500 | Index:  28 | Slot:  28 | Storage:  11.23 KB | Overwrites:   - | Hash Ops:  88925 | Time: 0.015s | ETA:  934.0s
[NODE-05] Block  29/500 | Index:  29 | Slot:  29 | Storage:  11.62 KB | Overwrites:   - | Hash Ops:  95711 | Time: 0.056s | ETA:  933.4s
[NODE-05] Block  30/500 | Index:  30 | Slot:  30 | Storage:  12.01 KB | Overwrites:   - | Hash Ops: 101003 | Time: 0.041s | ETA:  932.4s
[NODE-05] Block  31/500 | Index:  31 | Slot:  31 | Storage:  12.40 KB | Overwrites:   - | Hash Ops: 101928 | Time: 0.007s | ETA:  932.5s
[NODE-05] Block  32/500 | Index:  32 | Slot:  32 | Storage:  12.80 KB | Overwrites:   - | Hash Ops: 103092 | Time: 0.012s | ETA:  931.2s
[NODE-05] Block  33/500 | Index:  33 | Slot:  33 | Storage:  13.19 KB | Overwrites:   - | Hash Ops: 108772 | Time: 0.041s | ETA:  930.3s
[NODE-05] Block  34/500 | Index:  34 | Slot:  34 | Storage:  13.58 KB | Overwrites:   - | Hash Ops: 114247 | Time: 0.040s | ETA:  929.1s
[NODE-05] Block  35/500 | Index:  35 | Slot:  35 | Storage:  13.97 KB | Overwrites:   - | Hash Ops: 117962 | Time: 0.028s | ETA:  927.9s
[NODE-05] Block  36/500 | Index:  36 | Slot:  36 | Storage:  14.36 KB | Overwrites:   - | Hash Ops: 129057 | Time: 0.075s | ETA:  927.4s
[NODE-05] Block  37/500 | Index:  37 | Slot:  37 | Storage:  14.75 KB | Overwrites:   - | Hash Ops: 130331 | Time: 0.015s | ETA:  926.2s
[NODE-05] Block  38/500 | Index:  38 | Slot:  38 | Storage:  15.15 KB | Overwrites:   - | Hash Ops: 132956 | Time: 0.022s | ETA:  924.6s
[NODE-05] Block  39/500 | Index:  39 | Slot:  39 | Storage:  15.54 KB | Overwrites:   - | Hash Ops: 138950 | Time: 0.043s | ETA:  923.6s
[NODE-05] Block  40/500 | Index:  40 | Slot:  40 | Storage:  15.93 KB | Overwrites:   - | Hash Ops: 145669 | Time: 0.044s | ETA:  922.1s
[NODE-05] Block  41/500 | Index:  41 | Slot:  41 | Storage:  16.32 KB | Overwrites:   - | Hash Ops: 153264 | Time: 0.053s | ETA:  922.1s
[NODE-05] Block  42/500 | Index:  42 | Slot:  42 | Storage:  16.71 KB | Overwrites:   - | Hash Ops: 153727 | Time: 0.007s | ETA:  920.4s
[NODE-05] Block  43/500 | Index:  43 | Slot:  43 | Storage:  17.10 KB | Overwrites:   - | Hash Ops: 154703 | Time: 0.007s | ETA:  918.9s
[NODE-05] Block  44/500 | Index:  44 | Slot:  44 | Storage:  17.49 KB | Overwrites:   - | Hash Ops: 156159 | Time: 0.016s | ETA:  917.1s
[NODE-05] Block  45/500 | Index:  45 | Slot:  45 | Storage:  17.88 KB | Overwrites:   - | Hash Ops: 158731 | Time: 0.019s | ETA:  915.5s
[NODE-05] Block  46/500 | Index:  46 | Slot:  46 | Storage:  18.27 KB | Overwrites:   - | Hash Ops: 159703 | Time: 0.012s | ETA:  913.5s
[NODE-05] Block  47/500 | Index:  47 | Slot:  47 | Storage:  18.66 KB | Overwrites:   - | Hash Ops: 162973 | Time: 0.025s | ETA:  912.0s
[NODE-05] Block  48/500 | Index:  48 | Slot:  48 | Storage:  19.05 KB | Overwrites:   - | Hash Ops: 167010 | Time: 0.030s | ETA:  910.1s
[NODE-05] Block  49/500 | Index:  49 | Slot:  49 | Storage:  19.44 KB | Overwrites:   - | Hash Ops: 167632 | Time: 0.006s | ETA:  908.2s
[NODE-05] Block  50/500 | Index:  50 | Slot:  50 | Storage:  19.83 KB | Overwrites:   - | Hash Ops: 168371 | Time: 0.007s | ETA:  906.3s
[NODE-05] Block  51/500 | Index:  51 | Slot:  51 | Storage:  20.22 KB | Overwrites:   - | Hash Ops: 169721 | Time: 0.012s | ETA:  905.2s
[NODE-05] Block  52/500 | Index:  52 | Slot:  52 | Storage:  20.62 KB | Overwrites:   - | Hash Ops: 172022 | Time: 0.016s | ETA:  903.4s
[NODE-05] Block  53/500 | Index:  53 | Slot:  53 | Storage:  21.01 KB | Overwrites:   - | Hash Ops: 188320 | Time: 0.109s | ETA:  902.3s
[NODE-05] Block  54/500 | Index:  54 | Slot:  54 | Storage:  21.40 KB | Overwrites:   - | Hash Ops: 190793 | Time: 0.020s | ETA:  900.5s
[NODE-05] Block  55/500 | Index:  55 | Slot:  55 | Storage:  21.79 KB | Overwrites:   - | Hash Ops: 194090 | Time: 0.030s | ETA:  898.6s
[NODE-05] Block  56/500 | Index:  56 | Slot:  56 | Storage:  22.18 KB | Overwrites:   - | Hash Ops: 206644 | Time: 0.086s | ETA:  897.1s
[NODE-05] Block  57/500 | Index:  57 | Slot:  57 | Storage:  22.57 KB | Overwrites:   - | Hash Ops: 209746 | Time: 0.036s | ETA:  895.4s
[NODE-05] Block  58/500 | Index:  58 | Slot:  58 | Storage:  22.96 KB | Overwrites:   - | Hash Ops: 212824 | Time: 0.023s | ETA:  893.8s
[NODE-05] Block  59/500 | Index:  59 | Slot:  59 | Storage:  23.35 KB | Overwrites:   - | Hash Ops: 213239 | Time: 0.006s | ETA:  891.6s
[NODE-05] Block  60/500 | Index:  60 | Slot:  60 | Storage:  23.74 KB | Overwrites:   - | Hash Ops: 215187 | Time: 0.013s | ETA:  889.6s
[NODE-05] Block  61/500 | Index:  61 | Slot:  61 | Storage:  24.13 KB | Overwrites:   - | Hash Ops: 217330 | Time: 0.020s | ETA:  889.4s
[NODE-05] Block  62/500 | Index:  62 | Slot:  62 | Storage:  24.52 KB | Overwrites:   - | Hash Ops: 228015 | Time: 0.073s | ETA:  887.8s
[NODE-05] Block  63/500 | Index:  63 | Slot:  63 | Storage:  24.92 KB | Overwrites:   - | Hash Ops: 248436 | Time: 0.139s | ETA:  886.6s
[NODE-05] Block  64/500 | Index:  64 | Slot:  64 | Storage:  25.31 KB | Overwrites:   - | Hash Ops: 248809 | Time: 0.009s | ETA:  884.8s
[NODE-05] Block  65/500 | Index:  65 | Slot:  65 | Storage:  25.70 KB | Overwrites:   - | Hash Ops: 248949 | Time: 0.001s | ETA:  882.7s
[NODE-05] Block  66/500 | Index:  66 | Slot:  66 | Storage:  26.09 KB | Overwrites:   - | Hash Ops: 255811 | Time: 0.048s | ETA:  880.8s
[NODE-05] Block  67/500 | Index:  67 | Slot:  67 | Storage:  26.48 KB | Overwrites:   - | Hash Ops: 256451 | Time: 0.008s | ETA:  879.0s
[NODE-05] Block  68/500 | Index:  68 | Slot:  68 | Storage:  26.87 KB | Overwrites:   - | Hash Ops: 263173 | Time: 0.049s | ETA:  877.2s
[NODE-05] Block  69/500 | Index:  69 | Slot:  69 | Storage:  27.26 KB | Overwrites:   - | Hash Ops: 266172 | Time: 0.020s | ETA:  875.1s
[NODE-05] Block  70/500 | Index:  70 | Slot:  70 | Storage:  27.65 KB | Overwrites:   - | Hash Ops: 269271 | Time: 0.024s | ETA:  873.4s
[NODE-05] Block  71/500 | Index:  71 | Slot:  71 | Storage:  28.04 KB | Overwrites:   - | Hash Ops: 269938 | Time: 0.006s | ETA:  872.1s
[NODE-05] Block  72/500 | Index:  72 | Slot:  72 | Storage:  28.44 KB | Overwrites:   - | Hash Ops: 272384 | Time: 0.020s | ETA:  870.0s
[NODE-05] Block  73/500 | Index:  73 | Slot:  73 | Storage:  28.82 KB | Overwrites:   - | Hash Ops: 275759 | Time: 0.026s | ETA:  868.1s
[NODE-05] Block  74/500 | Index:  74 | Slot:  74 | Storage:  29.21 KB | Overwrites:   - | Hash Ops: 280702 | Time: 0.036s | ETA:  867.0s
[NODE-05] Block  75/500 | Index:  75 | Slot:  75 | Storage:  29.60 KB | Overwrites:   - | Hash Ops: 281762 | Time: 0.015s | ETA:  864.9s
[NODE-05] Block  76/500 | Index:  76 | Slot:  76 | Storage:  29.99 KB | Overwrites:   - | Hash Ops: 285100 | Time: 0.029s | ETA:  862.8s
[NODE-05] Block  77/500 | Index:  77 | Slot:  77 | Storage:  30.38 KB | Overwrites:   - | Hash Ops: 291895 | Time: 0.046s | ETA:  861.0s
[NODE-05] Block  78/500 | Index:  78 | Slot:  78 | Storage:  30.77 KB | Overwrites:   - | Hash Ops: 292816 | Time: 0.014s | ETA:  858.9s
[NODE-05] Block  79/500 | Index:  79 | Slot:  79 | Storage:  31.17 KB | Overwrites:   - | Hash Ops: 295717 | Time: 0.020s | ETA:  856.9s
[NODE-05] Block  80/500 | Index:  80 | Slot:  80 | Storage:  31.56 KB | Overwrites:   - | Hash Ops: 300038 | Time: 0.036s | ETA:  854.9s
[NODE-05] Block  81/500 | Index:  81 | Slot:  81 | Storage:  31.95 KB | Overwrites:   - | Hash Ops: 301081 | Time: 0.007s | ETA:  853.7s
[NODE-05] Block  82/500 | Index:  82 | Slot:  82 | Storage:  32.34 KB | Overwrites:   - | Hash Ops: 302403 | Time: 0.012s | ETA:  851.6s
[NODE-05] Block  83/500 | Index:  83 | Slot:  83 | Storage:  32.73 KB | Overwrites:   - | Hash Ops: 314534 | Time: 0.086s | ETA:  849.9s
[NODE-05] Block  84/500 | Index:  84 | Slot:  84 | Storage:  33.12 KB | Overwrites:   - | Hash Ops: 324004 | Time: 0.068s | ETA:  848.1s
[NODE-05] Block  85/500 | Index:  85 | Slot:  85 | Storage:  33.51 KB | Overwrites:   - | Hash Ops: 332676 | Time: 0.061s | ETA:  846.2s
[NODE-05] Block  86/500 | Index:  86 | Slot:  86 | Storage:  33.90 KB | Overwrites:   - | Hash Ops: 332956 | Time: 0.006s | ETA:  844.0s
[NODE-05] Block  87/500 | Index:  87 | Slot:  87 | Storage:  34.29 KB | Overwrites:   - | Hash Ops: 334027 | Time: 0.011s | ETA:  841.9s
[NODE-05] Block  88/500 | Index:  88 | Slot:  88 | Storage:  34.69 KB | Overwrites:   - | Hash Ops: 341274 | Time: 0.049s | ETA:  840.0s
[NODE-05] Block  89/500 | Index:  89 | Slot:  89 | Storage:  35.08 KB | Overwrites:   - | Hash Ops: 345573 | Time: 0.032s | ETA:  838.1s
[NODE-05] Block  90/500 | Index:  90 | Slot:  90 | Storage:  35.47 KB | Overwrites:   - | Hash Ops: 346260 | Time: 0.009s | ETA:  835.9s
[NODE-05] Block  91/500 | Index:  91 | Slot:  91 | Storage:  35.86 KB | Overwrites:   - | Hash Ops: 348418 | Time: 0.015s | ETA:  834.6s
[NODE-05] Block  92/500 | Index:  92 | Slot:  92 | Storage:  36.25 KB | Overwrites:   - | Hash Ops: 351928 | Time: 0.023s | ETA:  832.5s
[NODE-05] Block  93/500 | Index:  93 | Slot:  93 | Storage:  36.64 KB | Overwrites:   - | Hash Ops: 358698 | Time: 0.046s | ETA:  830.5s
[NODE-05] Block  94/500 | Index:  94 | Slot:  94 | Storage:  37.03 KB | Overwrites:   - | Hash Ops: 365783 | Time: 0.050s | ETA:  828.6s
[NODE-05] Block  95/500 | Index:  95 | Slot:  95 | Storage:  37.42 KB | Overwrites:   - | Hash Ops: 366285 | Time: 0.007s | ETA:  826.4s
[NODE-05] Block  96/500 | Index:  96 | Slot:  96 | Storage:  37.81 KB | Overwrites:   - | Hash Ops: 366334 | Time: 0.002s | ETA:  824.3s
[NODE-05] Block  97/500 | Index:  97 | Slot:  97 | Storage:  38.20 KB | Overwrites:   - | Hash Ops: 366553 | Time: 0.006s | ETA:  822.5s
[NODE-05] Block  98/500 | Index:  98 | Slot:  98 | Storage:  38.59 KB | Overwrites:   - | Hash Ops: 370552 | Time: 0.033s | ETA:  820.4s
[NODE-05] Block  99/500 | Index:  99 | Slot:  99 | Storage:  38.98 KB | Overwrites:   - | Hash Ops: 372808 | Time: 0.020s | ETA:  818.5s
[NODE-05] Block 100/500 | Index: 100 | Slot:   0 | Storage:  39.06 KB | Overwrites: Slot   0 | Hash Ops: 375833 | Time: 0.020s | ETA:  816.4s
[NODE-05] Block 101/500 | Index: 101 | Slot:   1 | Storage:  39.07 KB | Overwrites: Slot   1 | Hash Ops: 377012 | Time: 0.016s | ETA:  814.8s
[NODE-05] Block 102/500 | Index: 102 | Slot:   2 | Storage:  39.07 KB | Overwrites: Slot   2 | Hash Ops: 377591 | Time: 0.007s | ETA:  812.6s
[NODE-05] Block 103/500 | Index: 103 | Slot:   3 | Storage:  39.08 KB | Overwrites: Slot   3 | Hash Ops: 378440 | Time: 0.011s | ETA:  810.5s
[NODE-05] Block 104/500 | Index: 104 | Slot:   4 | Storage:  39.08 KB | Overwrites: Slot   4 | Hash Ops: 380950 | Time: 0.020s | ETA:  808.4s
[NODE-05] Block 105/500 | Index: 105 | Slot:   5 | Storage:  39.09 KB | Overwrites: Slot   5 | Hash Ops: 382974 | Time: 0.019s | ETA:  806.4s
[NODE-05] Block 106/500 | Index: 106 | Slot:   6 | Storage:  39.09 KB | Overwrites: Slot   6 | Hash Ops: 389365 | Time: 0.047s | ETA:  804.4s
[NODE-05] Block 107/500 | Index: 107 | Slot:   7 | Storage:  39.10 KB | Overwrites: Slot   7 | Hash Ops: 389643 | Time: 0.003s | ETA:  802.3s
[NODE-05] Block 108/500 | Index: 108 | Slot:   8 | Storage:  39.10 KB | Overwrites: Slot   8 | Hash Ops: 393749 | Time: 0.030s | ETA:  800.3s
[NODE-05] Block 109/500 | Index: 109 | Slot:   9 | Storage:  39.11 KB | Overwrites: Slot   9 | Hash Ops: 393784 | Time: 0.000s | ETA:  798.2s
[NODE-05] Block 110/500 | Index: 110 | Slot:  10 | Storage:  39.10 KB | Overwrites: Slot  10 | Hash Ops: 397791 | Time: 0.028s | ETA:  796.1s
[NODE-05] Block 111/500 | Index: 111 | Slot:  11 | Storage:  39.11 KB | Overwrites: Slot  11 | Hash Ops: 401288 | Time: 0.030s | ETA:  794.5s
[NODE-05] Block 112/500 | Index: 112 | Slot:  12 | Storage:  39.11 KB | Overwrites: Slot  12 | Hash Ops: 405793 | Time: 0.034s | ETA:  792.6s
[NODE-05] Block 113/500 | Index: 113 | Slot:  13 | Storage:  39.12 KB | Overwrites: Slot  13 | Hash Ops: 406325 | Time: 0.011s | ETA:  790.5s
[NODE-05] Block 114/500 | Index: 114 | Slot:  14 | Storage:  39.12 KB | Overwrites: Slot  14 | Hash Ops: 406785 | Time: 0.009s | ETA:  788.3s
[NODE-05] Block 115/500 | Index: 115 | Slot:  15 | Storage:  39.12 KB | Overwrites: Slot  15 | Hash Ops: 407045 | Time: 0.004s | ETA:  786.3s
[NODE-05] Block 116/500 | Index: 116 | Slot:  16 | Storage:  39.12 KB | Overwrites: Slot  16 | Hash Ops: 411426 | Time: 0.029s | ETA:  784.3s
[NODE-05] Block 117/500 | Index: 117 | Slot:  17 | Storage:  39.12 KB | Overwrites: Slot  17 | Hash Ops: 417390 | Time: 0.043s | ETA:  782.3s
[NODE-05] Block 118/500 | Index: 118 | Slot:  18 | Storage:  39.12 KB | Overwrites: Slot  18 | Hash Ops: 417478 | Time: 0.002s | ETA:  780.2s
[NODE-05] Block 119/500 | Index: 119 | Slot:  19 | Storage:  39.12 KB | Overwrites: Slot  19 | Hash Ops: 423098 | Time: 0.041s | ETA:  778.3s
[NODE-05] Block 120/500 | Index: 120 | Slot:  20 | Storage:  39.12 KB | Overwrites: Slot  20 | Hash Ops: 424043 | Time: 0.014s | ETA:  776.1s
[NODE-05] Block 121/500 | Index: 121 | Slot:  21 | Storage:  39.12 KB | Overwrites: Slot  21 | Hash Ops: 427907 | Time: 0.028s | ETA:  774.5s
[NODE-05] Block 122/500 | Index: 122 | Slot:  22 | Storage:  39.12 KB | Overwrites: Slot  22 | Hash Ops: 435531 | Time: 0.075s | ETA:  772.6s
[NODE-05] Block 123/500 | Index: 123 | Slot:  23 | Storage:  39.13 KB | Overwrites: Slot  23 | Hash Ops: 438480 | Time: 0.020s | ETA:  770.5s
[NODE-05] Block 124/500 | Index: 124 | Slot:  24 | Storage:  39.13 KB | Overwrites: Slot  24 | Hash Ops: 443861 | Time: 0.042s | ETA:  768.5s
[NODE-05] Block 125/500 | Index: 125 | Slot:  25 | Storage:  39.14 KB | Overwrites: Slot  25 | Hash Ops: 446169 | Time: 0.016s | ETA:  766.3s
[NODE-05] Block 126/500 | Index: 126 | Slot:  26 | Storage:  39.14 KB | Overwrites: Slot  26 | Hash Ops: 447509 | Time: 0.014s | ETA:  764.2s
[NODE-05] Block 127/500 | Index: 127 | Slot:  27 | Storage:  39.14 KB | Overwrites: Slot  27 | Hash Ops: 474809 | Time: 0.190s | ETA:  762.7s
[NODE-05] Block 128/500 | Index: 128 | Slot:  28 | Storage:  39.15 KB | Overwrites: Slot  28 | Hash Ops: 480493 | Time: 0.042s | ETA:  760.8s
[NODE-05] Block 129/500 | Index: 129 | Slot:  29 | Storage:  39.15 KB | Overwrites: Slot  29 | Hash Ops: 483127 | Time: 0.021s | ETA:  758.7s
[NODE-05] Block 130/500 | Index: 130 | Slot:  30 | Storage:  39.15 KB | Overwrites: Slot  30 | Hash Ops: 487274 | Time: 0.032s | ETA:  756.7s
[NODE-05] Block 131/500 | Index: 131 | Slot:  31 | Storage:  39.15 KB | Overwrites: Slot  31 | Hash Ops: 488076 | Time: 0.009s | ETA:  755.0s
[NODE-05] Block 132/500 | Index: 132 | Slot:  32 | Storage:  39.15 KB | Overwrites: Slot  32 | Hash Ops: 503234 | Time: 0.103s | ETA:  753.1s
[NODE-05] Block 133/500 | Index: 133 | Slot:  33 | Storage:  39.15 KB | Overwrites: Slot  33 | Hash Ops: 504401 | Time: 0.012s | ETA:  751.0s
[NODE-05] Block 134/500 | Index: 134 | Slot:  34 | Storage:  39.16 KB | Overwrites: Slot  34 | Hash Ops: 517090 | Time: 0.089s | ETA:  749.2s
[NODE-05] Block 135/500 | Index: 135 | Slot:  35 | Storage:  39.16 KB | Overwrites: Slot  35 | Hash Ops: 520093 | Time: 0.019s | ETA:  747.1s
[NODE-05] Block 136/500 | Index: 136 | Slot:  36 | Storage:  39.16 KB | Overwrites: Slot  36 | Hash Ops: 521887 | Time: 0.015s | ETA:  745.0s
[NODE-05] Block 137/500 | Index: 137 | Slot:  37 | Storage:  39.16 KB | Overwrites: Slot  37 | Hash Ops: 522462 | Time: 0.006s | ETA:  742.9s
[NODE-05] Block 138/500 | Index: 138 | Slot:  38 | Storage:  39.16 KB | Overwrites: Slot  38 | Hash Ops: 524310 | Time: 0.013s | ETA:  740.8s
[NODE-05] Block 139/500 | Index: 139 | Slot:  39 | Storage:  39.16 KB | Overwrites: Slot  39 | Hash Ops: 527882 | Time: 0.026s | ETA:  738.7s
[NODE-05] Block 140/500 | Index: 140 | Slot:  40 | Storage:  39.16 KB | Overwrites: Slot  40 | Hash Ops: 530531 | Time: 0.018s | ETA:  736.6s
[NODE-05] Block 141/500 | Index: 141 | Slot:  41 | Storage:  39.17 KB | Overwrites: Slot  41 | Hash Ops: 531541 | Time: 0.007s | ETA:  734.7s
[NODE-05] Block 142/500 | Index: 142 | Slot:  42 | Storage:  39.17 KB | Overwrites: Slot  42 | Hash Ops: 534184 | Time: 0.025s | ETA:  732.7s
[NODE-05] Block 143/500 | Index: 143 | Slot:  43 | Storage:  39.18 KB | Overwrites: Slot  43 | Hash Ops: 534856 | Time: 0.012s | ETA:  730.6s
[NODE-05] Block 144/500 | Index: 144 | Slot:  44 | Storage:  39.18 KB | Overwrites: Slot  44 | Hash Ops: 535198 | Time: 0.006s | ETA:  728.5s
[NODE-05] Block 145/500 | Index: 145 | Slot:  45 | Storage:  39.18 KB | Overwrites: Slot  45 | Hash Ops: 547567 | Time: 0.086s | ETA:  726.5s
[NODE-05] Block 146/500 | Index: 146 | Slot:  46 | Storage:  39.18 KB | Overwrites: Slot  46 | Hash Ops: 548805 | Time: 0.012s | ETA:  724.5s
[NODE-05] Block 147/500 | Index: 147 | Slot:  47 | Storage:  39.19 KB | Overwrites: Slot  47 | Hash Ops: 550816 | Time: 0.017s | ETA:  722.4s
[NODE-05] Block 148/500 | Index: 148 | Slot:  48 | Storage:  39.19 KB | Overwrites: Slot  48 | Hash Ops: 565032 | Time: 0.097s | ETA:  720.5s
[NODE-05] Block 149/500 | Index: 149 | Slot:  49 | Storage:  39.19 KB | Overwrites: Slot  49 | Hash Ops: 566703 | Time: 0.011s | ETA:  718.5s
[NODE-05] Block 150/500 | Index: 150 | Slot:  50 | Storage:  39.20 KB | Overwrites: Slot  50 | Hash Ops: 567749 | Time: 0.007s | ETA:  716.4s
[NODE-05] Block 151/500 | Index: 151 | Slot:  51 | Storage:  39.20 KB | Overwrites: Slot  51 | Hash Ops: 569419 | Time: 0.016s | ETA:  714.6s
[NODE-05] Block 152/500 | Index: 152 | Slot:  52 | Storage:  39.20 KB | Overwrites: Slot  52 | Hash Ops: 571011 | Time: 0.019s | ETA:  712.5s
[NODE-05] Block 153/500 | Index: 153 | Slot:  53 | Storage:  39.20 KB | Overwrites: Slot  53 | Hash Ops: 578681 | Time: 0.055s | ETA:  710.5s
[NODE-05] Block 154/500 | Index: 154 | Slot:  54 | Storage:  39.21 KB | Overwrites: Slot  54 | Hash Ops: 580333 | Time: 0.011s | ETA:  708.4s
[NODE-05] Block 155/500 | Index: 155 | Slot:  55 | Storage:  39.21 KB | Overwrites: Slot  55 | Hash Ops: 581522 | Time: 0.011s | ETA:  706.3s
[NODE-05] Block 156/500 | Index: 156 | Slot:  56 | Storage:  39.21 KB | Overwrites: Slot  56 | Hash Ops: 586565 | Time: 0.035s | ETA:  704.2s
[NODE-05] Block 157/500 | Index: 157 | Slot:  57 | Storage:  39.21 KB | Overwrites: Slot  57 | Hash Ops: 600969 | Time: 0.100s | ETA:  702.3s
[NODE-05] Block 158/500 | Index: 158 | Slot:  58 | Storage:  39.22 KB | Overwrites: Slot  58 | Hash Ops: 605166 | Time: 0.032s | ETA:  700.3s
[NODE-05] Block 159/500 | Index: 159 | Slot:  59 | Storage:  39.22 KB | Overwrites: Slot  59 | Hash Ops: 610816 | Time: 0.045s | ETA:  698.2s
[NODE-05] Block 160/500 | Index: 160 | Slot:  60 | Storage:  39.22 KB | Overwrites: Slot  60 | Hash Ops: 611158 | Time: 0.006s | ETA:  696.2s
[NODE-05] Block 161/500 | Index: 161 | Slot:  61 | Storage:  39.22 KB | Overwrites: Slot  61 | Hash Ops: 611368 | Time: 0.005s | ETA:  694.4s
[NODE-05] Block 162/500 | Index: 162 | Slot:  62 | Storage:  39.22 KB | Overwrites: Slot  62 | Hash Ops: 617247 | Time: 0.042s | ETA:  692.4s
[NODE-05] Block 163/500 | Index: 163 | Slot:  63 | Storage:  39.22 KB | Overwrites: Slot  63 | Hash Ops: 621644 | Time: 0.036s | ETA:  690.3s
[NODE-05] Block 164/500 | Index: 164 | Slot:  64 | Storage:  39.23 KB | Overwrites: Slot  64 | Hash Ops: 624600 | Time: 0.023s | ETA:  688.3s
[NODE-05] Block 165/500 | Index: 165 | Slot:  65 | Storage:  39.23 KB | Overwrites: Slot  65 | Hash Ops: 625419 | Time: 0.007s | ETA:  686.2s
[NODE-05] Block 166/500 | Index: 166 | Slot:  66 | Storage:  39.24 KB | Overwrites: Slot  66 | Hash Ops: 628926 | Time: 0.031s | ETA:  684.1s
[NODE-05] Block 167/500 | Index: 167 | Slot:  67 | Storage:  39.24 KB | Overwrites: Slot  67 | Hash Ops: 634939 | Time: 0.040s | ETA:  682.1s
[NODE-05] Block 168/500 | Index: 168 | Slot:  68 | Storage:  39.24 KB | Overwrites: Slot  68 | Hash Ops: 638871 | Time: 0.029s | ETA:  680.0s
[NODE-05] Block 169/500 | Index: 169 | Slot:  69 | Storage:  39.24 KB | Overwrites: Slot  69 | Hash Ops: 647871 | Time: 0.066s | ETA:  678.0s
[NODE-05] Block 170/500 | Index: 170 | Slot:  70 | Storage:  39.24 KB | Overwrites: Slot  70 | Hash Ops: 654733 | Time: 0.047s | ETA:  676.0s
[NODE-05] Block 171/500 | Index: 171 | Slot:  71 | Storage:  39.24 KB | Overwrites: Slot  71 | Hash Ops: 660366 | Time: 0.043s | ETA:  674.1s
[NODE-05] Block 172/500 | Index: 172 | Slot:  72 | Storage:  39.25 KB | Overwrites: Slot  72 | Hash Ops: 661802 | Time: 0.015s | ETA:  672.1s
[NODE-05] Block 173/500 | Index: 173 | Slot:  73 | Storage:  39.25 KB | Overwrites: Slot  73 | Hash Ops: 663488 | Time: 0.020s | ETA:  670.0s
[NODE-05] Block 174/500 | Index: 174 | Slot:  74 | Storage:  39.26 KB | Overwrites: Slot  74 | Hash Ops: 670690 | Time: 0.052s | ETA:  668.0s
[NODE-05] Block 175/500 | Index: 175 | Slot:  75 | Storage:  39.26 KB | Overwrites: Slot  75 | Hash Ops: 682950 | Time: 0.085s | ETA:  666.1s
[NODE-05] Block 176/500 | Index: 176 | Slot:  76 | Storage:  39.26 KB | Overwrites: Slot  76 | Hash Ops: 683935 | Time: 0.015s | ETA:  664.0s
[NODE-05] Block 177/500 | Index: 177 | Slot:  77 | Storage:  39.26 KB | Overwrites: Slot  77 | Hash Ops: 692668 | Time: 0.060s | ETA:  662.0s
[NODE-05] Block 178/500 | Index: 178 | Slot:  78 | Storage:  39.27 KB | Overwrites: Slot  78 | Hash Ops: 693532 | Time: 0.010s | ETA:  659.9s
[NODE-05] Block 179/500 | Index: 179 | Slot:  79 | Storage:  39.27 KB | Overwrites: Slot  79 | Hash Ops: 695498 | Time: 0.013s | ETA:  657.9s
[NODE-05] Block 180/500 | Index: 180 | Slot:  80 | Storage:  39.27 KB | Overwrites: Slot  80 | Hash Ops: 696982 | Time: 0.014s | ETA:  655.8s
[NODE-05] Block 181/500 | Index: 181 | Slot:  81 | Storage:  39.27 KB | Overwrites: Slot  81 | Hash Ops: 703516 | Time: 0.047s | ETA:  654.0s
[NODE-05] Block 182/500 | Index: 182 | Slot:  82 | Storage:  39.28 KB | Overwrites: Slot  82 | Hash Ops: 705682 | Time: 0.015s | ETA:  651.9s
[NODE-05] Block 183/500 | Index: 183 | Slot:  83 | Storage:  39.28 KB | Overwrites: Slot  83 | Hash Ops: 715611 | Time: 0.069s | ETA:  649.9s
[NODE-05] Block 184/500 | Index: 184 | Slot:  84 | Storage:  39.28 KB | Overwrites: Slot  84 | Hash Ops: 715801 | Time: 0.001s | ETA:  647.8s
[NODE-05] Block 185/500 | Index: 185 | Slot:  85 | Storage:  39.28 KB | Overwrites: Slot  85 | Hash Ops: 715995 | Time: 0.002s | ETA:  645.7s
[NODE-05] Block 186/500 | Index: 186 | Slot:  86 | Storage:  39.29 KB | Overwrites: Slot  86 | Hash Ops: 717710 | Time: 0.017s | ETA:  643.6s
[NODE-05] Block 187/500 | Index: 187 | Slot:  87 | Storage:  39.29 KB | Overwrites: Slot  87 | Hash Ops: 723793 | Time: 0.044s | ETA:  641.6s
[NODE-05] Block 188/500 | Index: 188 | Slot:  88 | Storage:  39.29 KB | Overwrites: Slot  88 | Hash Ops: 725581 | Time: 0.012s | ETA:  639.5s
[NODE-05] Block 189/500 | Index: 189 | Slot:  89 | Storage:  39.29 KB | Overwrites: Slot  89 | Hash Ops: 725667 | Time: 0.004s | ETA:  637.4s
[NODE-05] Block 190/500 | Index: 190 | Slot:  90 | Storage:  39.29 KB | Overwrites: Slot  90 | Hash Ops: 729388 | Time: 0.027s | ETA:  635.4s
[NODE-05] Block 191/500 | Index: 191 | Slot:  91 | Storage:  39.30 KB | Overwrites: Slot  91 | Hash Ops: 729470 | Time: 0.001s | ETA:  633.5s
[NODE-05] Block 192/500 | Index: 192 | Slot:  92 | Storage:  39.29 KB | Overwrites: Slot  92 | Hash Ops: 729547 | Time: 0.002s | ETA:  631.4s
[NODE-05] Block 193/500 | Index: 193 | Slot:  93 | Storage:  39.30 KB | Overwrites: Slot  93 | Hash Ops: 734906 | Time: 0.044s | ETA:  629.3s
[NODE-05] Block 194/500 | Index: 194 | Slot:  94 | Storage:  39.30 KB | Overwrites: Slot  94 | Hash Ops: 745269 | Time: 0.073s | ETA:  627.3s
[NODE-05] Block 195/500 | Index: 195 | Slot:  95 | Storage:  39.31 KB | Overwrites: Slot  95 | Hash Ops: 752780 | Time: 0.053s | ETA:  625.3s
[NODE-05] Block 196/500 | Index: 196 | Slot:  96 | Storage:  39.31 KB | Overwrites: Slot  96 | Hash Ops: 760649 | Time: 0.061s | ETA:  623.3s
[NODE-05] Block 197/500 | Index: 197 | Slot:  97 | Storage:  39.31 KB | Overwrites: Slot  97 | Hash Ops: 763316 | Time: 0.026s | ETA:  621.3s
[NODE-05] Block 198/500 | Index: 198 | Slot:  98 | Storage:  39.32 KB | Overwrites: Slot  98 | Hash Ops: 764439 | Time: 0.019s | ETA:  619.2s
[NODE-05] Block 199/500 | Index: 199 | Slot:  99 | Storage:  39.32 KB | Overwrites: Slot  99 | Hash Ops: 768134 | Time: 0.027s | ETA:  617.2s
[NODE-05] Block 200/500 | Index: 200 | Slot:   0 | Storage:  39.32 KB | Overwrites: Slot   0 | Hash Ops: 769326 | Time: 0.009s | ETA:  615.1s
[NODE-05] Block 201/500 | Index: 201 | Slot:   1 | Storage:  39.32 KB | Overwrites: Slot   1 | Hash Ops: 773520 | Time: 0.030s | ETA:  613.2s
[NODE-05] Block 202/500 | Index: 202 | Slot:   2 | Storage:  39.32 KB | Overwrites: Slot   2 | Hash Ops: 781408 | Time: 0.057s | ETA:  611.2s
[NODE-05] Block 203/500 | Index: 203 | Slot:   3 | Storage:  39.32 KB | Overwrites: Slot   3 | Hash Ops: 783932 | Time: 0.021s | ETA:  609.2s
[NODE-05] Block 204/500 | Index: 204 | Slot:   4 | Storage:  39.32 KB | Overwrites: Slot   4 | Hash Ops: 784704 | Time: 0.009s | ETA:  607.1s
[NODE-05] Block 205/500 | Index: 205 | Slot:   5 | Storage:  39.32 KB | Overwrites: Slot   5 | Hash Ops: 786558 | Time: 0.016s | ETA:  605.1s
[NODE-05] Block 206/500 | Index: 206 | Slot:   6 | Storage:  39.33 KB | Overwrites: Slot   6 | Hash Ops: 787884 | Time: 0.013s | ETA:  603.0s
[NODE-05] Block 207/500 | Index: 207 | Slot:   7 | Storage:  39.33 KB | Overwrites: Slot   7 | Hash Ops: 789638 | Time: 0.016s | ETA:  600.9s
[NODE-05] Block 208/500 | Index: 208 | Slot:   8 | Storage:  39.33 KB | Overwrites: Slot   8 | Hash Ops: 792473 | Time: 0.030s | ETA:  598.9s
[NODE-05] Block 209/500 | Index: 209 | Slot:   9 | Storage:  39.33 KB | Overwrites: Slot   9 | Hash Ops: 793341 | Time: 0.010s | ETA:  596.8s
[NODE-05] Block 210/500 | Index: 210 | Slot:  10 | Storage:  39.33 KB | Overwrites: Slot  10 | Hash Ops: 803154 | Time: 0.069s | ETA:  594.8s
[NODE-05] Block 211/500 | Index: 211 | Slot:  11 | Storage:  39.33 KB | Overwrites: Slot  11 | Hash Ops: 808720 | Time: 0.041s | ETA:  592.9s
[NODE-05] Block 212/500 | Index: 212 | Slot:  12 | Storage:  39.33 KB | Overwrites: Slot  12 | Hash Ops: 820366 | Time: 0.082s | ETA:  590.9s
[NODE-05] Block 213/500 | Index: 213 | Slot:  13 | Storage:  39.33 KB | Overwrites: Slot  13 | Hash Ops: 822134 | Time: 0.013s | ETA:  588.8s
[NODE-05] Block 214/500 | Index: 214 | Slot:  14 | Storage:  39.33 KB | Overwrites: Slot  14 | Hash Ops: 823566 | Time: 0.016s | ETA:  586.7s
[NODE-05] Block 215/500 | Index: 215 | Slot:  15 | Storage:  39.33 KB | Overwrites: Slot  15 | Hash Ops: 829017 | Time: 0.037s | ETA:  584.6s
[NODE-05] Block 216/500 | Index: 216 | Slot:  16 | Storage:  39.34 KB | Overwrites: Slot  16 | Hash Ops: 835790 | Time: 0.044s | ETA:  582.6s
[NODE-05] Block 217/500 | Index: 217 | Slot:  17 | Storage:  39.34 KB | Overwrites: Slot  17 | Hash Ops: 837396 | Time: 0.011s | ETA:  580.5s
[NODE-05] Block 218/500 | Index: 218 | Slot:  18 | Storage:  39.34 KB | Overwrites: Slot  18 | Hash Ops: 846318 | Time: 0.063s | ETA:  578.5s
[NODE-05] Block 219/500 | Index: 219 | Slot:  19 | Storage:  39.34 KB | Overwrites: Slot  19 | Hash Ops: 847572 | Time: 0.017s | ETA:  576.4s
[NODE-05] Block 220/500 | Index: 220 | Slot:  20 | Storage:  39.34 KB | Overwrites: Slot  20 | Hash Ops: 848850 | Time: 0.009s | ETA:  574.3s
[NODE-05] Block 221/500 | Index: 221 | Slot:  21 | Storage:  39.34 KB | Overwrites: Slot  21 | Hash Ops: 852192 | Time: 0.028s | ETA:  572.4s
[NODE-05] Block 222/500 | Index: 222 | Slot:  22 | Storage:  39.34 KB | Overwrites: Slot  22 | Hash Ops: 853495 | Time: 0.013s | ETA:  570.3s
[NODE-05] Block 223/500 | Index: 223 | Slot:  23 | Storage:  39.34 KB | Overwrites: Slot  23 | Hash Ops: 854181 | Time: 0.008s | ETA:  568.3s
[NODE-05] Block 224/500 | Index: 224 | Slot:  24 | Storage:  39.34 KB | Overwrites: Slot  24 | Hash Ops: 855884 | Time: 0.021s | ETA:  566.2s
[NODE-05] Block 225/500 | Index: 225 | Slot:  25 | Storage:  39.34 KB | Overwrites: Slot  25 | Hash Ops: 855897 | Time: 0.000s | ETA:  564.1s
[NODE-05] Block 226/500 | Index: 226 | Slot:  26 | Storage:  39.34 KB | Overwrites: Slot  26 | Hash Ops: 862056 | Time: 0.044s | ETA:  562.1s
[NODE-05] Block 227/500 | Index: 227 | Slot:  27 | Storage:  39.33 KB | Overwrites: Slot  27 | Hash Ops: 864433 | Time: 0.017s | ETA:  560.0s
[NODE-05] Block 228/500 | Index: 228 | Slot:  28 | Storage:  39.33 KB | Overwrites: Slot  28 | Hash Ops: 870529 | Time: 0.043s | ETA:  557.9s
[NODE-05] Block 229/500 | Index: 229 | Slot:  29 | Storage:  39.34 KB | Overwrites: Slot  29 | Hash Ops: 880763 | Time: 0.072s | ETA:  556.0s
[NODE-05] Block 230/500 | Index: 230 | Slot:  30 | Storage:  39.34 KB | Overwrites: Slot  30 | Hash Ops: 881914 | Time: 0.009s | ETA:  553.9s
[NODE-05] Block 231/500 | Index: 231 | Slot:  31 | Storage:  39.34 KB | Overwrites: Slot  31 | Hash Ops: 884979 | Time: 0.026s | ETA:  552.0s
[NODE-05] Block 232/500 | Index: 232 | Slot:  32 | Storage:  39.34 KB | Overwrites: Slot  32 | Hash Ops: 888129 | Time: 0.024s | ETA:  549.9s
[NODE-05] Block 233/500 | Index: 233 | Slot:  33 | Storage:  39.34 KB | Overwrites: Slot  33 | Hash Ops: 889421 | Time: 0.013s | ETA:  547.8s
[NODE-05] Block 234/500 | Index: 234 | Slot:  34 | Storage:  39.34 KB | Overwrites: Slot  34 | Hash Ops: 897765 | Time: 0.061s | ETA:  545.8s
[NODE-05] Block 235/500 | Index: 235 | Slot:  35 | Storage:  39.34 KB | Overwrites: Slot  35 | Hash Ops: 902760 | Time: 0.034s | ETA:  543.7s
[NODE-05] Block 236/500 | Index: 236 | Slot:  36 | Storage:  39.34 KB | Overwrites: Slot  36 | Hash Ops: 905257 | Time: 0.021s | ETA:  541.6s
[NODE-05] Block 237/500 | Index: 237 | Slot:  37 | Storage:  39.34 KB | Overwrites: Slot  37 | Hash Ops: 908714 | Time: 0.028s | ETA:  539.5s
[NODE-05] Block 238/500 | Index: 238 | Slot:  38 | Storage:  39.34 KB | Overwrites: Slot  38 | Hash Ops: 911504 | Time: 0.027s | ETA:  537.5s
[NODE-05] Block 239/500 | Index: 239 | Slot:  39 | Storage:  39.35 KB | Overwrites: Slot  39 | Hash Ops: 913802 | Time: 0.020s | ETA:  535.4s
[NODE-05] Block 240/500 | Index: 240 | Slot:  40 | Storage:  39.35 KB | Overwrites: Slot  40 | Hash Ops: 915781 | Time: 0.014s | ETA:  533.3s
[NODE-05] Block 241/500 | Index: 241 | Slot:  41 | Storage:  39.34 KB | Overwrites: Slot  41 | Hash Ops: 917702 | Time: 0.016s | ETA:  531.4s
[NODE-05] Block 242/500 | Index: 242 | Slot:  42 | Storage:  39.34 KB | Overwrites: Slot  42 | Hash Ops: 927697 | Time: 0.071s | ETA:  529.4s
[NODE-05] Block 243/500 | Index: 243 | Slot:  43 | Storage:  39.35 KB | Overwrites: Slot  43 | Hash Ops: 940459 | Time: 0.089s | ETA:  527.4s
[NODE-05] Block 244/500 | Index: 244 | Slot:  44 | Storage:  39.35 KB | Overwrites: Slot  44 | Hash Ops: 944517 | Time: 0.030s | ETA:  525.3s
[NODE-05] Block 245/500 | Index: 245 | Slot:  45 | Storage:  39.35 KB | Overwrites: Slot  45 | Hash Ops: 951253 | Time: 0.045s | ETA:  523.3s
[NODE-05] Block 246/500 | Index: 246 | Slot:  46 | Storage:  39.35 KB | Overwrites: Slot  46 | Hash Ops: 952360 | Time: 0.012s | ETA:  521.2s
[NODE-05] Block 247/500 | Index: 247 | Slot:  47 | Storage:  39.35 KB | Overwrites: Slot  47 | Hash Ops: 958323 | Time: 0.045s | ETA:  519.2s
[NODE-05] Block 248/500 | Index: 248 | Slot:  48 | Storage:  39.35 KB | Overwrites: Slot  48 | Hash Ops: 959960 | Time: 0.019s | ETA:  517.1s
[NODE-05] Block 249/500 | Index: 249 | Slot:  49 | Storage:  39.35 KB | Overwrites: Slot  49 | Hash Ops: 960467 | Time: 0.007s | ETA:  515.0s
[NODE-05] Block 250/500 | Index: 250 | Slot:  50 | Storage:  39.35 KB | Overwrites: Slot  50 | Hash Ops: 963861 | Time: 0.026s | ETA:  512.9s
[NODE-05] Block 251/500 | Index: 251 | Slot:  51 | Storage:  39.35 KB | Overwrites: Slot  51 | Hash Ops: 970732 | Time: 0.055s | ETA:  511.0s
[NODE-05] Block 252/500 | Index: 252 | Slot:  52 | Storage:  39.35 KB | Overwrites: Slot  52 | Hash Ops: 970943 | Time: 0.005s | ETA:  508.9s
[NODE-05] Block 253/500 | Index: 253 | Slot:  53 | Storage:  39.35 KB | Overwrites: Slot  53 | Hash Ops: 973176 | Time: 0.018s | ETA:  506.9s
[NODE-05] Block 254/500 | Index: 254 | Slot:  54 | Storage:  39.35 KB | Overwrites: Slot  54 | Hash Ops: 982230 | Time: 0.060s | ETA:  504.8s
[NODE-05] Block 255/500 | Index: 255 | Slot:  55 | Storage:  39.35 KB | Overwrites: Slot  55 | Hash Ops: 982997 | Time: 0.005s | ETA:  502.7s
[NODE-05] Block 256/500 | Index: 256 | Slot:  56 | Storage:  39.35 KB | Overwrites: Slot  56 | Hash Ops: 987148 | Time: 0.032s | ETA:  500.7s
[NODE-05] Block 257/500 | Index: 257 | Slot:  57 | Storage:  39.35 KB | Overwrites: Slot  57 | Hash Ops: 993562 | Time: 0.046s | ETA:  498.7s
[NODE-05] Block 258/500 | Index: 258 | Slot:  58 | Storage:  39.35 KB | Overwrites: Slot  58 | Hash Ops: 993783 | Time: 0.005s | ETA:  496.6s
[NODE-05] Block 259/500 | Index: 259 | Slot:  59 | Storage:  39.35 KB | Overwrites: Slot  59 | Hash Ops: 997451 | Time: 0.033s | ETA:  494.5s
[NODE-05] Block 260/500 | Index: 260 | Slot:  60 | Storage:  39.35 KB | Overwrites: Slot  60 | Hash Ops: 999634 | Time: 0.017s | ETA:  492.5s
[NODE-05] Block 261/500 | Index: 261 | Slot:  61 | Storage:  39.35 KB | Overwrites: Slot  61 | Hash Ops: 1003545 | Time: 0.030s | ETA:  490.5s
[NODE-05] Block 262/500 | Index: 262 | Slot:  62 | Storage:  39.35 KB | Overwrites: Slot  62 | Hash Ops: 1017552 | Time: 0.102s | ETA:  488.5s
[NODE-05] Block 263/500 | Index: 263 | Slot:  63 | Storage:  39.35 KB | Overwrites: Slot  63 | Hash Ops: 1029380 | Time: 0.082s | ETA:  486.5s
[NODE-05] Block 264/500 | Index: 264 | Slot:  64 | Storage:  39.35 KB | Overwrites: Slot  64 | Hash Ops: 1034206 | Time: 0.032s | ETA:  484.4s
[NODE-05] Block 265/500 | Index: 265 | Slot:  65 | Storage:  39.35 KB | Overwrites: Slot  65 | Hash Ops: 1043730 | Time: 0.068s | ETA:  482.4s
[NODE-05] Block 266/500 | Index: 266 | Slot:  66 | Storage:  39.35 KB | Overwrites: Slot  66 | Hash Ops: 1045020 | Time: 0.012s | ETA:  480.3s
[NODE-05] Block 267/500 | Index: 267 | Slot:  67 | Storage:  39.35 KB | Overwrites: Slot  67 | Hash Ops: 1045926 | Time: 0.010s | ETA:  478.3s
[NODE-05] Block 268/500 | Index: 268 | Slot:  68 | Storage:  39.35 KB | Overwrites: Slot  68 | Hash Ops: 1048957 | Time: 0.020s | ETA:  476.2s
[NODE-05] Block 269/500 | Index: 269 | Slot:  69 | Storage:  39.35 KB | Overwrites: Slot  69 | Hash Ops: 1053505 | Time: 0.034s | ETA:  474.1s
[NODE-05] Block 270/500 | Index: 270 | Slot:  70 | Storage:  39.35 KB | Overwrites: Slot  70 | Hash Ops: 1056277 | Time: 0.023s | ETA:  472.1s
[NODE-05] Block 271/500 | Index: 271 | Slot:  71 | Storage:  39.35 KB | Overwrites: Slot  71 | Hash Ops: 1063454 | Time: 0.051s | ETA:  470.1s
[NODE-05] Block 272/500 | Index: 272 | Slot:  72 | Storage:  39.35 KB | Overwrites: Slot  72 | Hash Ops: 1065893 | Time: 0.016s | ETA:  468.0s
[NODE-05] Block 273/500 | Index: 273 | Slot:  73 | Storage:  39.35 KB | Overwrites: Slot  73 | Hash Ops: 1066468 | Time: 0.007s | ETA:  466.0s
[NODE-05] Block 274/500 | Index: 274 | Slot:  74 | Storage:  39.35 KB | Overwrites: Slot  74 | Hash Ops: 1069508 | Time: 0.040s | ETA:  463.9s
[NODE-05] Block 275/500 | Index: 275 | Slot:  75 | Storage:  39.35 KB | Overwrites: Slot  75 | Hash Ops: 1074056 | Time: 0.041s | ETA:  461.9s
[NODE-05] Block 276/500 | Index: 276 | Slot:  76 | Storage:  39.36 KB | Overwrites: Slot  76 | Hash Ops: 1076825 | Time: 0.031s | ETA:  459.8s
[NODE-05] Block 277/500 | Index: 277 | Slot:  77 | Storage:  39.36 KB | Overwrites: Slot  77 | Hash Ops: 1080784 | Time: 0.041s | ETA:  457.8s
[NODE-05] Block 278/500 | Index: 278 | Slot:  78 | Storage:  39.36 KB | Overwrites: Slot  78 | Hash Ops: 1081959 | Time: 0.008s | ETA:  455.7s
[NODE-05] Block 279/500 | Index: 279 | Slot:  79 | Storage:  39.36 KB | Overwrites: Slot  79 | Hash Ops: 1082158 | Time: 0.004s | ETA:  453.6s
[NODE-05] Block 280/500 | Index: 280 | Slot:  80 | Storage:  39.36 KB | Overwrites: Slot  80 | Hash Ops: 1084934 | Time: 0.023s | ETA:  451.6s
[NODE-05] Block 281/500 | Index: 281 | Slot:  81 | Storage:  39.36 KB | Overwrites: Slot  81 | Hash Ops: 1086365 | Time: 0.010s | ETA:  449.6s
[NODE-05] Block 282/500 | Index: 282 | Slot:  82 | Storage:  39.35 KB | Overwrites: Slot  82 | Hash Ops: 1086512 | Time: 0.004s | ETA:  447.5s
[NODE-05] Block 283/500 | Index: 283 | Slot:  83 | Storage:  39.35 KB | Overwrites: Slot  83 | Hash Ops: 1091931 | Time: 0.046s | ETA:  445.4s
[NODE-05] Block 284/500 | Index: 284 | Slot:  84 | Storage:  39.35 KB | Overwrites: Slot  84 | Hash Ops: 1096748 | Time: 0.041s | ETA:  443.4s
[NODE-05] Block 285/500 | Index: 285 | Slot:  85 | Storage:  39.35 KB | Overwrites: Slot  85 | Hash Ops: 1097905 | Time: 0.008s | ETA:  441.3s
[NODE-05] Block 286/500 | Index: 286 | Slot:  86 | Storage:  39.35 KB | Overwrites: Slot  86 | Hash Ops: 1104539 | Time: 0.075s | ETA:  439.3s
[NODE-05] Block 287/500 | Index: 287 | Slot:  87 | Storage:  39.35 KB | Overwrites: Slot  87 | Hash Ops: 1115886 | Time: 0.082s | ETA:  437.2s
[NODE-05] Block 288/500 | Index: 288 | Slot:  88 | Storage:  39.35 KB | Overwrites: Slot  88 | Hash Ops: 1116239 | Time: 0.008s | ETA:  435.2s
[NODE-05] Block 289/500 | Index: 289 | Slot:  89 | Storage:  39.35 KB | Overwrites: Slot  89 | Hash Ops: 1118311 | Time: 0.029s | ETA:  433.1s
[NODE-05] Block 290/500 | Index: 290 | Slot:  90 | Storage:  39.35 KB | Overwrites: Slot  90 | Hash Ops: 1118784 | Time: 0.010s | ETA:  431.0s
[NODE-05] Block 291/500 | Index: 291 | Slot:  91 | Storage:  39.36 KB | Overwrites: Slot  91 | Hash Ops: 1121353 | Time: 0.035s | ETA:  429.1s
[NODE-05] Block 292/500 | Index: 292 | Slot:  92 | Storage:  39.36 KB | Overwrites: Slot  92 | Hash Ops: 1123980 | Time: 0.040s | ETA:  427.0s
[NODE-05] Block 293/500 | Index: 293 | Slot:  93 | Storage:  39.36 KB | Overwrites: Slot  93 | Hash Ops: 1125265 | Time: 0.024s | ETA:  425.0s
[NODE-05] Block 294/500 | Index: 294 | Slot:  94 | Storage:  39.36 KB | Overwrites: Slot  94 | Hash Ops: 1125960 | Time: 0.008s | ETA:  422.9s
[NODE-05] Block 295/500 | Index: 295 | Slot:  95 | Storage:  39.36 KB | Overwrites: Slot  95 | Hash Ops: 1137303 | Time: 0.083s | ETA:  420.9s
[NODE-05] Block 296/500 | Index: 296 | Slot:  96 | Storage:  39.36 KB | Overwrites: Slot  96 | Hash Ops: 1137498 | Time: 0.003s | ETA:  418.8s
[NODE-05] Block 297/500 | Index: 297 | Slot:  97 | Storage:  39.36 KB | Overwrites: Slot  97 | Hash Ops: 1138615 | Time: 0.011s | ETA:  416.8s
[NODE-05] Block 298/500 | Index: 298 | Slot:  98 | Storage:  39.36 KB | Overwrites: Slot  98 | Hash Ops: 1141574 | Time: 0.021s | ETA:  414.7s
[NODE-05] Block 299/500 | Index: 299 | Slot:  99 | Storage:  39.36 KB | Overwrites: Slot  99 | Hash Ops: 1150241 | Time: 0.058s | ETA:  412.7s
[NODE-05] Block 300/500 | Index: 300 | Slot:   0 | Storage:  39.36 KB | Overwrites: Slot   0 | Hash Ops: 1154677 | Time: 0.033s | ETA:  410.6s
[NODE-05] Block 301/500 | Index: 301 | Slot:   1 | Storage:  39.36 KB | Overwrites: Slot   1 | Hash Ops: 1155101 | Time: 0.003s | ETA:  408.6s
[NODE-05] Block 302/500 | Index: 302 | Slot:   2 | Storage:  39.36 KB | Overwrites: Slot   2 | Hash Ops: 1161193 | Time: 0.041s | ETA:  406.6s
[NODE-05] Block 303/500 | Index: 303 | Slot:   3 | Storage:  39.36 KB | Overwrites: Slot   3 | Hash Ops: 1172612 | Time: 0.080s | ETA:  404.5s
[NODE-05] Block 304/500 | Index: 304 | Slot:   4 | Storage:  39.36 KB | Overwrites: Slot   4 | Hash Ops: 1179225 | Time: 0.052s | ETA:  402.5s
[NODE-05] Block 305/500 | Index: 305 | Slot:   5 | Storage:  39.36 KB | Overwrites: Slot   5 | Hash Ops: 1183412 | Time: 0.029s | ETA:  400.4s
[NODE-05] Block 306/500 | Index: 306 | Slot:   6 | Storage:  39.36 KB | Overwrites: Slot   6 | Hash Ops: 1185000 | Time: 0.014s | ETA:  398.4s
[NODE-05] Block 307/500 | Index: 307 | Slot:   7 | Storage:  39.36 KB | Overwrites: Slot   7 | Hash Ops: 1187019 | Time: 0.017s | ETA:  396.3s
[NODE-05] Block 308/500 | Index: 308 | Slot:   8 | Storage:  39.36 KB | Overwrites: Slot   8 | Hash Ops: 1189255 | Time: 0.015s | ETA:  394.2s
[NODE-05] Block 309/500 | Index: 309 | Slot:   9 | Storage:  39.36 KB | Overwrites: Slot   9 | Hash Ops: 1192734 | Time: 0.028s | ETA:  392.2s
[NODE-05] Block 310/500 | Index: 310 | Slot:  10 | Storage:  39.36 KB | Overwrites: Slot  10 | Hash Ops: 1195904 | Time: 0.021s | ETA:  390.1s
[NODE-05] Block 311/500 | Index: 311 | Slot:  11 | Storage:  39.36 KB | Overwrites: Slot  11 | Hash Ops: 1196904 | Time: 0.011s | ETA:  388.1s
[NODE-05] Block 312/500 | Index: 312 | Slot:  12 | Storage:  39.36 KB | Overwrites: Slot  12 | Hash Ops: 1197220 | Time: 0.007s | ETA:  386.0s
[NODE-05] Block 313/500 | Index: 313 | Slot:  13 | Storage:  39.36 KB | Overwrites: Slot  13 | Hash Ops: 1201447 | Time: 0.030s | ETA:  384.0s
[NODE-05] Block 314/500 | Index: 314 | Slot:  14 | Storage:  39.36 KB | Overwrites: Slot  14 | Hash Ops: 1204271 | Time: 0.024s | ETA:  381.9s
[NODE-05] Block 315/500 | Index: 315 | Slot:  15 | Storage:  39.36 KB | Overwrites: Slot  15 | Hash Ops: 1204823 | Time: 0.012s | ETA:  379.8s
[NODE-05] Block 316/500 | Index: 316 | Slot:  16 | Storage:  39.36 KB | Overwrites: Slot  16 | Hash Ops: 1207161 | Time: 0.019s | ETA:  377.8s
[NODE-05] Block 317/500 | Index: 317 | Slot:  17 | Storage:  39.36 KB | Overwrites: Slot  17 | Hash Ops: 1208202 | Time: 0.012s | ETA:  375.7s
[NODE-05] Block 318/500 | Index: 318 | Slot:  18 | Storage:  39.36 KB | Overwrites: Slot  18 | Hash Ops: 1210118 | Time: 0.013s | ETA:  373.7s
[NODE-05] Block 319/500 | Index: 319 | Slot:  19 | Storage:  39.35 KB | Overwrites: Slot  19 | Hash Ops: 1210965 | Time: 0.007s | ETA:  371.6s
[NODE-05] Block 320/500 | Index: 320 | Slot:  20 | Storage:  39.35 KB | Overwrites: Slot  20 | Hash Ops: 1213275 | Time: 0.019s | ETA:  369.5s
[NODE-05] Block 321/500 | Index: 321 | Slot:  21 | Storage:  39.36 KB | Overwrites: Slot  21 | Hash Ops: 1218384 | Time: 0.042s | ETA:  367.5s
[NODE-05] Block 322/500 | Index: 322 | Slot:  22 | Storage:  39.36 KB | Overwrites: Slot  22 | Hash Ops: 1223485 | Time: 0.038s | ETA:  365.5s
[NODE-05] Block 323/500 | Index: 323 | Slot:  23 | Storage:  39.36 KB | Overwrites: Slot  23 | Hash Ops: 1226877 | Time: 0.026s | ETA:  363.4s
[NODE-05] Block 324/500 | Index: 324 | Slot:  24 | Storage:  39.36 KB | Overwrites: Slot  24 | Hash Ops: 1229140 | Time: 0.019s | ETA:  361.3s
[NODE-05] Block 325/500 | Index: 325 | Slot:  25 | Storage:  39.36 KB | Overwrites: Slot  25 | Hash Ops: 1237449 | Time: 0.057s | ETA:  359.3s
[NODE-05] Block 326/500 | Index: 326 | Slot:  26 | Storage:  39.36 KB | Overwrites: Slot  26 | Hash Ops: 1243918 | Time: 0.044s | ETA:  357.2s
[NODE-05] Block 327/500 | Index: 327 | Slot:  27 | Storage:  39.36 KB | Overwrites: Slot  27 | Hash Ops: 1250961 | Time: 0.053s | ETA:  355.2s
[NODE-05] Block 328/500 | Index: 328 | Slot:  28 | Storage:  39.36 KB | Overwrites: Slot  28 | Hash Ops: 1255452 | Time: 0.030s | ETA:  353.1s
[NODE-05] Block 329/500 | Index: 329 | Slot:  29 | Storage:  39.36 KB | Overwrites: Slot  29 | Hash Ops: 1258518 | Time: 0.024s | ETA:  351.1s
[NODE-05] Block 330/500 | Index: 330 | Slot:  30 | Storage:  39.36 KB | Overwrites: Slot  30 | Hash Ops: 1270578 | Time: 0.085s | ETA:  349.1s
[NODE-05] Block 331/500 | Index: 331 | Slot:  31 | Storage:  39.36 KB | Overwrites: Slot  31 | Hash Ops: 1271351 | Time: 0.009s | ETA:  347.0s
[NODE-05] Block 332/500 | Index: 332 | Slot:  32 | Storage:  39.36 KB | Overwrites: Slot  32 | Hash Ops: 1274917 | Time: 0.026s | ETA:  345.0s
[NODE-05] Block 333/500 | Index: 333 | Slot:  33 | Storage:  39.36 KB | Overwrites: Slot  33 | Hash Ops: 1276689 | Time: 0.012s | ETA:  342.9s
[NODE-05] Block 334/500 | Index: 334 | Slot:  34 | Storage:  39.36 KB | Overwrites: Slot  34 | Hash Ops: 1277821 | Time: 0.008s | ETA:  340.9s
[NODE-05] Block 335/500 | Index: 335 | Slot:  35 | Storage:  39.36 KB | Overwrites: Slot  35 | Hash Ops: 1279478 | Time: 0.016s | ETA:  338.8s
[NODE-05] Block 336/500 | Index: 336 | Slot:  36 | Storage:  39.36 KB | Overwrites: Slot  36 | Hash Ops: 1289688 | Time: 0.070s | ETA:  336.8s
[NODE-05] Block 337/500 | Index: 337 | Slot:  37 | Storage:  39.36 KB | Overwrites: Slot  37 | Hash Ops: 1291895 | Time: 0.019s | ETA:  334.7s
[NODE-05] Block 338/500 | Index: 338 | Slot:  38 | Storage:  39.36 KB | Overwrites: Slot  38 | Hash Ops: 1293637 | Time: 0.014s | ETA:  332.7s
[NODE-05] Block 339/500 | Index: 339 | Slot:  39 | Storage:  39.36 KB | Overwrites: Slot  39 | Hash Ops: 1295126 | Time: 0.014s | ETA:  330.6s
[NODE-05] Block 340/500 | Index: 340 | Slot:  40 | Storage:  39.36 KB | Overwrites: Slot  40 | Hash Ops: 1307881 | Time: 0.086s | ETA:  328.6s
[NODE-05] Block 341/500 | Index: 341 | Slot:  41 | Storage:  39.36 KB | Overwrites: Slot  41 | Hash Ops: 1308202 | Time: 0.008s | ETA:  326.5s
[NODE-05] Block 342/500 | Index: 342 | Slot:  42 | Storage:  39.36 KB | Overwrites: Slot  42 | Hash Ops: 1308721 | Time: 0.008s | ETA:  324.5s
[NODE-05] Block 343/500 | Index: 343 | Slot:  43 | Storage:  39.36 KB | Overwrites: Slot  43 | Hash Ops: 1311740 | Time: 0.029s | ETA:  322.4s
[NODE-05] Block 344/500 | Index: 344 | Slot:  44 | Storage:  39.36 KB | Overwrites: Slot  44 | Hash Ops: 1312924 | Time: 0.016s | ETA:  320.4s
[NODE-05] Block 345/500 | Index: 345 | Slot:  45 | Storage:  39.36 KB | Overwrites: Slot  45 | Hash Ops: 1316027 | Time: 0.024s | ETA:  318.3s
[NODE-05] Block 346/500 | Index: 346 | Slot:  46 | Storage:  39.36 KB | Overwrites: Slot  46 | Hash Ops: 1319952 | Time: 0.030s | ETA:  316.3s
[NODE-05] Block 347/500 | Index: 347 | Slot:  47 | Storage:  39.36 KB | Overwrites: Slot  47 | Hash Ops: 1320759 | Time: 0.006s | ETA:  314.2s
[NODE-05] Block 348/500 | Index: 348 | Slot:  48 | Storage:  39.36 KB | Overwrites: Slot  48 | Hash Ops: 1323190 | Time: 0.017s | ETA:  312.2s
[NODE-05] Block 349/500 | Index: 349 | Slot:  49 | Storage:  39.36 KB | Overwrites: Slot  49 | Hash Ops: 1323732 | Time: 0.004s | ETA:  310.1s
[NODE-05] Block 350/500 | Index: 350 | Slot:  50 | Storage:  39.36 KB | Overwrites: Slot  50 | Hash Ops: 1323894 | Time: 0.001s | ETA:  308.1s
[NODE-05] Block 351/500 | Index: 351 | Slot:  51 | Storage:  39.36 KB | Overwrites: Slot  51 | Hash Ops: 1326394 | Time: 0.018s | ETA:  306.0s
[NODE-05] Block 352/500 | Index: 352 | Slot:  52 | Storage:  39.36 KB | Overwrites: Slot  52 | Hash Ops: 1336640 | Time: 0.077s | ETA:  304.0s
[NODE-05] Block 353/500 | Index: 353 | Slot:  53 | Storage:  39.36 KB | Overwrites: Slot  53 | Hash Ops: 1336933 | Time: 0.002s | ETA:  302.0s
[NODE-05] Block 354/500 | Index: 354 | Slot:  54 | Storage:  39.36 KB | Overwrites: Slot  54 | Hash Ops: 1337718 | Time: 0.005s | ETA:  299.9s
[NODE-05] Block 355/500 | Index: 355 | Slot:  55 | Storage:  39.36 KB | Overwrites: Slot  55 | Hash Ops: 1338312 | Time: 0.009s | ETA:  297.8s
[NODE-05] Block 356/500 | Index: 356 | Slot:  56 | Storage:  39.36 KB | Overwrites: Slot  56 | Hash Ops: 1344531 | Time: 0.050s | ETA:  295.8s
[NODE-05] Block 357/500 | Index: 357 | Slot:  57 | Storage:  39.36 KB | Overwrites: Slot  57 | Hash Ops: 1352280 | Time: 0.059s | ETA:  293.7s
[NODE-05] Block 358/500 | Index: 358 | Slot:  58 | Storage:  39.36 KB | Overwrites: Slot  58 | Hash Ops: 1353764 | Time: 0.014s | ETA:  291.7s
[NODE-05] Block 359/500 | Index: 359 | Slot:  59 | Storage:  39.36 KB | Overwrites: Slot  59 | Hash Ops: 1355467 | Time: 0.015s | ETA:  289.6s
[NODE-05] Block 360/500 | Index: 360 | Slot:  60 | Storage:  39.36 KB | Overwrites: Slot  60 | Hash Ops: 1358337 | Time: 0.023s | ETA:  287.5s
[NODE-05] Block 361/500 | Index: 361 | Slot:  61 | Storage:  39.36 KB | Overwrites: Slot  61 | Hash Ops: 1358495 | Time: 0.004s | ETA:  285.5s
[NODE-05] Block 362/500 | Index: 362 | Slot:  62 | Storage:  39.36 KB | Overwrites: Slot  62 | Hash Ops: 1359216 | Time: 0.011s | ETA:  283.5s
[NODE-05] Block 363/500 | Index: 363 | Slot:  63 | Storage:  39.35 KB | Overwrites: Slot  63 | Hash Ops: 1360674 | Time: 0.014s | ETA:  281.4s
[NODE-05] Block 364/500 | Index: 364 | Slot:  64 | Storage:  39.35 KB | Overwrites: Slot  64 | Hash Ops: 1361762 | Time: 0.009s | ETA:  279.3s
[NODE-05] Block 365/500 | Index: 365 | Slot:  65 | Storage:  39.35 KB | Overwrites: Slot  65 | Hash Ops: 1368072 | Time: 0.042s | ETA:  277.3s
[NODE-05] Block 366/500 | Index: 366 | Slot:  66 | Storage:  39.35 KB | Overwrites: Slot  66 | Hash Ops: 1378106 | Time: 0.070s | ETA:  275.2s
[NODE-05] Block 367/500 | Index: 367 | Slot:  67 | Storage:  39.36 KB | Overwrites: Slot  67 | Hash Ops: 1380973 | Time: 0.023s | ETA:  273.2s
[NODE-05] Block 368/500 | Index: 368 | Slot:  68 | Storage:  39.36 KB | Overwrites: Slot  68 | Hash Ops: 1385053 | Time: 0.032s | ETA:  271.1s
[NODE-05] Block 369/500 | Index: 369 | Slot:  69 | Storage:  39.36 KB | Overwrites: Slot  69 | Hash Ops: 1388337 | Time: 0.026s | ETA:  269.0s
[NODE-05] Block 370/500 | Index: 370 | Slot:  70 | Storage:  39.36 KB | Overwrites: Slot  70 | Hash Ops: 1393726 | Time: 0.041s | ETA:  267.0s
[NODE-05] Block 371/500 | Index: 371 | Slot:  71 | Storage:  39.36 KB | Overwrites: Slot  71 | Hash Ops: 1397743 | Time: 0.033s | ETA:  265.0s
[NODE-05] Block 372/500 | Index: 372 | Slot:  72 | Storage:  39.36 KB | Overwrites: Slot  72 | Hash Ops: 1400156 | Time: 0.021s | ETA:  262.9s
[NODE-05] Block 373/500 | Index: 373 | Slot:  73 | Storage:  39.36 KB | Overwrites: Slot  73 | Hash Ops: 1402954 | Time: 0.019s | ETA:  260.8s
[NODE-05] Block 374/500 | Index: 374 | Slot:  74 | Storage:  39.36 KB | Overwrites: Slot  74 | Hash Ops: 1417781 | Time: 0.100s | ETA:  258.8s
[NODE-05] Block 375/500 | Index: 375 | Slot:  75 | Storage:  39.36 KB | Overwrites: Slot  75 | Hash Ops: 1418734 | Time: 0.010s | ETA:  256.8s
[NODE-05] Block 376/500 | Index: 376 | Slot:  76 | Storage:  39.36 KB | Overwrites: Slot  76 | Hash Ops: 1419532 | Time: 0.012s | ETA:  254.7s
[NODE-05] Block 377/500 | Index: 377 | Slot:  77 | Storage:  39.36 KB | Overwrites: Slot  77 | Hash Ops: 1425375 | Time: 0.038s | ETA:  252.6s
[NODE-05] Block 378/500 | Index: 378 | Slot:  78 | Storage:  39.36 KB | Overwrites: Slot  78 | Hash Ops: 1429653 | Time: 0.033s | ETA:  250.6s
[NODE-05] Block 379/500 | Index: 379 | Slot:  79 | Storage:  39.36 KB | Overwrites: Slot  79 | Hash Ops: 1435324 | Time: 0.041s | ETA:  248.5s
[NODE-05] Block 380/500 | Index: 380 | Slot:  80 | Storage:  39.36 KB | Overwrites: Slot  80 | Hash Ops: 1440447 | Time: 0.037s | ETA:  246.5s
[NODE-05] Block 381/500 | Index: 381 | Slot:  81 | Storage:  39.36 KB | Overwrites: Slot  81 | Hash Ops: 1444184 | Time: 0.028s | ETA:  244.4s
[NODE-05] Block 382/500 | Index: 382 | Slot:  82 | Storage:  39.36 KB | Overwrites: Slot  82 | Hash Ops: 1447220 | Time: 0.023s | ETA:  242.4s
[NODE-05] Block 383/500 | Index: 383 | Slot:  83 | Storage:  39.36 KB | Overwrites: Slot  83 | Hash Ops: 1459763 | Time: 0.099s | ETA:  240.3s
[NODE-05] Block 384/500 | Index: 384 | Slot:  84 | Storage:  39.36 KB | Overwrites: Slot  84 | Hash Ops: 1466523 | Time: 0.044s | ETA:  238.3s
[NODE-05] Block 385/500 | Index: 385 | Slot:  85 | Storage:  39.36 KB | Overwrites: Slot  85 | Hash Ops: 1467846 | Time: 0.014s | ETA:  236.2s
[NODE-05] Block 386/500 | Index: 386 | Slot:  86 | Storage:  39.36 KB | Overwrites: Slot  86 | Hash Ops: 1473220 | Time: 0.036s | ETA:  234.2s
[NODE-05] Block 387/500 | Index: 387 | Slot:  87 | Storage:  39.36 KB | Overwrites: Slot  87 | Hash Ops: 1473341 | Time: 0.003s | ETA:  232.1s
[NODE-05] Block 388/500 | Index: 388 | Slot:  88 | Storage:  39.36 KB | Overwrites: Slot  88 | Hash Ops: 1475069 | Time: 0.016s | ETA:  230.0s
[NODE-05] Block 389/500 | Index: 389 | Slot:  89 | Storage:  39.36 KB | Overwrites: Slot  89 | Hash Ops: 1478683 | Time: 0.033s | ETA:  228.0s
[NODE-05] Block 390/500 | Index: 390 | Slot:  90 | Storage:  39.37 KB | Overwrites: Slot  90 | Hash Ops: 1489845 | Time: 0.079s | ETA:  225.9s
[NODE-05] Block 391/500 | Index: 391 | Slot:  91 | Storage:  39.37 KB | Overwrites: Slot  91 | Hash Ops: 1498394 | Time: 0.067s | ETA:  223.9s
[NODE-05] Block 392/500 | Index: 392 | Slot:  92 | Storage:  39.37 KB | Overwrites: Slot  92 | Hash Ops: 1499664 | Time: 0.012s | ETA:  221.9s
[NODE-05] Block 393/500 | Index: 393 | Slot:  93 | Storage:  39.37 KB | Overwrites: Slot  93 | Hash Ops: 1501985 | Time: 0.019s | ETA:  219.8s
[NODE-05] Block 394/500 | Index: 394 | Slot:  94 | Storage:  39.37 KB | Overwrites: Slot  94 | Hash Ops: 1503348 | Time: 0.013s | ETA:  217.7s
[NODE-05] Block 395/500 | Index: 395 | Slot:  95 | Storage:  39.37 KB | Overwrites: Slot  95 | Hash Ops: 1511829 | Time: 0.065s | ETA:  215.7s
[NODE-05] Block 396/500 | Index: 396 | Slot:  96 | Storage:  39.37 KB | Overwrites: Slot  96 | Hash Ops: 1514217 | Time: 0.016s | ETA:  213.6s
[NODE-05] Block 397/500 | Index: 397 | Slot:  97 | Storage:  39.37 KB | Overwrites: Slot  97 | Hash Ops: 1518218 | Time: 0.031s | ETA:  211.6s
[NODE-05] Block 398/500 | Index: 398 | Slot:  98 | Storage:  39.37 KB | Overwrites: Slot  98 | Hash Ops: 1520557 | Time: 0.019s | ETA:  209.5s
[NODE-05] Block 399/500 | Index: 399 | Slot:  99 | Storage:  39.37 KB | Overwrites: Slot  99 | Hash Ops: 1524938 | Time: 0.030s | ETA:  207.5s
[NODE-05] Block 400/500 | Index: 400 | Slot:   0 | Storage:  39.36 KB | Overwrites: Slot   0 | Hash Ops: 1525121 | Time: 0.006s | ETA:  205.4s
[NODE-05] Block 401/500 | Index: 401 | Slot:   1 | Storage:  39.36 KB | Overwrites: Slot   1 | Hash Ops: 1531015 | Time: 0.043s | ETA:  203.4s
[NODE-05] Block 402/500 | Index: 402 | Slot:   2 | Storage:  39.36 KB | Overwrites: Slot   2 | Hash Ops: 1533737 | Time: 0.026s | ETA:  201.3s
[NODE-05] Block 403/500 | Index: 403 | Slot:   3 | Storage:  39.36 KB | Overwrites: Slot   3 | Hash Ops: 1537770 | Time: 0.030s | ETA:  199.3s
[NODE-05] Block 404/500 | Index: 404 | Slot:   4 | Storage:  39.37 KB | Overwrites: Slot   4 | Hash Ops: 1540548 | Time: 0.019s | ETA:  197.2s
[NODE-05] Block 405/500 | Index: 405 | Slot:   5 | Storage:  39.37 KB | Overwrites: Slot   5 | Hash Ops: 1549048 | Time: 0.060s | ETA:  195.1s
[NODE-05] Block 406/500 | Index: 406 | Slot:   6 | Storage:  39.36 KB | Overwrites: Slot   6 | Hash Ops: 1549806 | Time: 0.009s | ETA:  193.1s
[NODE-05] Block 407/500 | Index: 407 | Slot:   7 | Storage:  39.36 KB | Overwrites: Slot   7 | Hash Ops: 1552537 | Time: 0.027s | ETA:  191.0s
[NODE-05] Block 408/500 | Index: 408 | Slot:   8 | Storage:  39.36 KB | Overwrites: Slot   8 | Hash Ops: 1556730 | Time: 0.036s | ETA:  189.0s
[NODE-05] Block 409/500 | Index: 409 | Slot:   9 | Storage:  39.36 KB | Overwrites: Slot   9 | Hash Ops: 1563737 | Time: 0.050s | ETA:  186.9s
[NODE-05] Block 410/500 | Index: 410 | Slot:  10 | Storage:  39.36 KB | Overwrites: Slot  10 | Hash Ops: 1571460 | Time: 0.055s | ETA:  184.9s
[NODE-05] Block 411/500 | Index: 411 | Slot:  11 | Storage:  39.37 KB | Overwrites: Slot  11 | Hash Ops: 1573452 | Time: 0.017s | ETA:  182.8s
[NODE-05] Block 412/500 | Index: 412 | Slot:  12 | Storage:  39.37 KB | Overwrites: Slot  12 | Hash Ops: 1578812 | Time: 0.049s | ETA:  180.8s
[NODE-05] Block 413/500 | Index: 413 | Slot:  13 | Storage:  39.37 KB | Overwrites: Slot  13 | Hash Ops: 1579986 | Time: 0.008s | ETA:  178.7s
[NODE-05] Block 414/500 | Index: 414 | Slot:  14 | Storage:  39.37 KB | Overwrites: Slot  14 | Hash Ops: 1580257 | Time: 0.002s | ETA:  176.7s
[NODE-05] Block 415/500 | Index: 415 | Slot:  15 | Storage:  39.37 KB | Overwrites: Slot  15 | Hash Ops: 1580958 | Time: 0.005s | ETA:  174.6s
[NODE-05] Block 416/500 | Index: 416 | Slot:  16 | Storage:  39.37 KB | Overwrites: Slot  16 | Hash Ops: 1588028 | Time: 0.055s | ETA:  172.6s
[NODE-05] Block 417/500 | Index: 417 | Slot:  17 | Storage:  39.37 KB | Overwrites: Slot  17 | Hash Ops: 1588998 | Time: 0.006s | ETA:  170.5s
[NODE-05] Block 418/500 | Index: 418 | Slot:  18 | Storage:  39.36 KB | Overwrites: Slot  18 | Hash Ops: 1598747 | Time: 0.066s | ETA:  168.5s
[NODE-05] Block 419/500 | Index: 419 | Slot:  19 | Storage:  39.37 KB | Overwrites: Slot  19 | Hash Ops: 1633415 | Time: 0.235s | ETA:  166.4s
[NODE-05] Block 420/500 | Index: 420 | Slot:  20 | Storage:  39.37 KB | Overwrites: Slot  20 | Hash Ops: 1637191 | Time: 0.028s | ETA:  164.4s
[NODE-05] Block 421/500 | Index: 421 | Slot:  21 | Storage:  39.37 KB | Overwrites: Slot  21 | Hash Ops: 1638694 | Time: 0.014s | ETA:  162.3s
[NODE-05] Block 422/500 | Index: 422 | Slot:  22 | Storage:  39.37 KB | Overwrites: Slot  22 | Hash Ops: 1639827 | Time: 0.012s | ETA:  160.3s
[NODE-05] Block 423/500 | Index: 423 | Slot:  23 | Storage:  39.37 KB | Overwrites: Slot  23 | Hash Ops: 1641941 | Time: 0.017s | ETA:  158.2s
[NODE-05] Block 424/500 | Index: 424 | Slot:  24 | Storage:  39.36 KB | Overwrites: Slot  24 | Hash Ops: 1647303 | Time: 0.035s | ETA:  156.2s
[NODE-05] Block 425/500 | Index: 425 | Slot:  25 | Storage:  39.36 KB | Overwrites: Slot  25 | Hash Ops: 1649879 | Time: 0.026s | ETA:  154.1s
[NODE-05] Block 426/500 | Index: 426 | Slot:  26 | Storage:  39.36 KB | Overwrites: Slot  26 | Hash Ops: 1654578 | Time: 0.034s | ETA:  152.0s
[NODE-05] Block 427/500 | Index: 427 | Slot:  27 | Storage:  39.36 KB | Overwrites: Slot  27 | Hash Ops: 1658697 | Time: 0.030s | ETA:  150.0s
[NODE-05] Block 428/500 | Index: 428 | Slot:  28 | Storage:  39.36 KB | Overwrites: Slot  28 | Hash Ops: 1661715 | Time: 0.023s | ETA:  147.9s
[NODE-05] Block 429/500 | Index: 429 | Slot:  29 | Storage:  39.36 KB | Overwrites: Slot  29 | Hash Ops: 1664569 | Time: 0.023s | ETA:  145.9s
[NODE-05] Block 430/500 | Index: 430 | Slot:  30 | Storage:  39.36 KB | Overwrites: Slot  30 | Hash Ops: 1667952 | Time: 0.027s | ETA:  143.8s
[NODE-05] Block 431/500 | Index: 431 | Slot:  31 | Storage:  39.36 KB | Overwrites: Slot  31 | Hash Ops: 1671304 | Time: 0.032s | ETA:  141.8s
[NODE-05] Block 432/500 | Index: 432 | Slot:  32 | Storage:  39.36 KB | Overwrites: Slot  32 | Hash Ops: 1675547 | Time: 0.031s | ETA:  139.7s
[NODE-05] Block 433/500 | Index: 433 | Slot:  33 | Storage:  39.36 KB | Overwrites: Slot  33 | Hash Ops: 1683772 | Time: 0.061s | ETA:  137.7s
[NODE-05] Block 434/500 | Index: 434 | Slot:  34 | Storage:  39.36 KB | Overwrites: Slot  34 | Hash Ops: 1688717 | Time: 0.033s | ETA:  135.7s
[NODE-05] Block 435/500 | Index: 435 | Slot:  35 | Storage:  39.36 KB | Overwrites: Slot  35 | Hash Ops: 1691092 | Time: 0.020s | ETA:  133.6s
[NODE-05] Block 436/500 | Index: 436 | Slot:  36 | Storage:  39.36 KB | Overwrites: Slot  36 | Hash Ops: 1692304 | Time: 0.009s | ETA:  131.5s
[NODE-05] Block 437/500 | Index: 437 | Slot:  37 | Storage:  39.36 KB | Overwrites: Slot  37 | Hash Ops: 1696545 | Time: 0.054s | ETA:  129.5s
[NODE-05] Block 438/500 | Index: 438 | Slot:  38 | Storage:  39.36 KB | Overwrites: Slot  38 | Hash Ops: 1699426 | Time: 0.020s | ETA:  127.4s
[NODE-05] Block 439/500 | Index: 439 | Slot:  39 | Storage:  39.36 KB | Overwrites: Slot  39 | Hash Ops: 1701007 | Time: 0.033s | ETA:  125.4s
[NODE-05] Block 440/500 | Index: 440 | Slot:  40 | Storage:  39.36 KB | Overwrites: Slot  40 | Hash Ops: 1701978 | Time: 0.010s | ETA:  123.3s
[NODE-05] Block 441/500 | Index: 441 | Slot:  41 | Storage:  39.36 KB | Overwrites: Slot  41 | Hash Ops: 1704135 | Time: 0.018s | ETA:  121.3s
[NODE-05] Block 442/500 | Index: 442 | Slot:  42 | Storage:  39.36 KB | Overwrites: Slot  42 | Hash Ops: 1719882 | Time: 0.108s | ETA:  119.2s
[NODE-05] Block 443/500 | Index: 443 | Slot:  43 | Storage:  39.36 KB | Overwrites: Slot  43 | Hash Ops: 1720486 | Time: 0.012s | ETA:  117.2s
[NODE-05] Block 444/500 | Index: 444 | Slot:  44 | Storage:  39.36 KB | Overwrites: Slot  44 | Hash Ops: 1724572 | Time: 0.035s | ETA:  115.1s
[NODE-05] Block 445/500 | Index: 445 | Slot:  45 | Storage:  39.36 KB | Overwrites: Slot  45 | Hash Ops: 1725198 | Time: 0.004s | ETA:  113.1s
[NODE-05] Block 446/500 | Index: 446 | Slot:  46 | Storage:  39.36 KB | Overwrites: Slot  46 | Hash Ops: 1727725 | Time: 0.017s | ETA:  111.0s
[NODE-05] Block 447/500 | Index: 447 | Slot:  47 | Storage:  39.36 KB | Overwrites: Slot  47 | Hash Ops: 1728143 | Time: 0.007s | ETA:  108.9s
[NODE-05] Block 448/500 | Index: 448 | Slot:  48 | Storage:  39.36 KB | Overwrites: Slot  48 | Hash Ops: 1729336 | Time: 0.008s | ETA:  106.9s
[NODE-05] Block 449/500 | Index: 449 | Slot:  49 | Storage:  39.36 KB | Overwrites: Slot  49 | Hash Ops: 1734229 | Time: 0.036s | ETA:  104.8s
[NODE-05] Block 450/500 | Index: 450 | Slot:  50 | Storage:  39.36 KB | Overwrites: Slot  50 | Hash Ops: 1736488 | Time: 0.017s | ETA:  102.8s
[NODE-05] Block 451/500 | Index: 451 | Slot:  51 | Storage:  39.36 KB | Overwrites: Slot  51 | Hash Ops: 1740841 | Time: 0.034s | ETA:  100.7s
[NODE-05] Block 452/500 | Index: 452 | Slot:  52 | Storage:  39.36 KB | Overwrites: Slot  52 | Hash Ops: 1741366 | Time: 0.007s | ETA:   98.7s
[NODE-05] Block 453/500 | Index: 453 | Slot:  53 | Storage:  39.36 KB | Overwrites: Slot  53 | Hash Ops: 1748712 | Time: 0.052s | ETA:   96.6s
[NODE-05] Block 454/500 | Index: 454 | Slot:  54 | Storage:  39.36 KB | Overwrites: Slot  54 | Hash Ops: 1749332 | Time: 0.010s | ETA:   94.6s
[NODE-05] Block 455/500 | Index: 455 | Slot:  55 | Storage:  39.36 KB | Overwrites: Slot  55 | Hash Ops: 1750640 | Time: 0.014s | ETA:   92.5s
[NODE-05] Block 456/500 | Index: 456 | Slot:  56 | Storage:  39.36 KB | Overwrites: Slot  56 | Hash Ops: 1751926 | Time: 0.012s | ETA:   90.4s
[NODE-05] Block 457/500 | Index: 457 | Slot:  57 | Storage:  39.36 KB | Overwrites: Slot  57 | Hash Ops: 1756930 | Time: 0.038s | ETA:   88.4s
[NODE-05] Block 458/500 | Index: 458 | Slot:  58 | Storage:  39.36 KB | Overwrites: Slot  58 | Hash Ops: 1757282 | Time: 0.006s | ETA:   86.3s
[NODE-05] Block 459/500 | Index: 459 | Slot:  59 | Storage:  39.36 KB | Overwrites: Slot  59 | Hash Ops: 1765636 | Time: 0.060s | ETA:   84.3s
[NODE-05] Block 460/500 | Index: 460 | Slot:  60 | Storage:  39.36 KB | Overwrites: Slot  60 | Hash Ops: 1767302 | Time: 0.011s | ETA:   82.2s
[NODE-05] Block 461/500 | Index: 461 | Slot:  61 | Storage:  39.36 KB | Overwrites: Slot  61 | Hash Ops: 1775277 | Time: 0.057s | ETA:   80.2s
[NODE-05] Block 462/500 | Index: 462 | Slot:  62 | Storage:  39.36 KB | Overwrites: Slot  62 | Hash Ops: 1775369 | Time: 0.003s | ETA:   78.1s
[NODE-05] Block 463/500 | Index: 463 | Slot:  63 | Storage:  39.36 KB | Overwrites: Slot  63 | Hash Ops: 1776010 | Time: 0.005s | ETA:   76.1s
[NODE-05] Block 464/500 | Index: 464 | Slot:  64 | Storage:  39.36 KB | Overwrites: Slot  64 | Hash Ops: 1778165 | Time: 0.015s | ETA:   74.0s
[NODE-05] Block 465/500 | Index: 465 | Slot:  65 | Storage:  39.36 KB | Overwrites: Slot  65 | Hash Ops: 1781648 | Time: 0.027s | ETA:   72.0s
[NODE-05] Block 466/500 | Index: 466 | Slot:  66 | Storage:  39.36 KB | Overwrites: Slot  66 | Hash Ops: 1782774 | Time: 0.014s | ETA:   69.9s
[NODE-05] Block 467/500 | Index: 467 | Slot:  67 | Storage:  39.36 KB | Overwrites: Slot  67 | Hash Ops: 1785606 | Time: 0.019s | ETA:   67.8s
[NODE-05] Block 468/500 | Index: 468 | Slot:  68 | Storage:  39.36 KB | Overwrites: Slot  68 | Hash Ops: 1800795 | Time: 0.110s | ETA:   65.8s
[NODE-05] Block 469/500 | Index: 469 | Slot:  69 | Storage:  39.36 KB | Overwrites: Slot  69 | Hash Ops: 1802160 | Time: 0.009s | ETA:   63.7s
[NODE-05] Block 470/500 | Index: 470 | Slot:  70 | Storage:  39.36 KB | Overwrites: Slot  70 | Hash Ops: 1811410 | Time: 0.063s | ETA:   61.7s
[NODE-05] Block 471/500 | Index: 471 | Slot:  71 | Storage:  39.36 KB | Overwrites: Slot  71 | Hash Ops: 1815094 | Time: 0.025s | ETA:   59.6s
[NODE-05] Block 472/500 | Index: 472 | Slot:  72 | Storage:  39.36 KB | Overwrites: Slot  72 | Hash Ops: 1816185 | Time: 0.011s | ETA:   57.6s
[NODE-05] Block 473/500 | Index: 473 | Slot:  73 | Storage:  39.36 KB | Overwrites: Slot  73 | Hash Ops: 1819988 | Time: 0.025s | ETA:   55.5s
[NODE-05] Block 474/500 | Index: 474 | Slot:  74 | Storage:  39.36 KB | Overwrites: Slot  74 | Hash Ops: 1820311 | Time: 0.006s | ETA:   53.4s
[NODE-05] Block 475/500 | Index: 475 | Slot:  75 | Storage:  39.36 KB | Overwrites: Slot  75 | Hash Ops: 1823943 | Time: 0.028s | ETA:   51.4s
[NODE-05] Block 476/500 | Index: 476 | Slot:  76 | Storage:  39.36 KB | Overwrites: Slot  76 | Hash Ops: 1828725 | Time: 0.034s | ETA:   49.3s
[NODE-05] Block 477/500 | Index: 477 | Slot:  77 | Storage:  39.36 KB | Overwrites: Slot  77 | Hash Ops: 1829921 | Time: 0.008s | ETA:   47.3s
[NODE-05] Block 478/500 | Index: 478 | Slot:  78 | Storage:  39.36 KB | Overwrites: Slot  78 | Hash Ops: 1833133 | Time: 0.026s | ETA:   45.2s
[NODE-05] Block 479/500 | Index: 479 | Slot:  79 | Storage:  39.36 KB | Overwrites: Slot  79 | Hash Ops: 1835090 | Time: 0.016s | ETA:   43.2s
[NODE-05] Block 480/500 | Index: 480 | Slot:  80 | Storage:  39.36 KB | Overwrites: Slot  80 | Hash Ops: 1837527 | Time: 0.021s | ETA:   41.1s
[NODE-05] Block 481/500 | Index: 481 | Slot:  81 | Storage:  39.36 KB | Overwrites: Slot  81 | Hash Ops: 1839438 | Time: 0.016s | ETA:   39.1s
[NODE-05] Block 482/500 | Index: 482 | Slot:  82 | Storage:  39.36 KB | Overwrites: Slot  82 | Hash Ops: 1859586 | Time: 0.136s | ETA:   37.0s
[NODE-05] Block 483/500 | Index: 483 | Slot:  83 | Storage:  39.36 KB | Overwrites: Slot  83 | Hash Ops: 1870408 | Time: 0.072s | ETA:   35.0s
[NODE-05] Block 484/500 | Index: 484 | Slot:  84 | Storage:  39.36 KB | Overwrites: Slot  84 | Hash Ops: 1871719 | Time: 0.013s | ETA:   32.9s
[NODE-05] Block 485/500 | Index: 485 | Slot:  85 | Storage:  39.36 KB | Overwrites: Slot  85 | Hash Ops: 1874090 | Time: 0.018s | ETA:   30.8s
[NODE-05] Block 486/500 | Index: 486 | Slot:  86 | Storage:  39.36 KB | Overwrites: Slot  86 | Hash Ops: 1875945 | Time: 0.016s | ETA:   28.8s
[NODE-05] Block 487/500 | Index: 487 | Slot:  87 | Storage:  39.36 KB | Overwrites: Slot  87 | Hash Ops: 1882711 | Time: 0.048s | ETA:   26.7s
[NODE-05] Block 488/500 | Index: 488 | Slot:  88 | Storage:  39.36 KB | Overwrites: Slot  88 | Hash Ops: 1888936 | Time: 0.044s | ETA:   24.7s
[NODE-05] Block 489/500 | Index: 489 | Slot:  89 | Storage:  39.36 KB | Overwrites: Slot  89 | Hash Ops: 1890205 | Time: 0.013s | ETA:   22.6s
[NODE-05] Block 490/500 | Index: 490 | Slot:  90 | Storage:  39.36 KB | Overwrites: Slot  90 | Hash Ops: 1893491 | Time: 0.022s | ETA:   20.6s
[NODE-05] Block 491/500 | Index: 491 | Slot:  91 | Storage:  39.36 KB | Overwrites: Slot  91 | Hash Ops: 1894605 | Time: 0.009s | ETA:   18.5s
[NODE-05] Block 492/500 | Index: 492 | Slot:  92 | Storage:  39.36 KB | Overwrites: Slot  92 | Hash Ops: 1901372 | Time: 0.049s | ETA:   16.4s
[NODE-05] Block 493/500 | Index: 493 | Slot:  93 | Storage:  39.36 KB | Overwrites: Slot  93 | Hash Ops: 1906657 | Time: 0.049s | ETA:   14.4s
[NODE-05] Block 494/500 | Index: 494 | Slot:  94 | Storage:  39.36 KB | Overwrites: Slot  94 | Hash Ops: 1915411 | Time: 0.061s | ETA:   12.3s
[NODE-05] Block 495/500 | Index: 495 | Slot:  95 | Storage:  39.36 KB | Overwrites: Slot  95 | Hash Ops: 1918108 | Time: 0.021s | ETA:   10.3s
[NODE-05] Block 496/500 | Index: 496 | Slot:  96 | Storage:  39.35 KB | Overwrites: Slot  96 | Hash Ops: 1918625 | Time: 0.007s | ETA:    8.2s
[NODE-05] Block 497/500 | Index: 497 | Slot:  97 | Storage:  39.36 KB | Overwrites: Slot  97 | Hash Ops: 1922351 | Time: 0.027s | ETA:    6.2s
[NODE-05] Block 498/500 | Index: 498 | Slot:  98 | Storage:  39.36 KB | Overwrites: Slot  98 | Hash Ops: 1926780 | Time: 0.034s | ETA:    4.1s
[NODE-05] Block 499/500 | Index: 499 | Slot:  99 | Storage:  39.36 KB | Overwrites: Slot  99 | Hash Ops: 1936965 | Time: 0.076s | ETA:    2.1s
[NODE-05] Block 500/500 | Index: 500 | Slot:   0 | Storage:  39.36 KB | Overwrites: Slot   0 | Hash Ops: 1939392 | Time: 0.022s | ETA:    0.0s
[NODE-05] Peer connections restored
[NODE-05] Completed in 1030.09 seconds

================================================================================
============================= SIMULATION COMPLETE ==============================
================================================================================

Total simulation time: 5162.67 seconds
Total blocks generated: 2500

--------------------------------------------------------------------------------
NETWORK CONSENSUS VERIFICATION
--------------------------------------------------------------------------------

Chain lengths:
  NODE-01: 500 blocks
  NODE-02: 500 blocks
  NODE-03: 500 blocks
  NODE-04: 500 blocks
  NODE-05: 500 blocks

Validation Statistics:
  NODE-01: Received=0, Validated=0, Rejected=0, Rate=0.00%
  NODE-02: Received=0, Validated=0, Rejected=0, Rate=0.00%
  NODE-03: Received=0, Validated=0, Rejected=0, Rate=0.00%
  NODE-04: Received=0, Validated=0, Rejected=0, Rate=0.00%
  NODE-05: Received=0, Validated=0, Rejected=0, Rate=0.00%

Storage Usage:
  NODE-01: 39.36 KB (Accessible: 100, Overwritten: 401)
  NODE-02: 39.36 KB (Accessible: 100, Overwritten: 401)
  NODE-03: 39.35 KB (Accessible: 100, Overwritten: 401)
  NODE-04: 39.35 KB (Accessible: 100, Overwritten: 401)
  NODE-05: 39.36 KB (Accessible: 100, Overwritten: 401)

--------------------------------------------------------------------------------
SIMULATION SUMMARY
--------------------------------------------------------------------------------

NODE-01:
  Blocks Created: 500
  Avg Mining Time: 0.0347s
  Avg Hash Computations: 931878
  Storage: 39.36 KB (Constant: True)
  Validation Rate: 0.00%

NODE-02:
  Blocks Created: 500
  Avg Mining Time: 0.0373s
  Avg Hash Computations: 1006743
  Storage: 39.36 KB (Constant: True)
  Validation Rate: 0.00%

NODE-03:
  Blocks Created: 500
  Avg Mining Time: 0.0381s
  Avg Hash Computations: 1076494
  Storage: 39.35 KB (Constant: True)
  Validation Rate: 0.00%

NODE-04:
  Blocks Created: 500
  Avg Mining Time: 0.0336s
  Avg Hash Computations: 946472
  Storage: 39.35 KB (Constant: True)
  Validation Rate: 0.00%

NODE-05:
  Blocks Created: 500
  Avg Mining Time: 0.0299s
  Avg Hash Computations: 958284
  Storage: 39.36 KB (Constant: True)
  Validation Rate: 0.00%

--------------------------------------------------------------------------------
EXPORTING RESULTS
--------------------------------------------------------------------------------

Metrics exported to results/metrics_NODE-01_20251113_171818.json
[NODE-01] Results exported:
  - block_details_NODE-01_20251113_155215.txt
  - metrics_NODE-01_20251113_171818.json
  - node_NODE-01_20251113_171818.json

Metrics exported to results/metrics_NODE-02_20251113_171818.json
[NODE-02] Results exported:
  - block_details_NODE-02_20251113_155215.txt
  - metrics_NODE-02_20251113_171818.json
  - node_NODE-02_20251113_171818.json

Metrics exported to results/metrics_NODE-03_20251113_171818.json
[NODE-03] Results exported:
  - block_details_NODE-03_20251113_155215.txt
  - metrics_NODE-03_20251113_171818.json
  - node_NODE-03_20251113_171818.json

Metrics exported to results/metrics_NODE-04_20251113_171818.json
[NODE-04] Results exported:
  - block_details_NODE-04_20251113_155215.txt
  - metrics_NODE-04_20251113_171818.json
  - node_NODE-04_20251113_171818.json

Metrics exported to results/metrics_NODE-05_20251113_171818.json
[NODE-05] Results exported:
  - block_details_NODE-05_20251113_155215.txt
  - metrics_NODE-05_20251113_171818.json
  - node_NODE-05_20251113_171818.json

Summary file: simulation_summary_20251113_171818.json

Simulation finished.
(venv) mcyber@mcyber-VirtualBox:~/ledger-amnesia$ 
```
