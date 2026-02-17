# python-flask-probe

Minimal Python Flask application used for deployment validation across any environment (local, Docker, Kubernetes, ECS, etc.).

This is the Python counterpart to the [node-express-probe](https://github.com/tyrelof/node-express-probe) and validates deployment across different stacks.

## Use Cases

- Validate Docker builds and images
- Test Kubernetes / ECS deployments
- Verify CI/CD smoke tests
- Experiment with runtime behavior across different platforms
- Backstage integration testing

---

## Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Root - basic service info |
| `/health` | GET | Health check (returns JSON) |
| `/healthz` | GET | Kubernetes-style health check |
| `/ready` | GET | Readiness probe |
| `/live` | GET | Liveness probe |
| `/api/v1/info` | GET | Detailed app info (time, hostname, version) |
| `/api/v1/version` | GET | Version and commit info |

---

## Local Development

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python src/app.py
```

The app will start on `http://localhost:8080`

### With Environment Variables

```bash
# Set custom version and commit
APP_VERSION=2.0.0 APP_COMMIT_SHA=abc123 python src/app.py
```

### Docker Local

```bash
# Build image
docker build -t python-probe:latest .

# Run container
docker run -p 8080:8080 python-probe:latest

# With environment variables
docker run -p 8080:8080 \
  -e APP_VERSION=2.0.0 \
  -e APP_COMMIT_SHA=abc123 \
  python-probe:latest
```

---

## Kubernetes Deployment

The app includes proper probe endpoints for Kubernetes:

```yaml
livenessProbe:
  httpGet:
    path: /live
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

See [k8s/deploy.yaml](k8s/deploy.yaml) for full deployment example.

---

## ECS / EC2 Deployment

The app works on any environment. Set environment variables via:

- EC2: User data script or SSM Parameter Store
- ECS: Task definition environment variables
- Docker: `-e` flag or `.env` file

```bash
# Example EC2 user data
#!/bin/bash
export APP_VERSION=1.0.0
export APP_COMMIT_SHA=${GIT_COMMIT}
python /app/src/app.py
```

---

## Configuration

| Variable | Default | Purpose |
|----------|---------|---------|
| `PORT` | `8080` | Port to listen on |
| `APP_VERSION` | `1.0.0` | Application version |
| `APP_COMMIT_SHA` | `unknown` | Git commit SHA (for tracking) |

---

## Production

For production, the Docker image uses **Gunicorn** (4 workers) instead of Flask's development server:

```bash
# Manual production run
gunicorn --bind 0.0.0.0:8080 --workers 4 --access-logfile - app:app
```

---

## Development

### Project Structure

```
src/
  app.py          # Flask application
requirements.txt  # Python dependencies
Dockerfile        # Docker image definition
k8s/              # Kubernetes manifests
chart/            # Helm chart (optional)
```

### Testing Endpoints

```bash
# Health checks
curl http://localhost:8080/health
curl http://localhost:8080/live
curl http://localhost:8080/ready

# App info
curl http://localhost:8080/api/v1/info
curl http://localhost:8080/api/v1/version
```

---

## License

MIT
