# Docker Counter App

Simple project to learn Docker, Docker compose and scaling with Docker.

## How to use

1. Clone the project
    
   ```bash
    git clone X
    cd docker-counter-app
   ```

2. Start with Docker Compose
    ```bash
    docker-compose up -d --scale web:[X]
    ```
    
3. Open browser

    App: http://localhost:80

## Useful Commands

### See logs
```bash
docker-compose logs
```

#### Web logs
```bash
docker-compose logs -f web
```

#### Load Balancer logs
```bash
docker-compose logs -f nginx
```

### Stop containers
```bash
docker-compose down
```

### Re-build image
```bash
docker-compose build --no-cache
```

### Enter in the container
```bash
docker-compose exec web bash
```
