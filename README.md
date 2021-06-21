# Video Discovery 📹 🔎 
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time 
from YouTube for a given tag/search query in a paginated response.

### Requirements

- Docker

## Usage

1. Copy .env.example to .env and set postgres password and youtube api key
1. Edit `DATABASE_URI` to `postgresql://<user>:<password>@<host>:5432/<database>` in .env
2. Apply migrations to database using `flask db upgrade`

### How to run in production

- Using docker compose run: `docker compose -f docker-compose-production.yaml up`

- Apply migration using: `docker compose -f docker-compose-production.yaml exec app flask db upgrade`

## API

### Search API

`http://127.0.0.1:5000/v1/videos?q=new&limit=2`

### Response
```
[
    {
        "description": "Welcome Back Friends! I'm so excited for this video. I finally replaced my Keurig machine in my Butler's Pantry with a new one and we are all loving it. Please ...",
        "id": 87,
        "publishedAt": "2021-06-21T14:57:03Z",
        "thumbnailUrl": "https://i.ytimg.com/vi/uWpb6UVJLfY/default.jpg",
        "title": "NEW COFFEE STATION/NEW NESPRESSO MACHINE"
    },
    {
        "description": "This is refresh. This is New Iced Coffee. #LetsMakeARefresh Scoprite di più su: https://www.lavazza.it/it/ Iscrivetevi al nostro canale YouTube: ...",
        "id": 95,
        "publishedAt": "2021-06-21T14:49:25Z",
        "thumbnailUrl": "https://i.ytimg.com/vi/llKvFShlF1Y/default.jpg",
        "title": "Lavazza Iced Coffee - Let&#39;s Make A Refresh  | Lavazza IT"
    }
]
```

### GET Videos 

`http://127.0.0.1:5000/v1/videos?limit=5&offset=2021-06-21T15:35:40Z`

### Response

```
[
    {
        "description": "Good Morning Magic Players! Welcome to Coffee and MTG, the morning Magic live stream show. Join us for Q&A and Decklist Review every weekday! Join my ...",
        "id": 108,
        "publishedAt": "2021-06-21T15:35:40Z",
        "thumbnailUrl": "https://i.ytimg.com/vi/8zA674opYLI/default.jpg",
        "title": "Velomachus Lorehold Combo Storms Modern Top 8 | Coffee and MTG June 21/2021 | Morning MTG Show!"
    },
    {
        "description": "Good Morning Magic Players! Welcome to Coffee and MTG, the morning Magic live stream show. Join us for Q&A and Decklist Review every weekday! Join my ...",
        "id": 51,
        "publishedAt": "2021-06-21T15:35:40Z",
        "thumbnailUrl": "https://i.ytimg.com/vi/8zA674opYLI/default.jpg",
        "title": "Velomachus Lorehold Combo Storms Modern Top 8 | Coffee and MTG June 21/2021 | Morning MTG Show!"
    }
```