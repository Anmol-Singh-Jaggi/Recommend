from django.shortcuts import render
from django.http import HttpResponse

import sys
sys.path.append('../../cypher_interface')
import py2neo_cypher_interface as pci

def index(request):
    usage = []
    usage.append(["/get_reco/?userid=<int>", "Get recommendations for the given userID"])
    usage.append(["/view_ratings/?userid=<int>", "Get the list of movies rated by the given userID"])
    usage.append(["/update_rating/?userid=<int>&movieid=<int>&rating=<int>", "Update rating for movieID by the given userID"])
    usage.append(["/list_movies", "List all the movies present in the database"])
    
    response_dict = {}
    response_dict["title"] = "Welcome to the NeoRec Recommendation System!!"
    response_dict["table_caption"] = "Usage"
    response_dict["table_headers"] = ["Query string", "Action"]
    response_dict["table_rows"] = usage
    
    return render(request, "render_table.html", response_dict)

def get_recommendations(request):
    userID = request.GET.get("userid")
    if not (userID and pci.is_userID_present(userID)):
        return HttpResponse("<b>Error:</b> UserID '" + str(userID) + "' not found")
    
    pci.compute_average_rating(userID)
    pci.compute_similarity(userID)
    query_result = pci.get_recommendations(userID)
    
    response_dict = {}
    response_dict["title"] = "View recommendations"
    response_dict["table_caption"] = "Recommendations for userID '" + str(userID) + "'"
    response_dict["table_headers"] = query_result.columns
    response_dict["table_rows"] = query_result
    
    return render(request, "render_table.html", response_dict)

def view_ratings(request):
    userID = request.GET.get("userid")
    if not (userID and pci.is_userID_present(userID)):
        return HttpResponse("<b>Error:</b> UserID '" + str(userID) + "' not found")

    query_result = pci.show_ratings(userID)

    response_dict = {}
    response_dict["title"] = "View ratings"
    response_dict["table_caption"] = "Ratings of userID '" + str(userID) + "'"
    response_dict["table_headers"] = query_result.columns
    response_dict["table_rows"] = query_result
    
    return render(request, "render_table.html", response_dict)

def update_rating(request):
    userID = request.GET.get("userid")
    if not (userID and pci.is_userID_present(userID)):
        return HttpResponse("<b>Error:</b> UserID '" + str(userID) + "' not found")
    
    movieID = request.GET.get("movieid")
    if not(movieID and pci.is_movieID_present(movieID)):
        return HttpResponse("<b>Error:</b> MovieID '" + str(movieID) + "' not found")
    
    rating = request.GET.get("rating")
    if not (int(rating) >=1 and int(rating) <= 5):
        return HttpResponse("<b>Error:</b> Invalid rating value '" + str(rating) + "'")
    
    query_result = pci.update_rating(userID, movieID, rating)
    
    return HttpResponse("Rating updated!!")

def list_movies(request):
    query_result = pci.show_movies()

    response_dict = {}
    response_dict["title"] = "List of movies"
    response_dict["table_caption"] = "List of movies"
    response_dict["table_headers"] = query_result.columns
    response_dict["table_rows"] = query_result
    
    return render(request, "render_table.html", response_dict)

