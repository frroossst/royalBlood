# attribute dict fmt => {"parent" : [{"children" : []}, {"name" : "NAME"} ], {"age" : int}, {"marriage" : }, {"house" : }, {...}}
# tree dict fmt => {"parent" : [child0,child1], "child0" : None, "child1" : None, ...}

import json



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

class method():

    def __init__(self) -> None:
        pass

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


class node():

    def __init__(self) -> None:
        pass

    def addNode(self,name) -> None:
        self.name = name

        content = method.loadJSON("server.json")
        if self.name in content:
            raise ValueError ("duplicate nodes cannot exist")

        dictFMT = {"children" : [], "alive" : True}

        content[self.name] = dictFMT
        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def addChildren(self,parent,children) -> None:
        self.parent = parent
        self.children = children

        if not isinstance(self.children,list):
            raise TypeError ("children argument must be a list")

        content = method.loadJSON("server.json")

        content[self.parent]["children"] = self.children

        method.dumpJSON(content,"server.json")



N = node()
N.addNode("Elizabeth")
N.addChildren("Elizabeth",["Edward","Andrew"])
