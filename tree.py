# dict fmt => {"parent" : [children, ]}

import json

treeGraph = {}

class Node():

    def __init__(self) -> None:
        pass

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
                raise KeyError ("Parent node does not exist")



N = Node()
N.addNode("Elizabeth")
N.addChildren("Elizabeth",["Charles", "Andrew"])
print(treeGraph)