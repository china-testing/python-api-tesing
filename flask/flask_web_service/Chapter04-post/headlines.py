import feedparser
from flask import Flask
from flask import render_template
from flask import request
import json
import urllib

app = Flask(__name__)

RSS_FEEDS = {'ft': 'http://www.ftchinese.com/rss/feed',
             'zhihu': 'https://www.zhihu.com/rss',
             'people': 'http://www.people.com.cn/rss/politics.xml',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

DEFAULTS = {'publication': 'ft',
            'city': 'London,UK',
            'currency_from': 'GBP',
            'currency_to': 'USD'
            }


@app.route("/", methods=['GET', 'POST'])
def home():
    # get customised headlines, based on user input or default
    publication = request.form.get('publication')
    if not publication:
        publication = DEFAULTS['publication']
    articles = get_news(publication)
    # get customised weather based on user input or default
    return render_template("home.html", articles=articles)


def get_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed['entries']


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000, debug=True)
