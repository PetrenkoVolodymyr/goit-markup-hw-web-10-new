import json
from bson.objectid import ObjectId

from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://ukrcima:567234@mymongo.bpoqivq.mongodb.net/?retryWrites=true&w=majority&appName=MyMongo"
client = MongoClient(CONNECTION_STRING)
db= client['hw']

with open('qoutes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname':quote['author']})
    if author:
        db.quotes.insert_one({'quote':quote['quote'], 'tags':quote['tags'],'author':ObjectId(author['_id'])})