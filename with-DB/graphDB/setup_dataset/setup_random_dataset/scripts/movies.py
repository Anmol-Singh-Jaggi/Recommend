#/usr/bin/python2
from dataset_size import MOVIE_COUNT

def generate_movie_id(index):
    ret = str(index)
    return ret

def main():
    print "movieID:ID(Movie)"
    for i in xrange(MOVIE_COUNT):
        node = generate_movie_id(i+1)
        print node

if __name__ == '__main__':
    main()
