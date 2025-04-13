import matplotlib.pyplot as plt
import os

x = [1, 2, 3, 4]
y = [10, 15, 13, 17]

plt.figure()
plt.plot(x, y, marker='o')
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

out_path = os.path.join(OUTPUT_DIR, "plot.png")
plt.savefig(out_path)
print(f"✅ plot.png written to: {out_path}")