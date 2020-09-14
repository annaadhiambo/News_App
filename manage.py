from flask import Flask,render_template
from app.requests import NewsRequests
app = Flask(__name__)
@app.route('/')
def index():
    news = NewsRequests()
    news= news.get_top_headlines( sources='')
    # return news
    return render_template('index.html',articles=news['articles'])
    return '<h1 style="color:red; text-align:center; font-size:70px; background-color:grey; height:20vh;" > World News </h1>'


    

    
if __name__ == '__main__':
    app.run(debug = True)