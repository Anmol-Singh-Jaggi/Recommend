from include.cypher_interface import *

def main():
    userID = raw_input("Enter your User ID: ")
    if not is_userID_present(userID):
        print "userID not found!!"
        return -1
    
    menu = "\n1. Get recommendations\n2. List all the movies\n3. List the movies you have rated\n4. Update rating\n"
    while True:
        option = int(raw_input(menu))
        if option is 1:
            print get_recommendations(userID)
        elif option is 2:
            print show_movies()
        elif option is 3:
            print show_ratings(userID)
        elif option is 4:
            movieID = raw_input("Enter the ID of the movie: ")
            if not is_movieID_present(movieID):
                print "Movie not found!!"
                continue
            rating = raw_input("Enter new rating [1-10]: ")
            if not (int(rating) > 0 and int(rating) < 11):
                print "Invalid rating!!"
                continue
            print update_rating(userID, movieID, rating)
        else:
            print "Invalid option!!"
            return -1

if __name__ == '__main__':
    main()
