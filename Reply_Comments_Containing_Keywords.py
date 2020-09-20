import praw

# Change the "ENTER-..." strings to your information
r = praw.Reddit(user_agent='ENTER-YOUR-USER-AGENT',
                client_id='ENTER-YOUR-CLIENT-ID', client_secret="ENTER-YOUR-CLIENT-SECRET",
                username='ENTER-USERNAME', password='ENTER-PASSWORD')

subreddit = reddit.subreddit('aww')  # Any subreddit you want to monitor

bot_phrase = 'Good doggo!'  # Phrase that the bot replies with

# any set of keywords to find in subreddits
keywords = {'dog', 'puppy', 'doggo', 'pupper'}

# this views the top 10 (can be changed) posts in that subbreddit
for submission in subreddit.hot(limit=10):
    # makes the post title lowercase so we can compare our keywords with it.
    n_title = submission.title.lower()
    for i in keywords:  # goes through our keywords
        if i in n_title:  # if one of our keywords matches a title in the top 10 of the subreddit

            numFound = numFound + 1
            # replies and outputs to the command line
            print('Bot replying to: ')
            print("Title: ", submission.title)
            print("Text: ", submission.selftext)
            print("Score: ", submission.score)
            print("---------------------------------")
            print('Bot saying: ', bot_phrase)
            print()
            submission.reply(bot_phrase)

if numFound == 0:
    print("\nSorry, didn't find any posts with those keywords :(")
