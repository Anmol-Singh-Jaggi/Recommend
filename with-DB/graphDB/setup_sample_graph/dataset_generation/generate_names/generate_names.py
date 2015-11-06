first_names_file = open("names/first-names.txt")
last_names_file = open("names/last-names.txt")

first_names = [first_name.strip() for first_name in first_names_file]
last_names = [last_name.strip() for last_name in last_names_file]
full_names = []

for first_name in first_names:
    for last_name in last_names:
        full_name = first_name.strip() + " " + last_name.strip()
        print full_name
