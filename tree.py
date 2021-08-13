# attribute dict fmt => {"parent" : [{"children" : []}, {"name" : "NAME"} ], {"age" : int}, {"marriage" : }, {"house" : }, {...}}
# tree dict fmt => {"parent" : [child0,child1], "child0" : None, "child1" : None, ...}

import json

treeGraph = {}
attributeDict = {}

class Node():

    def __init__(self) -> None:
        pass

    def __str__(self):
        print(treeGraph)

    def addNode(self,nodeName):
        self.nodeName = nodeName
        if self.nodeName not in treeGraph:
            treeGraph[self.nodeName] = []
            attributeDict[self.nodeName] = {}
        else:
            raise KeyError ("Node already exists")

    def updateNode(self,node,what):
        self.node = node
        self.what = what

        if self.node not in treeGraph:
            raise KeyError ("Node does not exist")
        else:
            if self.what == "title":
                title = input("enter title : ")
                attributeDict[self.node]["title"] = title
            elif self.what == "house":
                house = input("enter house name : ")
                attributeDict[self.node]["house"] = house
            elif self.what == "age":
                age = int(input("enter age : "))
                attributeDict[self.node]["age"] = age
            elif self.what == "marriage":
                marriage = input("married to : ")
                attributeDict[self.node]["married to"] = marriage
            elif self.what == "children":
                children = []
                print("enter list of children : ")
                while True:
                    addChild = input("enter child name : ")
                    if addChild != "/break":
                        children.append(addChild)
                    else:
                        break
                Node.addChildren(self,self.node,children)
                attributeDict[self.node]["children"] = children
                for i in children:
                    treeGraph[i] = None
            else:
                raise SyntaxError ("what argument not passed")

    def addChildren(self,parent,children): #children is a list of strings
        self.parent = parent
        self.children = children
        if self.parent in treeGraph:
            treeGraph[self.parent].extend(self.children)
        else:
            raise KeyError ("Node does not exist")

    @classmethod
    def printTree(self):
        visited = []
        for i in treeGraph:
            if i not in visited:
                visited.append(i)
                print(i)

N = Node()

N.addNode("Elizabeth")
N.addNode("Mary")
N.updateNode("Elizabeth","children")
print(type(treeGraph["Lise"]))
print(treeGraph)
print(attributeDict)
N.printTree()