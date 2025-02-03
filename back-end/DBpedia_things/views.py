from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from SPARQLWrapper import SPARQLWrapper, JSON, XML
from rdflib import Graph
from pyshacl import validate
import os

def get_bird_info_json(request):
    sparql = SPARQLWrapper("https://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    sparql.setQuery("""
        SELECT ?bird ?label ?abstract ?scientificName ?family ?species ?genus ?thumbnail ?url WHERE {
            ?bird rdf:type dbo:Bird ;
                rdfs:label ?label ;
                dbo:abstract ?abstract .
            
            OPTIONAL { ?bird dbp:scientificName ?scientificName . }
            OPTIONAL { ?bird dbp:family ?family . }
            OPTIONAL { ?bird dbp:species ?species . }
            OPTIONAL { ?bird dbp:genus ?genus . }
            OPTIONAL { ?bird dbo:thumbnail ?thumbnail . }
            OPTIONAL { ?bird dbp:url ?url . }
            
            FILTER (lang(?label) = "en")
            FILTER (lang(?abstract) = "en")
        }
        LIMIT 5000
    """)

    try:
        results = sparql.query().convert()
        birds = []

        for result in results["results"]["bindings"]:
            birds.append({
                "uri": result["bird"]["value"],
                "name": result["label"]["value"],
                "description": result["abstract"]["value"],
                "scientific_name": result.get("scientificName", {}).get("value", "Unknown"),
                "family": result.get("family", {}).get("value", "Unknown"),
                "species": result.get("species", {}).get("value", "Unknown"),
                "genus": result.get("genus", {}).get("value", "Unknown"),
                "thumbnail": result.get("thumbnail", {}).get("value", None),
                "url": result.get("url", {}).get("value", None),
            })

        return JsonResponse(birds, safe=False, json_dumps_params={'indent': 4})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def get_bird_info_rdf(request):
    sparql = SPARQLWrapper("https://dbpedia.org/sparql")
    sparql.setReturnFormat("xml")

    sparql.setQuery("""
        CONSTRUCT {
            ?bird rdf:type dbo:Bird ;
                  rdfs:label ?label ;
                  dbo:abstract ?abstract ;
                  dbp:scientificName ?scientificName ;
                  dbp:family ?family ;
                  dbp:species ?species ;
                  dbp:genus ?genus ;
                  dbo:thumbnail ?thumbnail ;
                  dbp:url ?url .
        } WHERE {
            ?bird rdf:type dbo:Bird ;
                  rdfs:label ?label ;
                  dbo:abstract ?abstract .

            OPTIONAL { ?bird dbp:scientificName ?scientificName . }
            OPTIONAL { ?bird dbp:family ?family . }
            OPTIONAL { ?bird dbp:species ?species . }
            OPTIONAL { ?bird dbp:genus ?genus . }
            OPTIONAL { ?bird dbo:thumbnail ?thumbnail . }
            OPTIONAL { ?bird dbp:url ?url . }

            FILTER (lang(?label) = "en")
            FILTER (lang(?abstract) = "en")
        }
        LIMIT 5000
    """)

    try:
        results = sparql.query().response.read().decode('utf-8')  # citire ca șir de caractere

        g = Graph()
        g.parse(data=results, format="xml")

        formatted_rdf = g.serialize(format="pretty-xml")

        return HttpResponse(formatted_rdf, content_type="application/rdf+xml")

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)
    

def get_bird_info(request):
    sparql = SPARQLWrapper("https://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    sparql.setQuery("""
        SELECT ?bird ?label ?abstract ?scientificName ?family ?species ?genus ?thumbnail ?url WHERE {
            ?bird rdf:type dbo:Bird ;
                  rdfs:label ?label ;
                  dbo:abstract ?abstract .

            OPTIONAL { ?bird dbp:scientificName ?scientificName . }
            OPTIONAL { ?bird dbp:family ?family . }
            OPTIONAL { ?bird dbp:species ?species . }
            OPTIONAL { ?bird dbp:genus ?genus . }
            OPTIONAL { ?bird dbo:thumbnail ?thumbnail . }
            OPTIONAL { ?bird dbp:url ?url . }

            FILTER (lang(?label) = "en")
            FILTER (lang(?abstract) = "en")
        }
        LIMIT 250
    """)

    try:
        results = sparql.query().convert()
        birds_data = []

        for result in results["results"]["bindings"]:
            bird = {
                "uri": result["bird"]["value"],
                "name": result["label"]["value"],
                "description": result["abstract"]["value"],
                "scientific_name": result.get("scientificName", {}).get("value", "Unknown"),
                "family": result.get("family", {}).get("value", "Unknown"),
                "species": result.get("species", {}).get("value", "Unknown"),
                "genus": result.get("genus", {}).get("value", "Unknown"),
                "thumbnail": result.get("thumbnail", {}).get("value", "Unknown"),
                "url": result.get("url", {}).get("value", "Unknown"),
            }
            birds_data.append(bird)

        return birds_data
    except Exception as e:
        print(f"Error fetching data from DBpedia: {str(e)}")
        return []


def validate_rdf(data):
    shacl_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shapes.ttl')

    # print("Validating RDF Data:\n", data)

    g = Graph()
    g.parse(data=data, format='turtle')

    

    g_shacl = Graph()
    g_shacl.parse(shacl_file, format='turtle')

    conforms, results_graph, results_text = validate(g, shacl_graph=shacl_file)

    if conforms:
        print("The data is valid according to the shape.")
        return True
    else:
        print("The data is not valid according to the shape.")
        return False



def clean_value(value):
    if value is None or value.strip() == "":
        return "Unknown"
    return value.replace('"', "'")


def escape_special_characters(value):
    if value is None:
        return "Unknown"
    value = value.replace("\\", "\\\\")
    value = value.replace('"', '\\"')
    value = value.replace("'", "\\'")
    value = value.replace("\n", "\\n").replace("\r", "\\r")
    return value


def map_bird_to_ontology(data):
    mapped_data = []

    base_uri = "http://www.semanticweb.org/anton/ontologies/2025/0/mirt_ont#"

    for bird in data:
        cleaned_species = escape_special_characters(clean_value(bird['species']))
        cleaned_scientific_name = escape_special_characters(clean_value(bird['scientific_name']))
        cleaned_family = escape_special_characters(clean_value(bird['family']))
        cleaned_genus = escape_special_characters(clean_value(bird['genus']))
        cleaned_thumbnail = escape_special_characters(clean_value(bird['thumbnail']))
        cleaned_url = escape_special_characters(clean_value(bird['url']))
        cleaned_description = escape_special_characters(clean_value(bird['description']))
        cleaned_name = escape_special_characters(clean_value(bird['name']))

        species_values = cleaned_species.split(",") if "," in cleaned_species else [cleaned_species]
        species_statements = " ".join(f'<{bird["uri"]}> mirt:hasSpecies "{species.strip()}" .' for species in species_values)

        insert_query = f"""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX mirt: <{base_uri}>

            INSERT DATA {{
                <{bird['uri']}> rdf:type mirt:Bird ;
                                mirt:hasScientificName "{cleaned_scientific_name}" ;
                                mirt:hasFamily "{cleaned_family}" ;
                                mirt:hasGenus "{cleaned_genus}" ;
                                mirt:hasThumbnail "{cleaned_thumbnail}" ;
                                mirt:hasUrl "{cleaned_url}" ;
                                mirt:hasDescription "{cleaned_description}" ;
                                rdfs:label "{cleaned_name}" .
                {species_statements}
            }}
        """
        mapped_data.append(insert_query)

    return mapped_data



def map_bird_to_ontology_v2(data):
    mapped_data = []

    base_uri = "http://www.semanticweb.org/anton/ontologies/2025/0/mirt_ont#"

    for bird in data:
        cleaned_species = escape_special_characters(clean_value(bird['species']))
        cleaned_scientific_name = escape_special_characters(clean_value(bird['scientific_name']))
        cleaned_family = escape_special_characters(clean_value(bird['family']))
        cleaned_genus = escape_special_characters(clean_value(bird['genus']))
        cleaned_thumbnail = escape_special_characters(clean_value(bird['thumbnail']))
        cleaned_url = escape_special_characters(clean_value(bird['url']))
        cleaned_description = escape_special_characters(clean_value(bird['description']))
        cleaned_name = escape_special_characters(clean_value(bird['name']))

        species_values = cleaned_species.split(",") if "," in cleaned_species else [cleaned_species]
        species_statements = " ".join(f'<{bird["uri"]}> mirt:hasSpecies "{species.strip()}" .' for species in species_values)

        rdf_data = f"""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX mirt: <{base_uri}>

            <{bird['uri']}> rdf:type mirt:Bird ;
                                mirt:hasScientificName "{cleaned_scientific_name}" ;
                                mirt:hasFamily "{cleaned_family}" ;
                                mirt:hasGenus "{cleaned_genus}" ;
                                mirt:hasThumbnail "{cleaned_thumbnail}" ;
                                mirt:hasUrl "{cleaned_url}" ;
                                mirt:hasDescription "{cleaned_description}" ;
                                rdfs:label "{cleaned_name}" .
        """

        rdf_data_fuseki = f"""
            <{bird['uri']}> rdf:type mirt:Bird ;
                                mirt:hasScientificName "{cleaned_scientific_name}" ;
                                mirt:hasFamily "{cleaned_family}" ;
                                mirt:hasGenus "{cleaned_genus}" ;
                                mirt:hasThumbnail "{cleaned_thumbnail}" ;
                                mirt:hasUrl "{cleaned_url}" ;
                                mirt:hasDescription "{cleaned_description}" ;
                                rdfs:label "{cleaned_name}" .
        """

        if validate_rdf(rdf_data):
            insert_query = f"""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX mirt: <{base_uri}>

                INSERT DATA {{
                    {rdf_data_fuseki}
                    {species_statements}
                }}
            """
            mapped_data.append(insert_query)

    return mapped_data


def insert_data_to_fuseki(queries):
    sparql = SPARQLWrapper("https://my-fuseki-server-27d8893374fe.herokuapp.com/birds-and-locations/update")
    sparql.setMethod("POST")
    sparql.setReturnFormat(JSON)

    for query in queries:
        sparql.setQuery(query)
        try:
            sparql.query()
        except Exception as e:
            print(f"Error inserting data into Fuseki: {str(e)}")


def insert_equivalence_to_fuseki():
    sparql = SPARQLWrapper("https://my-fuseki-server-27d8893374fe.herokuapp.com/birds-and-locations/update")
    sparql.setMethod("POST")
    sparql.setReturnFormat(JSON)

    insert_equivalence_query = """
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX mirt_ont: <http://www.semanticweb.org/anton/ontologies/2025/0/mirt_ont#>

        INSERT DATA {
            mirt_ont:Bird owl:equivalentClass dbo:Bird .
        }
    """

    sparql.setQuery(insert_equivalence_query)

    try:
        sparql.query()
        print("Equivalence inserted successfully")
    except Exception as e:
        print(f"Error inserting data into Fuseki: {str(e)}")


def get_and_insert_bird_data(request):
    insert_equivalence_to_fuseki()
    birds_data = get_bird_info(request)
    mapped_data = map_bird_to_ontology_v2(birds_data)
    insert_data_to_fuseki(mapped_data)

    return HttpResponse("Data inserted successfully", status=200)


# LOCATION


def get_location_info_json(request):
    sparql = SPARQLWrapper("https://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    sparql.setQuery("""
        SELECT ?place ?label ?abstract ?latitude ?longitude WHERE {
            ?place rdf:type dbo:Place ;
                rdfs:label ?label ;
                dbo:abstract ?abstract .
            
            OPTIONAL { ?place geo:lat ?latitude . }
            OPTIONAL { ?place geo:long ?longitude . }

            FILTER (lang(?label) = "en")
            FILTER (lang(?abstract) = "en")
        }
        LIMIT 5000
    """)

    try:
        results = sparql.query().convert()
        locations = []

        for result in results["results"]["bindings"]:
            latitude = result.get("latitude", {}).get("value", "Unknown")
            longitude = result.get("longitude", {}).get("value", "Unknown")


            if latitude != "Unknown":
                latitude = float(latitude)
            if longitude != "Unknown":
                longitude = float(longitude)

            locations.append({
                "uri": result["place"]["value"],
                "name": result["label"]["value"],
                "description": result["abstract"]["value"],
                "coordinates": {
                    "latitude": latitude,
                    "longitude": longitude
                }
            })

        return JsonResponse(locations, safe=False, json_dumps_params={'indent': 4})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def get_location_info(request):
    sparql = SPARQLWrapper("https://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    # sparql.setQuery("""
    #     SELECT ?place ?label ?abstract ?latitude ?longitude WHERE {
    #         ?place rdf:type dbo:Location ;
    #             rdfs:label ?label ;
    #             dbo:abstract ?abstract .

    #         OPTIONAL { ?place geo:lat ?latitude . }
    #         OPTIONAL { ?place geo:long ?longitude . }

    #         FILTER (lang(?label) = "en")
    #         FILTER (lang(?abstract) = "en")
    #     }
    #     LIMIT 50
    # """)

    sparql.setQuery("""
        SELECT ?place ?label ?abstract ?latitude ?longitude
        WHERE {
            ?place rdf:type ?type ;
                rdfs:label ?label ;
                dbo:abstract ?abstract ;
                geo:lat ?latitude ;
                geo:long ?longitude .

            FILTER (lang(?label) = "en")
            FILTER (lang(?abstract) = "en")

            FILTER (?type IN (dbo:City, dbo:Country, dbo:Region, dbo:Capital))

            FILTER (strlen(?abstract) > 200)  
        }
        ORDER BY DESC(strlen(?abstract))  
        LIMIT 250
    """)

    try:
        results = sparql.query().convert()
        locations = []

        for result in results["results"]["bindings"]:
            latitude = result.get("latitude", {}).get("value", "Unknown")
            longitude = result.get("longitude", {}).get("value", "Unknown")

            if latitude != "Unknown":
                latitude = float(latitude)
            if longitude != "Unknown":
                longitude = float(longitude)

            locations.append({
                "uri": result["place"]["value"],
                "name": result["label"]["value"],
                "description": result["abstract"]["value"],
                "coordinates": {
                    "latitude": latitude,
                    "longitude": longitude
                }
            })
        return locations
    except Exception as e:
        print(f"Error fetching data from DBpedia: {str(e)}")
        return []


def map_location_to_ontology(data):
    mapped_data = []

    base_uri = "http://www.semanticweb.org/anton/ontologies/2025/0/mirt_ont#"

    for location in data:
        cleaned_name = escape_special_characters(clean_value(location['name']))
        cleaned_description = escape_special_characters(clean_value(location['description']))

        latitude = location['coordinates'].get('latitude', "Unknown")
        longitude = location['coordinates'].get('longitude', "Unknown")

        insert_query = f"""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
            PREFIX mirt: <{base_uri}>

            INSERT DATA {{
                <{location['uri']}> rdf:type mirt:Location ;
                                        rdfs:label "{cleaned_name}" ;
                                        mirt:hasDescription "{cleaned_description}" ;
                                        geo:lat {latitude} ;
                                        geo:long {longitude} .
            }}
        """
        mapped_data.append(insert_query)

    return mapped_data


def map_location_to_ontology_v2(data):
    mapped_data = []

    base_uri = "http://www.semanticweb.org/anton/ontologies/2025/0/mirt_ont#"

    for location in data:
        cleaned_name = escape_special_characters(clean_value(location['name']))
        cleaned_description = escape_special_characters(clean_value(location['description']))

        latitude = location['coordinates'].get('latitude', "Unknown")
        longitude = location['coordinates'].get('longitude', "Unknown")

        rdf_data = f"""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
            PREFIX mirt: <{base_uri}>

            <{location['uri']}> rdf:type mirt:Location ;
                                        rdfs:label "{cleaned_name}" ;
                                        mirt:hasDescription "{cleaned_description}" ;
                                        geo:lat {latitude} ;
                                        geo:long {longitude} .
        """

        rdf_data_fuseki = f"""
            <{location['uri']}> rdf:type mirt:Location ;
                                        rdfs:label "{cleaned_name}" ;
                                        mirt:hasDescription "{cleaned_description}" ;
                                        geo:lat {latitude} ;
                                        geo:long {longitude} .
        """

        if validate_rdf(rdf_data):
            insert_query = f"""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
                PREFIX mirt: <{base_uri}>

                INSERT DATA {{
                    {rdf_data_fuseki}
                }}
            """
            mapped_data.append(insert_query)

    return mapped_data


def get_and_insert_location_data(request):
    locations_data = get_location_info(request)
    mapped_data = map_location_to_ontology_v2(locations_data)
    insert_data_to_fuseki(mapped_data)

    return HttpResponse("Data inserted successfully", status=200)