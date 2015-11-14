import sys
sys.path.append('../cypher_interface')
from py2neo_cypher_interface import *

def main():
    output_file = open("predicted.csv", "w")
    userID_list = get_userID_list()
    for row in userID_list:
        userID = row[0]
        print userID
        predicted_ratings = get_recommendations_by_movieID(userID)
        for row2 in predicted_ratings:
            movieID = row2[0]
            rating = row2[1]
            print >> output_file, userID + "\t" + movieID + "\t" + str(rating)

if __name__ == "__main__":
    main()
