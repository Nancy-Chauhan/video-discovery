# Video Discovery

## Installation

### Requirements

- python 3.9
- Pipenv for dependency management

## Usage

1. Copy .env.example to .env and set postgres password and youtube api key
1. Edit `DATABASE_URI` to `postgresql://<user>:<password>@<host>:5432/<database>` in .env
2. Apply migrations to database using `flask db upgrade`

### How to run in production

- Using docker compose run: `docker compose -f docker-compose-production.yaml up`

- Apply migration using: `docker compose -f docker-compose-production.yaml exec app flask db upgrade`

## API

### Search API

`http://127.0.0.1:5000/v1/videos?q=new`

### GET Videos 

`http://127.0.0.1:5000/v1/videos?limit=5&offset=2021-06-21T15:35:40Z`