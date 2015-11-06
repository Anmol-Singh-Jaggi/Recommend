mkdir -p csv
python ./generate_csv/users.py > csv/users.csv
python ./generate_csv/movies.py > csv/movies.csv
python ./generate_csv/ratings.py > csv/ratings.csv
