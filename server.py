from flask import Flask
from flask import send_file
from flask import request

import db
import data

app = Flask(__name__)

server = 'localhost'

def login_success(nesID):
    cust_data = data.get_data(nesID)
    return send_file("index2.html")


@app.route('/hc')
def hc():
    return send_file('static.html')

@app.route('/JS_Dependencies/Chart.bundle.min.js')
def Chartjs():
    return send_file('JS_Dependencies/Chart.bundle.min.js')

@app.route("/JS_Dependencies/StarAdmin-Free-Bootstrap-Admin-Template-master/css/style.css")
def css():
    return send_file('JS_Dependencies/StarAdmin-Free-Bootstrap-Admin-Template-master/css/style.css')

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/hcPage.html')
def hcpage():
    return send_file("hcPage.html")

@app.route('/<page>')
def js_page2(page):
    try:
        return send_file(page)
    except:
        print(page+" not found")

@app.route('/login', methods = ['POST'])
def POST_login():
    password = request.values['password']
    username = request.values['netid']
    nesID = db.get_user(username, password)
    if nesID == "" :
        return send_file('loginfail.html')
    else:
        return login_success(nesID)


@app.route('/css/<page>')
def css_page(page):
    try:
        return send_file("/css/"+page)
    except:
        print("/css/"+page+" not found")
        return ""

@app.route('/js/<page>')
def js_page(page):
    try:
        return send_file("/js/"+page)
    except:
        print("/js/"+page+" not found")
        return ""




if __name__ == '__main__':
    app.run()
