from flask import Flask, render_template, request, url_for, redirect
import json
from pymongo import MongoClient
from bson import json_util
app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
rating = db.rating



# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route('/', methods=('GET', 'POST'))
# def index():
#     return render_template('index.html')

@app.route('/', methods=('POST'))
def index():
    if request.method=='POST':
        user = request.form['user_id']
        anime = request.form['anime_id']
        rating = request.form['rating']

        #content = request.form['content']
        #myquery = { "content": content }
        #degree = request.form['degree']
        #newvalues = { "$set": { "degree": degree } }

        """ mydoc = todos.find_one(myquery)
        print("mydoc: ", mydoc)
        if (mydoc == None):
            todos.insert_one({'content': content, 'degree': degree})
        else:
            todos.update_one(myquery, newvalues) """
        mydoc = {'user_id': user, 'anime_id': anime, 'rating': rating}
        todos.insert_one(mydoc)
        return json.loads(json_util.dumps(mydoc))
    #return "rqting creqted"

@app.route('/get-rating', methods=('GET'))
def get_rating():
    if request.method=='GET':
        