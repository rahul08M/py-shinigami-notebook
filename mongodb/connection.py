# Here's an example of how to use PyMongo to connect to a MongoDB instance:

import pymongo


def client():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    return client
