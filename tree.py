# attribute dict fmt => {"parent" : [{"children" : []}, {"name" : "NAME"} ], {"age" : int}, {"marriage" : }, {"house" : }, {...}}
# tree dict fmt => {"parent" : [child0,child1], "child0" : None, "child1" : None, ...}

import json

treeGraph = {}
attributeDict = {}

class Node():

    root = ""

    def __init__(self) -> None:
        pass

    def __str__(self):
        print(treeGraph)

    def addNode(self,nodeName,isRoot=False):
        self.nodeName = nodeName

        if isRoot:
            Node.root = self.nodeName

        if self.nodeName not in treeGraph:
            treeGraph[self.nodeName] = []
            attributeDict[self.nodeName] = {}
        else:
            raise KeyError ("Node already exists")

    def updateNode(self,node,what):
        self.node = node
        self.what = what
        print(self.node)
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
                print("enter children : ")
                while True:
                    addChild = input("enter child name : ")
                    if addChild != "/break":
                        children.append(addChild)
                    else:
                        break
                Node.addChildren(self,self.node,children)
                
                for i in children:
                    treeGraph[i] = []
            else:
                raise SyntaxError ("missing positional argument 'what'")

    def addChildren(self,parent,children): #children is a list of strings
        self.parent = parent
        self.children = children
        if self.parent in treeGraph:
            treeGraph[self.parent].extend(self.children)
        else:
            raise KeyError ("Node does not exist")

    @classmethod
    def getRoot(self):
        return Node.root

    @classmethod
    def BFS(self,graph,node):
        # node is the starting position
        # graph is the graph in dictionary format
        visited=[]
        queue=[]    
        visited.append(node)
        queue.append(node)
        
        while queue:
            s = queue.pop(0)
            for x in graph[s]:
                if x not in visited:
                    visited.append(x)
                    queue.append(x)
        return visited

    def printTree(self):
        rootNode = Node.getRoot()
        bfsVisited = Node.BFS(treeGraph,rootNode)
        top = []
        keys = list(treeGraph.keys())
        values = list(treeGraph.values())
        for i in keys:
            if i not in values:
                print(i)


N = Node()
N.addNode("A",isRoot=True)
N.updateNode("A","children")
N.updateNode("B","children")
N.updateNode("C","children")
rootNode = N.getRoot()
# print(treeGraph)
# print(attributeDict)
N.printTree()
