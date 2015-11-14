#/usr/bin/python2
import users
import movies
from dataset_size import *
import sys
import random

def main():
    print ":START_ID(User),rating:int,:END_ID(Movie)"
    progress = 0
    for i in xrange(USER_COUNT):
        for j in xrange(MOVIE_COUNT):
            has_rated = bool(random.getrandbits(1))
            if has_rated is True:
                rating = random.randint(RATING_MIN, RATING_MAX)
                assert(rating >= RATING_MIN and rating <= RATING_MAX)
                node = users.generate_user_id(i+1) + "," + str(rating) + "," + movies.generate_movie_id(j+1)
                print node
        
        # Generating progress status
        if ((i+1)*100.0)/USER_COUNT - progress >= 1:
            progress = ((i+1)*100.0)/USER_COUNT
            print >>sys.stderr,"\r" + str(progress) + "%",
    print >>sys.stderr,""

if __name__ == '__main__':
    main()
