# Simulation 01 Results

## Results exported to `results/`
  - block_details_20251111_161751.txt
  - metrics_20251111_163955.json
  - network_20251111_163955.json

## Simulation 01 Terminal Output
- Storage vs Block Number:
<img width="805" height="515" alt="Screenshot 2025-11-14 at 2 45 57 am" src="https://github.com/user-attachments/assets/acb66741-d805-4436-9b74-5d375d7bd1b0" />

- Block Generation Time vs Block Number:
<img width="532" height="369" alt="Screenshot 2025-11-14 at 3 20 24 am" src="https://github.com/user-attachments/assets/777f16fc-68bd-4034-b4bc-3a0373254173" />

- Hash Operations per Block vs Block Number:
<img width="653" height="420" alt="Screenshot 2025-11-15 at 6 45 37 am" src="https://github.com/user-attachments/assets/c5f30a68-87bc-47ff-b36e-ebbba64749fb" />


- Terminal Output (text):
```
(venv) mcyber@mcyber-VirtualBox:~/ledger-amnesia$ python simulation/run_simulation.py 500
Initializing network with 5 nodes...
Configuration:
  Buffer Size (N):     100 slots
  Block Interval (Δt): 2 seconds
  Difficulty (D):      12 (2^12 = 4096 hashes)
  Expected Storage:    37.50 KB
  Simulation Blocks:   500
  Block log file:      results/block_details_20251111_161751.txt

======================================================================
================= STARTING LEDGER AMNESIA SIMULATION =================
======================================================================

Block   1/500 | Slot:   1 | Storage:   0.71 KB | Overwrites:   - | Hash Ops:   6350 | Time: 0.047s | ETA: 299.0s
Block   2/500 | Slot:   2 | Storage:   1.10 KB | Overwrites:   - | Hash Ops:   7299 | Time: 0.007s | ETA: 825.4s
Block   3/500 | Slot:   3 | Storage:   1.49 KB | Overwrites:   - | Hash Ops:   8389 | Time: 0.010s | ETA: 956.7s
Block   4/500 | Slot:   4 | Storage:   1.88 KB | Overwrites:   - | Hash Ops:  12510 | Time: 0.028s | ETA: 1046.0s
Block   5/500 | Slot:   5 | Storage:   2.27 KB | Overwrites:   - | Hash Ops:  13357 | Time: 0.007s | ETA: 1106.6s
Block   6/500 | Slot:   6 | Storage:   2.66 KB | Overwrites:   - | Hash Ops:  16204 | Time: 0.019s | ETA: 1145.0s
Block   7/500 | Slot:   7 | Storage:   3.05 KB | Overwrites:   - | Hash Ops:  17205 | Time: 0.007s | ETA: 1152.6s
Block   8/500 | Slot:   8 | Storage:   3.44 KB | Overwrites:   - | Hash Ops:  27217 | Time: 0.072s | ETA: 1182.7s
Block   9/500 | Slot:   9 | Storage:   3.83 KB | Overwrites:   - | Hash Ops:  27397 | Time: 0.001s | ETA: 1196.5s
Block  10/500 | Slot:  10 | Storage:   4.23 KB | Overwrites:   - | Hash Ops:  27803 | Time: 0.003s | ETA: 1206.1s
Block  11/500 | Slot:  11 | Storage:   4.62 KB | Overwrites:   - | Hash Ops:  34735 | Time: 0.050s | ETA: 1215.5s
Block  12/500 | Slot:  12 | Storage:   5.01 KB | Overwrites:   - | Hash Ops:  34873 | Time: 0.001s | ETA: 1216.5s
Block  13/500 | Slot:  13 | Storage:   5.41 KB | Overwrites:   - | Hash Ops:  46472 | Time: 0.078s | ETA: 1223.4s
Block  14/500 | Slot:  14 | Storage:   5.80 KB | Overwrites:   - | Hash Ops:  60644 | Time: 0.097s | ETA: 1225.5s
Block  15/500 | Slot:  15 | Storage:   6.20 KB | Overwrites:   - | Hash Ops:  60871 | Time: 0.002s | ETA: 1223.7s
Block  16/500 | Slot:  16 | Storage:   6.59 KB | Overwrites:   - | Hash Ops:  65247 | Time: 0.030s | ETA: 1228.0s
Block  17/500 | Slot:  17 | Storage:   6.98 KB | Overwrites:   - | Hash Ops:  66780 | Time: 0.010s | ETA: 1226.1s
Block  18/500 | Slot:  18 | Storage:   7.38 KB | Overwrites:   - | Hash Ops:  76210 | Time: 0.067s | ETA: 1225.8s
Block  19/500 | Slot:  19 | Storage:   7.77 KB | Overwrites:   - | Hash Ops:  76721 | Time: 0.003s | ETA: 1225.2s
Block  20/500 | Slot:  20 | Storage:   8.16 KB | Overwrites:   - | Hash Ops:  79919 | Time: 0.022s | ETA: 1221.7s
Block  21/500 | Slot:  21 | Storage:   8.56 KB | Overwrites:   - | Hash Ops:  80742 | Time: 0.006s | ETA: 1222.1s
Block  22/500 | Slot:  22 | Storage:   8.95 KB | Overwrites:   - | Hash Ops:  82856 | Time: 0.016s | ETA: 1225.0s
Block  23/500 | Slot:  23 | Storage:   9.34 KB | Overwrites:   - | Hash Ops:  87859 | Time: 0.035s | ETA: 1221.1s
Block  24/500 | Slot:  24 | Storage:   9.74 KB | Overwrites:   - | Hash Ops:  88321 | Time: 0.003s | ETA: 1218.1s
Block  25/500 | Slot:  25 | Storage:  10.13 KB | Overwrites:   - | Hash Ops:  92550 | Time: 0.030s | ETA: 1217.4s
Block  26/500 | Slot:  26 | Storage:  10.53 KB | Overwrites:   - | Hash Ops:  95429 | Time: 0.021s | ETA: 1216.3s
Block  27/500 | Slot:  27 | Storage:  10.92 KB | Overwrites:   - | Hash Ops:  97148 | Time: 0.012s | ETA: 1213.5s
Block  28/500 | Slot:  28 | Storage:  11.31 KB | Overwrites:   - | Hash Ops: 101056 | Time: 0.029s | ETA: 1210.3s
Block  29/500 | Slot:  29 | Storage:  11.71 KB | Overwrites:   - | Hash Ops: 104607 | Time: 0.024s | ETA: 1208.9s
Block  30/500 | Slot:  30 | Storage:  12.10 KB | Overwrites:   - | Hash Ops: 106657 | Time: 0.014s | ETA: 1207.3s
Block  31/500 | Slot:  31 | Storage:  12.49 KB | Overwrites:   - | Hash Ops: 122964 | Time: 0.114s | ETA: 1205.8s
Block  32/500 | Slot:  32 | Storage:  12.89 KB | Overwrites:   - | Hash Ops: 124599 | Time: 0.012s | ETA: 1203.2s
Block  33/500 | Slot:  33 | Storage:  13.28 KB | Overwrites:   - | Hash Ops: 126914 | Time: 0.016s | ETA: 1202.0s
Block  34/500 | Slot:  34 | Storage:  13.67 KB | Overwrites:   - | Hash Ops: 129948 | Time: 0.021s | ETA: 1200.0s
Block  35/500 | Slot:  35 | Storage:  14.07 KB | Overwrites:   - | Hash Ops: 130450 | Time: 0.004s | ETA: 1198.9s
Block  36/500 | Slot:  36 | Storage:  14.46 KB | Overwrites:   - | Hash Ops: 135519 | Time: 0.034s | ETA: 1197.7s
Block  37/500 | Slot:  37 | Storage:  14.85 KB | Overwrites:   - | Hash Ops: 135543 | Time: 0.000s | ETA: 1196.2s
Block  38/500 | Slot:  38 | Storage:  15.25 KB | Overwrites:   - | Hash Ops: 141841 | Time: 0.042s | ETA: 1195.6s
Block  39/500 | Slot:  39 | Storage:  15.64 KB | Overwrites:   - | Hash Ops: 142479 | Time: 0.005s | ETA: 1193.0s
Block  40/500 | Slot:  40 | Storage:  16.03 KB | Overwrites:   - | Hash Ops: 144926 | Time: 0.017s | ETA: 1190.8s
Block  41/500 | Slot:  41 | Storage:  16.43 KB | Overwrites:   - | Hash Ops: 145494 | Time: 0.004s | ETA: 1188.3s
Block  42/500 | Slot:  42 | Storage:  16.82 KB | Overwrites:   - | Hash Ops: 145841 | Time: 0.002s | ETA: 1186.8s
Block  43/500 | Slot:  43 | Storage:  17.21 KB | Overwrites:   - | Hash Ops: 150277 | Time: 0.031s | ETA: 1185.5s
Block  44/500 | Slot:  44 | Storage:  17.61 KB | Overwrites:   - | Hash Ops: 162120 | Time: 0.086s | ETA: 1184.2s
Block  45/500 | Slot:  45 | Storage:  18.00 KB | Overwrites:   - | Hash Ops: 162926 | Time: 0.005s | ETA: 1180.3s
Block  46/500 | Slot:  46 | Storage:  18.39 KB | Overwrites:   - | Hash Ops: 163724 | Time: 0.005s | ETA: 1179.4s
Block  47/500 | Slot:  47 | Storage:  18.79 KB | Overwrites:   - | Hash Ops: 165554 | Time: 0.012s | ETA: 1177.7s
Block  48/500 | Slot:  48 | Storage:  19.18 KB | Overwrites:   - | Hash Ops: 167898 | Time: 0.016s | ETA: 1176.7s
Block  49/500 | Slot:  49 | Storage:  19.58 KB | Overwrites:   - | Hash Ops: 178173 | Time: 0.077s | ETA: 1175.0s
Block  50/500 | Slot:  50 | Storage:  19.97 KB | Overwrites:   - | Hash Ops: 178661 | Time: 0.003s | ETA: 1172.0s
Block  51/500 | Slot:  51 | Storage:  20.37 KB | Overwrites:   - | Hash Ops: 182204 | Time: 0.025s | ETA: 1169.2s
Block  52/500 | Slot:  52 | Storage:  20.76 KB | Overwrites:   - | Hash Ops: 182465 | Time: 0.002s | ETA: 1165.7s
Block  53/500 | Slot:  53 | Storage:  21.15 KB | Overwrites:   - | Hash Ops: 185937 | Time: 0.025s | ETA: 1164.6s
Block  54/500 | Slot:  54 | Storage:  21.55 KB | Overwrites:   - | Hash Ops: 188140 | Time: 0.015s | ETA: 1162.4s
Block  55/500 | Slot:  55 | Storage:  21.94 KB | Overwrites:   - | Hash Ops: 192564 | Time: 0.031s | ETA: 1160.6s
Block  56/500 | Slot:  56 | Storage:  22.34 KB | Overwrites:   - | Hash Ops: 194473 | Time: 0.013s | ETA: 1157.5s
Block  57/500 | Slot:  57 | Storage:  22.73 KB | Overwrites:   - | Hash Ops: 202769 | Time: 0.057s | ETA: 1155.5s
Block  58/500 | Slot:  58 | Storage:  23.12 KB | Overwrites:   - | Hash Ops: 205947 | Time: 0.036s | ETA: 1152.2s
Block  59/500 | Slot:  59 | Storage:  23.52 KB | Overwrites:   - | Hash Ops: 213893 | Time: 0.056s | ETA: 1149.6s
Block  60/500 | Slot:  60 | Storage:  23.91 KB | Overwrites:   - | Hash Ops: 216678 | Time: 0.019s | ETA: 1146.3s
Block  61/500 | Slot:  61 | Storage:  24.31 KB | Overwrites:   - | Hash Ops: 229172 | Time: 0.093s | ETA: 1143.6s
Block  62/500 | Slot:  62 | Storage:  24.70 KB | Overwrites:   - | Hash Ops: 231017 | Time: 0.012s | ETA: 1141.7s
Block  63/500 | Slot:  63 | Storage:  25.09 KB | Overwrites:   - | Hash Ops: 234167 | Time: 0.021s | ETA: 1138.9s
Block  64/500 | Slot:  64 | Storage:  25.48 KB | Overwrites:   - | Hash Ops: 237003 | Time: 0.019s | ETA: 1136.8s
Block  65/500 | Slot:  65 | Storage:  25.88 KB | Overwrites:   - | Hash Ops: 237916 | Time: 0.007s | ETA: 1134.4s
Block  66/500 | Slot:  66 | Storage:  26.27 KB | Overwrites:   - | Hash Ops: 238265 | Time: 0.002s | ETA: 1131.0s
Block  67/500 | Slot:  67 | Storage:  26.66 KB | Overwrites:   - | Hash Ops: 238738 | Time: 0.004s | ETA: 1128.1s
Block  68/500 | Slot:  68 | Storage:  27.06 KB | Overwrites:   - | Hash Ops: 243392 | Time: 0.032s | ETA: 1125.7s
Block  69/500 | Slot:  69 | Storage:  27.45 KB | Overwrites:   - | Hash Ops: 244834 | Time: 0.010s | ETA: 1123.4s
Block  70/500 | Slot:  70 | Storage:  27.84 KB | Overwrites:   - | Hash Ops: 245580 | Time: 0.006s | ETA: 1121.5s
Block  71/500 | Slot:  71 | Storage:  28.24 KB | Overwrites:   - | Hash Ops: 247467 | Time: 0.013s | ETA: 1119.1s
Block  72/500 | Slot:  72 | Storage:  28.63 KB | Overwrites:   - | Hash Ops: 251539 | Time: 0.028s | ETA: 1115.9s
Block  73/500 | Slot:  73 | Storage:  29.02 KB | Overwrites:   - | Hash Ops: 255537 | Time: 0.028s | ETA: 1112.8s
Block  74/500 | Slot:  74 | Storage:  29.42 KB | Overwrites:   - | Hash Ops: 256889 | Time: 0.009s | ETA: 1110.2s
Block  75/500 | Slot:  75 | Storage:  29.81 KB | Overwrites:   - | Hash Ops: 258171 | Time: 0.009s | ETA: 1107.3s
Block  76/500 | Slot:  76 | Storage:  30.20 KB | Overwrites:   - | Hash Ops: 274592 | Time: 0.113s | ETA: 1105.6s
Block  77/500 | Slot:  77 | Storage:  30.60 KB | Overwrites:   - | Hash Ops: 275685 | Time: 0.008s | ETA: 1102.6s
Block  78/500 | Slot:  78 | Storage:  30.99 KB | Overwrites:   - | Hash Ops: 277520 | Time: 0.013s | ETA: 1100.5s
Block  79/500 | Slot:  79 | Storage:  31.39 KB | Overwrites:   - | Hash Ops: 278393 | Time: 0.007s | ETA: 1098.3s
Block  80/500 | Slot:  80 | Storage:  31.78 KB | Overwrites:   - | Hash Ops: 280740 | Time: 0.017s | ETA: 1095.8s
Block  81/500 | Slot:  81 | Storage:  32.17 KB | Overwrites:   - | Hash Ops: 290398 | Time: 0.068s | ETA: 1093.4s
Block  82/500 | Slot:  82 | Storage:  32.57 KB | Overwrites:   - | Hash Ops: 291055 | Time: 0.005s | ETA: 1090.7s
Block  83/500 | Slot:  83 | Storage:  32.96 KB | Overwrites:   - | Hash Ops: 293767 | Time: 0.019s | ETA: 1088.5s
Block  84/500 | Slot:  84 | Storage:  33.35 KB | Overwrites:   - | Hash Ops: 299903 | Time: 0.043s | ETA: 1086.8s
Block  85/500 | Slot:  85 | Storage:  33.75 KB | Overwrites:   - | Hash Ops: 304958 | Time: 0.038s | ETA: 1084.6s
Block  86/500 | Slot:  86 | Storage:  34.14 KB | Overwrites:   - | Hash Ops: 307070 | Time: 0.014s | ETA: 1082.2s
Block  87/500 | Slot:  87 | Storage:  34.54 KB | Overwrites:   - | Hash Ops: 309095 | Time: 0.014s | ETA: 1079.1s
Block  88/500 | Slot:  88 | Storage:  34.93 KB | Overwrites:   - | Hash Ops: 312632 | Time: 0.025s | ETA: 1077.0s
Block  89/500 | Slot:  89 | Storage:  35.32 KB | Overwrites:   - | Hash Ops: 317124 | Time: 0.032s | ETA: 1074.9s
Block  90/500 | Slot:  90 | Storage:  35.71 KB | Overwrites:   - | Hash Ops: 321223 | Time: 0.029s | ETA: 1072.7s
Block  91/500 | Slot:  91 | Storage:  36.11 KB | Overwrites:   - | Hash Ops: 322022 | Time: 0.006s | ETA: 1070.2s
Block  92/500 | Slot:  92 | Storage:  36.50 KB | Overwrites:   - | Hash Ops: 322089 | Time: 0.001s | ETA: 1067.4s
Block  93/500 | Slot:  93 | Storage:  36.89 KB | Overwrites:   - | Hash Ops: 325093 | Time: 0.032s | ETA: 1064.9s
Block  94/500 | Slot:  94 | Storage:  37.28 KB | Overwrites:   - | Hash Ops: 325583 | Time: 0.004s | ETA: 1062.1s
Block  95/500 | Slot:  95 | Storage:  37.68 KB | Overwrites:   - | Hash Ops: 331265 | Time: 0.055s | ETA: 1059.7s
Block  96/500 | Slot:  96 | Storage:  38.07 KB | Overwrites:   - | Hash Ops: 331445 | Time: 0.001s | ETA: 1057.2s
Block  97/500 | Slot:  97 | Storage:  38.46 KB | Overwrites:   - | Hash Ops: 334956 | Time: 0.031s | ETA: 1055.1s
Block  98/500 | Slot:  98 | Storage:  38.85 KB | Overwrites:   - | Hash Ops: 337192 | Time: 0.017s | ETA: 1052.3s
Block  99/500 | Slot:  99 | Storage:  39.25 KB | Overwrites:   - | Hash Ops: 338885 | Time: 0.022s | ETA: 1049.6s
Block 100/500 | Slot:   0 | Storage:  39.34 KB | Overwrites: Slot   0 | Hash Ops: 343305 | Time: 0.047s | ETA: 1047.3s
Block 101/500 | Slot:   1 | Storage:  39.34 KB | Overwrites: Slot   1 | Hash Ops: 344329 | Time: 0.013s | ETA: 1044.2s
Block 102/500 | Slot:   2 | Storage:  39.34 KB | Overwrites: Slot   2 | Hash Ops: 348332 | Time: 0.038s | ETA: 1041.3s
Block 103/500 | Slot:   3 | Storage:  39.35 KB | Overwrites: Slot   3 | Hash Ops: 349530 | Time: 0.014s | ETA: 1039.3s
Block 104/500 | Slot:   4 | Storage:  39.35 KB | Overwrites: Slot   4 | Hash Ops: 352949 | Time: 0.038s | ETA: 1036.4s
Block 105/500 | Slot:   5 | Storage:  39.36 KB | Overwrites: Slot   5 | Hash Ops: 355579 | Time: 0.023s | ETA: 1033.8s
Block 106/500 | Slot:   6 | Storage:  39.37 KB | Overwrites: Slot   6 | Hash Ops: 355754 | Time: 0.002s | ETA: 1031.1s
Block 107/500 | Slot:   7 | Storage:  39.37 KB | Overwrites: Slot   7 | Hash Ops: 356571 | Time: 0.006s | ETA: 1028.8s
Block 108/500 | Slot:   8 | Storage:  39.38 KB | Overwrites: Slot   8 | Hash Ops: 358466 | Time: 0.029s | ETA: 1026.3s
Block 109/500 | Slot:   9 | Storage:  39.38 KB | Overwrites: Slot   9 | Hash Ops: 363026 | Time: 0.037s | ETA: 1023.9s
Block 110/500 | Slot:  10 | Storage:  39.38 KB | Overwrites: Slot  10 | Hash Ops: 367339 | Time: 0.033s | ETA: 1021.1s
Block 111/500 | Slot:  11 | Storage:  39.39 KB | Overwrites: Slot  11 | Hash Ops: 375362 | Time: 0.076s | ETA: 1018.9s
Block 112/500 | Slot:  12 | Storage:  39.39 KB | Overwrites: Slot  12 | Hash Ops: 375910 | Time: 0.004s | ETA: 1015.9s
Block 113/500 | Slot:  13 | Storage:  39.39 KB | Overwrites: Slot  13 | Hash Ops: 378745 | Time: 0.021s | ETA: 1013.4s
Block 114/500 | Slot:  14 | Storage:  39.39 KB | Overwrites: Slot  14 | Hash Ops: 379259 | Time: 0.004s | ETA: 1010.8s
Block 115/500 | Slot:  15 | Storage:  39.39 KB | Overwrites: Slot  15 | Hash Ops: 379345 | Time: 0.001s | ETA: 1008.3s
Block 116/500 | Slot:  16 | Storage:  39.39 KB | Overwrites: Slot  16 | Hash Ops: 387247 | Time: 0.095s | ETA: 1006.0s
Block 117/500 | Slot:  17 | Storage:  39.39 KB | Overwrites: Slot  17 | Hash Ops: 390676 | Time: 0.031s | ETA: 1003.6s
Block 118/500 | Slot:  18 | Storage:  39.40 KB | Overwrites: Slot  18 | Hash Ops: 393612 | Time: 0.028s | ETA: 1000.7s
Block 119/500 | Slot:  19 | Storage:  39.40 KB | Overwrites: Slot  19 | Hash Ops: 393800 | Time: 0.001s | ETA: 998.2s
Block 120/500 | Slot:  20 | Storage:  39.40 KB | Overwrites: Slot  20 | Hash Ops: 398010 | Time: 0.030s | ETA: 995.9s
Block 121/500 | Slot:  21 | Storage:  39.41 KB | Overwrites: Slot  21 | Hash Ops: 398146 | Time: 0.004s | ETA: 993.6s
Block 122/500 | Slot:  22 | Storage:  39.41 KB | Overwrites: Slot  22 | Hash Ops: 405803 | Time: 0.084s | ETA: 991.0s
Block 123/500 | Slot:  23 | Storage:  39.41 KB | Overwrites: Slot  23 | Hash Ops: 417440 | Time: 0.110s | ETA: 989.0s
Block 124/500 | Slot:  24 | Storage:  39.42 KB | Overwrites: Slot  24 | Hash Ops: 427900 | Time: 0.105s | ETA: 986.7s
Block 125/500 | Slot:  25 | Storage:  39.42 KB | Overwrites: Slot  25 | Hash Ops: 429110 | Time: 0.018s | ETA: 984.4s
Block 126/500 | Slot:  26 | Storage:  39.42 KB | Overwrites: Slot  26 | Hash Ops: 431048 | Time: 0.014s | ETA: 981.5s
Block 127/500 | Slot:  27 | Storage:  39.42 KB | Overwrites: Slot  27 | Hash Ops: 431349 | Time: 0.006s | ETA: 978.6s
Block 128/500 | Slot:  28 | Storage:  39.42 KB | Overwrites: Slot  28 | Hash Ops: 435016 | Time: 0.040s | ETA: 976.2s
Block 129/500 | Slot:  29 | Storage:  39.42 KB | Overwrites: Slot  29 | Hash Ops: 440033 | Time: 0.059s | ETA: 973.6s
Block 130/500 | Slot:  30 | Storage:  39.43 KB | Overwrites: Slot  30 | Hash Ops: 444183 | Time: 0.038s | ETA: 971.3s
Block 131/500 | Slot:  31 | Storage:  39.43 KB | Overwrites: Slot  31 | Hash Ops: 446633 | Time: 0.043s | ETA: 968.7s
Block 132/500 | Slot:  32 | Storage:  39.43 KB | Overwrites: Slot  32 | Hash Ops: 451915 | Time: 0.059s | ETA: 966.0s
Block 133/500 | Slot:  33 | Storage:  39.43 KB | Overwrites: Slot  33 | Hash Ops: 454174 | Time: 0.024s | ETA: 963.1s
Block 134/500 | Slot:  34 | Storage:  39.44 KB | Overwrites: Slot  34 | Hash Ops: 461406 | Time: 0.112s | ETA: 961.2s
Block 135/500 | Slot:  35 | Storage:  39.44 KB | Overwrites: Slot  35 | Hash Ops: 463706 | Time: 0.020s | ETA: 959.0s
Block 136/500 | Slot:  36 | Storage:  39.44 KB | Overwrites: Slot  36 | Hash Ops: 478333 | Time: 0.150s | ETA: 956.4s
Block 137/500 | Slot:  37 | Storage:  39.45 KB | Overwrites: Slot  37 | Hash Ops: 479894 | Time: 0.014s | ETA: 954.0s
Block 138/500 | Slot:  38 | Storage:  39.45 KB | Overwrites: Slot  38 | Hash Ops: 482007 | Time: 0.026s | ETA: 951.3s
Block 139/500 | Slot:  39 | Storage:  39.46 KB | Overwrites: Slot  39 | Hash Ops: 483749 | Time: 0.025s | ETA: 948.9s
Block 140/500 | Slot:  40 | Storage:  39.46 KB | Overwrites: Slot  40 | Hash Ops: 485596 | Time: 0.026s | ETA: 946.6s
Block 141/500 | Slot:  41 | Storage:  39.46 KB | Overwrites: Slot  41 | Hash Ops: 487053 | Time: 0.027s | ETA: 944.0s
Block 142/500 | Slot:  42 | Storage:  39.46 KB | Overwrites: Slot  42 | Hash Ops: 489303 | Time: 0.029s | ETA: 941.2s
Block 143/500 | Slot:  43 | Storage:  39.47 KB | Overwrites: Slot  43 | Hash Ops: 490318 | Time: 0.018s | ETA: 938.3s
Block 144/500 | Slot:  44 | Storage:  39.47 KB | Overwrites: Slot  44 | Hash Ops: 493254 | Time: 0.032s | ETA: 935.8s
Block 145/500 | Slot:  45 | Storage:  39.48 KB | Overwrites: Slot  45 | Hash Ops: 503491 | Time: 0.098s | ETA: 933.1s
Block 146/500 | Slot:  46 | Storage:  39.48 KB | Overwrites: Slot  46 | Hash Ops: 508017 | Time: 0.066s | ETA: 930.5s
Block 147/500 | Slot:  47 | Storage:  39.48 KB | Overwrites: Slot  47 | Hash Ops: 512001 | Time: 0.031s | ETA: 927.5s
Block 148/500 | Slot:  48 | Storage:  39.48 KB | Overwrites: Slot  48 | Hash Ops: 520963 | Time: 0.076s | ETA: 924.9s
Block 149/500 | Slot:  49 | Storage:  39.49 KB | Overwrites: Slot  49 | Hash Ops: 525168 | Time: 0.031s | ETA: 922.1s
Block 150/500 | Slot:  50 | Storage:  39.49 KB | Overwrites: Slot  50 | Hash Ops: 526816 | Time: 0.044s | ETA: 919.3s
Block 151/500 | Slot:  51 | Storage:  39.49 KB | Overwrites: Slot  51 | Hash Ops: 530380 | Time: 0.030s | ETA: 917.0s
Block 152/500 | Slot:  52 | Storage:  39.50 KB | Overwrites: Slot  52 | Hash Ops: 532838 | Time: 0.021s | ETA: 914.6s
Block 153/500 | Slot:  53 | Storage:  39.49 KB | Overwrites: Slot  53 | Hash Ops: 533036 | Time: 0.005s | ETA: 911.8s
Block 154/500 | Slot:  54 | Storage:  39.50 KB | Overwrites: Slot  54 | Hash Ops: 539193 | Time: 0.064s | ETA: 909.4s
Block 155/500 | Slot:  55 | Storage:  39.50 KB | Overwrites: Slot  55 | Hash Ops: 551912 | Time: 0.137s | ETA: 907.1s
Block 156/500 | Slot:  56 | Storage:  39.50 KB | Overwrites: Slot  56 | Hash Ops: 553280 | Time: 0.010s | ETA: 904.2s
Block 157/500 | Slot:  57 | Storage:  39.50 KB | Overwrites: Slot  57 | Hash Ops: 560097 | Time: 0.070s | ETA: 901.8s
Block 158/500 | Slot:  58 | Storage:  39.51 KB | Overwrites: Slot  58 | Hash Ops: 562159 | Time: 0.015s | ETA: 899.2s
Block 159/500 | Slot:  59 | Storage:  39.51 KB | Overwrites: Slot  59 | Hash Ops: 565495 | Time: 0.034s | ETA: 896.7s
Block 160/500 | Slot:  60 | Storage:  39.51 KB | Overwrites: Slot  60 | Hash Ops: 566843 | Time: 0.011s | ETA: 894.3s
Block 161/500 | Slot:  61 | Storage:  39.51 KB | Overwrites: Slot  61 | Hash Ops: 567110 | Time: 0.002s | ETA: 891.4s
Block 162/500 | Slot:  62 | Storage:  39.52 KB | Overwrites: Slot  62 | Hash Ops: 568694 | Time: 0.011s | ETA: 888.8s
Block 163/500 | Slot:  63 | Storage:  39.52 KB | Overwrites: Slot  63 | Hash Ops: 572200 | Time: 0.042s | ETA: 886.4s
Block 164/500 | Slot:  64 | Storage:  39.53 KB | Overwrites: Slot  64 | Hash Ops: 578537 | Time: 0.078s | ETA: 883.8s
Block 165/500 | Slot:  65 | Storage:  39.53 KB | Overwrites: Slot  65 | Hash Ops: 579629 | Time: 0.025s | ETA: 881.3s
Block 166/500 | Slot:  66 | Storage:  39.54 KB | Overwrites: Slot  66 | Hash Ops: 590353 | Time: 0.136s | ETA: 879.0s
Block 167/500 | Slot:  67 | Storage:  39.54 KB | Overwrites: Slot  67 | Hash Ops: 591358 | Time: 0.008s | ETA: 876.5s
Block 168/500 | Slot:  68 | Storage:  39.54 KB | Overwrites: Slot  68 | Hash Ops: 592869 | Time: 0.024s | ETA: 874.0s
Block 169/500 | Slot:  69 | Storage:  39.54 KB | Overwrites: Slot  69 | Hash Ops: 596520 | Time: 0.031s | ETA: 871.4s
Block 170/500 | Slot:  70 | Storage:  39.55 KB | Overwrites: Slot  70 | Hash Ops: 599602 | Time: 0.035s | ETA: 869.0s
Block 171/500 | Slot:  71 | Storage:  39.55 KB | Overwrites: Slot  71 | Hash Ops: 600258 | Time: 0.014s | ETA: 866.0s
Block 172/500 | Slot:  72 | Storage:  39.55 KB | Overwrites: Slot  72 | Hash Ops: 601615 | Time: 0.017s | ETA: 863.4s
Block 173/500 | Slot:  73 | Storage:  39.55 KB | Overwrites: Slot  73 | Hash Ops: 601844 | Time: 0.008s | ETA: 860.8s
Block 174/500 | Slot:  74 | Storage:  39.56 KB | Overwrites: Slot  74 | Hash Ops: 603275 | Time: 0.010s | ETA: 858.1s
Block 175/500 | Slot:  75 | Storage:  39.56 KB | Overwrites: Slot  75 | Hash Ops: 603477 | Time: 0.002s | ETA: 855.5s
Block 176/500 | Slot:  76 | Storage:  39.56 KB | Overwrites: Slot  76 | Hash Ops: 603799 | Time: 0.002s | ETA: 852.9s
Block 177/500 | Slot:  77 | Storage:  39.56 KB | Overwrites: Slot  77 | Hash Ops: 605836 | Time: 0.016s | ETA: 850.5s
Block 178/500 | Slot:  78 | Storage:  39.56 KB | Overwrites: Slot  78 | Hash Ops: 608408 | Time: 0.051s | ETA: 848.0s
Block 179/500 | Slot:  79 | Storage:  39.56 KB | Overwrites: Slot  79 | Hash Ops: 612712 | Time: 0.030s | ETA: 845.4s
Block 180/500 | Slot:  80 | Storage:  39.57 KB | Overwrites: Slot  80 | Hash Ops: 614770 | Time: 0.017s | ETA: 842.7s
Block 181/500 | Slot:  81 | Storage:  39.57 KB | Overwrites: Slot  81 | Hash Ops: 617380 | Time: 0.019s | ETA: 840.0s
Block 182/500 | Slot:  82 | Storage:  39.57 KB | Overwrites: Slot  82 | Hash Ops: 618683 | Time: 0.009s | ETA: 837.7s
Block 183/500 | Slot:  83 | Storage:  39.58 KB | Overwrites: Slot  83 | Hash Ops: 624731 | Time: 0.041s | ETA: 835.1s
Block 184/500 | Slot:  84 | Storage:  39.58 KB | Overwrites: Slot  84 | Hash Ops: 628940 | Time: 0.028s | ETA: 832.5s
Block 185/500 | Slot:  85 | Storage:  39.58 KB | Overwrites: Slot  85 | Hash Ops: 629219 | Time: 0.002s | ETA: 830.0s
Block 186/500 | Slot:  86 | Storage:  39.58 KB | Overwrites: Slot  86 | Hash Ops: 629304 | Time: 0.002s | ETA: 827.3s
Block 187/500 | Slot:  87 | Storage:  39.58 KB | Overwrites: Slot  87 | Hash Ops: 635929 | Time: 0.045s | ETA: 824.7s
Block 188/500 | Slot:  88 | Storage:  39.59 KB | Overwrites: Slot  88 | Hash Ops: 637426 | Time: 0.011s | ETA: 822.0s
Block 189/500 | Slot:  89 | Storage:  39.59 KB | Overwrites: Slot  89 | Hash Ops: 638142 | Time: 0.005s | ETA: 819.4s
Block 190/500 | Slot:  90 | Storage:  39.60 KB | Overwrites: Slot  90 | Hash Ops: 639663 | Time: 0.014s | ETA: 816.6s
Block 191/500 | Slot:  91 | Storage:  39.60 KB | Overwrites: Slot  91 | Hash Ops: 641595 | Time: 0.019s | ETA: 813.9s
Block 192/500 | Slot:  92 | Storage:  39.60 KB | Overwrites: Slot  92 | Hash Ops: 645626 | Time: 0.033s | ETA: 811.1s
Block 193/500 | Slot:  93 | Storage:  39.61 KB | Overwrites: Slot  93 | Hash Ops: 646970 | Time: 0.009s | ETA: 808.5s
Block 194/500 | Slot:  94 | Storage:  39.61 KB | Overwrites: Slot  94 | Hash Ops: 648200 | Time: 0.016s | ETA: 806.0s
Block 195/500 | Slot:  95 | Storage:  39.62 KB | Overwrites: Slot  95 | Hash Ops: 650897 | Time: 0.021s | ETA: 803.4s
Block 196/500 | Slot:  96 | Storage:  39.62 KB | Overwrites: Slot  96 | Hash Ops: 656991 | Time: 0.046s | ETA: 800.9s
Block 197/500 | Slot:  97 | Storage:  39.62 KB | Overwrites: Slot  97 | Hash Ops: 663704 | Time: 0.049s | ETA: 798.4s
Block 198/500 | Slot:  98 | Storage:  39.63 KB | Overwrites: Slot  98 | Hash Ops: 665929 | Time: 0.015s | ETA: 795.6s
Block 199/500 | Slot:  99 | Storage:  39.63 KB | Overwrites: Slot  99 | Hash Ops: 666102 | Time: 0.002s | ETA: 792.7s
Block 200/500 | Slot:   0 | Storage:  39.63 KB | Overwrites: Slot   0 | Hash Ops: 673190 | Time: 0.047s | ETA: 790.3s
Block 201/500 | Slot:   1 | Storage:  39.63 KB | Overwrites: Slot   1 | Hash Ops: 673847 | Time: 0.004s | ETA: 787.6s
Block 202/500 | Slot:   2 | Storage:  39.63 KB | Overwrites: Slot   2 | Hash Ops: 675565 | Time: 0.015s | ETA: 784.7s
Block 203/500 | Slot:   3 | Storage:  39.63 KB | Overwrites: Slot   3 | Hash Ops: 683688 | Time: 0.057s | ETA: 782.2s
Block 204/500 | Slot:   4 | Storage:  39.63 KB | Overwrites: Slot   4 | Hash Ops: 688804 | Time: 0.034s | ETA: 779.8s
Block 205/500 | Slot:   5 | Storage:  39.63 KB | Overwrites: Slot   5 | Hash Ops: 689911 | Time: 0.011s | ETA: 777.0s
Block 206/500 | Slot:   6 | Storage:  39.63 KB | Overwrites: Slot   6 | Hash Ops: 691099 | Time: 0.012s | ETA: 774.5s
Block 207/500 | Slot:   7 | Storage:  39.63 KB | Overwrites: Slot   7 | Hash Ops: 695596 | Time: 0.030s | ETA: 771.9s
Block 208/500 | Slot:   8 | Storage:  39.63 KB | Overwrites: Slot   8 | Hash Ops: 698890 | Time: 0.026s | ETA: 769.3s
Block 209/500 | Slot:   9 | Storage:  39.63 KB | Overwrites: Slot   9 | Hash Ops: 699861 | Time: 0.010s | ETA: 766.5s
Block 210/500 | Slot:  10 | Storage:  39.63 KB | Overwrites: Slot  10 | Hash Ops: 715795 | Time: 0.107s | ETA: 763.9s
Block 211/500 | Slot:  11 | Storage:  39.63 KB | Overwrites: Slot  11 | Hash Ops: 718353 | Time: 0.023s | ETA: 761.4s
Block 212/500 | Slot:  12 | Storage:  39.64 KB | Overwrites: Slot  12 | Hash Ops: 725294 | Time: 0.054s | ETA: 758.7s
Block 213/500 | Slot:  13 | Storage:  39.64 KB | Overwrites: Slot  13 | Hash Ops: 726336 | Time: 0.008s | ETA: 756.2s
Block 214/500 | Slot:  14 | Storage:  39.64 KB | Overwrites: Slot  14 | Hash Ops: 729657 | Time: 0.022s | ETA: 753.6s
Block 215/500 | Slot:  15 | Storage:  39.64 KB | Overwrites: Slot  15 | Hash Ops: 733108 | Time: 0.029s | ETA: 751.0s
Block 216/500 | Slot:  16 | Storage:  39.64 KB | Overwrites: Slot  16 | Hash Ops: 735232 | Time: 0.014s | ETA: 748.5s
Block 217/500 | Slot:  17 | Storage:  39.64 KB | Overwrites: Slot  17 | Hash Ops: 736640 | Time: 0.009s | ETA: 745.9s
Block 218/500 | Slot:  18 | Storage:  39.64 KB | Overwrites: Slot  18 | Hash Ops: 739138 | Time: 0.016s | ETA: 743.1s
Block 219/500 | Slot:  19 | Storage:  39.65 KB | Overwrites: Slot  19 | Hash Ops: 745893 | Time: 0.049s | ETA: 740.6s
Block 220/500 | Slot:  20 | Storage:  39.65 KB | Overwrites: Slot  20 | Hash Ops: 752650 | Time: 0.047s | ETA: 737.9s
Block 221/500 | Slot:  21 | Storage:  39.65 KB | Overwrites: Slot  21 | Hash Ops: 753289 | Time: 0.004s | ETA: 735.2s
Block 222/500 | Slot:  22 | Storage:  39.64 KB | Overwrites: Slot  22 | Hash Ops: 755669 | Time: 0.016s | ETA: 732.4s
Block 223/500 | Slot:  23 | Storage:  39.65 KB | Overwrites: Slot  23 | Hash Ops: 758152 | Time: 0.017s | ETA: 729.8s
Block 224/500 | Slot:  24 | Storage:  39.64 KB | Overwrites: Slot  24 | Hash Ops: 758432 | Time: 0.002s | ETA: 727.1s
Block 225/500 | Slot:  25 | Storage:  39.64 KB | Overwrites: Slot  25 | Hash Ops: 761645 | Time: 0.023s | ETA: 724.3s
Block 226/500 | Slot:  26 | Storage:  39.65 KB | Overwrites: Slot  26 | Hash Ops: 763521 | Time: 0.017s | ETA: 721.8s
Block 227/500 | Slot:  27 | Storage:  39.65 KB | Overwrites: Slot  27 | Hash Ops: 768389 | Time: 0.033s | ETA: 719.0s
Block 228/500 | Slot:  28 | Storage:  39.65 KB | Overwrites: Slot  28 | Hash Ops: 768438 | Time: 0.000s | ETA: 716.4s
Block 229/500 | Slot:  29 | Storage:  39.65 KB | Overwrites: Slot  29 | Hash Ops: 776608 | Time: 0.054s | ETA: 713.7s
Block 230/500 | Slot:  30 | Storage:  39.65 KB | Overwrites: Slot  30 | Hash Ops: 777960 | Time: 0.009s | ETA: 711.0s
Block 231/500 | Slot:  31 | Storage:  39.65 KB | Overwrites: Slot  31 | Hash Ops: 778606 | Time: 0.004s | ETA: 708.3s
Block 232/500 | Slot:  32 | Storage:  39.65 KB | Overwrites: Slot  32 | Hash Ops: 780508 | Time: 0.016s | ETA: 705.6s
Block 233/500 | Slot:  33 | Storage:  39.65 KB | Overwrites: Slot  33 | Hash Ops: 781483 | Time: 0.014s | ETA: 702.9s
Block 234/500 | Slot:  34 | Storage:  39.65 KB | Overwrites: Slot  34 | Hash Ops: 782771 | Time: 0.013s | ETA: 700.3s
Block 235/500 | Slot:  35 | Storage:  39.65 KB | Overwrites: Slot  35 | Hash Ops: 785957 | Time: 0.021s | ETA: 697.7s
Block 236/500 | Slot:  36 | Storage:  39.65 KB | Overwrites: Slot  36 | Hash Ops: 786695 | Time: 0.006s | ETA: 695.0s
Block 237/500 | Slot:  37 | Storage:  39.65 KB | Overwrites: Slot  37 | Hash Ops: 790094 | Time: 0.024s | ETA: 692.5s
Block 238/500 | Slot:  38 | Storage:  39.65 KB | Overwrites: Slot  38 | Hash Ops: 791001 | Time: 0.006s | ETA: 689.8s
Block 239/500 | Slot:  39 | Storage:  39.64 KB | Overwrites: Slot  39 | Hash Ops: 795234 | Time: 0.029s | ETA: 687.1s
Block 240/500 | Slot:  40 | Storage:  39.65 KB | Overwrites: Slot  40 | Hash Ops: 796949 | Time: 0.011s | ETA: 684.4s
Block 241/500 | Slot:  41 | Storage:  39.65 KB | Overwrites: Slot  41 | Hash Ops: 797063 | Time: 0.001s | ETA: 682.0s
Block 242/500 | Slot:  42 | Storage:  39.65 KB | Overwrites: Slot  42 | Hash Ops: 808006 | Time: 0.074s | ETA: 679.4s
Block 243/500 | Slot:  43 | Storage:  39.65 KB | Overwrites: Slot  43 | Hash Ops: 829123 | Time: 0.142s | ETA: 676.8s
Block 244/500 | Slot:  44 | Storage:  39.65 KB | Overwrites: Slot  44 | Hash Ops: 847820 | Time: 0.126s | ETA: 674.2s
Block 245/500 | Slot:  45 | Storage:  39.64 KB | Overwrites: Slot  45 | Hash Ops: 848518 | Time: 0.008s | ETA: 671.4s
Block 246/500 | Slot:  46 | Storage:  39.64 KB | Overwrites: Slot  46 | Hash Ops: 851787 | Time: 0.022s | ETA: 668.9s
Block 247/500 | Slot:  47 | Storage:  39.64 KB | Overwrites: Slot  47 | Hash Ops: 853000 | Time: 0.012s | ETA: 666.3s
Block 248/500 | Slot:  48 | Storage:  39.64 KB | Overwrites: Slot  48 | Hash Ops: 853430 | Time: 0.003s | ETA: 663.6s
Block 249/500 | Slot:  49 | Storage:  39.64 KB | Overwrites: Slot  49 | Hash Ops: 856796 | Time: 0.027s | ETA: 661.2s
Block 250/500 | Slot:  50 | Storage:  39.64 KB | Overwrites: Slot  50 | Hash Ops: 862005 | Time: 0.038s | ETA: 658.5s
Block 251/500 | Slot:  51 | Storage:  39.65 KB | Overwrites: Slot  51 | Hash Ops: 873694 | Time: 0.080s | ETA: 655.9s
Block 252/500 | Slot:  52 | Storage:  39.64 KB | Overwrites: Slot  52 | Hash Ops: 876453 | Time: 0.018s | ETA: 653.2s
Block 253/500 | Slot:  53 | Storage:  39.65 KB | Overwrites: Slot  53 | Hash Ops: 877447 | Time: 0.007s | ETA: 650.6s
Block 254/500 | Slot:  54 | Storage:  39.64 KB | Overwrites: Slot  54 | Hash Ops: 877555 | Time: 0.003s | ETA: 647.9s
Block 255/500 | Slot:  55 | Storage:  39.64 KB | Overwrites: Slot  55 | Hash Ops: 878186 | Time: 0.012s | ETA: 645.3s
Block 256/500 | Slot:  56 | Storage:  39.64 KB | Overwrites: Slot  56 | Hash Ops: 880985 | Time: 0.019s | ETA: 642.7s
Block 257/500 | Slot:  57 | Storage:  39.64 KB | Overwrites: Slot  57 | Hash Ops: 884503 | Time: 0.032s | ETA: 639.9s
Block 258/500 | Slot:  58 | Storage:  39.64 KB | Overwrites: Slot  58 | Hash Ops: 886047 | Time: 0.015s | ETA: 637.1s
Block 259/500 | Slot:  59 | Storage:  39.64 KB | Overwrites: Slot  59 | Hash Ops: 889339 | Time: 0.025s | ETA: 634.4s
Block 260/500 | Slot:  60 | Storage:  39.64 KB | Overwrites: Slot  60 | Hash Ops: 893629 | Time: 0.032s | ETA: 631.7s
Block 261/500 | Slot:  61 | Storage:  39.65 KB | Overwrites: Slot  61 | Hash Ops: 894986 | Time: 0.013s | ETA: 628.9s
Block 262/500 | Slot:  62 | Storage:  39.65 KB | Overwrites: Slot  62 | Hash Ops: 900347 | Time: 0.039s | ETA: 626.3s
Block 263/500 | Slot:  63 | Storage:  39.64 KB | Overwrites: Slot  63 | Hash Ops: 900896 | Time: 0.008s | ETA: 623.6s
Block 264/500 | Slot:  64 | Storage:  39.64 KB | Overwrites: Slot  64 | Hash Ops: 904362 | Time: 0.029s | ETA: 620.9s
Block 265/500 | Slot:  65 | Storage:  39.64 KB | Overwrites: Slot  65 | Hash Ops: 911673 | Time: 0.050s | ETA: 618.2s
Block 266/500 | Slot:  66 | Storage:  39.64 KB | Overwrites: Slot  66 | Hash Ops: 913670 | Time: 0.017s | ETA: 615.6s
Block 267/500 | Slot:  67 | Storage:  39.64 KB | Overwrites: Slot  67 | Hash Ops: 921383 | Time: 0.051s | ETA: 612.9s
Block 268/500 | Slot:  68 | Storage:  39.64 KB | Overwrites: Slot  68 | Hash Ops: 924668 | Time: 0.027s | ETA: 610.3s
Block 269/500 | Slot:  69 | Storage:  39.64 KB | Overwrites: Slot  69 | Hash Ops: 927873 | Time: 0.021s | ETA: 607.7s
Block 270/500 | Slot:  70 | Storage:  39.64 KB | Overwrites: Slot  70 | Hash Ops: 928521 | Time: 0.007s | ETA: 605.2s
Block 271/500 | Slot:  71 | Storage:  39.64 KB | Overwrites: Slot  71 | Hash Ops: 935412 | Time: 0.046s | ETA: 602.6s
Block 272/500 | Slot:  72 | Storage:  39.65 KB | Overwrites: Slot  72 | Hash Ops: 940905 | Time: 0.074s | ETA: 600.2s
Block 273/500 | Slot:  73 | Storage:  39.65 KB | Overwrites: Slot  73 | Hash Ops: 944833 | Time: 0.044s | ETA: 597.6s
Block 274/500 | Slot:  74 | Storage:  39.65 KB | Overwrites: Slot  74 | Hash Ops: 949598 | Time: 0.056s | ETA: 595.1s
Block 275/500 | Slot:  75 | Storage:  39.65 KB | Overwrites: Slot  75 | Hash Ops: 957420 | Time: 0.087s | ETA: 592.5s
Block 276/500 | Slot:  76 | Storage:  39.65 KB | Overwrites: Slot  76 | Hash Ops: 962209 | Time: 0.035s | ETA: 589.9s
Block 277/500 | Slot:  77 | Storage:  39.65 KB | Overwrites: Slot  77 | Hash Ops: 969709 | Time: 0.056s | ETA: 587.4s
Block 278/500 | Slot:  78 | Storage:  39.66 KB | Overwrites: Slot  78 | Hash Ops: 971132 | Time: 0.014s | ETA: 584.7s
Block 279/500 | Slot:  79 | Storage:  39.66 KB | Overwrites: Slot  79 | Hash Ops: 980853 | Time: 0.076s | ETA: 582.2s
Block 280/500 | Slot:  80 | Storage:  39.66 KB | Overwrites: Slot  80 | Hash Ops: 987246 | Time: 0.056s | ETA: 579.6s
Block 281/500 | Slot:  81 | Storage:  39.66 KB | Overwrites: Slot  81 | Hash Ops: 987761 | Time: 0.004s | ETA: 577.0s
Block 282/500 | Slot:  82 | Storage:  39.66 KB | Overwrites: Slot  82 | Hash Ops: 988708 | Time: 0.007s | ETA: 574.3s
Block 283/500 | Slot:  83 | Storage:  39.65 KB | Overwrites: Slot  83 | Hash Ops: 989253 | Time: 0.004s | ETA: 571.6s
Block 284/500 | Slot:  84 | Storage:  39.66 KB | Overwrites: Slot  84 | Hash Ops: 992169 | Time: 0.024s | ETA: 569.1s
Block 285/500 | Slot:  85 | Storage:  39.66 KB | Overwrites: Slot  85 | Hash Ops: 995601 | Time: 0.035s | ETA: 566.5s
Block 286/500 | Slot:  86 | Storage:  39.66 KB | Overwrites: Slot  86 | Hash Ops: 1007547 | Time: 0.086s | ETA: 564.0s
Block 287/500 | Slot:  87 | Storage:  39.66 KB | Overwrites: Slot  87 | Hash Ops: 1007687 | Time: 0.003s | ETA: 561.4s
Block 288/500 | Slot:  88 | Storage:  39.66 KB | Overwrites: Slot  88 | Hash Ops: 1014931 | Time: 0.048s | ETA: 558.8s
Block 289/500 | Slot:  89 | Storage:  39.66 KB | Overwrites: Slot  89 | Hash Ops: 1014956 | Time: 0.000s | ETA: 556.1s
Block 290/500 | Slot:  90 | Storage:  39.66 KB | Overwrites: Slot  90 | Hash Ops: 1016048 | Time: 0.008s | ETA: 553.4s
Block 291/500 | Slot:  91 | Storage:  39.66 KB | Overwrites: Slot  91 | Hash Ops: 1017773 | Time: 0.012s | ETA: 550.9s
Block 292/500 | Slot:  92 | Storage:  39.66 KB | Overwrites: Slot  92 | Hash Ops: 1050403 | Time: 0.231s | ETA: 548.3s
Block 293/500 | Slot:  93 | Storage:  39.66 KB | Overwrites: Slot  93 | Hash Ops: 1050761 | Time: 0.003s | ETA: 545.8s
Block 294/500 | Slot:  94 | Storage:  39.66 KB | Overwrites: Slot  94 | Hash Ops: 1057498 | Time: 0.065s | ETA: 543.2s
Block 295/500 | Slot:  95 | Storage:  39.66 KB | Overwrites: Slot  95 | Hash Ops: 1058513 | Time: 0.017s | ETA: 540.5s
Block 296/500 | Slot:  96 | Storage:  39.66 KB | Overwrites: Slot  96 | Hash Ops: 1061434 | Time: 0.031s | ETA: 537.9s
Block 297/500 | Slot:  97 | Storage:  39.66 KB | Overwrites: Slot  97 | Hash Ops: 1068565 | Time: 0.057s | ETA: 535.1s
Block 298/500 | Slot:  98 | Storage:  39.66 KB | Overwrites: Slot  98 | Hash Ops: 1069481 | Time: 0.006s | ETA: 532.5s
Block 299/500 | Slot:  99 | Storage:  39.66 KB | Overwrites: Slot  99 | Hash Ops: 1070610 | Time: 0.011s | ETA: 529.9s
Block 300/500 | Slot:   0 | Storage:  39.66 KB | Overwrites: Slot   0 | Hash Ops: 1076688 | Time: 0.060s | ETA: 527.3s
Block 301/500 | Slot:   1 | Storage:  39.66 KB | Overwrites: Slot   1 | Hash Ops: 1086729 | Time: 0.068s | ETA: 524.7s
Block 302/500 | Slot:   2 | Storage:  39.66 KB | Overwrites: Slot   2 | Hash Ops: 1093422 | Time: 0.051s | ETA: 522.1s
Block 303/500 | Slot:   3 | Storage:  39.66 KB | Overwrites: Slot   3 | Hash Ops: 1095130 | Time: 0.012s | ETA: 519.5s
Block 304/500 | Slot:   4 | Storage:  39.66 KB | Overwrites: Slot   4 | Hash Ops: 1097588 | Time: 0.034s | ETA: 517.0s
Block 305/500 | Slot:   5 | Storage:  39.66 KB | Overwrites: Slot   5 | Hash Ops: 1099098 | Time: 0.027s | ETA: 514.3s
Block 306/500 | Slot:   6 | Storage:  39.66 KB | Overwrites: Slot   6 | Hash Ops: 1110662 | Time: 0.096s | ETA: 511.7s
Block 307/500 | Slot:   7 | Storage:  39.66 KB | Overwrites: Slot   7 | Hash Ops: 1117322 | Time: 0.050s | ETA: 509.1s
Block 308/500 | Slot:   8 | Storage:  39.66 KB | Overwrites: Slot   8 | Hash Ops: 1118790 | Time: 0.020s | ETA: 506.5s
Block 309/500 | Slot:   9 | Storage:  39.66 KB | Overwrites: Slot   9 | Hash Ops: 1119245 | Time: 0.003s | ETA: 503.8s
Block 310/500 | Slot:  10 | Storage:  39.66 KB | Overwrites: Slot  10 | Hash Ops: 1119336 | Time: 0.001s | ETA: 501.2s
Block 311/500 | Slot:  11 | Storage:  39.66 KB | Overwrites: Slot  11 | Hash Ops: 1130408 | Time: 0.100s | ETA: 498.6s
Block 312/500 | Slot:  12 | Storage:  39.66 KB | Overwrites: Slot  12 | Hash Ops: 1132334 | Time: 0.028s | ETA: 496.0s
Block 313/500 | Slot:  13 | Storage:  39.66 KB | Overwrites: Slot  13 | Hash Ops: 1133926 | Time: 0.013s | ETA: 493.3s
Block 314/500 | Slot:  14 | Storage:  39.66 KB | Overwrites: Slot  14 | Hash Ops: 1135391 | Time: 0.013s | ETA: 490.5s
Block 315/500 | Slot:  15 | Storage:  39.66 KB | Overwrites: Slot  15 | Hash Ops: 1138701 | Time: 0.025s | ETA: 487.8s
Block 316/500 | Slot:  16 | Storage:  39.66 KB | Overwrites: Slot  16 | Hash Ops: 1143193 | Time: 0.031s | ETA: 485.2s
Block 317/500 | Slot:  17 | Storage:  39.66 KB | Overwrites: Slot  17 | Hash Ops: 1145717 | Time: 0.021s | ETA: 482.5s
Block 318/500 | Slot:  18 | Storage:  39.66 KB | Overwrites: Slot  18 | Hash Ops: 1145964 | Time: 0.002s | ETA: 479.9s
Block 319/500 | Slot:  19 | Storage:  39.65 KB | Overwrites: Slot  19 | Hash Ops: 1146949 | Time: 0.007s | ETA: 477.2s
Block 320/500 | Slot:  20 | Storage:  39.65 KB | Overwrites: Slot  20 | Hash Ops: 1148653 | Time: 0.015s | ETA: 474.4s
Block 321/500 | Slot:  21 | Storage:  39.65 KB | Overwrites: Slot  21 | Hash Ops: 1165182 | Time: 0.156s | ETA: 471.9s
Block 322/500 | Slot:  22 | Storage:  39.65 KB | Overwrites: Slot  22 | Hash Ops: 1165751 | Time: 0.015s | ETA: 469.2s
Block 323/500 | Slot:  23 | Storage:  39.65 KB | Overwrites: Slot  23 | Hash Ops: 1166112 | Time: 0.010s | ETA: 466.6s
Block 324/500 | Slot:  24 | Storage:  39.65 KB | Overwrites: Slot  24 | Hash Ops: 1172007 | Time: 0.045s | ETA: 464.0s
Block 325/500 | Slot:  25 | Storage:  39.65 KB | Overwrites: Slot  25 | Hash Ops: 1173968 | Time: 0.026s | ETA: 461.3s
Block 326/500 | Slot:  26 | Storage:  39.65 KB | Overwrites: Slot  26 | Hash Ops: 1175470 | Time: 0.018s | ETA: 458.7s
Block 327/500 | Slot:  27 | Storage:  39.65 KB | Overwrites: Slot  27 | Hash Ops: 1176027 | Time: 0.004s | ETA: 456.1s
Block 328/500 | Slot:  28 | Storage:  39.66 KB | Overwrites: Slot  28 | Hash Ops: 1192213 | Time: 0.137s | ETA: 453.5s
Block 329/500 | Slot:  29 | Storage:  39.66 KB | Overwrites: Slot  29 | Hash Ops: 1204958 | Time: 0.120s | ETA: 450.9s
Block 330/500 | Slot:  30 | Storage:  39.66 KB | Overwrites: Slot  30 | Hash Ops: 1205638 | Time: 0.005s | ETA: 448.3s
Block 331/500 | Slot:  31 | Storage:  39.66 KB | Overwrites: Slot  31 | Hash Ops: 1209477 | Time: 0.052s | ETA: 445.8s
Block 332/500 | Slot:  32 | Storage:  39.66 KB | Overwrites: Slot  32 | Hash Ops: 1214080 | Time: 0.049s | ETA: 443.1s
Block 333/500 | Slot:  33 | Storage:  39.66 KB | Overwrites: Slot  33 | Hash Ops: 1227371 | Time: 0.093s | ETA: 440.5s
Block 334/500 | Slot:  34 | Storage:  39.66 KB | Overwrites: Slot  34 | Hash Ops: 1228696 | Time: 0.016s | ETA: 437.9s
Block 335/500 | Slot:  35 | Storage:  39.66 KB | Overwrites: Slot  35 | Hash Ops: 1237945 | Time: 0.074s | ETA: 435.2s
Block 336/500 | Slot:  36 | Storage:  39.66 KB | Overwrites: Slot  36 | Hash Ops: 1246057 | Time: 0.087s | ETA: 432.6s
Block 337/500 | Slot:  37 | Storage:  39.66 KB | Overwrites: Slot  37 | Hash Ops: 1256278 | Time: 0.071s | ETA: 430.0s
Block 338/500 | Slot:  38 | Storage:  39.66 KB | Overwrites: Slot  38 | Hash Ops: 1258591 | Time: 0.016s | ETA: 427.5s
Block 339/500 | Slot:  39 | Storage:  39.66 KB | Overwrites: Slot  39 | Hash Ops: 1263219 | Time: 0.033s | ETA: 424.8s
Block 340/500 | Slot:  40 | Storage:  39.66 KB | Overwrites: Slot  40 | Hash Ops: 1269371 | Time: 0.043s | ETA: 422.2s
Block 341/500 | Slot:  41 | Storage:  39.66 KB | Overwrites: Slot  41 | Hash Ops: 1269627 | Time: 0.002s | ETA: 419.6s
Block 342/500 | Slot:  42 | Storage:  39.66 KB | Overwrites: Slot  42 | Hash Ops: 1280656 | Time: 0.088s | ETA: 417.0s
Block 343/500 | Slot:  43 | Storage:  39.66 KB | Overwrites: Slot  43 | Hash Ops: 1294747 | Time: 0.102s | ETA: 414.4s
Block 344/500 | Slot:  44 | Storage:  39.66 KB | Overwrites: Slot  44 | Hash Ops: 1295353 | Time: 0.018s | ETA: 411.8s
Block 345/500 | Slot:  45 | Storage:  39.66 KB | Overwrites: Slot  45 | Hash Ops: 1297356 | Time: 0.017s | ETA: 409.1s
Block 346/500 | Slot:  46 | Storage:  39.66 KB | Overwrites: Slot  46 | Hash Ops: 1297595 | Time: 0.008s | ETA: 406.5s
Block 347/500 | Slot:  47 | Storage:  39.66 KB | Overwrites: Slot  47 | Hash Ops: 1297720 | Time: 0.001s | ETA: 403.7s
Block 348/500 | Slot:  48 | Storage:  39.66 KB | Overwrites: Slot  48 | Hash Ops: 1300989 | Time: 0.049s | ETA: 401.1s
Block 349/500 | Slot:  49 | Storage:  39.66 KB | Overwrites: Slot  49 | Hash Ops: 1301433 | Time: 0.004s | ETA: 398.5s
Block 350/500 | Slot:  50 | Storage:  39.66 KB | Overwrites: Slot  50 | Hash Ops: 1305562 | Time: 0.033s | ETA: 395.8s
Block 351/500 | Slot:  51 | Storage:  39.65 KB | Overwrites: Slot  51 | Hash Ops: 1310370 | Time: 0.037s | ETA: 393.1s
Block 352/500 | Slot:  52 | Storage:  39.65 KB | Overwrites: Slot  52 | Hash Ops: 1310538 | Time: 0.001s | ETA: 390.4s
Block 353/500 | Slot:  53 | Storage:  39.65 KB | Overwrites: Slot  53 | Hash Ops: 1312917 | Time: 0.021s | ETA: 387.7s
Block 354/500 | Slot:  54 | Storage:  39.66 KB | Overwrites: Slot  54 | Hash Ops: 1318645 | Time: 0.039s | ETA: 385.1s
Block 355/500 | Slot:  55 | Storage:  39.66 KB | Overwrites: Slot  55 | Hash Ops: 1322294 | Time: 0.036s | ETA: 382.4s
Block 356/500 | Slot:  56 | Storage:  39.66 KB | Overwrites: Slot  56 | Hash Ops: 1323300 | Time: 0.011s | ETA: 379.8s
Block 357/500 | Slot:  57 | Storage:  39.66 KB | Overwrites: Slot  57 | Hash Ops: 1328450 | Time: 0.048s | ETA: 377.2s
Block 358/500 | Slot:  58 | Storage:  39.66 KB | Overwrites: Slot  58 | Hash Ops: 1334824 | Time: 0.060s | ETA: 374.5s
Block 359/500 | Slot:  59 | Storage:  39.66 KB | Overwrites: Slot  59 | Hash Ops: 1335203 | Time: 0.003s | ETA: 371.9s
Block 360/500 | Slot:  60 | Storage:  39.66 KB | Overwrites: Slot  60 | Hash Ops: 1336925 | Time: 0.014s | ETA: 369.3s
Block 361/500 | Slot:  61 | Storage:  39.66 KB | Overwrites: Slot  61 | Hash Ops: 1337726 | Time: 0.006s | ETA: 366.6s
Block 362/500 | Slot:  62 | Storage:  39.66 KB | Overwrites: Slot  62 | Hash Ops: 1339646 | Time: 0.020s | ETA: 364.0s
Block 363/500 | Slot:  63 | Storage:  39.66 KB | Overwrites: Slot  63 | Hash Ops: 1340668 | Time: 0.008s | ETA: 361.3s
Block 364/500 | Slot:  64 | Storage:  39.66 KB | Overwrites: Slot  64 | Hash Ops: 1348521 | Time: 0.081s | ETA: 358.7s
Block 365/500 | Slot:  65 | Storage:  39.66 KB | Overwrites: Slot  65 | Hash Ops: 1358668 | Time: 0.078s | ETA: 356.0s
Block 366/500 | Slot:  66 | Storage:  39.66 KB | Overwrites: Slot  66 | Hash Ops: 1365704 | Time: 0.048s | ETA: 353.3s
Block 367/500 | Slot:  67 | Storage:  39.66 KB | Overwrites: Slot  67 | Hash Ops: 1369925 | Time: 0.029s | ETA: 350.7s
Block 368/500 | Slot:  68 | Storage:  39.66 KB | Overwrites: Slot  68 | Hash Ops: 1376896 | Time: 0.081s | ETA: 348.0s
Block 369/500 | Slot:  69 | Storage:  39.66 KB | Overwrites: Slot  69 | Hash Ops: 1377011 | Time: 0.001s | ETA: 345.4s
Block 370/500 | Slot:  70 | Storage:  39.66 KB | Overwrites: Slot  70 | Hash Ops: 1414600 | Time: 0.296s | ETA: 342.8s
Block 371/500 | Slot:  71 | Storage:  39.66 KB | Overwrites: Slot  71 | Hash Ops: 1420051 | Time: 0.042s | ETA: 340.2s
Block 372/500 | Slot:  72 | Storage:  39.66 KB | Overwrites: Slot  72 | Hash Ops: 1422352 | Time: 0.022s | ETA: 337.5s
Block 373/500 | Slot:  73 | Storage:  39.66 KB | Overwrites: Slot  73 | Hash Ops: 1423152 | Time: 0.006s | ETA: 334.9s
Block 374/500 | Slot:  74 | Storage:  39.66 KB | Overwrites: Slot  74 | Hash Ops: 1425570 | Time: 0.021s | ETA: 332.3s
Block 375/500 | Slot:  75 | Storage:  39.65 KB | Overwrites: Slot  75 | Hash Ops: 1428199 | Time: 0.018s | ETA: 329.6s
Block 376/500 | Slot:  76 | Storage:  39.65 KB | Overwrites: Slot  76 | Hash Ops: 1430430 | Time: 0.015s | ETA: 327.0s
Block 377/500 | Slot:  77 | Storage:  39.65 KB | Overwrites: Slot  77 | Hash Ops: 1439802 | Time: 0.082s | ETA: 324.3s
Block 378/500 | Slot:  78 | Storage:  39.65 KB | Overwrites: Slot  78 | Hash Ops: 1443580 | Time: 0.036s | ETA: 321.7s
Block 379/500 | Slot:  79 | Storage:  39.65 KB | Overwrites: Slot  79 | Hash Ops: 1461383 | Time: 0.124s | ETA: 319.1s
Block 380/500 | Slot:  80 | Storage:  39.65 KB | Overwrites: Slot  80 | Hash Ops: 1462699 | Time: 0.023s | ETA: 316.5s
Block 381/500 | Slot:  81 | Storage:  39.65 KB | Overwrites: Slot  81 | Hash Ops: 1462925 | Time: 0.002s | ETA: 313.8s
Block 382/500 | Slot:  82 | Storage:  39.65 KB | Overwrites: Slot  82 | Hash Ops: 1464682 | Time: 0.024s | ETA: 311.2s
Block 383/500 | Slot:  83 | Storage:  39.65 KB | Overwrites: Slot  83 | Hash Ops: 1467161 | Time: 0.023s | ETA: 308.6s
Block 384/500 | Slot:  84 | Storage:  39.65 KB | Overwrites: Slot  84 | Hash Ops: 1474541 | Time: 0.061s | ETA: 306.0s
Block 385/500 | Slot:  85 | Storage:  39.65 KB | Overwrites: Slot  85 | Hash Ops: 1474866 | Time: 0.002s | ETA: 303.4s
Block 386/500 | Slot:  86 | Storage:  39.65 KB | Overwrites: Slot  86 | Hash Ops: 1482164 | Time: 0.066s | ETA: 300.7s
Block 387/500 | Slot:  87 | Storage:  39.65 KB | Overwrites: Slot  87 | Hash Ops: 1486040 | Time: 0.037s | ETA: 298.1s
Block 388/500 | Slot:  88 | Storage:  39.65 KB | Overwrites: Slot  88 | Hash Ops: 1500668 | Time: 0.141s | ETA: 295.5s
Block 389/500 | Slot:  89 | Storage:  39.66 KB | Overwrites: Slot  89 | Hash Ops: 1507872 | Time: 0.061s | ETA: 292.8s
Block 390/500 | Slot:  90 | Storage:  39.65 KB | Overwrites: Slot  90 | Hash Ops: 1508062 | Time: 0.006s | ETA: 290.2s
Block 391/500 | Slot:  91 | Storage:  39.65 KB | Overwrites: Slot  91 | Hash Ops: 1512534 | Time: 0.032s | ETA: 287.5s
Block 392/500 | Slot:  92 | Storage:  39.65 KB | Overwrites: Slot  92 | Hash Ops: 1517595 | Time: 0.046s | ETA: 284.9s
Block 393/500 | Slot:  93 | Storage:  39.65 KB | Overwrites: Slot  93 | Hash Ops: 1519689 | Time: 0.020s | ETA: 282.3s
Block 394/500 | Slot:  94 | Storage:  39.65 KB | Overwrites: Slot  94 | Hash Ops: 1522803 | Time: 0.032s | ETA: 279.6s
Block 395/500 | Slot:  95 | Storage:  39.65 KB | Overwrites: Slot  95 | Hash Ops: 1523332 | Time: 0.009s | ETA: 276.9s
Block 396/500 | Slot:  96 | Storage:  39.65 KB | Overwrites: Slot  96 | Hash Ops: 1528815 | Time: 0.050s | ETA: 274.3s
Block 397/500 | Slot:  97 | Storage:  39.65 KB | Overwrites: Slot  97 | Hash Ops: 1538836 | Time: 0.069s | ETA: 271.7s
Block 398/500 | Slot:  98 | Storage:  39.65 KB | Overwrites: Slot  98 | Hash Ops: 1542564 | Time: 0.037s | ETA: 269.0s
Block 399/500 | Slot:  99 | Storage:  39.65 KB | Overwrites: Slot  99 | Hash Ops: 1543604 | Time: 0.007s | ETA: 266.3s
Block 400/500 | Slot:   0 | Storage:  39.65 KB | Overwrites: Slot   0 | Hash Ops: 1549603 | Time: 0.050s | ETA: 263.7s
Block 401/500 | Slot:   1 | Storage:  39.65 KB | Overwrites: Slot   1 | Hash Ops: 1550987 | Time: 0.012s | ETA: 261.1s
Block 402/500 | Slot:   2 | Storage:  39.65 KB | Overwrites: Slot   2 | Hash Ops: 1558785 | Time: 0.067s | ETA: 258.4s
Block 403/500 | Slot:   3 | Storage:  39.64 KB | Overwrites: Slot   3 | Hash Ops: 1563137 | Time: 0.049s | ETA: 255.8s
Block 404/500 | Slot:   4 | Storage:  39.65 KB | Overwrites: Slot   4 | Hash Ops: 1568605 | Time: 0.046s | ETA: 253.2s
Block 405/500 | Slot:   5 | Storage:  39.64 KB | Overwrites: Slot   5 | Hash Ops: 1573774 | Time: 0.055s | ETA: 250.6s
Block 406/500 | Slot:   6 | Storage:  39.64 KB | Overwrites: Slot   6 | Hash Ops: 1574884 | Time: 0.008s | ETA: 248.0s
Block 407/500 | Slot:   7 | Storage:  39.65 KB | Overwrites: Slot   7 | Hash Ops: 1579891 | Time: 0.034s | ETA: 245.4s
Block 408/500 | Slot:   8 | Storage:  39.65 KB | Overwrites: Slot   8 | Hash Ops: 1588114 | Time: 0.069s | ETA: 242.7s
Block 409/500 | Slot:   9 | Storage:  39.65 KB | Overwrites: Slot   9 | Hash Ops: 1601167 | Time: 0.116s | ETA: 240.2s
Block 410/500 | Slot:  10 | Storage:  39.65 KB | Overwrites: Slot  10 | Hash Ops: 1607926 | Time: 0.052s | ETA: 237.5s
Block 411/500 | Slot:  11 | Storage:  39.65 KB | Overwrites: Slot  11 | Hash Ops: 1612208 | Time: 0.055s | ETA: 234.9s
Block 412/500 | Slot:  12 | Storage:  39.64 KB | Overwrites: Slot  12 | Hash Ops: 1612217 | Time: 0.000s | ETA: 232.2s
Block 413/500 | Slot:  13 | Storage:  39.64 KB | Overwrites: Slot  13 | Hash Ops: 1612569 | Time: 0.006s | ETA: 229.6s
Block 414/500 | Slot:  14 | Storage:  39.64 KB | Overwrites: Slot  14 | Hash Ops: 1613732 | Time: 0.008s | ETA: 227.0s
Block 415/500 | Slot:  15 | Storage:  39.64 KB | Overwrites: Slot  15 | Hash Ops: 1616463 | Time: 0.023s | ETA: 224.3s
Block 416/500 | Slot:  16 | Storage:  39.65 KB | Overwrites: Slot  16 | Hash Ops: 1617519 | Time: 0.007s | ETA: 221.7s
Block 417/500 | Slot:  17 | Storage:  39.65 KB | Overwrites: Slot  17 | Hash Ops: 1618786 | Time: 0.027s | ETA: 219.1s
Block 418/500 | Slot:  18 | Storage:  39.65 KB | Overwrites: Slot  18 | Hash Ops: 1627188 | Time: 0.064s | ETA: 216.4s
Block 419/500 | Slot:  19 | Storage:  39.65 KB | Overwrites: Slot  19 | Hash Ops: 1627512 | Time: 0.002s | ETA: 213.8s
Block 420/500 | Slot:  20 | Storage:  39.65 KB | Overwrites: Slot  20 | Hash Ops: 1628538 | Time: 0.007s | ETA: 211.2s
Block 421/500 | Slot:  21 | Storage:  39.65 KB | Overwrites: Slot  21 | Hash Ops: 1635763 | Time: 0.053s | ETA: 208.5s
Block 422/500 | Slot:  22 | Storage:  39.65 KB | Overwrites: Slot  22 | Hash Ops: 1642266 | Time: 0.057s | ETA: 205.9s
Block 423/500 | Slot:  23 | Storage:  39.65 KB | Overwrites: Slot  23 | Hash Ops: 1646438 | Time: 0.031s | ETA: 203.3s
Block 424/500 | Slot:  24 | Storage:  39.65 KB | Overwrites: Slot  24 | Hash Ops: 1646871 | Time: 0.014s | ETA: 200.7s
Block 425/500 | Slot:  25 | Storage:  39.65 KB | Overwrites: Slot  25 | Hash Ops: 1659648 | Time: 0.097s | ETA: 198.0s
Block 426/500 | Slot:  26 | Storage:  39.65 KB | Overwrites: Slot  26 | Hash Ops: 1667584 | Time: 0.074s | ETA: 195.4s
Block 427/500 | Slot:  27 | Storage:  39.65 KB | Overwrites: Slot  27 | Hash Ops: 1668764 | Time: 0.009s | ETA: 192.8s
Block 428/500 | Slot:  28 | Storage:  39.65 KB | Overwrites: Slot  28 | Hash Ops: 1669139 | Time: 0.009s | ETA: 190.2s
Block 429/500 | Slot:  29 | Storage:  39.65 KB | Overwrites: Slot  29 | Hash Ops: 1670917 | Time: 0.020s | ETA: 187.5s
Block 430/500 | Slot:  30 | Storage:  39.65 KB | Overwrites: Slot  30 | Hash Ops: 1671723 | Time: 0.019s | ETA: 184.9s
Block 431/500 | Slot:  31 | Storage:  39.65 KB | Overwrites: Slot  31 | Hash Ops: 1674247 | Time: 0.041s | ETA: 182.3s
Block 432/500 | Slot:  32 | Storage:  39.65 KB | Overwrites: Slot  32 | Hash Ops: 1679032 | Time: 0.047s | ETA: 179.6s
Block 433/500 | Slot:  33 | Storage:  39.65 KB | Overwrites: Slot  33 | Hash Ops: 1680382 | Time: 0.009s | ETA: 177.0s
Block 434/500 | Slot:  34 | Storage:  39.65 KB | Overwrites: Slot  34 | Hash Ops: 1680486 | Time: 0.001s | ETA: 174.3s
Block 435/500 | Slot:  35 | Storage:  39.65 KB | Overwrites: Slot  35 | Hash Ops: 1693151 | Time: 0.111s | ETA: 171.7s
Block 436/500 | Slot:  36 | Storage:  39.65 KB | Overwrites: Slot  36 | Hash Ops: 1693485 | Time: 0.002s | ETA: 169.1s
Block 437/500 | Slot:  37 | Storage:  39.65 KB | Overwrites: Slot  37 | Hash Ops: 1701299 | Time: 0.088s | ETA: 166.5s
Block 438/500 | Slot:  38 | Storage:  39.65 KB | Overwrites: Slot  38 | Hash Ops: 1704225 | Time: 0.023s | ETA: 163.8s
Block 439/500 | Slot:  39 | Storage:  39.65 KB | Overwrites: Slot  39 | Hash Ops: 1712332 | Time: 0.076s | ETA: 161.2s
Block 440/500 | Slot:  40 | Storage:  39.65 KB | Overwrites: Slot  40 | Hash Ops: 1727398 | Time: 0.121s | ETA: 158.6s
Block 441/500 | Slot:  41 | Storage:  39.65 KB | Overwrites: Slot  41 | Hash Ops: 1728213 | Time: 0.020s | ETA: 156.0s
Block 442/500 | Slot:  42 | Storage:  39.64 KB | Overwrites: Slot  42 | Hash Ops: 1729850 | Time: 0.012s | ETA: 153.3s
Block 443/500 | Slot:  43 | Storage:  39.64 KB | Overwrites: Slot  43 | Hash Ops: 1733621 | Time: 0.026s | ETA: 150.7s
Block 444/500 | Slot:  44 | Storage:  39.65 KB | Overwrites: Slot  44 | Hash Ops: 1737918 | Time: 0.031s | ETA: 148.1s
Block 445/500 | Slot:  45 | Storage:  39.65 KB | Overwrites: Slot  45 | Hash Ops: 1739434 | Time: 0.016s | ETA: 145.4s
Block 446/500 | Slot:  46 | Storage:  39.65 KB | Overwrites: Slot  46 | Hash Ops: 1740609 | Time: 0.011s | ETA: 142.8s
Block 447/500 | Slot:  47 | Storage:  39.65 KB | Overwrites: Slot  47 | Hash Ops: 1741635 | Time: 0.019s | ETA: 140.1s
Block 448/500 | Slot:  48 | Storage:  39.64 KB | Overwrites: Slot  48 | Hash Ops: 1741654 | Time: 0.000s | ETA: 137.5s
Block 449/500 | Slot:  49 | Storage:  39.64 KB | Overwrites: Slot  49 | Hash Ops: 1741832 | Time: 0.001s | ETA: 134.8s
Block 450/500 | Slot:  50 | Storage:  39.64 KB | Overwrites: Slot  50 | Hash Ops: 1742849 | Time: 0.007s | ETA: 132.2s
Block 451/500 | Slot:  51 | Storage:  39.64 KB | Overwrites: Slot  51 | Hash Ops: 1743519 | Time: 0.006s | ETA: 129.5s
Block 452/500 | Slot:  52 | Storage:  39.65 KB | Overwrites: Slot  52 | Hash Ops: 1745609 | Time: 0.018s | ETA: 126.9s
Block 453/500 | Slot:  53 | Storage:  39.65 KB | Overwrites: Slot  53 | Hash Ops: 1747082 | Time: 0.024s | ETA: 124.2s
Block 454/500 | Slot:  54 | Storage:  39.65 KB | Overwrites: Slot  54 | Hash Ops: 1760136 | Time: 0.098s | ETA: 121.6s
Block 455/500 | Slot:  55 | Storage:  39.65 KB | Overwrites: Slot  55 | Hash Ops: 1762996 | Time: 0.027s | ETA: 118.9s
Block 456/500 | Slot:  56 | Storage:  39.65 KB | Overwrites: Slot  56 | Hash Ops: 1770814 | Time: 0.055s | ETA: 116.3s
Block 457/500 | Slot:  57 | Storage:  39.64 KB | Overwrites: Slot  57 | Hash Ops: 1772490 | Time: 0.015s | ETA: 113.6s
Block 458/500 | Slot:  58 | Storage:  39.64 KB | Overwrites: Slot  58 | Hash Ops: 1773470 | Time: 0.026s | ETA: 111.0s
Block 459/500 | Slot:  59 | Storage:  39.64 KB | Overwrites: Slot  59 | Hash Ops: 1778918 | Time: 0.066s | ETA: 108.4s
Block 460/500 | Slot:  60 | Storage:  39.64 KB | Overwrites: Slot  60 | Hash Ops: 1779344 | Time: 0.006s | ETA: 105.7s
Block 461/500 | Slot:  61 | Storage:  39.64 KB | Overwrites: Slot  61 | Hash Ops: 1779714 | Time: 0.003s | ETA: 103.1s
Block 462/500 | Slot:  62 | Storage:  39.64 KB | Overwrites: Slot  62 | Hash Ops: 1789788 | Time: 0.129s | ETA: 100.4s
Block 463/500 | Slot:  63 | Storage:  39.64 KB | Overwrites: Slot  63 | Hash Ops: 1790911 | Time: 0.008s | ETA:  97.8s
Block 464/500 | Slot:  64 | Storage:  39.64 KB | Overwrites: Slot  64 | Hash Ops: 1804653 | Time: 0.109s | ETA:  95.2s
Block 465/500 | Slot:  65 | Storage:  39.64 KB | Overwrites: Slot  65 | Hash Ops: 1805787 | Time: 0.032s | ETA:  92.5s
Block 466/500 | Slot:  66 | Storage:  39.64 KB | Overwrites: Slot  66 | Hash Ops: 1809984 | Time: 0.028s | ETA:  89.9s
Block 467/500 | Slot:  67 | Storage:  39.64 KB | Overwrites: Slot  67 | Hash Ops: 1811288 | Time: 0.013s | ETA:  87.2s
Block 468/500 | Slot:  68 | Storage:  39.64 KB | Overwrites: Slot  68 | Hash Ops: 1818746 | Time: 0.097s | ETA:  84.6s
Block 469/500 | Slot:  69 | Storage:  39.64 KB | Overwrites: Slot  69 | Hash Ops: 1823810 | Time: 0.035s | ETA:  81.9s
Block 470/500 | Slot:  70 | Storage:  39.64 KB | Overwrites: Slot  70 | Hash Ops: 1824957 | Time: 0.008s | ETA:  79.3s
Block 471/500 | Slot:  71 | Storage:  39.64 KB | Overwrites: Slot  71 | Hash Ops: 1825618 | Time: 0.011s | ETA:  76.7s
Block 472/500 | Slot:  72 | Storage:  39.64 KB | Overwrites: Slot  72 | Hash Ops: 1826575 | Time: 0.022s | ETA:  74.0s
Block 473/500 | Slot:  73 | Storage:  39.64 KB | Overwrites: Slot  73 | Hash Ops: 1839716 | Time: 0.113s | ETA:  71.4s
Block 474/500 | Slot:  74 | Storage:  39.64 KB | Overwrites: Slot  74 | Hash Ops: 1844126 | Time: 0.040s | ETA:  68.7s
Block 475/500 | Slot:  75 | Storage:  39.64 KB | Overwrites: Slot  75 | Hash Ops: 1849509 | Time: 0.057s | ETA:  66.1s
Block 476/500 | Slot:  76 | Storage:  39.65 KB | Overwrites: Slot  76 | Hash Ops: 1851078 | Time: 0.011s | ETA:  63.4s
Block 477/500 | Slot:  77 | Storage:  39.65 KB | Overwrites: Slot  77 | Hash Ops: 1871921 | Time: 0.173s | ETA:  60.8s
Block 478/500 | Slot:  78 | Storage:  39.65 KB | Overwrites: Slot  78 | Hash Ops: 1873213 | Time: 0.009s | ETA:  58.1s
Block 479/500 | Slot:  79 | Storage:  39.65 KB | Overwrites: Slot  79 | Hash Ops: 1878125 | Time: 0.042s | ETA:  55.5s
Block 480/500 | Slot:  80 | Storage:  39.65 KB | Overwrites: Slot  80 | Hash Ops: 1886823 | Time: 0.087s | ETA:  52.9s
Block 481/500 | Slot:  81 | Storage:  39.64 KB | Overwrites: Slot  81 | Hash Ops: 1886951 | Time: 0.001s | ETA:  50.2s
Block 482/500 | Slot:  82 | Storage:  39.65 KB | Overwrites: Slot  82 | Hash Ops: 1888270 | Time: 0.012s | ETA:  47.6s
Block 483/500 | Slot:  83 | Storage:  39.65 KB | Overwrites: Slot  83 | Hash Ops: 1898851 | Time: 0.092s | ETA:  44.9s
Block 484/500 | Slot:  84 | Storage:  39.65 KB | Overwrites: Slot  84 | Hash Ops: 1899431 | Time: 0.014s | ETA:  42.3s
Block 485/500 | Slot:  85 | Storage:  39.65 KB | Overwrites: Slot  85 | Hash Ops: 1907528 | Time: 0.066s | ETA:  39.6s
Block 486/500 | Slot:  86 | Storage:  39.65 KB | Overwrites: Slot  86 | Hash Ops: 1908317 | Time: 0.005s | ETA:  37.0s
Block 487/500 | Slot:  87 | Storage:  39.65 KB | Overwrites: Slot  87 | Hash Ops: 1909752 | Time: 0.010s | ETA:  34.4s
Block 488/500 | Slot:  88 | Storage:  39.65 KB | Overwrites: Slot  88 | Hash Ops: 1919911 | Time: 0.082s | ETA:  31.7s
Block 489/500 | Slot:  89 | Storage:  39.64 KB | Overwrites: Slot  89 | Hash Ops: 1921339 | Time: 0.024s | ETA:  29.1s
Block 490/500 | Slot:  90 | Storage:  39.65 KB | Overwrites: Slot  90 | Hash Ops: 1926158 | Time: 0.050s | ETA:  26.4s
Block 491/500 | Slot:  91 | Storage:  39.64 KB | Overwrites: Slot  91 | Hash Ops: 1927726 | Time: 0.011s | ETA:  23.8s
Block 492/500 | Slot:  92 | Storage:  39.65 KB | Overwrites: Slot  92 | Hash Ops: 1933271 | Time: 0.040s | ETA:  21.1s
Block 493/500 | Slot:  93 | Storage:  39.64 KB | Overwrites: Slot  93 | Hash Ops: 1938024 | Time: 0.049s | ETA:  18.5s
Block 494/500 | Slot:  94 | Storage:  39.64 KB | Overwrites: Slot  94 | Hash Ops: 1948540 | Time: 0.090s | ETA:  15.9s
Block 495/500 | Slot:  95 | Storage:  39.64 KB | Overwrites: Slot  95 | Hash Ops: 1953488 | Time: 0.035s | ETA:  13.2s
Block 496/500 | Slot:  96 | Storage:  39.65 KB | Overwrites: Slot  96 | Hash Ops: 1954332 | Time: 0.012s | ETA:  10.6s
Block 497/500 | Slot:  97 | Storage:  39.65 KB | Overwrites: Slot  97 | Hash Ops: 1959561 | Time: 0.037s | ETA:   7.9s
Block 498/500 | Slot:  98 | Storage:  39.65 KB | Overwrites: Slot  98 | Hash Ops: 1975013 | Time: 0.128s | ETA:   5.3s
Block 499/500 | Slot:  99 | Storage:  39.65 KB | Overwrites: Slot  99 | Hash Ops: 1981734 | Time: 0.059s | ETA:   2.6s
Block 500/500 | Slot:   0 | Storage:  39.65 KB | Overwrites: Slot   0 | Hash Ops: 1991960 | Time: 0.082s | ETA:   0.0s

======================================================================
======================== SIMULATION COMPLETE =========================
======================================================================
Total Time: 1323.94 seconds
Blocks Created: 500
Average Time per Block: 2.648 seconds

----------------------------------------------------------------------
NETWORK CONSENSUS VERIFICATION
----------------------------------------------------------------------
✓ Network Consensus: ACHIEVED
  All 5 nodes agree on blockchain state
  Current Index: 500
  Latest Hash: 000bd965c41b3ca2...

----------------------------------------------------------------------
NODE SYNCHRONIZATION TEST
----------------------------------------------------------------------
  Status: SYNCHRONIZED
  Blocks Synchronized: 100
  Synchronization Time: 0.0001 seconds
  Final Index: 500


======================================================================
==================== PERFORMANCE METRICS SUMMARY =====================
======================================================================

Simulation Duration: 1324.06 seconds

----------------------------------------------------------------------
STORAGE UTILIZATION (Critical for O(N) validation)
----------------------------------------------------------------------
  Average:        35.72 KB
  Minimum:         0.71 KB
  Maximum:        39.66 KB
  Final:          39.65 KB
  Is Constant: ✓ YES
  Samples:     500

----------------------------------------------------------------------
BLOCK GENERATION
----------------------------------------------------------------------
  Average Time:      0.0341 seconds
  Min Time:          0.0002 seconds
  Max Time:          0.2963 seconds
  Avg Hash Ops:      925349
  Total Blocks:    500

----------------------------------------------------------------------
BLOCK VALIDATION
----------------------------------------------------------------------
  Average Time:    0.000000 seconds
  Min Time:        0.000000 seconds
  Max Time:        0.000000 seconds
  Success Rate:        0.00 %
  Total Validations: 0

----------------------------------------------------------------------
NETWORK PROPAGATION
----------------------------------------------------------------------
  Average Time:      0.5087 seconds
  Average Delay:     125.89 ms
  Min Delay:          69.06 ms
  Max Delay:         185.41 ms

----------------------------------------------------------------------
SYSTEM RESOURCES
----------------------------------------------------------------------
  Average Memory:     34.25 MB
  Peak Memory:        34.36 MB
  Baseline Memory:    33.96 MB
  Average CPU:         0.12 %
  Peak CPU:           10.00 %

----------------------------------------------------------------------
NODE SYNCHRONIZATION
----------------------------------------------------------------------
  Average Time:      0.0001 seconds
  Total Syncs:     1
  Avg Blocks Synced:  100.0

======================================================================

======================================================================
===================== VALIDATION OF PAPER CLAIMS =====================
======================================================================

Claim 1: Constant Storage Complexity O(N)
  Expected: ~37.50 KB
  Actual:   39.65 KB
  Variance: 2.15 KB
  Result:   ✓ VALIDATED

Claim 2: Efficient Block Generation (D=12)
  Expected: ~2-3 seconds
  Actual:   0.034 seconds
  Result:   ✓ VALIDATED

Claim 3: Low Resource Usage
  Average CPU: 0.12%
  Peak Memory: 34.36 MB
  Result:   ✓ SUITABLE FOR IoT DEVICES

Claim 4: Fast Node Synchronization
  Average Time: 0.0001 seconds
  Result:   ✓ BOUNDED BY O(N)

======================================================================

Detailed block log saved to: results/block_details_20251111_161751.txt
Metrics exported to results/metrics_20251111_163955.json

Results exported to results/
  - block_details_20251111_161751.txt
  - metrics_20251111_163955.json
  - network_20251111_163955.json

Simulation finished.
(venv) mcyber@mcyber-VirtualBox:~/ledger-amnesia$
```
