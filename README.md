
# Reddit Bot

It's a simple project to read data from Reddit API and send notifications in Telegram Bot.



## Features

- Read Data From Reddit API.
- Send Message to Telegram Bot.
- Mark checkpoint in the database to prevent duplicate notifications.
- Translate notification


## Requirements
 - Docker
 - Reddit API Token ( You can create on https://www.reddit.com/prefs/apps)
 - Telegram API Token ( You can check documentation on https://core.telegram.org/bots/tutorial)
 - Get Chat IDs (https://api.telegram.org/bot{YOUR_TELEGRAM_TOKEN}/getUpdates)
## Run Locally

Clone the project

```bash
  git clone https://github.com/elieljales/reddit-bot-telegram
```

Edit configs in Dockerfile and script.py
```bash
    REDDIT_CLIENT_ID 
    REDDIT_CLIENT_SECRET 
    REDDIT_USERNAME 
    REDDIT_PASSWORD 
    TELEGRAM_BOT_TOKEN 
```
```python
    subreddits = ["YOUR_SUBREDDIT_HERE","YOUR_SUBREDDIT_HERE"]
    chat_ids = ["YOUR_CHAT_ID_HERE", "YOUR_CHAT_ID_HERE"] 
``` 


Go to the project directory

```bash
  cd reddit-bot-telegram
```

Build Docker

```bash
  docker build -t reddit-bot-telegram .   
```

Run Container
```bash
   docker run -d reddit-bot-telegram  
```


## Run on Fly.io

Your can host this bot on [Fly.io](https://fly.io/) for free.

To do that you need create a account and configurate your local environment and run: 

 
```bash
    fly launch
```
## Authors

- [@elieljales](https://www.github.com/elieljales)

