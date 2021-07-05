#!/usr/bin/env python3
import numpy as np

NULL = []


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
        s.level = node.level + 1
    return successors


def breadth_first_search(nodelist, goal_node):
    new_nodes = []
    new_nodes .append(Node([],[],0))
    for node in nodelist:
        if np.array_equal(node.node,goal_node.node):
            print("got_solution")
            print("solution level:", node.level, "goal node:")
            print(node.node)
            x = node
            while (x.predecessor != []):
                # print(x.node)
                x = x.predecessor
                print("Level:", x.level, "Node:")
                print(x.node)
            return

        if(node.node != []):
            y = successors_of_nodes(node)

            for i in range(len(y)):
                new_nodes.append(y[i])

    if new_nodes != []:
        return(breadth_first_search(new_nodes,goal_node))

    else:
        print("No solution")
        return NULL


class Node():
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
    nodelist =[]

    f_node.node = np.array([[3, 6, 4], [0, 1, 2], [8, 7, 5]])

    nodelist.append(f_node)
    goal_node.node = np.array([ [1, 2, 3], [8, 0, 4], [7, 6, 5] ])


    breadth_first_search(nodelist, goal_node)
