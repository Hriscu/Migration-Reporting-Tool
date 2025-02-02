from django.shortcuts import render
from SPARQLWrapper import SPARQLWrapper, JSON
from django.http import JsonResponse
from fuzzywuzzy import fuzz
from django.views.decorators.cache import cache_page
from django.http import HttpResponse

BASE_URI = "http://www.semanticweb.org/anton/ontologies/2025/0/mirt_ont#"

def get_posts_from_fuseki():
    sparql = SPARQLWrapper("https://my-fuseki-server-27d8893374fe.herokuapp.com/posts-and-comments/query")
    sparql.setReturnFormat(JSON)

    query = f"""
    PREFIX owl:      <http://www.w3.org/2002/07/owl#>
    PREFIX rdf:      <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs:     <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xml:      <http://www.w3.org/XML/1998/namespace>
    PREFIX xsd:      <http://www.w3.org/2001/XMLSchema#>
    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

    PREFIX mirt_ont: <{BASE_URI}>

    SELECT ?post ?id ?title ?text ?url ?subreddit ?score ?num_comments ?created_at ?location ?latitude ?longitude WHERE {{
        ?post rdf:type mirt_ont:Post ;
              mirt_ont:hasId ?id ;
              mirt_ont:hasTitle ?title ;
              mirt_ont:hasText ?text ;
              mirt_ont:hasUrl ?url ;
              mirt_ont:hasSubreddit ?subreddit ;
              mirt_ont:hasScore ?score ;
              mirt_ont:hasNumComments ?num_comments ;
              mirt_ont:hasCreatedAt ?created_at ;
              mirt_ont:hasLocation ?location ;
              geo:lat ?latitude ;
              geo:long ?longitude .
    }}
    """

    sparql.setQuery(query)
    results = sparql.query().convert()

    posts = []
    for result in results["results"]["bindings"]:
        if result['location']['value'] != "Unknown":
            print(result['location']['value'])
            posts.append({
                'uri': result['post']['value'],
                'id': result['id']['value'],
                'title': result['title']['value'],
                'text': result['text']['value'],
                'url': result['url']['value'],
                'subreddit': result['subreddit']['value'],
                'score': result['score']['value'],
                'num_comments': result['num_comments']['value'],
                'created_at': result['created_at']['value'],
                'location': result['location']['value'],
                'latitude': result['latitude']['value'],
                'longitude': result['longitude']['value']
            })

    return posts


def get_comments_from_fuseki():
    sparql = SPARQLWrapper("https://my-fuseki-server-27d8893374fe.herokuapp.com/posts-and-comments/query")
    sparql.setReturnFormat(JSON)

    query = f"""
    PREFIX owl:      <http://www.w3.org/2002/07/owl#>
    PREFIX rdf:      <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs:     <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xml:      <http://www.w3.org/XML/1998/namespace>
    PREFIX xsd:      <http://www.w3.org/2001/XMLSchema#>

    PREFIX mirt_ont: <{BASE_URI}>
    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

    SELECT ?comment ?id ?text ?score ?created_at ?post_id ?location ?latitude ?longitude WHERE {{
        ?comment rdf:type mirt_ont:Comment ;
                 mirt_ont:hasId ?id ;
                 mirt_ont:hasText ?text ;
                 mirt_ont:hasScore ?score ;
                 mirt_ont:hasCreatedAt ?created_at ;
                 mirt_ont:hasPostId ?post_id ;
                 mirt_ont:hasLocation ?location ;
                 geo:lat ?latitude ;
                 geo:long ?longitude .
    }}
    """

    sparql.setQuery(query)
    results = sparql.query().convert()

    comments = []
    for result in results["results"]["bindings"]:
        if result['location']['value'] != "Unknown":
            comments.append({
                'uri': result['comment']['value'],
                'id': result['id']['value'],
                'text': result['text']['value'],
                'score': result['score']['value'],
                'created_at': result['created_at']['value'],
                'post_id': result['post_id']['value'],
                'location': result['location']['value'],
                'latitude': result['latitude']['value'],
                'longitude': result['longitude']['value']
            })
    
    return comments


def get_relations_for_posts(request):
    posts = get_posts_from_fuseki()

    sparql = SPARQLWrapper("https://my-fuseki-server-27d8893374fe.herokuapp.com/relations/query")
    sparql.setReturnFormat(JSON)

    relations_locations = []
    relations_birds = []

    for post in posts:
        post_uri = post['uri']

        query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX mirt_ont: <{BASE_URI}>
        PREFIX dbpedia: <http://dbpedia.org/resource/>

        SELECT ?post_uri ?location WHERE {{
            <{post_uri}> mirt_ont:hasLocation ?location .
        }}
        """
        sparql.setQuery(query)
        results = sparql.query().convert()

        for result in results["results"]["bindings"]:
            res = {
                'post_uri': post_uri,
                'location': result['location']['value']
            }
            # print(f'{res}\n\n')
            relations_locations.append(res)
        
        query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX mirt_ont: <{BASE_URI}>
        PREFIX dbpedia: <http://dbpedia.org/resource/>

        SELECT ?post_uri ?bird WHERE {{
            <{post_uri}> mirt_ont:hasBird ?bird .
        }}
        """
        sparql.setQuery(query)
        results = sparql.query().convert()

        for result in results["results"]["bindings"]:
            res = {
                'post_uri': post_uri,
                'bird': result['bird']['value']
            }
            # print(f'{res}\n\n')
            relations_birds.append(res)

    return posts, relations_locations, relations_birds


def get_relations_for_comments(request):
    comments = get_comments_from_fuseki()

    sparql = SPARQLWrapper("https://my-fuseki-server-27d8893374fe.herokuapp.com/relations/query")
    sparql.setReturnFormat(JSON)

    relations_locations = []
    relations_birds = []

    for comment in comments:
        comment_uri = comment['uri']

        query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX mirt_ont: <{BASE_URI}>
        PREFIX dbpedia: <http://dbpedia.org/resource/>

        SELECT ?post_uri ?location WHERE {{
            <{comment_uri}> mirt_ont:hasLocation ?location .
        }}
        """
        sparql.setQuery(query)
        results = sparql.query().convert()

        for result in results["results"]["bindings"]:
            res = {
                'comment_uri': comment_uri,
                'location': result['location']['value']
            }
            # print(f'{res}\n\n')
            relations_locations.append(res)
        
        query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX mirt_ont: <{BASE_URI}>
        PREFIX dbpedia: <http://dbpedia.org/resource/>

        SELECT ?post_uri ?bird WHERE {{
            <{comment_uri}> mirt_ont:hasBird ?bird .
        }}
        """
        sparql.setQuery(query)
        results = sparql.query().convert()

        for result in results["results"]["bindings"]:
            res = {
                'comment_uri': comment_uri,
                'bird': result['bird']['value']
            }
            # print(f'{res}\n\n')
            relations_birds.append(res)

    return comments, relations_locations, relations_birds

@cache_page(60 * 45)
def make_object_for_front(request):
    posts, posts_relations_locations, posts_relations_birds = get_relations_for_posts(request)
    comments, comments_relations_locations, comments_relations_birds = get_relations_for_comments(request)

    data_dict_posts =  {post['uri']: post for post in posts}
    data_dict_comments = {comment['uri']: comment for comment in comments}

    for relation in posts_relations_locations:
        uri = relation['post_uri']
        if uri in data_dict_posts:
            if 'locations' not in data_dict_posts[uri]:
                data_dict_posts[uri]['locations'] = []
            data_dict_posts[uri]['locations'].append(relation['location'])

    for relation in posts_relations_birds:
        uri = relation['post_uri']
        if uri in data_dict_posts:
            if 'birds' not in data_dict_posts[uri]:
                data_dict_posts[uri]['birds'] = []
            data_dict_posts[uri]['birds'].append(relation['bird'])

    for relation in comments_relations_locations:
        uri = relation['comment_uri']
        if uri in data_dict_comments:
            if 'locations' not in data_dict_comments[uri]:
                data_dict_comments[uri]['locations'] = []
            data_dict_comments[uri]['locations'].append(relation['location'])

    for relation in comments_relations_birds:
        uri = relation['comment_uri']
        if uri in data_dict_comments:
            if 'birds' not in data_dict_comments[uri]:
                data_dict_comments[uri]['birds'] = []
            data_dict_comments[uri]['birds'].append(relation['bird'])

    merged_data = {**data_dict_posts, **data_dict_comments}

    my_data = list(merged_data.values())

    return JsonResponse(my_data, safe=False, json_dumps_params={'indent': 4})
    # return my_data