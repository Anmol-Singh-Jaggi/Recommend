from django.shortcuts import render
from django.http import HttpResponse

from cypher_interface import *

def index(request):
    graph = Graph()
    
    usage = []
    usage.append(["/get_reco?userid=<int>", "Get recommendations for the given userID"])
    usage.append(["/view_ratings?userid=<int>", "Get the list of movies rated by the given userID"])
    usage.append(["/update_rating?userid=<int>&movieid=<int>&rating=<int>", "Update rating for movieID by the given userID"])
    usage.append(["/list_movies", "List all the movies present in the database"])
    
    response_dict = {}
    response_dict["title"] = "Welcome to the NeoRec Recommendation System!!"
    response_dict["table_caption"] = "Usage"
    response_dict["table_headers"] = ["Query string", "Action"]
    response_dict["table_rows"] = usage
    
    return render(request, "render_table.html", response_dict)

def get_recommendations(request):
    userID = request.GET.get("userid")
    if not (userID and is_userID_present(userID)):
        return HttpResponse("<b>Error:</b> UserID '" + str(userID) + "' not found")
    
    graph = Graph()
    
    script_name = "compute_similarity.cql"
    query = craft_cypher_command(script_name, str(userID))
    query_result = graph.cypher.execute(query)
    
    script_name = "get_recommendations.cql"
    query = craft_cypher_command(script_name, str(userID))
    query_result = graph.cypher.execute(query)
    
    response_dict = {}
    response_dict["title"] = "View recommendations"
    response_dict["table_caption"] = "Recommendations for userID '" + str(userID) + "'"
    response_dict["table_headers"] = query_result.columns
    response_dict["table_rows"] = query_result
    
    return render(request, "render_table.html", response_dict)

def view_ratings(request):
    userID = request.GET.get("userid")
    if not (userID and is_userID_present(userID)):
        return HttpResponse("<b>Error:</b> UserID '" + str(userID) + "' not found")
    
    graph = Graph()
    
    script_name = "show_ratings.cql"
    query = craft_cypher_command(script_name, str(userID))
    query_result = graph.cypher.execute(query)

    response_dict = {}
    response_dict["title"] = "View ratings"
    response_dict["table_caption"] = "Ratings of userID '" + str(userID) + "'"
    response_dict["table_headers"] = query_result.columns
    response_dict["table_rows"] = query_result
    
    return render(request, "render_table.html", response_dict)

def update_rating(request):
    userID = request.GET.get("userid")
    if not (userID and is_userID_present(userID)):
        return HttpResponse("<b>Error:</b> UserID '" + str(userID) + "' not found")
    
    movieID = request.GET.get("movieid")
    if not(movieID and is_movieID_present(movieID)):
        return HttpResponse("<b>Error:</b> MovieID '" + str(movieID) + "' not found")
    
    rating = request.GET.get("rating")
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

    response_dict = {}
    response_dict["title"] = "List of movies"
    response_dict["table_caption"] = "List of movies"
    response_dict["table_headers"] = query_result.columns
    response_dict["table_rows"] = query_result
    
    return render(request, "render_table.html", response_dict)

