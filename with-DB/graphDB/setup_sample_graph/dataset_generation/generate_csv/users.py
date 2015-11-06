#/usr/bin/python2
from dataset_size import user_count

def generate_user_id(index):
    ret = str(index)
    return ret

def main():
    print "userID:ID(User)"
    for i in xrange(user_count):
        node = generate_user_id(i+1)
        print node

if __name__ == '__main__':
    main()
