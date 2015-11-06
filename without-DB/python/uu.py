import scipy as sp
import time
import pickle
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import math
from collections import defaultdict

f = open("/home/goel/rec/data/u1.base",'r')
  
user_train = {}
user_mean = {}
user_ratings = {}

simy = {}
n_all = {}

def init_user_train():
    for line in f:
        # token = [int(n) for n in line.split()
        token = line.split()
        
        if token[0] not in user_train:
            user_train.setdefault(token[0],{})
            user_mean.setdefault(token[0],float(0))
            user_ratings.setdefault(token[0],0)

        user_train[token[0]].update({token[1]:float(token[2])})
        user_ratings[token[0]] += 1
        user_mean[token[0]] += float(token[2])

    for key in user_mean: 
        user_mean[key] = user_mean[key]/user_ratings[key]


def compute_sim():
    # store = open('/home/goel/rec/simy_dump.txt','a')

    for u in user_train:
        for v in user_train:
            num = 0.0
            norm_u = 0.0
            norm_v = 0.0
            if u not in simy:
                    simy.setdefault(u,{})
            if(u!=v):
                for x in user_train[u]:
                    if x in user_train[v]:
                        r_u = user_train[u][x]-user_mean[u]
                        r_v = user_train[v][x]-user_mean[v]
                        # print str(r_u) + "  " + str(r_v)
                        num += r_u * r_v
                        norm_u += math.fabs(r_u*r_u)
                        norm_v += math.fabs(r_v*r_v)

                norm_u = math.sqrt(norm_u)
                norm_v = math.sqrt(norm_v)
                ans = (num+1)/(norm_u*norm_v+1)
                # if ans>1.01 or ans<-1.01:
                #     print u + " & " + v + " : " + str(ans)
                simy[u].update( {v : (num+1)/(norm_u*norm_v+1)} )
            
            else:
                simy[u].update({v:float(1)})
            # store.write(u+'\t'+v+'\t'+str(simy[u][v])+'\n')



def find_neighbors(n_size):
    
    for u in user_train:
        n_all.setdefault(u,{})
        minm = 1.1
        vert = u
        for v in simy[u]:
            if len(n_all[u]) < n_size:
                if minm>simy[u][v]:
                    minm = simy[u][v]
                    vert = v
                n_all[u].update({v:float(simy[u][v])})

            else:
                if minm<simy[u][v]:
                    minm = simy[u][v]
                    del n_all[u][vert]
                    vert = v
                    n_all[u].update({v:float(simy[u][v])})

n_size = 1000

def predict():
    f1 = open("/home/goel/rec/data/u1.test",'r')
    f2 = open("/home/goel/rec/uu_pred." +str(n_size) ,'w')
    for line in f1:
        token = line.split()
        pred = 0.0
        norm = 0.0
        for v in n_all[token[0]]:
            if token[1] in user_train[v]:
                rating = user_train[v][token[1]] - user_mean[v]
                sim = simy[token[0]][v]
                pred += rating*sim
                # print pred
                norm += abs(sim)
        ans =  user_mean[token[0]] + (pred+1)/(norm+1)
        if ans>5:
            ans = 5
        if ans<1:
            ans = 1 
        f2.write(token[0]+'\t'+token[1]+'\t'+token[2]+'\t'+str(ans)+'\n')
    f1.close()
    f2.close() 


def print_user_train():
    for key in user_train:
        print key + ' : ' + str(user_train[key])
        time.sleep(3)

def get_user_mean(user):
    return user_mean[user]

def get_user_ratings(user):
    return user_ratings[user];
        
def get_uu_sim(u,v):
    return simy[u][v]

init_user_train()
# print user_train['4']
# print user_train['4']['11']
# n_size = input("Enter the max neighbourhood size")
compute_sim()
find_neighbors(n_size)
predict()

f.close()
