from django.shortcuts import render
from django.http import HttpResponse

from py2neo import *

import sys
sys.path.append('../include')
from common import craft_cypher_command

def index(request):
    response_string = ""
    response_string += "<b>Welcome to the NeoRec Recommendation Engine!</b><br><br>"
    response_string += "Usage-:<br><br>"
    response_string += "<i>/get_reco/<b>userID</b></i> : Get recommendations for the given userID<br>"
    response_string += "<i>/view_ratings/<b>userID</b></i> : Get the list of movies rated by the given userID<br>"
    response_string += "<i>/update_rating/<b>userID/movieID/rating</b></i> : Update rating for movieID by the given userID<br>"
    response_string += "<i>/list_movies</i> : List all the movies present in the database<br>"
    return HttpResponse(response_string)

def get_recommendation(request, userID):
    graph = Graph()
    
    script_name = "compute_similarity.cql"
    query = craft_cypher_command(script_name, str(userID))
    query_result = graph.cypher.execute(query)
    
    script_name = "get_recommendations.cql"
    query = craft_cypher_command(script_name, str(userID))
    query_result = graph.cypher.execute(query)
    
    response_string = "S.No., movieID, Predicted rating <br><br>"
    index = 1
    for record in query_result:
        response_string += str(index) + ", " + str(record[0]) + ", " + str(record[1]) + "<br>"
        index += 1
    
    return HttpResponse(response_string)

def view_ratings(request, userID):
    graph = Graph()
    
    script_name = "show_ratings.cql"
    query = craft_cypher_command(script_name, str(userID))
    query_result = graph.cypher.execute(query)
    
    response_string = "S.No., movieID, Rating <br><br>"
    index = 1
    for record in query_result:
        response_string += str(index) + ", " + str(record[0]) + ", " + str(record[1]) + "<br>"
        index += 1
    
    return HttpResponse(response_string)

def update_rating(request, userID, movieID, rating):
    graph = Graph()
    
    script_name = "update_rating.cql"
    query = craft_cypher_command(script_name, str(userID), str(movieID), str(rating))
    query_result = graph.cypher.execute(query)
    
    return HttpResponse("Rating updated!!")

def list_movies(request):
    graph = Graph()
    
    script_name = "show_movies.cql"
    query = craft_cypher_command(script_name)
    query_result = graph.cypher.execute(query)
    
    response_string = "S.No., movieID <br><br>"
    index = 1
    for record in query_result:
        response_string += str(index) + ", " + str(record[0]) + "<br>"
        index += 1
    
    return HttpResponse(response_string)
