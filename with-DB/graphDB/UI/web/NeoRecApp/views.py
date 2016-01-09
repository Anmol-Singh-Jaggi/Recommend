from django.shortcuts import render
from django.http import HttpResponse
from forms import *

import sys
sys.path.append('../../cypher_interface')
from py2neo_cypher_interface import execute_py2neo


def index(request):
    usage = []
    usage.append(
        ["Get recommendation for user ID: ", "get_reco", RecommendForm])
    usage.append(
        ["Get the list of movies rated by user ID: ", "view_ratings", UserIDForm])
    usage.append(
        ["Update rating for movie ID by user ID: ", "update_rating", UpdateRatingForm])
    usage.append(
        ["List all the movies present in the database: ", "list_movies", ""])

    response_dict = {}
    response_dict["title"] = "Welcome to the NeoRec Recommendation System!!"
    response_dict["table_caption"] = "Menu"
    response_dict["table_headers"] = ["Action", "Input"]
    response_dict["table_rows"] = usage

    return render(request, "index.html", response_dict)


def get_recommendations(request):
    userID = request.GET.get("userID")
    if not (userID and execute_py2neo("is_userID_present", userID)):
        return HttpResponse("<b>Error:</b> UserID '" + userID + "' not found")

    recoID = request.GET.get("recoID")
    if recoID == "1":
        execute_py2neo("compute_average_user_rating", userID)
        execute_py2neo("compute_user_similarity", userID)
        query_result = execute_py2neo(
            "get_recommendations_collaborative", userID)
    elif recoID == "2":
        execute_py2neo("compute_average_movie_rating")
        query_result = execute_py2neo("get_recommendations_content", userID)
    else:
        return HttpResponse("Invalid recoID!!")

    response_dict = {}
    response_dict["title"] = "View recommendations"
    response_dict[
        "table_caption"] = "Recommendations for userID '" + str(userID) + "'"
    response_dict["table_headers"] = query_result.columns
    response_dict["table_rows"] = query_result

    return render(request, "render_table.html", response_dict)


def view_ratings(request):
    userID = request.GET.get("userID")
    if not (userID and execute_py2neo("is_userID_present", userID)):
        return HttpResponse("<b>Error:</b> UserID '" + userID + "' not found")

    query_result = execute_py2neo("show_ratings", userID)

    response_dict = {}
    response_dict["title"] = "View ratings"
    response_dict["table_caption"] = "Ratings of userID '" + userID + "'"
    response_dict["table_headers"] = query_result.columns
    response_dict["table_rows"] = query_result

    return render(request, "render_table.html", response_dict)


def update_rating(request):
    userID = request.GET.get("userID")
    if not (userID and execute_py2neo("is_userID_present", userID)):
        return HttpResponse("<b>Error:</b> UserID '" + userID + "' not found")

    movieID = request.GET.get("movieID")
    if not(movieID and execute_py2neo("is_movieID_present", movieID)):
        return HttpResponse("<b>Error:</b> MovieID '" + movieID + "' not found")

    rating = request.GET.get("rating")
    if not (int(rating) >= 1 and int(rating) <= 5):
        return HttpResponse("<b>Error:</b> Invalid rating value '" + rating + "'")

    execute_py2neo("update_rating", userID, movieID, rating)

    return HttpResponse("Rating updated!!")


def list_movies(request):
    query_result = execute_py2neo("show_movies")

    response_dict = {}
    response_dict["title"] = "List of movies"
    response_dict["table_caption"] = "List of movies"
    response_dict["table_headers"] = query_result.columns
    response_dict["table_rows"] = query_result

    return render(request, "render_table.html", response_dict)
