from pymongo import MongoClient

import pandas as pd
client = MongoClient("mongodb+srv://sittichaitantanasiwakul:fAnNVJmPpCi9eW8T@clustersafe.fncdgxk.mongodb.net/")

db = client["mongodbVSCodePlaygroundDB"]
collection = db["sales"]

#for doc in collection.find():
    #print(doc)

data = list(collection.find())
df = pd.DataFrame(data)
print(df.head())





