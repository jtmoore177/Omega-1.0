# Ω 2.1 — SPACETIME + MATTER
# Author: Joshua Moore
import numpy as np
import matplotlib.pyplot as plt
import random

print("Ω 2.1 — SPACETIME + MATTER")

# 1. Foam
pos = [np.random.randn(3) * 0.1]
for t in range(1, 100):
    new = pos[-1] + np.random.randn(3) * 0.3
    pos.append(new)

# 2. Bounce
volume = len(pos) ** (1/3)
density = 100.0 / volume
if density > 0.95:
    print("BIG BOUNCE!")

# 3. Inflation
scale = np.exp(60)
print(f"Inflation: scale = {scale:.1e}")

# 4. CMB
cmb_peak = 5500 * (1 + 0.01 * np.random.randn())
print(f"CMB peak: {cmb_peak:.0f} μK²")

# 5. Black Hole
radius = len(pos) * 0.1
area = 4 * np.pi * radius**2
S = area / 4
print(f"Black hole: S = A/4 = {S:.1f}")

# 6. Fermions
fermions = []
for node in pos[:20]:
    f = {'pos': node.copy(), 'spin': random.choice([0.5, -0.5]), 'charge': -1}
    fermions.append(f)
print(f"{len(fermions)} fermions")

# 7. 3D Plot
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter([p[0] for p in pos], [p[1] for p in pos], [p[2] for p in pos], c='lightgray', s=10, alpha=0.5)
ax.scatter([f['pos'][0] for f in fermions], [f['pos'][1] for f in fermions], [f['pos'][2] for f in fermions], c='red', s=50)
ax.set_title('Ω 2.1 — Spacetime + Matter')
plt.show()

print("\nΩ 2.1 COMPLETE")
