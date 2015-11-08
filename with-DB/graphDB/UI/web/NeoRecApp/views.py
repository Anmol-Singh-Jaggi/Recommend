from django.shortcuts import render
from django.http import HttpResponse

from cypher_interface import *

def index(request):
    graph = Graph()
    
    usage = []
    usage.append(["/get_reco", "/userID", "Get recommendations for the given userID"])
    usage.append(["/view_ratings", "/userID", "Get the list of movies rated by the given userID"])
    usage.append(["/update_rating", "/userID/movieID/rating", "Update rating for movieID by the given userID"])
    usage.append(["/list_movies", "", "List all the movies present in the database"])
    
    response_dict = {}
    response_dict["title"] = "Welcome to the NeoRec Recommendation Engine!!"
    response_dict["table_caption"] = "Usage"
    response_dict["table_headers"] = ["Option", "Parameters", "Comments"]
    response_dict["table_rows"] = usage
    
    return render(request, "render_table.html", response_dict)

def get_recommendations(request, userID):
    if not is_userID_present(userID):
        return HttpResponse("<b>Error:</b> UserID '" + str(userID) + "' not found")
    
    graph = Graph()
    
    script_name = "compute_similarity.cql"
    query = craft_cypher_command(script_name, str(userID))
    query_result = graph.cypher.execute(query)
    
    script_name = "get_recommendations.cql"
    query = craft_cypher_command(script_name, str(userID))
    query_result = graph.cypher.execute(query)
    
    query_result_parsed = []
    index = 1
    for record in query_result:
        record_parsed = [index, record[0], record[1]]
        query_result_parsed.append(record_parsed)
        index += 1

    response_dict = {}
    response_dict["title"] = "View recommendations"
    response_dict["table_caption"] = "Recommendations for userID '" + str(userID) + "'"
    response_dict["table_headers"] = ["S.No", "movieID", "Predicted rating"]
    response_dict["table_rows"] = query_result_parsed
    
    return render(request, "render_table.html", response_dict)

def view_ratings(request, userID):
    if not is_userID_present(userID):
        return HttpResponse("<b>Error:</b> UserID '" + str(userID) + "' not found")
    
    graph = Graph()
    
    script_name = "show_ratings.cql"
    query = craft_cypher_command(script_name, str(userID))
    query_result = graph.cypher.execute(query)
    
    query_result_parsed = []
    index = 1
    for record in query_result:
        record_parsed = [index, record[0], record[1]]
        query_result_parsed.append(record_parsed)
        index += 1

    response_dict = {}
    response_dict["title"] = "View ratings"
    response_dict["table_caption"] = "Ratings of userID '" + str(userID) + "'"
    response_dict["table_headers"] = ["S.No", "movieID", "Rating"]
    response_dict["table_rows"] = query_result_parsed
    
    return render(request, "render_table.html", response_dict)

def update_rating(request, userID, movieID, rating):
    if not is_userID_present(userID):
        return HttpResponse("<b>Error:</b> UserID '" + str(userID) + "' not found")
    if not is_movieID_present(movieID):
        return HttpResponse("<b>Error:</b> MovieID '" + str(movieID) + "' not found")
    if not (int(rating) >=1 and int(rating) <= 10):
        return HttpResponse("<b>Error:</b> Invalid rating value '" + str(rating) + "'")
    
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
    
    query_result_parsed = []
    index = 1
    for record in query_result:
        record_parsed = [index, record[0]]
        query_result_parsed.append(record_parsed)
        index += 1

    response_dict = {}
    response_dict["title"] = "List of movies"
    response_dict["table_caption"] = "List of movies"
    response_dict["table_headers"] = ["S.No", "movieID"]
    response_dict["table_rows"] = query_result_parsed
    
    return render(request, "render_table.html", response_dict)

