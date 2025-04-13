library(plotly)
library(htmlwidgets)

# Create a basic interactive scatter plot
fig <- plot_ly(
  data = iris,
  x = ~Sepal.Length,
  y = ~Petal.Length,
  color = ~Species,
  type = 'scatter',
  mode = 'markers'
)

# Save as HTML to the expected output path
output_path <- file.path(Sys.getenv("OUTPUT_DIR", unset = "."), "plot.html")
saveWidget(fig, file = output_path, selfcontained = FALSE)

cat("✅ plot.html saved to:", output_path, "\n")

