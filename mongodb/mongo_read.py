import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['ninja']

db.coll.find_one()    # returns a single document
db.coll.find()    # returns a cursor - show 20 results - "it" to display more
db.coll.find({'shinobi_name': 'Kakashi', 'shinobi_age': 20})    # implicit logical "AND".

db.coll.find({'shinobi_age': {'$gt': 20}})   #  $gt selects those documents where the value of the field is greater than (i.e. >) the specified value
