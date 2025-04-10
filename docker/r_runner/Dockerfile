FROM r-base
RUN R -e "install.packages(c('ggplot2', 'plotly', 'rgl'), repos='http://cran.rstudio.com/')"
WORKDIR /app
COPY entrypoint.R .
CMD ["Rscript", "entrypoint.R"]
