import sys
sys.path.append('../include')
from common import craft_cypher_command

from py2neo import *

# input -> (userID)
def is_userID_present(*args):
    graph = Graph()
    script_name = "is_userID_present.cql"
    query = craft_cypher_command(script_name, *args)
    query_result = graph.cypher.execute(query)
    return bool(query_result[0][0])

# input -> (movieID)
def is_movieID_present(*args):
    graph = Graph()
    script_name = "is_movieID_present.cql"
    query = craft_cypher_command(script_name, *args)
    query_result = graph.cypher.execute(query)
    return bool(query_result[0][0])

