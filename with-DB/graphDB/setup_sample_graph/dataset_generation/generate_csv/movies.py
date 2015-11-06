#/usr/bin/python2
from dataset_size import movie_count

def generate_movie_id(index):
    ret = str(index)
    return ret

def main():
    print "movieID:ID(Movie)"
    for i in xrange(movie_count):
        node = generate_movie_id(i+1)
        print node

if __name__ == '__main__':
    main()
