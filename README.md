# Sample FastAPI

This repository contains some basic templates for FastAPI

It also contains `Dockerfile` and `docker-compose.yml` as a template to deploy FastAPI in Docker container.

# How to use

## Without Docker
1. Run `pip install -r requirements.txt`
2. Run `python app.py`
3. Go to `http://localhost:8000`
4. Enjoy!

## With Docker
1. Install Docker and Docker Compose if not already done so
2. Run `docker-compose up -d`
3. Go to `http://localhost:8000`
4. Enjoy!
5. To remove the container, run `docker-compose down`