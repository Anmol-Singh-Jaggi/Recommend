source_path="generate_csv"
destination_path="csv"

if [ -d "$destination_path" ]; then
    echo "The destination path '$destination_path/' already exists!!"
    echo "In case you want to recreate the csv dataset, delete that folder and run this script again."
    exit 0
fi

mkdir -p "$destination_path"

source_file_names=("users" "movies" "ratings")
for i in "${source_file_names[@]}"
do
   python "$source_path/$i.py" > "$destination_path/$i.csv"
done
