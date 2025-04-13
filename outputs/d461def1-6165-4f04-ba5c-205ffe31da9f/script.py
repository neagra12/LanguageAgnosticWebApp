import plotly.express as px
import os

# Create a sample interactive plot
fig = px.scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17],
    title="Interactive Scatter Plot",
    labels={"x": "X Axis", "y": "Y Axis"}
)

# Save the plot as HTML inside OUTPUT_DIR
out_path = os.path.join(OUTPUT_DIR, "plot.html")
fig.write_html(out_path)

print(f"✅ plot.html written to: {out_path}")
