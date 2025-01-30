from django.http import HttpResponse
from django.shortcuts import render
from pymongo import MongoClient
from django.http import JsonResponse
import os


MONGO_URI = 'mongodb+srv://MigrationReportingToolDb:gSuDEZ2eqM8x55wW@cluster0.c1zan.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
# try:
#     client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
#     client.server_info()
#     print("Connected to MongoDB")
# except Exception as e:
#     print(e)

db = client['MigrationReportingToolDb']
collection = db['reddit_posts']

def get_reddit_posts(request):
    # return HttpResponse("hello reddit")
    data = list(collection.find({}, {"_id": 0}))
    formatted_data = []
    for item in data:
        formatted_data.append({
            "title": item.get("title", "N/A"),
            "text": item.get("text", "N/A"),
            "subreddit": item.get("subreddit", "N/A"),
            "score": item.get("score", "N/A"),
            "url": item.get("url", "N/A"),
            "num_comments": item.get("num_comments", "N/A"),
            "created_at": item.get("created_at", "N/A"),
        })

    return JsonResponse(formatted_data, safe=False, json_dumps_params={'indent': 4})
    # print(data)
    # return JsonResponse(list(data), safe=False)