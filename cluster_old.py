#import pandas as pd
import csv
import math
from collections import defaultdict
import random
import csv
x =[]
with open("dataset.csv", 'r') as csvfile:
 reader = csv.reader(csvfile)
 for row in reader:
    x.append(row)
print(x)
print("--------------------------------------------------------------------------------------------------------")
print()
print("The centroids are :")
k = 6
centroids = []


def in1():
    for i in range(k):
        temp = []
        for j in range(len(x[0])):
            temp.append((random.random())*100)
        centroids.append(temp)
   # print(x)
    #print(centroids)
    ed = []
    for i in range(len(x)):
        temp = []
        for ind in range(len(centroids)):
            temp1 = 0
            for j in range(len(x[i])):
                temp1 += (float(centroids[ind][j]) - float(x[i][j])) ** 2
            temp.append(temp1 ** (0.5))
        ed.append(temp)
    #print(ed)
    clusters = []
    for i in range(len(ed)):
        min = 0
        mindist = ed[i][0]
        for j in range(k):
            if (mindist > ed[i][j]):
                min = j
                mindist = ed[i][j]
        clusters.append(min)
    return (clusters)


def in2(clusters):
    global centroids, k, x
    for ii in range(5):
        prev_centroids = centroids
        centroids = []
        for j in range(k):
            temp = []
            temp1 = 0
            for q in range(len(x[0])):
                temp.append(int(0))
            #  print(temp)
            for q in range(len(clusters)):
                if (clusters[q] == j):
                    # print(x[q])
                    for kk in range(len(x[q])):
                        temp[kk] = temp[kk] + float(x[q][kk])
                        temp1 += 1
            if (temp1 != 0):
                for kk in range(len(temp)):
                    temp[kk] = temp[kk] / temp1
                centroids.append(temp)
            else:
                centroids.append(prev_centroids[j])
        # print(centroids)
        ed = []
        for i in range(len(x)):
            temp = []
            for ind in range(len(centroids)):
                temp1 = 0
                for j in range(len(x[i])):
                    temp1 += (centroids[ind][j] - float(x[i][j])) ** 2
                temp.append(temp1 ** (0.5))
            ed.append(temp)
        clusters = []
        for i in range(len(ed)):
            min = 0
            mindist = ed[i][0]
            for j in range(k):
                if (mindist > ed[i][j]):
                    min = j
                    mindist = ed[i][j]
            clusters.append(min)
    return (clusters)


clusters = in1()
clusters = in2(clusters)
print(centroids)




















# def return_list(disease):
#     disease_list = []
#     match = disease.replace('^','_').split('_')
#     ctr = 1
#     for group in match:
#         if ctr%2==0:
#             disease_list.append(group)
#         ctr = ctr + 1

#     return disease_list

# with open("Scraped-Data/dataset_uncleaned.csv") as csvfile:
#     reader = csv.reader(csvfile)
#     disease=""
#     weight = 0
#     disease_list = []
#     dict_wt = {}
#     dict_=defaultdict(list)
#     for row in reader:

#         if row[0]!="\xc2\xa0" and row[0]!="":
#             disease = row[0]
#             disease_list = return_list(disease)
#             weight = row[1]

#         if row[2]!="\xc2\xa0" and row[2]!="":
#             symptom_list = return_list(row[2])

#             for d in disease_list:
#                 for s in symptom_list:
#                     dict_[d].append(s)
#                 dict_wt[d] = weight


# with open("dataset_clean.csv","w") as csvfile:
#     writer = csv.writer(csvfile)
#     for key,values in dict_.items():
#         for v in values:
#             key = str.encode(key).decode('utf-8')
#             writer.writerow([key,v,dict_wt[key]])
# columns = ['Source','Target','Weight']

# data = pd.read_csv("Scraped-Data/dataset_clean.csv",names=columns, encoding ="ISO-8859-1")