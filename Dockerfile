FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY pyproject.toml .

# Install the package
RUN pip install --no-cache-dir -e .

# Expose port (7860 for HF Spaces, will be overridden by platform)
EXPOSE 7860

# Run the application
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "7860"]
