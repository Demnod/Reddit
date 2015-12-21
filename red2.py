import praw

user_agent = ("Demnod Top10 0.1")

r = praw.Reddit("leagueoflegends")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("leagueoflegends")

for submission in subreddit.get_hot(limit=5):
	print "Title: ", submission.title
	print "Text: ", submission.selftext
	print "Score: ", submission.score
	print "=============\n"