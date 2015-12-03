import sys
sys.path.append('../cypher_interface')
from py2neo_cypher_interface import *
from timeit import default_timer as timer

def benchmark_collaborative():
    userID_list = get_userID_list()
    total_time_taken = 0
    for row in userID_list:
        userID = row[0]
        #print userID
        start = timer()
        get_recommendations_collaborative(userID)
        end = timer()
        total_time_taken += end - start
    
    return 1.0*total_time_taken/len(userID_list)

'''
def benchmark_content():
    userID_list = get_userID_list()
    total_time_taken = 0
    for row in userID_list:
        userID = row[0]
        #print userID
        start = timer()
        get_recommendations_content(userID)
        end = timer()
        total_time_taken += end - start
    
    return 1.0*total_time_taken/len(userID_list)
'''

def main():
    iterations = 5
    average_time_taken = 0.0
    
    for i in xrange(iterations):
        print "Iteration " + str(i+1) + "..."
        average_time_taken += benchmark_collaborative()
    average_time_taken /= iterations
    print "Collaborative = " + str(average_time_taken) + " s"

'''
    for i in xrange(iterations):
        average_time_taken += benchmark_content()
    average_time_taken /= iterations
    print "Content = " + str(average_time_taken) + " s"
'''

if __name__ == "__main__":
    main()
