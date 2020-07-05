import pymongo

client = pymongo.MongoClient(
   "mongodb+srv://keng85:kateengard3666980!@cluster0.t2vks.gcp.mongodb.net/test")
db = client.test
print(client)