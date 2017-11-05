from flask import Flask
from flask import send_file
app = Flask(__name__)


@app.route('/test')
def charts():
    return send_file('chart.html')

@app.route('/static')
def stat():
    return send_file('static.html')

@app.route('/JS_Dependencies/Chart.bundle.min.js')
def Chartjs():
    return send_file('JS_Dependencies/Chart.bundle.min.js')

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route("/JS_Dependencies/StarAdmin-Free-Bootstrap-Admin-Template-master/css/style.css")
def css():
    return send_file('JS_Dependencies/StarAdmin-Free-Bootstrap-Admin-Template-master/css/style.css')

if __name__ == '__main__':
    app.run()
