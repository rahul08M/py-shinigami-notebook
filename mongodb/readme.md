# mongo with python

### MongoDB is a popular NoSQL document-oriented database system that uses a flexible JSON-like data model and can scale horizontally across multiple servers.


## prerequisite
PyMongo: PyMongo is the official Python driver for MongoDB. It provides a simple and easy-to-use interface to interact with MongoDB from Python. To install PyMongo, you can use pip:

```
pip install pymongo
```

## mongo connection 
In PyMongo, the connection URL (Uniform Resource Locator) is used to specify the location and configuration details of the MongoDB instance to which you want to connect. 

The connection string consists of a URL that specifies the hostname, port number, and other optional parameters.

Here's an example of a connection string in PyMongo:

```
import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
```

In the example above, we create a MongoClient instance and pass the connection string 'mongodb://localhost:27017/'. This specifies that we want to connect to a MongoDB instance running on the local machine, using the default port number 27017.

