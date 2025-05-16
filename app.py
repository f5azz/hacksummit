from flask import Flask, Response, request
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

client = MongoClient("mongodb+srv://manisalian:PqXNq8KvMLpXplxP@crud.jeyup.mongodb.net/NEWS?retryWrites=true&w=majority&appName=NEWS")
db = client["NEWS"]

@app.route('/news', methods=['GET'])
def get_news_by_language():
    lang = request.args.get('lang', 'English')
    if lang not in db.list_collection_names():
        return Response(dumps({"error": "Invalid language or collection not found"}, ensure_ascii=False), status=404, mimetype='application/json')

    collection = db[lang]
    docs = list(collection.find({}, {"_id": 0}))
    
    return Response(dumps(docs, ensure_ascii=False), mimetype='application/json')

@app.route('/newsFront', methods=['GET'])
def get_news_front_by_language():
    lang = request.args.get('lang', 'English')
    if lang not in db.list_collection_names():
        return Response(dumps({"error": "Invalid language or collection not found"}, ensure_ascii=False), status=404, mimetype='application/json')

    collection = db[lang]
    docs = list(collection.find({}, {"post_id": 1,"img_url": 1,"title": 1}))
    
    return Response(dumps(docs, ensure_ascii=False), mimetype='application/json')

@app.route('/getSchol', methods=['GET'])
def get_schol_by_language():
    db = client["researchBasedScholarshipData"]
    lang = request.args.get('lang', 'English')
    if lang not in db.list_collection_names():
        return Response(dumps({"error": "Invalid language or collection not found"}, ensure_ascii=False), status=404, mimetype='application/json')

    collection = db[lang]
    docs = list(collection.find({}, {"_id":0}))
    
    return Response(dumps(docs, ensure_ascii=False), mimetype='application/json')

@app.route('/grocery', methods=['GET'])
def get_groc_by_language():
    db = client["Groceries"]
    lang = request.args.get('lang', 'English')
    if lang not in db.list_collection_names():
        return Response(dumps({"error": "Invalid language or collection not found"}, ensure_ascii=False), status=404, mimetype='application/json')

    collection = db[lang]
    docs = list(collection.find({}, {"_id":0}))
    
    return Response(dumps(docs, ensure_ascii=False), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
