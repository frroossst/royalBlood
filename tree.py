import json
import math
from typing import ValuesView



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
        except:
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
            raise Exception ("[ERROR] data dump failed")



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
    def DFS(self,graph,node):
        visited=[]
        queue=[]            

        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                algorithm.DFS(visited, graph, neighbour)

        return visited



class node():

    def __init__(self) -> None:
        pass

    def addNode(self,name) -> None:
        self.name = name

        content = method.loadJSON("server.json")
        if self.name in content:
            raise ValueError ("duplicate nodes cannot exist")

        dictFMT = {"children" : [], "alive" : True, "age" : math.nan, "marriage" : "", 
        "position" : "", "house" : ""}

        content[self.name] = dictFMT
        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

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

        content[self.name]["age"] = self.age

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def addMarriage(self,name,spouse):
        self.name = name
        self.spouse = spouse

        content = method.loadJSON("server.json")

        content[self.name]["marriage"] = self.spouse

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def addPosition(self,name,position):
        self.name = name
        self.position = position
        
        content = method.loadJSON("server.json")

        content[self.name]["position"] = self.position

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def addHouse(self,name,house):
        self.name = name
        self.house = house

        content = method.loadJSON("server.json")

        content[self.name]["house"] = self.house

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

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)



N = node()
method.clearall()
N.addNode("Elizabeth")
N.addChildren("Elizabeth",["Edward","Andrew"])
N.addAge("Elizabeth",95)
N.addHouse("Elizabeth","Windsor")
N.addMarriage("Elizabeth","Phillip")
N.addPosition("Elizabeth","Queen")
N.defineRoot("Elizabeth")