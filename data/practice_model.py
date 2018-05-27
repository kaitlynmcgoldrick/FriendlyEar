import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.externals import joblib

sent_df = pd.read_csv("sent_scores_data.csv")

sent_df = sent_df.sample(frac=1)
#print(sent_df.head())
x = sent_df.iloc[:,2:6]
#print(x.head())
y = sent_df.iloc[:,1:2]
#print(y.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

mlp = MLPClassifier(hidden_layer_sizes = (20,20,20,20,20), max_iter=1000)
mlp.fit(x_train, y_train.values.ravel())

predictions = mlp.predict(x_test)
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

joblib.dump(mlp, 'model.sav')
