import json
import math



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

        dictFMT = {"children" : [], "alive" : True, "crownOrder" : math.nan, "level" : math.nan, "age" : math.nan, "spouse" : "", 
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

    @classmethod
    def getChildren(self,name):
        self.name = name
        content = method.loadJSON("server.json")

        children = content[self.name]["children"]

        return children

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
        content[self.name]["level"] = 0

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

    @classmethod
    def getMaxLevel(self) -> int:
        content = method.loadJSON("server.json")
        max_level = 0
        
        for i in content:
            if content[i]["level"] > max_level:
                max_level = content[i]["level"]
            
        return max_level +1 # because the order's ordering starts from 0

    @classmethod
    def getLastLevel(self) -> list:

        content = method.loadJSON("server.json")
        max_level = node.getMaxLevel() - 1
        last_level_elements = []

        for i in content:
            if content[i]["level"] == max_level:
                last_level_elements.append(i)

        return last_level_elements



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

    # construct levels
    def constructLevel(self,max,level=0,counter=0):

        if counter > max:
            return None

        try:
            content = method.loadJSON("server.json")

            levelVar = level

            for i in content:
                if content[i]["level"] == levelVar: # to find the root
                    childrenLi = content[i]["children"]
                    for j in childrenLi:
                        content[j]["level"] = levelVar + 1
                else:
                    break

            method.dumpJSON(content,"server.json")

            G = game()
            G.constructLevel(max,level=levelVar+1,counter=counter+1)

        except:
            pass

    # construct the tree graph (dfs)
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
        
    @classmethod
    def printLevel(self,level):

        self.level = level
        curr_nodes = []

        content = method.loadJSON("server.json")
        
        for i in content:
            if content[i]["level"] == self.level:
                curr_nodes.append(i)

        return curr_nodes

    @classmethod
    def getAllLevels(self):
        all_levels = []
        
        max_iter = node.getMaxLevel()
        
        currLevel = 0
        while True:
            if currLevel < max_iter:
                lev = game.printLevel(currLevel)
                all_levels.append(lev)
                currLevel += 1
            else:
                break

        return all_levels

    @classmethod
    def getChildrenArrows(self,li):
        self.list = li
        left_child = "/ "
        right_child = chr(92)
        center_child = "| " 

        if len(self.list) == 1:
            return center_child
        elif len(self.list) % 2 == 0: 
            output = (((len(self.list)//2) * left_child) + ((len(self.list)//2 * right_child)))
            childArrows = output.split()
        elif len(self.list) % 2 != 0:
            output = ((len(self.list) - 1) * left_child) + center_child + ((len(self.list) - 1) * right_child)
            childArrows = output.split()
        else:
            raise ValueError ("unexpected list value")

        return childArrows

    @classmethod
    def getLastLevelSpace(self,li):
        self.li = li
        lastLevelSpace = 0
        iterVar = -2

        while True:
            if self.li[iterVar].isalpha():
                lastLevelSpace += len(self.li[iterVar])
                lastLevelSpace += 1 # one additional space character for the space between words
                iterVar -= 1
            else:
                lastLevelSpace -= 1
                break

        # print(lastLevelSpace)
        return lastLevelSpace

    def spaceOutGraph(self,li):
        self.li = li
        max_space = game.getLastLevelSpace(self.li)
        empty_space = " "

        for i in self.li:
            if i != "\n":
                charLen = len(i)
                emptyChars = (max_space - charLen) // 2
                print(empty_space * emptyChars, i, empty_space * emptyChars,end=" ")
            else:
                print(i)





    # print the tree graphically
    def printGraph(self):

        all_levels = game.getAllLevels()
        printLi = []

        for i in all_levels:
            arrows = game.getChildrenArrows(i)
            for a in arrows:
                # print(a,end=" ")
                printLi.append(a)
            printLi.append("\n")
            # print()
            for b in i:
                # print(b,end=" ")
                printLi.append(b)
            # print()
            printLi.append("\n")

        printLi.pop(1)
        print(printLi)
            
        G = game()
        G.spaceOutGraph(printLi)
        




N = node()
G = game()
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
# G.constructOrder()
# G.setCrownOrder()
# G.constructTree()
# G.printGraph()
# maxVar = len(method.loadJSON("server.json").keys())
# G.constructLevel(maxVar)
G.printGraph()