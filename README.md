# LanguageAgnosticWebApp
# Language Agnostic Visualization Web Application

## 🚀 Overview

This application allows users to write and execute data visualization scripts in either **Python** or **R**, and view the generated output (static, interactive, or 3D plots) directly in a web interface. It is built to demonstrate language-agnostic support for visualization libraries across both environments.

---

## 🧰 Tech Stack

- **Frontend**: React (TypeScript, TailwindCSS)
- **Backend**: FastAPI (Python)
- **Execution Environment**: Docker-based isolated runners for Python and R
- **Visualization Libraries**:
  - Python: `matplotlib`, `plotly`
  - R: `ggplot2`, `plotly`, `rgl`

---

## 📦 Folder Structure

```
.
├── backend              # FastAPI app
├── frontend             # React app
├── outputs              # Generated visualizations (shared via Docker volumes)
├── docker
│   ├── python_runner    # Docker image for Python execution
│   └── r_runner         # Docker image for R execution
└── docker-compose.yml
```

---

## 🧪 Sample Scripts

### Python

#### Static Plot (Matplotlib)
```python
import matplotlib.pyplot as plt
import os
os.makedirs(OUTPUT_DIR, exist_ok=True)
plt.plot([1, 2, 3], [3, 1, 2])
plt.title("Static Line Plot")
plt.savefig(f"{OUTPUT_DIR}/plot.png")
```

#### Interactive Plot (Plotly)
```python
import plotly.express as px
import os
os.makedirs(OUTPUT_DIR, exist_ok=True)
fig = px.scatter(x=[1, 2, 3], y=[4, 1, 6], title="Interactive Plot")
fig.write_html(f"{OUTPUT_DIR}/plot.html")
```

#### 3D Plot (Plotly)
```python
import plotly.graph_objects as go
import os
os.makedirs(OUTPUT_DIR, exist_ok=True)
fig = go.Figure(data=[go.Scatter3d(
    x=[1, 2, 3],
    y=[4, 5, 6],
    z=[7, 8, 9],
    mode='markers',
    marker=dict(size=5, color='blue')
)])
fig.write_html(f"{OUTPUT_DIR}/plot.html")
```

### R

#### Static Plot (ggplot2)
```r
library(ggplot2)
png(filename = file.path(Sys.getenv("OUTPUT_DIR"), "plot.png"))
ggplot(data.frame(x = 1:5, y = c(3, 2, 5, 1, 4)), aes(x, y)) +
  geom_col(fill = "steelblue") +
  ggtitle("Static Bar Plot")
dev.off()
```

#### Interactive Plot (plotly)
```r
library(plotly)
library(htmlwidgets)
fig <- plot_ly(
  data = iris,
  x = ~Sepal.Length,
  y = ~Petal.Length,
  color = ~Species,
  type = 'scatter',
  mode = 'markers'
)
output_path <- file.path(Sys.getenv("OUTPUT_DIR", unset = "."), "plot.html")
saveWidget(fig, file = output_path, selfcontained = FALSE)
```

#### 3D Plot (rgl)
```r
library(rgl)
open3d()
plot3d(rnorm(100), rnorm(100), rnorm(100), col="blue", size=3)
rgl.snapshot(file.path(Sys.getenv("OUTPUT_DIR"), "plot.png"))
rgl.close()
```

---

## 🔧 Running the App

### 1. Clone the repo
```bash
git clone https://github.com/neagra12/LanguageAgnosticWebApp.git
cd LanguageAgnosticWebApp
```

### 2. Build and Run
```bash
docker-compose up --build
```

- Backend: `http://localhost:8000`
- Frontend: `http://localhost:3000`
- Swagger Docs: `http://localhost:8000/docs`

---

## 🎥 Demo Checklist

✅ Static Python (matplotlib)  
✅ Interactive Python (plotly)  
✅ 3D Python (plotly)  
✅ Static R (ggplot2)  
✅ Interactive R (plotly)  
✅ 3D R (rgl)

---

## 🙌 Contributions & License

MIT License. Made with ❤️ for a technical assessment by Neeha.

