import subprocess
from common import *
NEO4J_SHELL_PATH = NEO4J_PATH + "/bin/neo4j-shell"

def execute_neo4j_shell(cypher_script_name, *args):
    cypher_command = craft_cypher_command(cypher_script_name, *args)
    return subprocess.check_output([NEO4J_SHELL_PATH, "-c", cypher_command])


# input -> (userID)
def is_userID_present(*args):
    script_name = "is_userID_present.cql"
    output = execute_neo4j_shell(script_name, *args)
    ret = output.splitlines()[3][2] is '0'
    return not ret

# input -> (movieID)
def is_movieID_present(*args):
    script_name = "is_movieID_present.cql"
    output = execute_neo4j_shell(script_name, *args)
    ret = output.splitlines()[3][2] is '0'
    return not ret

# input -> NULL
def show_movies(*args):
    script_name = "show_movies.cql"
    output = execute_neo4j_shell(script_name, *args)
    return output

# input -> (userID)
def show_ratings(*args):
    script_name = "show_ratings.cql"
    output = execute_neo4j_shell(script_name, *args)
    return output

# input -> (userID, movieID, rating)
def update_rating(*args):
    script_name = "update_rating.cql"
    output = execute_neo4j_shell(script_name, *args)
    return output

# input -> (userID)
def compute_similarity(*args):
    script_name = "compute_similarity.cql"
    output = execute_neo4j_shell(script_name, *args)
    return output

# input -> (userID)
def get_recommendations(*args):
    compute_similarity(*args)
    script_name = "get_recommendations.cql"
    output = execute_neo4j_shell(script_name, *args)
    return output

