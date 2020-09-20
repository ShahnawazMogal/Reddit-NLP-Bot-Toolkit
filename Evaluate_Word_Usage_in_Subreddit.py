import praw

# Enter your correct Reddit information into the variable below

reddit = praw.Reddit(user_agent='ENTER-YOUR-USER-AGENT',
                         client_id='ENTER-YOUR-CLIENT-ID', client_secret="ENTER-YOUR-CLIENT-SECRET",
                         username='ENTER-USERNAME', password='ENTER-PASSWORD'

# Any subreddit you want to find keywords
subreddit=reddit.subreddit('politics')

keywords={}  # makes a dictionary of keywords to and puts in values found in titles along with the number of occurrences

# this views the top 10 posts in that subbreddit
for submission in subreddit.hot(limit=10):
    # makes the post title lowercase so we can compare our keywords with it.
    n_title=submission.title.lower()
    print(">>>"+n_title+"<<<")  # Prints out the title
    n_title=n_title.split()
    for i in n_title:  # goes through the words in the title
        if i in keywords:  # increments the word count in the dictionary
          keywords[i] += 1
        else:
          keywords[i]=1

print(keywords)
