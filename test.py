from pymongo import MongoClient
import os


MDB_URI = os.environ['MONGODB_URI']

# Connect to your MongoDB cluster:
client = MongoClient(MDB_URI)

# List all the databases in the cluster:
for db_info in client.list_database_names():
   print(db_info)

# List all the collections in 'sample_mflix':
db = client['admin']
collections = db.list_collection_names()
for collection in collections:
   print(collection)