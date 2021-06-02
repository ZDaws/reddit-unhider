import os

import praw
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    password=os.environ["PASSWORD"],
    user_agent="Reddit Unhider",
    username=os.environ["USERNAME"],
)

num_hidden = 0
no_more = False
while not no_more:
    hidden_posts = reddit.user.me().hidden()
    no_more = True
    for post in hidden_posts:
        no_more = False
        print("Unhiding [%s] ... " % post.title)
        post.unhide()
        num_hidden += 1

print("\n%d posts unhidden!" % num_hidden)
