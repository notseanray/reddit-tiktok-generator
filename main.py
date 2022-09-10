import os
from PIL import Image
from PIL import ImageDraw
import glob
import praw

print("logged in as " + os.environ["RUSERNAME"])

class RedditPost:
    def __init__(self, post) -> None:
        self.author = post.author
        self.name = post.name
        self.num_comments = post.num_comments
        self.over_18 = post.over_18
        self.created_utc = post.created_utc
        self.score = post.score
        self.title = post.title
        self.upvote_ratio = post.upvote_ratio
        self.spoiler = post.spoiler
        self.edited = post.edited
        self.locked = post.locked
        self.content = post.selftext

    def speak(self):
        os.system("espeak '{}'".format(self.content))

    def titleCard(self):
        img = Image.new(mode="RGB", size=(800, 300))
        imgD = ImageDraw.Draw(img)
        imgD.text((300, 100), self.title, fill=(255, 255, 255))
        img.save("title.png")


def toppost(subreddit, amt=10):
    subreddit = r.subreddit(subreddit)
    posts = []
    top_python = subreddit.top(limit=amt)
    for submission in top_python:
        if not submission.stickied:
            posts.append(RedditPost(submission))
    return posts

# os.system("espeak 'i will twist the shit out of your testicles'")
r = praw.Reddit(username = os.environ["RUSERNAME"],
                password = os.environ["PASSWORD"],
                client_id = os.environ["CLIENT_ID"],
                client_secret = os.environ["CLIENT_SECRET"],
                user_agent = os.environ["USER_AGENT"])

posts = toppost("prorevenge", 2)

for p in posts:
    p.titleCard()
