import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['ninja']

db.coll.find_one()    # returns a single document
db.coll.find()    # returns a cursor - show 20 results - "it" to display more
db.coll.find({'shinobi_name': 'Kakashi', 'shinobi_age': 201})    # implicit logical "AND".
