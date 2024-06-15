import matplotlib.pyplot as plt
import numpy as np

# Data
labels = [
    "BENIGN", "DoS Hulk", "DDoS", "Portscan", "Infiltration - Portscan",
    "SSH-Patator - Attempted", "DoS GoldenEye - Attempted", "SSH-Patator",
    "Web Attack - SQL Injection", "Infiltration - Attempted", "FTP-Patator",
    "DoS GoldenEye", "Infiltration", "Web Attack - SQL Injection - Attempted",
    "FTP-Patator - Attempted", "Heartbleed", "DoS Slowloris", "Web Attack - Brute Force",
    "DoS Slowhttptest - Attempted", "DoS Slowhttptest", "Botnet", "Botnet - Attempted",
    "Web Attack - Brute Force - Attempted", "DoS Slowloris - Attempted", "Web Attack - XSS",
    "Web Attack - XSS - Attempted", "DoS Hulk - Attempted"
]

total_packets = [
    51417559, 2243308, 1273386, 32145, 211867, 173, 170, 163147, 140,
    117, 111018, 105874, 74361, 63, 61, 49296, 41009, 22082, 21894, 17745,
    9871, 8297, 8173, 6557, 5553, 4008, 2728
]

num_flows = [
    1582566, 158468, 95144, 159066, 71767, 27, 80, 2961, 13, 45, 3972,
    7567, 36, 5, 12, 11, 3859, 73, 3368, 174, 736, 4067, 1292, 1847, 18,
    655, 581
]

# Create subplots
fig, ax = plt.subplots(figsize=(14, 16))

# Bar widths
bar_width = 0.35
index = np.arange(len(labels))

# Plot total packets
ax.barh(index, total_packets, bar_width, label='Total Packets', log=True)
ax.barh(index + bar_width, num_flows, bar_width, label='Num Flows', log=True)

# Labeling
ax.set_ylabel('Labels')
ax.set_xlabel('Logarithmic Scale')
ax.set_title('Total Packets and Num Flows (Logarithmic Scale)')
ax.set_yticks(index + bar_width / 2)
ax.set_yticklabels(labels)

# Adding legend
ax.legend()

# Show plot
plt.tight_layout()
plt.grid(True, which="both", ls="--")
plt.show()

plt.savefig('plot.png', bbox_inches='tight', dpi=300)

