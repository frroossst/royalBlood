import json
import math
from typing import ContextManager



class method():

    def __init__(self) -> None:
        pass

    @classmethod
    def clearall(self) -> None:
        empty = {}
        method.dumpJSON(empty,"server.json")

    @classmethod
    def loadJSON(self,file) -> dict:
        self.filename = file
        try:
            with open(self.filename,"r") as fobj:
                content = json.load(fobj)
                fobj.close()
        except Exception as e:
            # print(e)
            return None

        return content
        
    @classmethod
    def dumpJSON(self,data,file) -> bool:
        try:
            with open(file,"w") as fobj:
                json.dump(data,fobj,indent=6)
                fobj.close()
            return True
        except:
            return False

    @classmethod
    def checkDump(self,response) -> bool:
        if response:
            return True
        else:
            raise Exception ("data dump failed")



class algorithm():

    def __init__(self) -> None:
        pass

    @classmethod
    def BFS(self,graph,node):
        # node is the starting position (in most cases the root)
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

    @classmethod
    def DFS(self, graph, node, visited):

        if node not in visited:
            visited.append(node)
            for k in graph[node]:
                algorithm.DFS(graph,k, visited)
        return visited



class node():

    def __init__(self) -> None:
        pass

    def addNode(self,name) -> None:
        self.name = name

        content = method.loadJSON("server.json")
        if self.name in content:
            raise ValueError ("duplicate nodes cannot exist")

        dictFMT = {"children" : [], "alive" : True, "crownOrder" : math.nan, "age" : math.nan, "spouse" : "", 
        "position" : "", "house" : ""}

        content[self.name] = dictFMT
        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def deleteNode(self,name):
        self.name = name

        content = method.loadJSON("server.json")

        del content[self.name]

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def getRoot(self):

        content = method.loadJSON("server.json")

        for i in content:
            if content[i]["root"]:
                return i
        else:
            raise Exception ("root not found")

    def addChildren(self,parent,children) -> None:
        self.parent = parent
        self.children = children

        if not isinstance(self.children,list):
            raise TypeError ("children argument must be a list")

        content = method.loadJSON("server.json")

        for i in self.children:
            if i in content:
                raise ValueError ("all names must be globally unique")

        content[self.parent]["children"] = self.children

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

        for j in self.children:
            N = node()
            N.addNode(j)

    def addAge(self,name,age):
        self.name = name
        self.age = age

        if not isinstance(self.age,int):
            raise TypeError ("age argument must be an integer")

        content = method.loadJSON("server.json")

        try:
            content[self.name]["age"] = self.age
        except:
            raise KeyError ("node does not exist")

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    @classmethod
    def getAge(self,name):
        self.name = name

        content = method.loadJSON("server.json")

        age = content[self.name]["age"]

        return age

    def addSpouse(self,name,spouse):
        self.name = name
        self.spouse = spouse

        content = method.loadJSON("server.json")

        if self.spouse not in content.keys():
            raise ValueError ("spouse must exist as a node")

        content[self.name]["spouse"] = self.spouse

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def addPosition(self,name,position):
        self.name = name
        self.position = position
        
        content = method.loadJSON("server.json")

        content[self.name]["position"] = self.position

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def removePosition(self,name):
        self.name = name

        content = method.loadJSON("server.json")

        content[self.name]["position"] = ""

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def addHouse(self,name,house):
        self.name = name
        self.house = house

        content = method.loadJSON("server.json")

        content[self.name]["house"] = self.house

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def removeHouse(self,name):
        self.name = name

        content = method.loadJSON("server.json")

        content[self.name]["house"] = ""

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def defineRoot(self,name):
        self.name = name

        content = method.loadJSON("server.json")

        keys = content.keys()
        for i in keys:
            try:
                if content[i]["root"]:
                    raise ValueError ("root can only be defined once")    
            except KeyError:
                pass

        content[self.name]["root"] = True
        # content[self.name]["crownOrder"] = 1

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def addGuardian(self,name,guardian):
        self.name = name
        self.guardian = guardian

        content = method.loadJSON("server.json")

        if self.guardian not in content.keys():
            raise ValueError ("guardian must exist as a node")
        
        elif content[self.name]["age"] < 18:
            raise Exception ("age must be below 18 for a guardian to be appointed")

        elif math.isnan(content[self.guardian]["age"]):
            raise Exception ("guardian must have a defined age")

        elif content[self.guardian]["age"] < 18: 
            raise Exception ("guardian must be above the age of 18")

        content[self.name]["guardian"] = self.guardian

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def removeGuardian(self,name):
        self.name = name

        content = method.loadJSON("server.json")

        content[self.name]["guardian"] = ""

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def setOrder(self,name,order):
        self.name = name
        self.order = order

        content = method.loadJSON("server.json")

        content[self.name]["crownOrder"] = self.order

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def removeRogueNodes(self):

        content = method.loadJSON("server.json")

        allChildren = []
        rootLi = []

        N = node()
        root = N.getRoot()
        allChildren.append(root)

        for i in content:
            allChildren.extend(content[i]["children"])

        for j in content:
            if j not in allChildren:
                rootLi.append(j)
        
        try:
            for k in rootLi:
                del content[k]
        except:
            pass

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)



class game():

    def __init__(self) -> None:
        pass

    # method for creating the crown order
    def setCrownOrder(self):
        G = game()
        N = node()
        G.constructTree()

        treeGraph = method.loadJSON("tree.json")
        content = method.loadJSON("server.json")

        counter = 1
        for i in treeGraph:
            N.setOrder(i,counter)
            counter += 1


    # method for ordering children
    def constructOrder(self):
        
        content = method.loadJSON("server.json")

        for i in content:
            ageLi = []
            childrenSorted = []
            childrenLi = content[i]["children"]
            for j in childrenLi:
                ageLi.append(node.getAge(j))

            zipped = zip(childrenLi,ageLi)
            ageSorted = (sorted(zipped, key = lambda t: t[1]))

            for k in ageSorted[::-1]:
                childrenSorted.append(k[0])
            
            content[i]["children"] = childrenSorted

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def constructTree(self):
        G = game()
        G.constructOrder()

        N = node()
        N.removeRogueNodes()

        treeGraph = {}

        content = method.loadJSON("server.json")

        for i in content:
            treeGraph[i] = content[i]["children"]

        root = N.getRoot()

        dfsg = algorithm.DFS(treeGraph,root,[])
        
        dataintegrity = method.dumpJSON(dfsg,"tree.json")
        method.checkDump(dataintegrity)
        



N = node()
# method.clearall()
# N.addNode("Elizabeth")
# N.addChildren("Elizabeth",["Edward","Andrew"])
# N.addAge("Elizabeth",95)
# N.addAge("Edward",15)
# N.addAge("Andrew",21)
# N.addHouse("Elizabeth","Windsor")
# N.addNode("Phillip")
# N.addSpouse("Elizabeth","Phillip")
# N.addPosition("Elizabeth","Queen")
# N.defineRoot("Elizabeth")
# N.addNode("Mary")
# N.addAge("Mary",21)
# N.addGuardian("Andrew","Mary")
G = game()
# G.constructOrder()
G.setCrownOrder()
# G.constructTree()