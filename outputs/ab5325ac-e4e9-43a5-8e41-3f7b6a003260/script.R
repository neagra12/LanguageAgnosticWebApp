library(plotly)
library(htmlwidgets)

# Create a basic 3D scatter plot using plotly
fig <- plot_ly(
  data = iris,
  x = ~Sepal.Length,
  y = ~Petal.Length,
  z = ~Sepal.Width,
  color = ~Species,
  type = "scatter3d",
  mode = "markers"
)

# Save it as an interactive HTML file
output_path <- file.path(Sys.getenv("OUTPUT_DIR", unset = "."), "plot.html")
saveWidget(fig, file = output_path, selfcontained = FALSE)

cat("✅ Interactive plot saved to:", output_path, "\n")
