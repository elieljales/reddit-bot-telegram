import praw
import os
import telebot
from deep_translator import GoogleTranslator
import sqlite3

reddit_client_id = os.getenv('REDDIT_CLIENT_ID')
reddit_client_secret = os.getenv('REDDIT_CLIENT_SECRET')
reddit_username = os.getenv('REDDIT_USERNAME')
reddit_password = os.getenv('REDDIT_PASSWORD')
telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')

reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    username=reddit_username,
    password=reddit_password,
    user_agent='Reddit Stream Bot'
)


conn = sqlite3.connect('./submissions.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS submission_ids (
        id TEXT PRIMARY KEY
    )
''')


def check_subreddit(subreddits, chat_ids):
    
    term = 'hiring'
    all_messages = []
    bot = telebot.TeleBot(telegram_token)

    for subreddit in subreddits:
        subreddit_obj = reddit.subreddit(subreddit)
        try:
            for submission in subreddit_obj.new(limit=20):
                if term in submission.title.lower():
                    submission_id = submission.id
                    # Check if the submission ID is already in the database
                    cursor.execute('SELECT id FROM submission_ids WHERE id = ?', (submission_id,))
                    if cursor.fetchone() is None:
                        all_messages.append(submission.title) 
                        print(submission.id)  
                        translated_title = GoogleTranslator(source='en', target='pt').translate(submission.title)
                        

                        for chat_id in chat_ids:
                            bot.send_message(
                                chat_id=chat_id,
                                text=f" PT: {translated_title} | EN: {submission.title} | {submission.shortlink}"
                            )

                        # Insert the submission ID into the database
                        cursor.execute('INSERT INTO submission_ids (id) VALUES (?)', (submission_id,))
                        conn.commit()
        except Exception as e:
            print(e)

    conn.close()

if __name__ == "__main__":
    subreddits = ["SUBREDDIT","SUBREDDIT"]
    chat_ids = ["CHAT_ID", "CHAT_ID"] 
    check_subreddit(subreddits, chat_ids)