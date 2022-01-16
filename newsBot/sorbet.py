import linkScraper
import praw

r = praw.Reddit('bot1')
subreddit = r.subreddit("news")

for submission in subreddit.hot(limit = 1):
    top_level_comments = list(submission.comments)
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
    for comments in top_level_comments:
        if "that's awful" in comments.body:
            print("Comment:", comments.body)
            print("User:", comments.author)
            r.redditor(str(comments.author)).message("TEST", "test message from PRAW")