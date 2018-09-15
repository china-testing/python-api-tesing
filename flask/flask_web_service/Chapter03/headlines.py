import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {'ft': 'http://www.ftchinese.com/rss/feed',
             'zhihu': 'https://www.zhihu.com/rss',
             'people': 'http://www.people.com.cn/rss/politics.xml',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}


@app.route("/")
@app.route("/<publication>")
def get_news(publication="ft"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000, debug=True)
