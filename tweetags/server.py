from flask import Flask, request
from utils.phraser import phrase_collector
from twitterapi import keyword_search

app = Flask(__name__)

@app.route('/phrase')
def phrase_finder():
    sentence = request.args.get('sentence', None)
    if sentence is None:
        return "No query string passed."
    tag_collector = phrase_collector(sentence)
    tags = [] # collect all data from tags
    for word in tag_collector:
        tags.append(list(set(keyword_search(word))))
    return {'tags': tags}

@app.route('/')
def index():
    return "Server is up!"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')