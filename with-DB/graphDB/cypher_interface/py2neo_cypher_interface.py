from common import craft_cypher_command
from py2neo import *
import inspect

graph = Graph()

def execute_py2neo(cypher_script_name, *args):
    cypher_command = craft_cypher_command(cypher_script_name, *args)
    return graph.cypher.execute(cypher_command)


# input -> (userID)
def is_userID_present(*args):
    script_name = inspect.currentframe().f_code.co_name + ".cql"
    output = execute_py2neo(script_name, *args)
    return output[0][0]

# input -> (movieID)
def is_movieID_present(*args):
    script_name = inspect.currentframe().f_code.co_name + ".cql"
    output = execute_py2neo(script_name, *args)
    return output[0][0]

# input -> NULL
def show_movies(*args):
    script_name = inspect.currentframe().f_code.co_name + ".cql"
    output = execute_py2neo(script_name, *args)
    return output

# input -> (userID)
def show_ratings(*args):
    script_name = inspect.currentframe().f_code.co_name + ".cql"
    output = execute_py2neo(script_name, *args)
    return output

# input -> (userID, movieID, rating)
def update_rating(*args):
    script_name = inspect.currentframe().f_code.co_name + ".cql"
    output = execute_py2neo(script_name, *args)
    return output

# input -> (userID)
def compute_average_user_rating(*args):
    script_name = inspect.currentframe().f_code.co_name + ".cql"
    output = execute_py2neo(script_name, *args)
    return output

# input -> (userID)
def compute_user_similarity(*args):
    script_name = inspect.currentframe().f_code.co_name + ".cql"
    output = execute_py2neo(script_name, *args)
    return output

# input -> (userID)
def get_recommendations_collaborative(*args):
    script_name = inspect.currentframe().f_code.co_name + ".cql"
    output = execute_py2neo(script_name, *args)
    return output

# input -> (userID)
def get_recommendations_collaborative_by_movieID(*args):
    script_name = inspect.currentframe().f_code.co_name + ".cql"
    output = execute_py2neo(script_name, *args)
    return output

# input -> NULL
def compute_average_movie_rating(*args):
    script_name = inspect.currentframe().f_code.co_name + ".cql"
    output = execute_py2neo(script_name, *args)
    return output

# input -> (userID)
def get_recommendations_content(*args):
    script_name = inspect.currentframe().f_code.co_name + ".cql"
    output = execute_py2neo(script_name, *args)
    return output

# input -> NULL
def get_userID_list(*args):
    script_name = inspect.currentframe().f_code.co_name + ".cql"
    output = execute_py2neo(script_name, *args)
    return output
