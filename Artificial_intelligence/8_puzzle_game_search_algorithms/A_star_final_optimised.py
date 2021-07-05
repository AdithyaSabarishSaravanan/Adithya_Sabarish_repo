#!/usr/bin/env python3
import numpy as np
import bisect
import time


def successors_of_nodes(node):
    successors = []
    row,column = np.where(node.node == 0)

    # move DOWN
    if 0 <= (row + 1) <= 2:
        successor1 = Node([], [], 0, 0)
        list = np.copy(node.node)
        list[row, column], list[row + 1, column] = list[row + 1, column], list[row, column]
        successor1.node = list
        successor1.level = node.level + 1
        successors.append(successor1)

    # move UP
    if 0 <= (row - 1) <= 2:
        successor2 = Node([], [], 0, 0)
        list = np.copy(node.node)
        list[row, column], list[row - 1, column] = list[row - 1, column], list[row, column]
        successor2.node = list
        successor2.level = node.level + 1
        successors.append(successor2)

    # move RIGHT
    if 0 <= (column + 1) <= 2:
        successor3 = Node([], [], 0, 0)
        list = np.copy(node.node)
        list[row, column], list[row, column + 1] = list[row, column + 1], list[row, column]
        successor3.node = list
        successor3.level = node.level + 1
        successors.append(successor3)

    # move LEFT
    if 0 <= (column - 1) <= 2:
        successor4 = Node([], [], 0, 0)
        list = np.copy(node.node)
        list[row, column], list[row, column - 1] = list[row, column - 1], list[row, column]
        successor4.node = list
        successor4.level = node.level + 1
        successors.append(successor4)

    return successors


def A_star(node_list, goal_node, h, time1):
    while True:
        if node_list == []:
            return ("No solution")

        node = node_list[0]
        node_list = node_list[1:]

        if np.array_equal(node.node, goal_node.node):
            print("got_solution")
            time2 = time.time()
            print("Time of execution = ", time2 - time1)
            print("Level=", node.level)
            print(node.node,'\n','\n')
            x = node
            while (x.predecessor != []):
                x = x.predecessor
                print("Level=", x.level)
                print(x.node,'\n','\n')

            return("Solution found")

        node_list = sort(node_list, goal_node, h, successors_of_nodes(node), node)



def sort(node_list, goal_node, h, y,f_node):

    if h == 1:
        for node in y:
            node.predecessor = f_node

            if not (np.array_equal(f_node.node, qn_node.node)):
                x = f_node.predecessor
                if np.array_equal(node.node, x.node):
                    node.cost = 1000
                    continue
            # print("Level=", node.level)
            res =0
            for i in range(1, 9):
                row1, column1 = np.where(node.node == i)
                row2, column2 = np.where(goal_node.node == i)
                if (row1 != row2) or (column1 != column2):
                    res = res + 1

            node.cost = res + node.level
            bisect.insort(node_list, node)

    if h == 2:
        for node in y:
            node.predecessor = f_node

            if not (np.array_equal(f_node.node, qn_node.node)):
                x = f_node.predecessor
                if np.array_equal(node.node, x.node):
                    node.cost = 1000
                    continue

            res_row = 0
            res_col = 0
            for i in range(1, 9):
                row, column = np.where(node.node == i)
                goal_row, goal_column = np.where(goal_node.node == i)
                res_row = res_row + abs(goal_row - row)
                res_col = res_col + abs(goal_column - column)
            res = res_row + res_col
            node.cost = res + node.level
            bisect.insort(node_list, node)

    return (node_list)

class Node:
    predecessor = None
    node = None
    cost = None
    level = None

    def __init__(self, node, predecessor, cost, level):
        self.node = node
        self.predecessor = predecessor
        self.cost = cost
        self.level = level
        
    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return (self.node[0] + "\n" + self.node[1] + "\n" + self.node[2] + "\n\n")
        # return self.node


if __name__ == "__main__":

    h = 2
    qn_node = Node([],[],0,0)

    goal_node = Node([],[],0,0)
    nodelist = []

    qn_node.node = np.array([[0,4,7 ], [1, 8,3], [2, 6,5] ])     # solution at depth level 28
    #qn_node.node = np.array([[0,8,7], [6,5,4], [3,2,1] ])     # solution at depth level 28
    #qn_node.node = np.array([[0,4,8], [7,2,1], [3,6,5] ])     # solution at depth level 22
    # qn_node.node = np.array([[2, 0, 4], [6, 7, 1], [8, 5, 3] ])     # solution at depth level 23
    # qn_node.node = np.array([[6, 4, 7], [8, 5, 0], [3, 2, 1] ])     # solution at depth level 31
    # qn_node.node = np.array([[5, 6, 7], [4, 0, 8], [3, 2, 1] ])     # solution at depth level 30 for a different goal G1
    # qn_node.node = np.array([[8, 6, 7], [2, 5, 4], [3, 0, 1] ])       # solution at depth level 31

    # qn_node.node = np.array([[4, 1, 3], [7, 2, 6], [5, 0, 8]])

    nodelist.append(qn_node)

    # goal_node.node = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])    #Goal G1
    goal_node.node = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    time1 = time.time()
    A_star(nodelist, goal_node,h,time1)
