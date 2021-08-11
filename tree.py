# dict fmt => {"parent" : [children, ]}

import json

treeGraph = {}

class Node():

    def __init__(self) -> None:
        pass

    def __str__(self):
        for i in treeGraph:
            print(i)
            print(treeGraph[i])
            print("_________")

    def addNode(self,name):
        self.name = name
        if treeGraph == {}:
            treeGraph[self.name] = []
            
        for i in treeGraph:           
            if i == self.name:
                pass
            else:
                treeGraph[self.name] = []
                break
        return treeGraph

    def addChildren(self,parent,children): #children is a list of strings
        self.parent = parent
        self.children = children
        for i in treeGraph:
            if i == self.parent:
                treeGraph[self.parent] = self.children
            else:
                pass



N = Node()
N.addNode("Elizabeth")
N.addNode("Mary")

N.addChildren("Elizabeth",["Charles", "Andrew"])
N.addChildren("Mary",["Francois","Charlie"])

print(treeGraph)
