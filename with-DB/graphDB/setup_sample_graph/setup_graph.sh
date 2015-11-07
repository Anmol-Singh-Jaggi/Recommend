source ../paths.py

echo
echo "-----Generating new dataset-----"
echo
cd dataset_generation
./generate_dataset.sh
cd ..

echo
echo "-----Stopping Neo4j-----"
echo
"$NEO4J_PATH/bin/neo4j" stop

echo
echo "-----Deleting old graph.db-----"
echo
rm -r "$NEO4J_PATH/data/graph.db"

echo
echo "-----Importing new dataset-----"
echo
"$NEO4J_PATH/bin/neo4j-import" --into "$NEO4J_PATH/data/graph.db" --nodes:Movie dataset_generation/csv/movies.csv --nodes:User dataset_generation/csv/users.csv --relationships:RATED dataset_generation/csv/ratings.csv

echo
echo "-----Starting Neo4j server-----"
echo
"$NEO4J_PATH/bin/neo4j" start

echo
echo "-----Adding uniqueness constraints-----"
echo
"$NEO4J_PATH/bin/neo4j-shell" -file "$CYPHER_SCRIPTS_PATH/add_constraint_userID.cql"
"$NEO4J_PATH/bin/neo4j-shell" -file "$CYPHER_SCRIPTS_PATH/add_constraint_movieID.cql"
