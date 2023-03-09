import pymongo


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['ninja']

# define the schema for the collection
schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["shinobi_name", "shinobi_age"],
        "properties": {
            "shinobi_name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "shinobi_age": {
                "bsonType": "int",
                "minimum": 0,
                "maximum": 120,
                "description": "must be an integer in the range 0-120 and is required"
            }
        }
    }
}

# create the collection with the validation schema
ninja_collection = db.create_collection("ninja_details", validator=schema)
