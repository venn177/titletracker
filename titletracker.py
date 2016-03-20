import praw
import time
from datetime import datetime

REDDIT_USERNAME = "" # username of the bot
REDDIT_PASS = "" # password of the bot
SUBREDDIT_NAME = "" # subreddit you wish to track
WAIT_TIME = 10 # seconds between checking the subreddit for picture links
WORD_WATCH = "" # word or phrase the bot tracks in titles of threads
PM_USER = "" # user that the bot PMs when it finds WORD_WATCH in the title of the post

def main():
    currentTime = '[' + str(datetime.now().strftime("%H:%M:%S")) + '] '
    r = praw.Reddit(user_agent = 'titletracker v0.1')
    print(currentTime + "Logging in...")
    r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning = True)
    already_done = set()

    while True:
        currentTime = '[' + str(datetime.now().strftime("%H:%M:%S")) + '] '
        print(currentTime + "Scanning for posts with your criteria...")
        submissions = r.get_subreddit(SUBREDDIT_NAME).get_new(limit=100)
        for item in submissions:
            if WORD_WATCH in item.title and item.id not in already_done:
                r.send_message(PM_USER, item.title, 'Found what you were looking for!\n\n' + item.url)
                already_done.add(item.id)
        currentTime = '[' + str(datetime.now().strftime("%H:%M:%S")) + '] '
        print(currentTime + 'Sleeping...')
        time.sleep(WAIT_TIME)

if __name__ == "__main__":
    main()
