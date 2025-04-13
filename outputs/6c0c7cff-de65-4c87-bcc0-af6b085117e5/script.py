import plotly.graph_objs as go
import plotly.offline as pyo
import os

# Sample data
import numpy as np

z = np.random.rand(10, 10)
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)

# Create 3D surface plot
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

# Save to HTML
output_path = os.path.join(OUTPUT_DIR, "plot.html")
pyo.plot(fig, filename=output_path, auto_open=False)

print(f"✅ 3D plot saved to: {output_path}")