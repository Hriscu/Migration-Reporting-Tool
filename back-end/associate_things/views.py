from django.shortcuts import render
from SPARQLWrapper import SPARQLWrapper, JSON
from django.http import JsonResponse

BASE_URI = "http://www.semanticweb.org/anton/ontologies/2025/0/mirt_ont#"

def get_posts_from_fuseki(request):
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

    SELECT ?post ?id ?title ?text ?url ?subreddit ?score ?num_comments ?created_at WHERE {{
        ?post rdf:type mirt_ont:Post ;
              mirt_ont:hasId ?id ;
              mirt_ont:hasTitle ?title ;
              mirt_ont:hasText ?text ;
              mirt_ont:hasUrl ?url ;
              mirt_ont:hasSubreddit ?subreddit ;
              mirt_ont:hasScore ?score ;
              mirt_ont:hasNumComments ?num_comments ;
              mirt_ont:hasCreatedAt ?created_at .
    }}
    """

    sparql.setQuery(query)
    results = sparql.query().convert()

    posts = []
    for result in results["results"]["bindings"]:
        posts.append({
            "uri": result["post"]["value"],
            "id": result["id"]["value"],
            "title": result["title"]["value"],
            "text": result["text"]["value"],
            "url": result["url"]["value"],
            "subreddit": result["subreddit"]["value"],
            "score": result["score"]["value"],
            "num_comments": result["num_comments"]["value"],
            "created_at": result["created_at"]["value"]
        })

    return posts


def get_comments_from_fuseki(request):
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

    SELECT ?comment ?id ?text ?score ?created_at ?post_id ?location ?lat ?long WHERE {{
        ?comment rdf:type mirt_ont:Comment ;
                 mirt_ont:hasId ?id ;
                 mirt_ont:hasText ?text ;
                 mirt_ont:hasScore ?score ;
                 mirt_ont:hasCreatedAt ?created_at ;
                 mirt_ont:hasPostId ?post_id ;
                 mirt_ont:hasLocation ?location .
        OPTIONAL {{ ?comment geo:lat ?lat . }}
        OPTIONAL {{ ?comment geo:long ?long . }}
    }}
    """

    sparql.setQuery(query)
    results = sparql.query().convert()

    comments = []
    for result in results["results"]["bindings"]:
        comments.append({
            "uri": result["comment"]["value"],
            "id": result["id"]["value"],
            "text": result["text"]["value"],
            "score": result["score"]["value"],
            "created_at": result["created_at"]["value"],
            "post_id": result["post_id"]["value"],
            "location": result["location"]["value"],
            "lat": result.get("lat", {}).get("value", None),
            "long": result.get("long", {}).get("value", None),
        })
    
    return comments


def get_birds_from_fuseki(request):
    sparql = SPARQLWrapper("https://my-fuseki-server-27d8893374fe.herokuapp.com/birds-and-locations/query")
    sparql.setReturnFormat(JSON)

    query = f"""
    PREFIX owl:      <http://www.w3.org/2002/07/owl#>
    PREFIX rdf:      <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs:     <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xml:      <http://www.w3.org/XML/1998/namespace>
    PREFIX xsd:      <http://www.w3.org/2001/XMLSchema#>

    PREFIX mirt_ont: <{BASE_URI}>
    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

    SELECT ?bird ?label ?description ?family ?genus ?scientific_name ?species ?thumbnail ?url WHERE {{
        ?bird rdf:type mirt_ont:Bird ;
              rdfs:label ?label ;
              mirt_ont:hasDescription ?description ;
              mirt_ont:hasFamily ?family ;
              mirt_ont:hasGenus ?genus ;
              mirt_ont:hasScientificName ?scientific_name ;
              mirt_ont:hasSpecies ?species ;
              mirt_ont:hasThumbnail ?thumbnail ;
              mirt_ont:hasUrl ?url .
    }}
    """

    sparql.setQuery(query)
    results = sparql.query().convert()

    birds = []
    for result in results["results"]["bindings"]:
        birds.append({
            "uri": result["bird"]["value"],
            "label": result["label"]["value"],
            "description": result["description"]["value"],
            "family": result["family"]["value"],
            "genus": result["genus"]["value"],
            "scientific_name": result["scientific_name"]["value"],
            "species": result["species"]["value"],
            "thumbnail": result["thumbnail"]["value"],
            "url": result["url"]["value"]
        })

    return birds


def get_locations_from_fuseki(request):
    sparql = SPARQLWrapper("https://my-fuseki-server-27d8893374fe.herokuapp.com/birds-and-locations/query")
    sparql.setReturnFormat(JSON)

    query = f"""
    PREFIX owl:      <http://www.w3.org/2002/07/owl#>
    PREFIX rdf:      <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs:     <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xml:      <http://www.w3.org/XML/1998/namespace>
    PREFIX xsd:      <http://www.w3.org/2001/XMLSchema#>

    PREFIX mirt_ont: <{BASE_URI}>
    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

    SELECT ?location ?label ?description ?lat ?long WHERE {{
        ?location rdf:type mirt_ont:Location ;
                  rdfs:label ?label ;
                  mirt_ont:hasDescription ?description .
        OPTIONAL {{ ?location geo:lat ?lat . }}
        OPTIONAL {{ ?location geo:long ?long . }}
    }}
    """

    sparql.setQuery(query)
    results = sparql.query().convert()

    locations = []
    for result in results["results"]["bindings"]:
        locations.append({
            "uri": result["location"]["value"],
            "label": result["label"]["value"],
            "description": result["description"]["value"],
            "lat": result.get("lat", {}).get("value", None),
            "long": result.get("long", {}).get("value", None)
        })

    return locations


def get_posts_view(request):
    posts = get_posts_from_fuseki(request)
    return JsonResponse(posts, safe=False, json_dumps_params={'indent': 4})


def get_comments_view(request):
    comments = get_comments_from_fuseki(request)
    return JsonResponse(comments, safe=False, json_dumps_params={'indent': 4})


def get_birds_view(request):
    birds = get_birds_from_fuseki(request)
    return JsonResponse(birds, safe=False, json_dumps_params={'indent': 4})


def get_locations_view(request):
    locations = get_locations_from_fuseki(request)
    return JsonResponse(locations, safe=False, json_dumps_params={'indent': 4})

