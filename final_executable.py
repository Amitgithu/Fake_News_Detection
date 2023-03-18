
import re
import string
def process_news(news):
    news = news.lower()
    news = re.sub('\[.*?\]', '', news)
    news = re.sub("\\W", " ", news)
    news = re.sub('https?://\S+|www\.\S+', '', news)
    news = re.sub('<.*?>+', '', news)
    news = re.sub('[%s]'% re.escape(string.punctuation), '',news)
    news = re.sub('\n','',news)
    news = re.sub('\w*\d\w*', '', news)
    return news

#from sklearn.feature_extraction.text import TfidfVectorizer
#vector = TfidfVectorizer()
'''
import pickle

# load the saved model from disk
with open('LogisticRegression.pkl', 'rb') as f:
    model = pickle.load(f)

#with open('Vector.pkl', 'rb') as vec:
#    Vector = pickle.load(vec)
 '''

import pandas as pd

import joblib
Vector = joblib.load('Vector.pkl')

model = joblib.load('LogisticRegression.pkl')

### Final for checking news
news = input("Enter news : ")
test_news = {"text" : [news]}
test_data = pd.DataFrame(test_news)
test_data["text"] = test_data["text"].apply(process_news)
x_test = test_data["text"]

#vector_x_test = Vector.fit(x_test)
vector_x_test = Vector.transform(x_test)

prediction = model.predict(vector_x_test)
if(prediction[0] == 'true'):
    print("Real News")
else:
    print("Fake News")

    To = input("Enter gmail :")
    import yagmail

    user = 'sharmapavan1226@gmail.com'
    password = 'lhqd eoll xcsd qypu'

    subject = 'Fake news'

    content = ['The news that you received is fake']
    
    with yagmail.SMTP(user, password) as yag:
        for i in range(10):
            yag.send(To, subject, content)
            print('email sent successfully')

    

