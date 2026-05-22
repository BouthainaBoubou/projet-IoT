from flask import Flask, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
from config import *

app  = Flask(__name__)
CORS(app)
col  = MongoClient(MONGO_URI)[DB_NAME][COLLECTION]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/latest")
def latest():
    doc = col.find_one(sort=[("_id", -1)])
    if doc:
        doc["_id"] = str(doc["_id"])
        return jsonify(doc)
    return jsonify({"humidity": None, "timestamp": "Aucune donnee"})

@app.route("/api/history")
def history():
    docs = list(col.find().sort("_id", -1).limit(50))
    for d in docs:
        d["_id"] = str(d["_id"])
    docs.reverse()
    return jsonify(docs)

if __name__ == "__main__":
    print("Serveur démarré sur http://localhost:5000")
    app.run(debug=True, port=5000)