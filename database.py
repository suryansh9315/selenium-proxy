from pymongo import MongoClient

uri = ("mongodb+srv://suryanshsharma9315:P6dX9tVj5ETHBwxw@cluster0.kyr3quh.mongodb.net/?retryWrites=true&w=majority"
       "&appName=Cluster0")
client = MongoClient(uri, uuidRepresentation='standard')


def connect_to_db():
    try:
        database = client.get_database("barsaati")
        trends = database.get_collection("trending")
        print('Connected to database')
        return trends
    except Exception as e:
        print(e)
        return None
