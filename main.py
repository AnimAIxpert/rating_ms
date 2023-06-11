# python3 -m flask --app app run
from flask import Flask, request
import json
from bson import json_util
from mongoClient import client
app = Flask(__name__)

db = client["animaixpert"]
rating_collection = db["rating"]

@app.route("/")
def hello_world():
    return "<p>Rating MS</p>"

@app.route("/create-rating", methods=['POST'])
def create_rating():
    new_rating = request.get_json()
    check_rating = rating_collection.find_one({"user_id": new_rating["user_id"],"anime_id": new_rating["anime_id"]}) # check if this user already rated this anime
    if not check_rating:
        rating_collection.insert_one(new_rating)
        json_response =json.loads(json_util.dumps(new_rating))
        print(json_response)
        return json_response, 201
    else:
        rating_collection.update_one({"user_id": new_rating["user_id"],"anime_id": new_rating["anime_id"]}, {"$set": {"rating": new_rating["rating"]}})
        json_response =json.loads(json_util.dumps(new_rating))
        print(json_response)
        return json_response, 201

@app.route("/get-rating", methods=['GET'])
def get_rating():
    ret = rating_collection.find()
    ans = []
    for rating in ret:
        rating.pop('_id')
        ans.append(rating)
    return ans, 200

@app.route("/get-rating-by-ids", methods=['GET'])
def get_rating_by_user():
    user_id = request.args.get('user_id')
    anime_id = request.args.get('anime_id')
    print(int(anime_id))
    ret = rating_collection.find({"user_id": user_id})
    # ret = rating_collection.find({"anime_id": anime_id})
    ans = []
    for rating in ret:
        if rating["anime_id"] == int(anime_id):
            rating.pop('_id')
            ans.append(rating)
    return ans, 200

@app.route("/get-ratings-by-user", methods=['GET'])
def get_ratings_by_user_id():
    user_id = request.args.get('user_id')
    ret = rating_collection.find({"user_id": user_id})
    ans = []
    for rating in ret:
        rating.pop('_id')
        ans.append(rating)
    return ans, 200