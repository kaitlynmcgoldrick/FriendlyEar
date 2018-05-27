import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
#nltk.download('punkt')
#nltk.download('vader_lexicon')

df = pd.read_csv("depressed_set.csv")
df2 = pd.read_csv("notdepressed_set.csv")

df = pd.concat([df, df2])
df = df.dropna(axis = 0, subset=['text'])
#vec_text = df['text']
#vt1 = vec_text[0]
#print(vt1)

#lines_list = tokenize.sent_tokenize(vt1)
sid = SentimentIntensityAnalyzer()
#for sentence in lines_list:
#	print(sentence)
#	ss = sid.polarity_scores(sentence)
#	for k in sorted(ss):
#		print('{0}: {1}, '.format(k, ss[k]), end='')
#	print()

sent_df = {"sentence":[], "classification":[], "pos":[], "neg":[], "neu":[], "comp":[]}

for i, row in df.iterrows():
	doc = row['text']
#	print(doc)
	cls = row['classification']
	lines_list = tokenize.sent_tokenize(doc)
	for sentence in lines_list:
		ss = sid.polarity_scores(sentence)
		sent_df["sentence"].append(sentence)
		sent_df["classification"].append(cls)
		sent_df["pos"].append(ss["pos"])
		sent_df["neg"].append(ss["neg"])
		sent_df["neu"].append(ss["neu"])
		sent_df["comp"].append(ss["compound"])

final_sent_df = pd.DataFrame(sent_df)
final_sent_df.to_csv("sent_scores_data.csv")
