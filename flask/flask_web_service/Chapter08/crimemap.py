from flask import Flask
from flask import render_template
from flask import request
import json
import dateparser
import datetime
import string
import dbconfig
if dbconfig.test:
    from mockdbhelper import MockDBHelper as DBHelper
else:
    from dbhelper import DBHelper


app = Flask(__name__)
DB = DBHelper()

categories = ['mugging', 'break-in']


def sanitize_string(userinput):
    whitelist = string.letters + string.digits + " !?.,;:-'()&"
    return filter(lambda x: x in whitelist, userinput)


def format_date(userdate):
    date = dateparser.parse(userdate)
    try:
        return datetime.datetime.strftime(date, "%Y-%m-%d")
    except TypeError:
        return None


@app.route("/")
def home(error_message=None):
    crimes = DB.get_all_crimes()
    crimes = json.dumps(crimes)
    return render_template("home.html", crimes=crimes, categories=categories, error_message=error_message)


@app.route("/submitcrime", methods=['POST'])
def submitcrime():
    try:
        error_message = None
        category = request.form.get("category")
        if category not in categories:
            return home()

        date = format_date(request.form.get("date"))
        if not date:
            return home("Invalid date. Please use yyyy-mm-dd format")
        try:
            latitude = float(request.form.get("latitude"))
            longitude = float(request.form.get("longitude"))
        except:
            error_message = "Latitude and Longitude have incorrect format"
            return home(error_message)
        description = sanitize_string(request.form.get("description"))
        DB.add_crime(category, date, latitude, longitude, description)
        return home()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=True)
