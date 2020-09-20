import praw  # Reddit's official API
import base64
from urllib.request import quote  # for making the parent comment into a link

# Change the "ENTER-..." strings to your information
r = praw.Reddit(user_agent='ENTER-YOUR-USER-AGENT',
                client_id='ENTER-YOUR-CLIENT-ID', client_secret="ENTER-YOUR-CLIENT-SECRET",
                username='ENTER-USERNAME', password='ENTER-PASSWORD')

r.read_only = False
# Choose your desired subreddit to analyse or just 'all' for full comment stream
subreddit = r.subreddit("ENTER-SUBREDDIT-OF-CHOICE")
comments = subreddit.stream.comments(
    skip_existing=True)  # get the comment stream

count = 1  # for the counter
keywords = {' Microsoft ', ' Facebook '}  # Change keywords as per your desire

for comment in comments:  # checks each comment in the comment stream
    text = str(comment.body)  # Fetch the body of the comment
    for i in keywords:
        if i in text:  # if one of our keywords matches a title
            print("____________________________________________________________________")
            print("found new comment! processing... (" + str(count) + ")")
            print(text)
            count += 1  # add 1 to the number
