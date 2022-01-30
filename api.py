from flask import Flask,jsonify
import random,logging
from main import get_meme, check_image

app = Flask(__name__)
count = 0
randommeme = ['meme','dankmeme','wholesomeme','memes']

@app.route('/givememe')
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