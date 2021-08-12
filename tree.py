# attribute dict fmt => {"parent" : [{"children" : []}, {"name" : "NAME"} ], {...}}
# tree dict fmt => {"parent" : [child0,child1], "child0" : None, "child1" : None, ...}

import json

treeGraph = {}
attributeDict = {}

class Node():

    def __init__(self) -> None:
        pass

    def __str__(self):
        print(treeGraph)

    def addNode(self,name):
        self.name = name
        if self.name not in treeGraph:
            treeGraph[self.name] = []
        else:
            raise KeyError ("Node already exists")


    def addChildren(self,parent,children): #children is a list of strings
        self.parent = parent
        self.children = children
        if self.parent in treeGraph:
            treeGraph[self.parent] = self.children
        else:
            raise KeyError ("Node does not exist")



N = Node()

N.addNode("Elizabeth")
N.addNode("Mary")

N.addChildren("Elizabeth",["Charles", "Andrew"])
N.addChildren("Mary",["Francois","Charlie"])

print(treeGraph)
