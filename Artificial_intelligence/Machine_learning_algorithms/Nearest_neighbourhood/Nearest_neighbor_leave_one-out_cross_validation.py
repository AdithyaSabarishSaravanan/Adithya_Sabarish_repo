#!/usr/bin/env python3
import numpy as np
from numpy import linalg as LA
from scipy.spatial import distance
import random

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

    all_data.sort(key=lambda x: distance.euclidean( x[0:14]/LA.norm(x[0:14]),s[0:14]/LA.norm(s[0:14]) ) )
    # all_data.sort(key=lambda x: distance.euclidean( x[0:14],s[0:14] ) )

    return (all_data[0])

def ffs(x):
    a = []
    for i in x:
        a.append(np.format_float_positional(i,precision=None, unique=True, trim='0', sign=False, pad_left=None))
    return a

if __name__ == "__main__":
    err =0
    k = 9   # configure according to the number of neighbours you want.

    file = open("app1.test")
    all_lines_1 = file.readlines()
    file = open("app1.data")
    all_lines_2 = file.readlines()
    all_lines = all_lines_1 + all_lines_2
    all_lines_copy = all_lines
    for test_line_number in range(len(all_lines_copy)):
        class_1_cnt = 0
        class_0_cnt = 0
        M_minus = []
        M_plus = []
        testline = all_lines[test_line_number]

        all_lines = [x for x in all_lines if (x != testline)]
        # print(all_lines)
        for line in all_lines:
            currentline = line.strip().split(",")
            currentline = [float(a) for a in currentline]
            # print(currentline)
            norm_current_line = LA.norm(currentline[0:14])
            currentline = currentline
            if (currentline[15] == 1.0):
                M_plus.append(currentline)
            else:
                M_minus.append(currentline)



        testline = testline.strip().split(",")
        testline = [float(a) for a in testline]
        test_data_pt = testline
        test_data_pt = test_data_pt
        print("------------------------------------------", '\n')
        print("Test data:", ffs(test_data_pt))
        k_closest_pts = k_NearestNeighbor(M_plus, M_minus, test_data_pt, k)
        test_data_pt = ffs(test_data_pt)
        for x in k_closest_pts:
            print("neighbours", ffs(x))
            if (x[15] == 1.0):
                class_1_cnt = class_1_cnt + 1
            elif (x[15] == 0.0):
                class_0_cnt = class_0_cnt + 1

        print("Class 0 neighbours:",class_0_cnt)
        print("Class 1 neighbours:",class_1_cnt)

        final_class = max(class_1_cnt, class_0_cnt)
        if(class_1_cnt == class_0_cnt):
            op_list = ['0.0','1.0']
            nn_output_test_pt_class = random.choice(op_list)
        else:
            if (final_class == class_1_cnt):
                nn_output_test_pt_class = '1.0'
            elif (final_class == class_0_cnt):
                nn_output_test_pt_class = '0.0'
        print("Test point class- output of NN:" , nn_output_test_pt_class)
        print("Actual class:",test_data_pt[15])
        if nn_output_test_pt_class != test_data_pt[15]:
            err = err+1
        print(err)
        all_lines = all_lines_copy
