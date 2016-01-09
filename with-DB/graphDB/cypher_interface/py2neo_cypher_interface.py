import sys
from os.path import dirname, realpath
sys.path.append(dirname(dirname(realpath(__file__))))
from paths import CYPHER_SCRIPTS_PATH

from py2neo import Graph


def craft_cypher_command(cypher_script_name, *args):
    cypher_script_path = CYPHER_SCRIPTS_PATH + cypher_script_name
    cypher_script = open(cypher_script_path).read()
    arg_index = 1
    for arg in args:
        cypher_script = cypher_script.replace("?" + str(arg_index), str(arg))
        arg_index += 1
    return cypher_script


graph = Graph()


def execute_py2neo(cypher_script_name, *args):
    cypher_command = craft_cypher_command(cypher_script_name + ".cql", *args)
    ret = graph.cypher.execute(cypher_command)
    if cypher_script_name in ["is_userID_present", "is_movieID_present"]:
        ret = ret[0][0]
    return ret
