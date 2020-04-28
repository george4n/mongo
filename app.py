import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient()
db = client['test-database']

collection = db.test_collection

post = {"author": "George",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
articles = db.articles
post_id = posts.insert_one(post).inserted_id
print(db.list_collection_names())

print("Hello")
print("Hello Again")
