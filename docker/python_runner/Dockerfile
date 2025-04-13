FROM python:3.10-slim

# Install packages
RUN pip install matplotlib plotly pandas kaleido
RUN pip install kaleido


WORKDIR /app

COPY entrypoint.py .

CMD ["python", "entrypoint.py"]
