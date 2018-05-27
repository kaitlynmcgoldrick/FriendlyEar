import praw
import pandas as pd

reddit = praw.Reddit(client_id = '5jIWSDuf-hzOnA', client_secret = '9DMjnsRO8PYj-Lr5ZBy_7NTAkkY', user_agent = 'sadbot', username = 'anneboat', password = 'Evergirl1')
subreddit = reddit.subreddit('depression')
submissions = subreddit.top(limit = 400)

topics_dict = { "text":[], "classification":[] }

for submission in submissions:
	topics_dict["text"].append(submission.selftext)
	topics_dict["classification"].append(1)

topics_data = pd.DataFrame(topics_dict)

topics_data.to_csv('depressed_set.csv')

subreddit2 = reddit.subreddit('CasualConversation')
submissions2 = subreddit2.top(limit = 400)

topics_dict2 = { "text":[], "classification":[]}

for submission in submissions2:
	topics_dict2["text"].append(submission.selftext)
	topics_dict2["classification"].append(0)

topics_data2 = pd.DataFrame(topics_dict2)
topics_data2.to_csv('notdepressed_set.csv')

