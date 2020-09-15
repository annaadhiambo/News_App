from . import main
from flask import render_template
from ..requests import NewsRequests

@main.route('/')
def index():
    news = NewsRequests()
    news= news.get_top_headlines( sources='')
    # return news
    return render_template('index.html',articles=news['articles'])