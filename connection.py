import pymongo
url = "mongodb+srv://LACR2008:LACR2008@luiscluster.pqvvz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
#print(client.test)