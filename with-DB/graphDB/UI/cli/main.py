from cypher_interface import *

def main():
    menu = "\n1. Get recommendations\n2. List all the movies\n3. List the movies rated\n4. Update rating\n"
    
    while True:
        option = int(raw_input(menu))
        
        if option is 1:
            userID = raw_input("Enter your user ID: ")
            if not is_userID_present(userID):
                print "userID not found!!"
                continue
            print get_recommendations(userID)
        
        elif option is 2:
            print show_movies()
        
        elif option is 3:
            userID = raw_input("Enter your user ID: ")
            if not is_userID_present(userID):
                print "userID not found!!"
                continue
            print show_ratings(userID)
        
        elif option is 4:
            userID = raw_input("Enter your user ID: ")
            if not is_userID_present(userID):
                print "userID not found!!"
                continue
            movieID = raw_input("Enter the movie ID: ")
            if not is_movieID_present(movieID):
                print "movieID not found!!"
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
