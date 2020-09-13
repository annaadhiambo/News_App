from flask import Flask,render_template
from newsapi import NewsApiClient
import os
from app import app


app = Flask(__name__)

# Views
@app.route('/')
def index():

    newsapi = NewsApiClient(api_key ="b6b97041f75646a49484f3adc0ff7156")
    top_headlines = newsapi.get_top_headlines(q='trump')

    articles = top_headlines["articles"]

    aut = []
    tit =[]
    descr =[]
    url =[]
    img =[]
    at =[]
    cont =[]

    for i in range(len(articles)):
        myarticles = articles[i]

        aut.append(myarticles['author'])
        tit.append(myarticles['title'])
        descr.append(myarticles['description'])
        url.append(myarticles['url'])
        img.append(myarticles['urlToImage'])
        at.append(myarticles['publishedAt'])
        cont.append(myarticles['content'])
                

        mylist = zip(aut, tit, descr, url ,img ,at ,cont)

        return render_template('index.html', context=mylist)

if __name__ == "__main__":
    app.run(debug=True)
    app.run
