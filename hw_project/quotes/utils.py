from pymongo import MongoClient

def get_mongobd():
    CONNECTION_STRING = "mongodb+srv://ukrcima:567234@mymongo.bpoqivq.mongodb.net/?retryWrites=true&w=majority&appName=MyMongo"
    client = MongoClient(CONNECTION_STRING)
    db= client['hw']
    return db