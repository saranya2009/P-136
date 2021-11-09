#Main Server file
from flask import Flask, jsonify, request
from data import data
app = Flask(__name__)

#home function
@app.route("/star")
def start():
 name = request.args.get("name")
 star_data = next(item for item in data if item["name"] == name)
 return jsonify({
 "data": star_data,
 "message": "success"
 }), 200

if __name__ == "__main__":
    app.run()