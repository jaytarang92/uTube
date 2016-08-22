from flask import Flask, url_for, request, jsonify
from flask import render_template
from flask_restful import Resource, Api
import tuber

app = Flask(__name__, static_url_path='/static')
api = Api(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/videos", methods=['GET','POST'])
def get():
    se_string = request.form['search']
    tube = tuber.Youtube()
    links = tube.search(se_string)
    return render_template('videos.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)
