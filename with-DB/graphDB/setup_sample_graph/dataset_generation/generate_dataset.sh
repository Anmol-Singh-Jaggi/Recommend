source_path="generate_csv"
destination_path="csv"

if [ -d "$destination_path" ]; then
    echo "The destination path '$destination_path/' already exists!!"
    echo "Delete it and run this script again to recreate it."
    exit 0
fi

mkdir -p "$destination_path"

source_file_names=("users" "movies" "ratings")
for i in "${source_file_names[@]}"
do
   python "$source_path/$i.py" > "$destination_path/$i.csv"
done
