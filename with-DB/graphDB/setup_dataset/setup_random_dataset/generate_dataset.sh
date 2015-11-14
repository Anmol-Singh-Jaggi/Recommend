mkdir -p csv
script_names=("users" "movies" "ratings")
for i in "${script_names[@]}"
do
   python "scripts/$i.py" > "csv/$i.csv"
done
