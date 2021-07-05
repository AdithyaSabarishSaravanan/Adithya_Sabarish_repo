#!/usr/bin/env python3
import numpy as np


def swap(node,r,c,nr,nc):
    list = np.copy(node.node)
    x,y  = list[r,c] , list[nr,nc]
    list[r,c] , list[nr,nc] = y,x
    return list


def successors_of_nodes(node):
    successors = []

    row,column = np.where(node.node == 0)
    successor1 = Node([],[],0)
    successor2 = Node([], [],0)
    successor3 = Node([], [],0)
    successor4 = Node([], [],0)
    row = row[0]
    column = column[0]

    if (row == 0 and column == 0):
        successor1.node = swap(node,row,column,row+1,column)
        successor2.node = swap(node,row,column,row,column+1)
        successors.extend([successor1,successor2])
    if(row == 0 and column == 1):
        successor1.node = swap(node,row,column,row,column-1)
        successor2.node = swap(node,row,column,row,column+1)
        successor3.node = swap(node,row,column,row+1,column)
        successors.extend([successor1, successor2, successor3])
    if (row == 0 and column == 2):
        successor1.node = swap(node,row,column,row,column-1)
        successor2.node = swap(node,row,column,row+1,column)
        successors.extend([successor1,successor2])
    if (row == 1 and column == 0):
        successor1.node = swap(node,row,column,row+1,column)
        successor2.node = swap(node,row,column,row-1,column)
        successor3.node = swap(node,row,column,row,column+1)
        successors.extend([successor1, successor2, successor3])
    if (row == 1 and column == 1):
        successor1.node = swap(node,row,column,row+1,column)
        successor2.node = swap(node,row,column,row-1,column)
        successor3.node = swap(node,row,column,row,column+1)
        successor4.node = swap(node,row,column,row,column-1)
        successors.extend([successor1, successor2, successor3, successor4])
    if (row == 1 and column == 2):
        successor1.node = swap(node,row,column,row+1,column)
        successor2.node = swap(node,row,column,row-1,column)
        successor3.node = swap(node,row,column,row,column-1)
        successors.extend([successor1, successor2, successor3])
    if (row == 2 and column == 0):
        successor1.node = swap(node,row,column,row,column+1)
        successor2.node = swap(node,row,column,row-1,column)
        successors.extend([successor1,successor2])
    if (row == 2 and column == 1):
        successor1.node = swap(node,row,column,row,column+1)
        successor2.node = swap(node,row,column,row,column-1)
        successor3.node = swap(node,row,column,row-1,column)
        successors.extend([successor1, successor2, successor3])
    if (row == 2 and column == 2):
        successor1.node = swap(node,row,column,row,column-1)
        successor2.node = swap(node,row,column,row-1,column)
        successors.extend([successor1,successor2])

    for s in successors:
        s.predecessor = node
        s.level = node.level+1
        # print(s.level)
    return successors


def iterative_deepening(f_node, goal_node):
    DepthLimit = 0

    while True:
        Result = Depth_first_search_B(f_node, goal_node,0,DepthLimit)
        DepthLimit = DepthLimit+1
        if(Result == "Solution found"):
            break

def Depth_first_search_B(node,goal_node,depth,limit):
    if np.array_equal(node.node, goal_node.node):
        print("got_solution")
        print("solution level:",node.level,"goal node:")
        print(node.node)
        x = node
        while (x.predecessor != []):
            # print(x.node)
            x = x.predecessor
            print("Level:",x.level,"Node:")
            print(x.node)
        return ("Solution found")
    new_nodes = successors_of_nodes(node)
    while new_nodes !=[] and depth<limit:
        Result = Depth_first_search_B(first(new_nodes),goal_node,depth+1,limit)

        if Result == "Solution found":
            return ("Solution found")
        new_nodes = rest(new_nodes)
    return ("No Solution")


def rest(nodes):
    return nodes[1:]

def first(nodes):
    return nodes[0]


class Node:
    predecessor = None
    node = None
    level = None
    def __init__(self, node, predecessor, level):
        self.node = node
        self.predecessor = predecessor
        self.level = level

if __name__ == "__main__":

    f_node = Node([],[],0)
    goal_node = Node([],[],0)

    f_node.node = np.array([[2, 0, 3], [1, 4, 6], [7, 5, 8]])

    goal_node.node = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    iterative_deepening(f_node, goal_node)
