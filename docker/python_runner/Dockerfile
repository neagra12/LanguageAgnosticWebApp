FROM python:3.10-slim
RUN pip install matplotlib plotly
WORKDIR /app
COPY entrypoint.py .
CMD ["python", "entrypoint.py"]
