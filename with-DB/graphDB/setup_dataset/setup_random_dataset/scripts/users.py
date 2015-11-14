#/usr/bin/python2
from dataset_size import USER_COUNT

def generate_user_id(index):
    ret = str(index)
    return ret

def main():
    print "userID:ID(User)"
    for i in xrange(USER_COUNT):
        node = generate_user_id(i+1)
        print node

if __name__ == '__main__':
    main()
