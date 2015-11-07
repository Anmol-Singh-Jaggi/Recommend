#/usr/bin/python2
import users
import movies
from dataset_size import *
import sys
import random

def main():
    print ":START_ID(User),rating:int,:END_ID(Movie)"
    progress = 0
    for i in xrange(user_count):
        for j in xrange(movie_count):
            has_rated = bool(random.getrandbits(1))
            if has_rated is True:
                rating = random.randint(1,10)
                assert(rating >= 1 and rating <= 10)
                node = users.generate_user_id(i+1) + "," + str(rating) + "," + movies.generate_movie_id(j+1)
                print node
        
        # Generating progress status
        if ((i+1)*100.0)/user_count - progress >= 1:
            progress = ((i+1)*100.0)/user_count
            print >>sys.stderr,"\r" + str(progress) + "%",
    print >>sys.stderr,""

if __name__ == '__main__':
    main()
