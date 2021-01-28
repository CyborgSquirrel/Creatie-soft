import pymongo

Client = pymongo.MongoClient("mongodb+srv://Calin:GUjTnNlQ56yD8ntL@matearenacluster.x6qt4.mongodb.net/test")

DB = Client['Probleme']

print(DB.list_collection_names())
