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
  
item_train = {}
item_mean = {}
item_ratings = {}
simy = {}
n_all = {}

def init_item_train():
    for line in f:
        # token = [int(n) for n in line.split()]
        token = line.split()

        if token[1] not in item_train:
            item_train.setdefault(token[1],{})
            item_mean.setdefault(token[1],float(0))
            item_ratings.setdefault(token[1],0)

        item_train[token[1]].update({token[0]:float(token[2])})
        item_ratings[token[1]] += 1
        item_mean[token[1]] += float(token[2])
        
    for key in item_mean:
        item_mean[key] = item_mean[key]/item_ratings[key]

def compute_sim():
    # store = open('/home/goel/rec/simy_dump.txt','a')

    for u in item_train:
        for v in item_train:
            num = 0.0
            norm_u = 0.0
            norm_v = 0.0
            if u not in simy:
                    simy.setdefault(u,{})
            if(u!=v):
                for x in item_train[u]:
                    if x in item_train[v]:
                        r_u = item_train[u][x]-item_mean[u]
                        r_v = item_train[v][x]-item_mean[v]
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
    
    for u in item_train:
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

n_size = 300

def predict():
    f1 = open("/home/goel/rec/data/u1.test",'r')
    f2 = open("/home/goel/rec/ii_pred." +str(n_size) ,'w')
    for line in f1:
        token = line.split()
        pred = 0.0
        norm = 0.0
        for v in n_all[token[1]]:
            if token[0] in item_train[v]:
                rating = item_train[v][token[0]] - item_mean[v]
                sim = simy[token[1]][v]
                pred += rating*sim
                # print pred
                norm += abs(sim)
        ans =  item_mean[token[1]] + (pred+1)/(norm+1)
        if ans>5:
            ans = 5
        if ans<1:
            ans = 1 
        f2.write(token[0]+'\t'+token[1]+'\t'+token[2]+'\t'+str(ans)+'\n')
    f1.close()
    f2.close() 


def print_item_train():
    for key in item_train:
        print key + ': ' + str(item_train[key])
        time.sleep(3)

def get_item_mean(item):
    return item_mean[item]

def get_item_ratings(item):
    return item_ratings[item]

        
def get_ii_sim(u,v):
    return simy[u][v]

init_item_train()
# print user_train['4']
# print user_train['4']['11']
# n_size = input("Enter the max neighbourhood size")
compute_sim()
find_neighbors(n_size)
predict()

f.close()
