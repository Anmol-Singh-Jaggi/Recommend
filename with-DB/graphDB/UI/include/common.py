import subprocess
import sys
sys.path.append('../..')
from paths import *

NEO4J_SHELL_PATH = NEO4J_PATH + "/bin/neo4j-shell"

def craft_cypher_command(cypher_script_name, *args):
    cypher_script_path = CYPHER_SCRIPTS_PATH + cypher_script_name
    cypher_script = open(cypher_script_path).read()
    arg_index = 1
    for arg in args:
        cypher_script = cypher_script.replace("?" + str(arg_index), arg)
        arg_index += 1
    return cypher_script

def execute_neo4j_shell(cypher_script_name, *args):
    cypher_command = craft_cypher_command(cypher_script_name, *args)
    return subprocess.check_output([NEO4J_SHELL_PATH, "-c", cypher_command])
