from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import json

application = Flask(__name__)


@application.route("/")
def index():
    return render_template("index.html", news_result="")

@application.route("/fake-news", methods=['GET'])
def load_model():

    # Get query string parameters
    news_string = request.args.get('query')

    # Check if 'query' parameter is missing or empty
    if not news_string:
        return render_template("index.html", news_result="Please provide a news headline.")

    ##### model loading ######
    loaded_model = None
    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)

    vectorizer = None
    with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)
    ###############
    # how to use model to predict
    prediction = loaded_model.predict(vectorizer.transform([news_string]))[0]
    # output will be 'FAKE' if fake, 'REAL' if real

    # Update web page with the result of fake/real given the provided news
    if prediction == "FAKE":
        result = "This news is fake."
    elif prediction == "REAL":
        result = "This news is real."
    else:
        result = "Unable to determine if this news is fake or real."

    return render_template("index.html", news_result=result)

if __name__ == "__main__":
    application.run()