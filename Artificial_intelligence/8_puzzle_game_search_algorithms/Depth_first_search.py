#!/usr/bin/env python3
import numpy as np

nodelist = np.array([[[0, 2, 3], [1, 4, 5], [7, 8, 6]]])
goal_node = np.array([[[1,2,3],[4,5,6],[7,8,0]]])
NULL = []
new_nodes = []

def swap(node,r,c,nr,nc):
    list = np.copy(node)
    x,y  = list[r,c] , list[nr,nc]
    list[r,c] , list[nr,nc] = y,x
    return list

def successors_of_nodes(node):
    successors =[]
    print(node)
    row,column = np.where(node == 0)

    row = row[0]
    column = column[0]
    if (row == 0 and column == 0):
        successor1 = swap(node,row,column,row,column-1)
        successor2 = swap(node,row,column,row,column+1)
        successors = [successor1, successor2]
    if(row == 0 and column == 1):
        successor1 = swap(node,row,column,row,column-1)
        successor2 = swap(node,row,column,row,column+1)
        successor3 = swap(node,row,column,row+1,column)
        successors = [successor1, successor2, successor3]
    if (row == 0 and column == 2):
        successor1 = swap(node,row,column,row,column-1)
        successor2 = swap(node,row,column,row+1,column)
        successors = [successor1, successor2]
    if (row == 1 and column == 0):
        successor1 = swap(node,row,column,row+1,column)
        successor2 = swap(node,row,column,row-1,column)
        successor3 = swap(node,row,column,row,column+1)
        successors =[successor1, successor2, successor3]
    if (row == 1 and column == 1):
        successor1 = swap(node,row,column,row+1,column)
        successor2 = swap(node,row,column,row-1,column)
        successor3 = swap(node,row,column,row,column+1)
        successor4 = swap(node,row,column,row,column-1)
        successors = [successor1, successor2, successor3, successor4]
    if (row == 1 and column == 2):
        successor1 = swap(node,row,column,row+1,column)
        successor2 = swap(node,row,column,row-1,column)
        successor3 = swap(node,row,column,row,column-1)
        successors = [successor1, successor2, successor3]
    if (row == 2 and column == 0):
        successor1 = swap(node,row,column,row,column+1)
        successor2 = swap(node,row,column,row-1,column)
        successors = [successor1, successor2]
    if (row == 2 and column == 1):
        successor1 = swap(node,row,column,row,column+1)
        successor2 = swap(node,row,column,row,column-1)
        successor3 = swap(node,row,column,row-1,column)
        successors =[successor1, successor2, successor3]
    if (row == 2 and column == 2):
        successor1 = swap(node,row,column,row,column-1)
        successor2 = swap(node,row,column,row-1,column)
        successors = [successor1, successor2]

    return successors


def depth_first_search(node, goal_node):

    if np.array_equal(node, goal_node):
        print("got_solution")
        print (node)
        return("Solution found")
    new_nodes = successors_of_nodes(node)
    # for i in range(len(y)):
    #     new_nodes.append(y[i])
    while new_nodes != []:
        result = depth_first_search(first(new_nodes),goal_node)
        if result =="Solution found" :
            return("Solution found")
        new_nodes = rest(new_nodes)
    return("No solution")

def rest(nodes):
    return nodes[1:]

def first(nodes):
    return nodes[0]

class Node():
    predecessor = None
    node = None
    # constructor
    def __init__(self, node, predecessor):
        self.node = node
        self.predecessor = predecessor

if __name__ == "__main__":
    depth_first_search(nodelist[0], goal_node[0])


