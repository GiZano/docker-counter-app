FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Add labels
LABEL org.opencontainers.image.title="Docker Counter App"
LABEL org.opencontainers.image.description="A scalable counter application"
LABEL org.opencontainers.image.version="2.0.0"

# Security: run as non-root user
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

EXPOSE 5000

CMD ["python", "app.py"]