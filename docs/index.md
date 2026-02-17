# Python Probe Documentation

## Overview

**python-probe** is a lightweight Flask application designed for deployment validation and testing across multiple environments (local, Docker, Kubernetes, ECS, EC2).

See [README.md](../README.md) for full project documentation.

## API Endpoints

### Health Checks

| Endpoint | Returns | Purpose |
|----------|---------|---------|
| `GET /` | JSON | Root endpoint with service info |
| `GET /health` | JSON `{status: "up"}` | Health check |
| `GET /healthz` | Empty 200 | Kubernetes-style health check |
| `GET /ready` | Empty 200 | Readiness probe |
| `GET /live` | Empty 200 | Liveness probe |

### Application Info

| Endpoint | Returns | Purpose |
|----------|---------|---------|
| `GET /api/v1/info` | JSON | Detailed app info (time, hostname, version, commit) |
| `GET /api/v1/version` | JSON | Version and commit SHA |

## Quick Start

### Local Development
```bash
./run.sh
```
App starts on `http://localhost:8080`

### Docker Compose
```bash
docker-compose up
```

### Docker
```bash
docker build -t python-probe .
docker run -p 8080:8080 python-probe
```

## Environment Variables

- `PORT` - Server port (default: 8080)
- `APP_VERSION` - Application version (default: 1.0.0)
- `APP_COMMIT_SHA` - Git commit SHA or build identifier (default: unknown)

## Testing

```bash
# Check if app is running
curl http://localhost:8080/health

# Get detailed info
curl http://localhost:8080/api/v1/info

# Kubernetes probes
curl http://localhost:8080/ready
curl http://localhost:8080/live
```

## Deployment

See [README.md](../README.md) for deployment instructions across different platforms:
- Local development
- Docker
- Kubernetes
- ECS / EC2
- Any cloud provider