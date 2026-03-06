# Testing Hub Server

A simple Python server in a Docker container for testing scripts and API calls. All responses include unique identifiers and timestamps to prevent caching.

## Quick Start with Docker

### 1. Build and run with Docker Compose
```bash
docker-compose up
```

The server will be available at `http://localhost:5000`

### 2. Or build and run manually
```bash
# Build the image
docker build -t testing-hub .

# Run the container
docker run -p 5000:5000 testing-hub
```

## Endpoints

### `GET /`
Root endpoint that returns server status with unique identifiers.

```bash
curl http://localhost:5000
```

### `GET|POST /test`
Test endpoint that echoes request information.

```bash
curl http://localhost:5000/test
curl -X POST http://localhost:5000/test?param=value
```

### `POST /echo`
Echo endpoint for testing POST data.

```bash
curl -X POST http://localhost:5000/echo \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### `GET /health`
Health check endpoint.

```bash
curl http://localhost:5000/health
```

## Cache-Busting Features

All responses include:
- **Unique IDs**: Each response gets a unique UUID
- **Timestamps**: Current ISO timestamp in every response
- **Server time**: Elapsed seconds since epoch for precise tracking
- **HTTP Headers**: `Cache-Control`, `Pragma`, and `Expires` headers prevent caching at all levels

This ensures every request gets a fresh response, making it ideal for testing caching behavior or script reliability.

## Notes

- Containerized with Docker for consistency across environments
- Health checks included for production deployment
- Hot reload enabled via docker-compose volume mount
- All responses are JSON formatted
- No database or persistent storage - purely for testing
