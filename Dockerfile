# Base Python Image
FROM python:3.9-slim

# Set Working Directory
WORKDIR /app

# Copy requirements and installa dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 5000

# Command to start the app
CMD ["python", "app.py"]