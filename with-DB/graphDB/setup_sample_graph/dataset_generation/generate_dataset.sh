source_path="generate_csv"
destination_path="csv"

mkdir -p "$destination_path"

source_file_names=("users" "movies" "ratings")
for i in "${source_file_names[@]}"
do
   python "$source_path/$i.py" > "$destination_path/$i.csv"
done
