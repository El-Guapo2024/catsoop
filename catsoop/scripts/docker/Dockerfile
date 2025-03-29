# Use Python 3.11 slim image
FROM python:3.11-slim

# Install build dependencies
RUN apt-get update && apt-get install -y \
    make \
    git \
    gcc \
    python3-dev \
    build-essential \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /catsoop

# Copy the entire CAT-SOOP source code
COPY . .

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# Install CAT-SOOP in development mode to keep source code accessible
RUN python3 setup.py develop

# Create configuration directory
RUN mkdir -p /root/.config/catsoop

# Copy Docker configuration to the default location
COPY catsoop/scripts/docker/docker_config.py /root/.config/catsoop/config.py

# Create data directory
RUN mkdir -p /catsoop/data

# Copy your course
COPY courses/number_sense /catsoop/data/courses/number_sense

# Make the startup script executable
RUN chmod +x catsoop/scripts/docker/start_catsoop.py

# Expose port 7667
EXPOSE 7667

# Set environment variables
ENV CATSOOP_HOST=0.0.0.0
ENV CATSOOP_PORT=7667
ENV CATSOOP_DATA_DIR=/catsoop/data
ENV CATSOOP_ENCRYPTION_KEY=docker_encryption_key_please_change_in_production
ENV PYTHONPATH=/catsoop
ENV CATSOOP_CONFIG=/catsoop/scripts/docker/docker_config.py

# Start CAT-SOOP
CMD ["python3", "catsoop/scripts/docker/start_catsoop.py"] 