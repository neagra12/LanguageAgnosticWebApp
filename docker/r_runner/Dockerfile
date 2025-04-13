FROM rocker/r-ver:4.3.1

# Install system dependencies and pandoc
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    libx11-dev \
    pandoc \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Install R packages
RUN R -e "install.packages(c('ggplot2', 'plotly', 'rgl', 'fs', 'htmlwidgets'), repos='http://cran.rstudio.com/')"

WORKDIR /app
COPY watcher.R .

CMD ["Rscript", "watcher.R"]
