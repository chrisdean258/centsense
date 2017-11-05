from flask import Flask
from flask import send_file
from flask import request

app = Flask(__name__)

server = 'localhost'

@app.route('/static')
def stat():
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

@app.route('/login', methods = ['POST'])
def POST_login():
    print(request.values)
    return send_file('static.html')





if __name__ == '__main__':
    app.run()
