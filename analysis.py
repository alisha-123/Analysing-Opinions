import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset=pd.read_csv('@narendramodi_stream.csv')

import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus=[]
output=[]
plen=0
nlen=0
neutral=0
for i in range(0,112):
    review = re.sub('[^a-zA-Z]',' ',dataset['tweet_text'][i])
    review = review.lower()
    review = review.split()
    ps=PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
   
from textblob import TextBlob

def get_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
    

i=0
for i in range(0,112):
    output.append(get_sentiment(corpus[i]))
dataset['output']=output

i=0
for i in range(0,112):
    if (dataset['output'][i])=="positive":
        plen=plen+1
    elif (dataset['output'][i])=="negative":
        nlen=nlen+1
    else:
        neutral=neutral+1


    #bag of words
'''from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,-1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.60, random_state = 0)


# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
'''