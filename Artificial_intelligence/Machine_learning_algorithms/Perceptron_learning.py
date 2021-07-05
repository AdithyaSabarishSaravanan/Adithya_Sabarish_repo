#!/usr/bin/env python3
import numpy as np

def Perceptron_learning(M_plus, M_minus):
    w =(1, 1, 1)
    Mplus_cc = "no"
    Mminus_cc = "no"
    i = 0

    while (Mplus_cc == "no") & (Mminus_cc == "no"):
        print(i+1,"th iteration")
        n_Mminus_cc = 0
        n_Mplus_cc = 0
        for m in M_plus:
            if np.dot(w,m) <=0 :
                w = w + m
            else:
                n_Mplus_cc = n_Mplus_cc + 1
                
        for m in M_minus:
            if np.dot(w,m) >0 :
                w = w - m
            else:
                n_Mminus_cc = n_Mminus_cc + 1

        if(n_Mplus_cc == len(M_plus)) & (n_Mminus_cc == len(M_minus)):
            Mplus_cc = "yes"
            Mminus_cc = "yes"

        i = i+1
        print (w)
    return w

if __name__ == "__main__":
    M_minus = np.array(([8, 4, 1], [8, 6, 1], [9, 2, 1], [9, 5, 1]))
    M_plus  = np.array(([6, 1, 1], [7, 3, 1], [8, 2, 1], [9, 0, 1]))

    w = Perceptron_learning(M_plus, M_minus)

