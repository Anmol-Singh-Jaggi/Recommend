import csv
from collections import OrderedDict

input_file_path = "../../../../dataset/u1.base"
output_path = "csv/"

def get_readings(file_path):
    readings = OrderedDict()
    
    file_handle = open(file_path)
    file_reader = csv.reader(file_handle, delimiter='\t')
    for line in file_reader:
        userID = line[0]
        movieID = line[1]
        rating = line[2]
    	readings.setdefault(userID, OrderedDict())[movieID] = rating
    
    return readings

def main():
    ratings_output_file = open(output_path + "ratings.csv", "w")
    header = ":START_ID(User),rating:int,:END_ID(Movie)"
    print >> ratings_output_file, header
    
    users_output_file = open(output_path + "users.csv", "w")
    header = "userID:ID(User)"
    print >> users_output_file, header
    
    movies_output_file = open(output_path + "movies.csv", "w")
    header = "movieID:ID(Movie)"
    print >> movies_output_file, header
    
    readings = get_readings(input_file_path)
    
    file_handle = open(input_file_path)
    userID_set = set()
    movieID_set = set()
    for userID, movieID_rating in readings.iteritems():
        userID_set.add(userID)         
        for movieID, rating in movieID_rating.iteritems():
            movieID_set.add(movieID)
            print >> ratings_output_file, userID + "," + rating + "," + movieID
    
    for userID in sorted(userID_set, key = int):
        print >> users_output_file, userID
        
    for movieID in sorted(movieID_set, key = int):
        print >> movies_output_file, movieID

if __name__ == "__main__":
    main()
    
