import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.externals import joblib
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize 
import numpy as np
#sent_df = pd.read_csv("sent_scores_data.csv")

#sent_df = sent_df.sample(frac=1)
#print(sent_df.head())
#x = sent_df.iloc[:,2:6]
#print(x.head())
#y = sent_df.iloc[:,1:2]
#print(y.head())

#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

#mlp = MLPClassifier(hidden_layer_sizes = (40,40,40,40,40), max_iter=1000)
#mlp.fit(x_train, y_train.values.ravel())

model = joblib.load('model.sav')

#predictions = mlp.predict(x_test)
#print(confusion_matrix(y_test,predictions))
#print(classification_report(y_test,predictions))
#joblib.dump(mlp, 'model.sav')

string = "I am feeling depressed lately."
string2 = "So tired and miserable lately."
string3 = "Can't take it anymore."
string4 = "I love my life!"
string5 = "I ate a sandwich for lunch."
string6 = "I'm happy af"
string7 = "I'm ok"
str_lst = [string, string2, string3, string4, string5, string6, string7]

#strl2 has an example of a positive potential google search, and a negative potential warning sign of seriously negative thought. correctly classifies both. 
strl2 = ["Where can I find a sandwich near me?", "I wish I could just disappear forever", "vine comps"]
sid = SentimentIntensityAnalyzer()
def scorer(text,model):
	ss = sid.polarity_scores(text)
	return model.predict(np.array([ss["compound"],ss["neg"],ss["neu"], ss["pos"]]).reshape(1,-1))
#print("sentence: {}, score: {}".format())
#print(scorer(string, model))

for s in strl2:
	print(s)
	print("score: ")
	print(scorer(s, model))
	print("\n")
