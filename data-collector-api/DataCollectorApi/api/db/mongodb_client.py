from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.MONGODB_SETTINGS['MONGO_URI'])
db = client[settings.MONGODB_SETTINGS['MONGO_DB_NAME']]
