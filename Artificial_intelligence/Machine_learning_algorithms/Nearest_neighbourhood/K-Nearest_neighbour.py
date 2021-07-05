#!/usr/bin/env python3
import numpy as np
from numpy import linalg as LA
from scipy.spatial import distance

def k_NearestNeighbor(M_plus, M_minus, s, k):
    V = []
    M_plus_copy = np.copy(M_plus)
    M_minus_copy = np.copy(M_minus)

    for i in range(k):
        a = NearestNeighbour(M_plus_copy, M_minus_copy, s)
        for x in M_plus:
            if (a == x).all():
                # print(x)
                M_plus_copy = [x for x in M_plus_copy if (x != a).any()]

        for x in M_minus:
            if (a == x).all():
                # print(x)
                M_minus_copy = [x for x in M_minus_copy if (x != a).any()]
        V.append(a) # V has the k neighbourhoods

    return V

def NearestNeighbour(M_plus, M_minus, s):
    all_data = []
    for x in M_plus:
        all_data.append (x)
    for x in M_minus:
        all_data.append (x)

    all_data.sort(key=lambda x: distance.euclidean( LA.norm(x[0:14]),LA.norm(s[0:14]) ) )

    return (all_data[0])

def ffs(x):
    a = []
    for i in x:
        a.append(np.format_float_positional(i,precision=None, unique=True, trim='0', sign=False, pad_left=None))
    return a

if __name__ == "__main__":
    M_minus = []
    M_plus  = []
    k = 5 # configure according to the number of neighbours you want.


    with open("app1.data","r") as infile:
        i = 0
        for line in infile:
            # print(i,".",line)
            i = i+1
            currentline = line.strip().split(",")
            currentline = [float(a) for a in currentline]
            # print(currentline)

            if(currentline[15] == 1.0):
                M_plus.append(currentline)
            else:
                M_minus.append(currentline)

    with open("app1.test","r") as infile:

        for line in infile:
            currentline = line.strip().split(",")
            currentline = [float(a) for a in currentline]
            test_data_pt = currentline
            print("------------------------------------------",'\n')
            print("Test data:",ffs(test_data_pt))
            k_closest_pts = k_NearestNeighbor(M_plus, M_minus, test_data_pt, k)
            for x in k_closest_pts:
                print("neighbours",ffs(x))