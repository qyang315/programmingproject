from flask import Flask,jsonify
import random,logging
from main import get_meme, check_image
from flask_cors import CORS, cross_origin

app = Flask(__name__)
count = 0
app.config['CORS_HEADERS'] = 'Content-Type'
randommeme = ['meme','dankmeme','wholesomeme','memes']

@app.route('/givememe',methods = ['GET'])
def random_meme():              #Random and one
    sub = random.choice(randommeme)
    r = get_meme(sub,100)
    requsted = random.choice(r)

    while not check_image(requsted["Url"]):
        requsted = random.choice(r)

    return jsonify({
        'Title':requsted["Title"],
        'Url': requsted["Url"],
        'Upvotes': requsted["Upvotes"],
        'Downvotes': requsted["Downvotes"],
        'Redditurl': requsted["Redditurl"],
        'Subreddit': requsted["Subreddit"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
