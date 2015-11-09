import sys
sys.path.append('../..')
from paths import *

def craft_cypher_command(cypher_script_name, *args):
    cypher_script_path = CYPHER_SCRIPTS_PATH + cypher_script_name
    cypher_script = open(cypher_script_path).read()
    arg_index = 1
    for arg in args:
        cypher_script = cypher_script.replace("?" + str(arg_index), arg)
        arg_index += 1
    return cypher_script

