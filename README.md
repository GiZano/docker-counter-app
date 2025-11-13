# Docker Counter App

Simple project to learn Docker and Docker Compose.

## How to use

1. Clone the project
    
    --- bash ---
    git clone <repository>
    cd docker-counter-app

2. Start with Docker Compose
    
    docker-compose up -
    
3. Open browser

    App: http://localhost:5000

## Useful Commands

### See logs
docker-compose logs

### Stop containers
docker-compose down

### Re-build image
docker-compose build --no-cache

### Enter in the container
docker-compose exec web bash