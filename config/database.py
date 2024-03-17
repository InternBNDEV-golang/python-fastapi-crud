# Establishing a connection to a MongoDB Atlas cluster using pymongo.

# Importing the MongoClient class from the pymongo library.
from pymongo import MongoClient
import dotenv
import os

dotenv.load_dotenv()

# Connecting to the MongoDB Atlas cluster using the MongoClient constructor and providing the connection string.
client = MongoClient(os.getenv("MONGO_URI"))

# Accessing the 'test' database within the connected cluster.
db = client[os.getenv("DB_NAME")]

# Accessing the 'users' collection within the 'test' database.
user_collection = db["users"]
