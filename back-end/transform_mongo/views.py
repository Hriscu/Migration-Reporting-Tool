from django.http import HttpResponse
from django.shortcuts import render
from pymongo import MongoClient
from django.http import JsonResponse
import os
from SPARQLWrapper import SPARQLWrapper, JSON, XML
from rdflib import Graph
from datetime import datetime


MONGO_URI = 'mongodb+srv://MigrationReportingToolDb:gSuDEZ2eqM8x55wW@cluster0.c1zan.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

def get_reddit_posts_json(request):
    db = client['MigrationReportingToolDb']
    collection = db['reddit_posts']
    # return HttpResponse("hello reddit")
    data = list(collection.find())
    formatted_data = []
    for item in data:
        formatted_data.append({
            'id': item.get('_id', 'N/A'),
            "title": item.get("title", "N/A"),
            "text": item.get("text", "N/A"),
            "subreddit": item.get("subreddit", "N/A"),
            "score": item.get("score", "N/A"),
            "url": item.get("url", "N/A"),
            "num_comments": item.get("num_comments", "N/A"),
            "created_at": item.get("created_at", "N/A"),
        })
    print(len(formatted_data))
    return JsonResponse(formatted_data, safe=False, json_dumps_params={'indent': 4})
    # print(data)
    # return JsonResponse(list(data), safe=False)


def get_reddit_comments_json(request):
    db = client['MigrationReportingToolDb']
    collection = db['reddit_comments']
    # return HttpResponse("hello reddit")
    data = list(collection.find())
    formatted_data = []
    for item in data:
        formatted_data.append({
            'created_at': item.get('created_at', 'N/A'),
            'keywords': item.get('keywords', []) if isinstance(item.get('keywords'), list) else [item.get('keywords', 'N/A')],
            'location': item.get('location', 'N/A'),
            'latitude': item.get('latitude', 'N/A'),
            'longitude': item.get('longitude', 'N/A'),
            'post_id': item.get('post_id', 'N/A'),
            'score': item.get('score', 'N/A'),
            'text': item.get('text', 'N/A'),
        })
    print(len(formatted_data))
    return JsonResponse(formatted_data, safe=False, json_dumps_params={'indent': 4})
    # print(data)
    # return JsonResponse(list(data), safe=False)


def get_reddit_posts(request):
    db = client['MigrationReportingToolDb']
    collection = db['reddit_posts']
    # return HttpResponse("hello reddit")


    try:
        data = list(collection.find())
        formatted_data = []
        for item in data:
            formatted_data.append({
                'id': item.get('_id', 'N/A'),
                'title': item.get('title', 'N/A'),
                'text': item.get('text', 'N/A'),
                'keywords': item.get('keywords', []) if isinstance(item.get('keywords'), list) else [item.get('keywords', 'N/A')],
                'subreddit': item.get('subreddit', 'N/A'),
                'score': item.get('score', 'N/A'),
                'url': item.get('url', 'N/A'),
                'num_comments': item.get('num_comments', 'N/A'),
                'created_at': item.get('created_at', 'N/A'),
                'location': item.get('location', 'N/A'),
                'latitude': item.get('latitude', 'N/A'),
                'longitude': item.get('longitude', 'N/A'),
            })
        return formatted_data
    except Exception as e:
        print(e)
        return []

def clean_value(value):
    if value is None or value.strip() == "":
        return 'Unknown'
    return value.replace('"', "'")


def escape_special_characters(value):
    if value is None or value.strip() == "":
        return 'Unknown'
    value = value.replace("\\", "\\\\")
    value = value.replace('"', '\\"')
    value = value.replace("'", "\\'")
    value = value.replace("\n", "\\n").replace("\r", "\\r")
    return value


def format_datetime(date):
    try:
        return date.strftime("%Y-%m-%dT%H:%M:%S") 
    except ValueError:
        return "N/A"


def map_posts_to_ontology(data):
    mapped_data = []

    base_uri = "http://www.semanticweb.org/anton/ontologies/2025/0/mirt_ont#"

    for post in data:
        cleaned_id = post['id']
        cleaned_title = escape_special_characters(clean_value(post['title']))
        cleaned_text = escape_special_characters(clean_value(post['text']))
        cleaned_subreddit = escape_special_characters(clean_value(post['subreddit']))
        cleaned_score = post['score']
        cleaned_keywords = escape_special_characters(', '.join(post['keywords'])) if isinstance(post['keywords'], list) else escape_special_characters(post['keywords'])
        cleaned_url = escape_special_characters(clean_value(post['url']))
        cleaned_num_comments = post['num_comments']
        cleaned_created_at = format_datetime(post['created_at'])
        cleaned_location = escape_special_characters(post['location'])
        cleaned_latitude = post['latitude']
        cleaned_longitude = post['longitude']

        insert_query = f"""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX mirt: <{base_uri}>
            PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

            INSERT DATA {{
                <{cleaned_url}> rdf:type mirt:Post ;
                    mirt:hasId "{cleaned_id}" ;
                    mirt:hasTitle "{cleaned_title}" ;
                    mirt:hasText "{cleaned_text}" ;
                    mirt:hasSubreddit "{cleaned_subreddit}" ;
                    mirt:hasScore "{cleaned_score}" ;
                    mirt:hasUrl "{cleaned_url}" ;
                    mirt:hasNumComments "{cleaned_num_comments}" ;
                    mirt:hasLocation "{cleaned_location}" ;
                    geo:lat "{cleaned_latitude}" ;
                    geo:long "{cleaned_longitude}" ;
                    mirt:hasCreatedAt "{cleaned_created_at}" .
            }}
        """
        mapped_data.append(insert_query)

    return mapped_data


def insert_data_to_fuseki(queries):
    sparql = SPARQLWrapper("https://my-fuseki-server-27d8893374fe.herokuapp.com/posts-and-comments/update")
    sparql.setMethod("POST")
    sparql.setReturnFormat(JSON)

    for query in queries:
        sparql.setQuery(query)
        try:
            sparql.query()
        except Exception as e:
            print(f"Error inserting data into Fuseki: {str(e)}")


def get_and_insert_posts(request):
    reddit_posts = get_reddit_posts(request)
    mapped_data = map_posts_to_ontology(reddit_posts)
    insert_data_to_fuseki(mapped_data)

    return HttpResponse("Data inserted successfully", status=200)


def get_reddit_comments(request):
    db = client['MigrationReportingToolDb']
    collection = db['reddit_comments']
    # return HttpResponse("hello reddit")
    try:
        data = list(collection.find())
        formatted_data = []
        for item in data:
            formatted_data.append({
                'id': item.get('_id', 'N/A'),
                'created_at': item.get('created_at', 'N/A'),
                'keywords': item.get('keywords', []) if isinstance(item.get('keywords'), list) else [item.get('keywords', 'N/A')],
                'location': item.get('location', 'N/A'),
                'latitude': item.get('latitude', 'N/A'),
                'longitude': item.get('longitude', 'N/A'),
                'post_id': item.get('post_id', 'N/A'),
                'score': item.get('score', 'N/A'),
                'text': item.get('text', 'N/A'),
            })
        return formatted_data
    except Exception as e:
        print(e)
        return []
    

def map_comments_to_ontology(data):
    mapped_data = []
    base_uri = "http://www.semanticweb.org/anton/ontologies/2025/0/mirt_ont#"

    for comment in data:
        cleaned_id = comment['id']
        cleaned_post_id = comment['post_id']
        cleaned_text = escape_special_characters(clean_value(comment['text']))
        cleaned_keywords = escape_special_characters(', '.join(comment['keywords'])) if isinstance(comment['keywords'], list) else escape_special_characters(comment['keywords'])
        cleaned_location = escape_special_characters(comment['location'])
        cleaned_latitude = comment['latitude']
        cleaned_longitude = comment['longitude']
        cleaned_score = comment['score']
        cleaned_created_at = format_datetime(comment['created_at'])

        insert_query = f"""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX mirt: <{base_uri}>
            PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

            INSERT DATA {{
                <{base_uri}/reddit/comment{cleaned_id}> rdf:type mirt:Comment ;
                    mirt:hasId "{cleaned_id}" ;
                    mirt:hasPostId "{cleaned_post_id}" ;
                    mirt:hasText "{cleaned_text}" ;
                    mirt:hasKeywords "{cleaned_keywords}" ;
                    mirt:hasLocation "{cleaned_location}" ;
                    geo:lat "{cleaned_latitude}" ;
                    geo:long "{cleaned_longitude}" ;
                    mirt:hasScore "{cleaned_score}" ;
                    mirt:hasCreatedAt "{cleaned_created_at}" .
            }}
        """
        mapped_data.append(insert_query)

    return mapped_data


def get_and_insert_comments(request):
    reddit_comments = get_reddit_comments(request)
    mapped_data = map_comments_to_ontology(reddit_comments)
    insert_data_to_fuseki(mapped_data)

    return HttpResponse("Data inserted successfully", status=200)