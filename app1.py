from flask import Flask, render_template, request
import pickle
import re
import string
import pandas as pd


vector = pickle.load(open('Vector.pkl','rb'))
model  = pickle.load(open('LogisticRegression.pkl','rb'))


# creating flask object
app = Flask(__name__)

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

def final_implement(news):
    
    news = input("Enter news : ")
    test_news = {"text" : [news]}
    test_data = pd.DataFrame(test_news)
    test_data["text"] = test_data["text"].apply(process_news)
    x_test = test_data["text"]

    vector_x_test = vector.fit(x_test)
    vector_x_test = vector.transform(x_test)
    prediction = model.predict(vector_x_test)
    
    return prediction

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    if request.method=='POST':
        message = request.form['news']
        final_news = process_news(message)
        pred = final_implement(final_news)

        ans=1

        return render_template('index.html',prediction=ans)
    
if __name__ =='__main__':
    app.run()


