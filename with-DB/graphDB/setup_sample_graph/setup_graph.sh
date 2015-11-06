echo
echo "-----Generating new dataset-----"
echo
cd dataset_generation
./generate_dataset.sh
cd ..

echo
echo "-----Stopping Neo4j-----"
echo
../neo4j/bin/neo4j stop

echo
echo "-----Deleting old graph.db-----"
echo
rm -r ../neo4j/data/graph.db

echo
echo "-----Importing new dataset-----"
echo
../neo4j/bin/neo4j-import --into ../neo4j/data/graph.db --nodes:Movie dataset_generation/csv/movies.csv --nodes:User dataset_generation/csv/users.csv --relationships:RATED dataset_generation/csv/ratings.csv

echo
echo "-----Starting Neo4j server-----"
echo
../neo4j/bin/neo4j start
