from flask import render_template
from newsapi import Newsapiclient


# Views
@app.route('/')
def index():

newsapi = Newsapiclient(api_key ="b6b97041f75646a49484f3adc0ff7156")
everything = newsapi.get_top_everything(sources = "bbc-news")

articles = everything["articles"]

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
        

    mytitle = zip(aut, tit, descr, url ,img ,at ,cont)

    return render_template('index.html', context=mytitle)