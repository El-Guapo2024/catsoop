# CAT-SOOP Docker Setup

This directory contains the Docker configuration files for running CAT-SOOP in a containerized environment.

## Files

- `start_catsoop.py`: Docker-optimized startup script
- `docker_config.py`: Docker-optimized CAT-SOOP configuration
- `Dockerfile`: Container build instructions
- `docker-compose.yml`: Docker Compose configuration

## Usage

### Using Docker Compose (Recommended)

1. Navigate to the root directory of the CAT-SOOP project
2. Run:
```bash
docker-compose -f catsoop/scripts/docker/docker-compose.yml up --build
```

### Using Docker Directly

1. Navigate to the root directory of the CAT-SOOP project
2. Build the image:
```bash
docker build -t catsoop -f catsoop/scripts/docker/Dockerfile .
```
3. Run the container:
```bash
docker run -p 7667:7667 catsoop
```

## Configuration

The Docker setup uses the following default settings:
- Port: 7667
- Authentication: Dummy authentication (username: default_user)
- Data storage: Persistent volume at /app/data
- WSGI Server: Waitress

To modify these settings:
1. Edit `docker_config.py` for CAT-SOOP configuration
2. Edit `docker-compose.yml` for Docker-specific settings
3. Edit environment variables in the Dockerfile or docker-compose.yml

## Environment Variables

- `CATSOOP_HOST`: Server host (default: 0.0.0.0)
- `CATSOOP_PORT`: Server port (default: 7667)
- `CATSOOP_CONFIG`: Path to config file
- `CATSOOP_DATA_DIR`: Path to data directory
- `CATSOOP_CONFIG_DIR`: Path to config directory
- `CATSOOP_ENCRYPTION_KEY`: Encryption key for logs

## Security Notes

- Change the `cs_secret_key` and `cs_encryption_key` in `docker_config.py` before deploying to production
- Consider using Docker secrets for sensitive configuration in production
- The default authentication is for development only - configure proper authentication for production use 