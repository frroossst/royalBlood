import random
import json
import math
import os



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
        if not os.path.exists("server.json"):
            empty = {}
            method.dumpJSON(empty,"server.json")

    def addNode(self,name) -> None:
        self.name = name

        content = method.loadJSON("server.json")
        if self.name in content:
            raise ValueError ("duplicate nodes cannot exist")

        dictFMT = {"children" : [],"isFemale" : True,"alive" : True, "crownOrder" : math.nan, "level" : math.nan, "age" : math.nan, "spouse" : "", 
        "position" : "", "house" : "", "title" : ""}

        content[self.name] = dictFMT
        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def deleteNode(self,name):
        self.name = name

        content = method.loadJSON("server.json")

        del content[self.name]

        dataintegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataintegrity)

    def addGender(self):

        content = method.loadJSON("server.json")
        mon = method.loadJSON("monarchs.json")

        for i in content:
            if i not in mon["firstNames"]["female"]:
                content[i]["isFemale"] = False

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
                raise ValueError (f"all names must be globally unique : {i}")

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

    def addTitle(self,name,title):
        self.name = name
        self.title = title

        content = method.loadJSON("server.json")

        content[self.name]["title"] = self.title

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
    def constructLevel(self):

        content = method.loadJSON("server.json")
        
        for i in content:
            children = content[i]["children"]
            currLevel = content[i]["level"]
            if math.isnan(currLevel):
                continue
            for j in children:
                content[j]["level"] = currLevel + 1

        dataIntegrity = method.dumpJSON(content,"server.json")
        method.checkDump(dataIntegrity)

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
        last_level = node.getLastLevel()
        childrenArrows = ["|","/","\\"]

        for i in self.li:
            if i in last_level:
                print(i,end=" ")
            elif i == "|":
                charLen = len(i)
                emptyChars = (max_space - charLen) // 2
                print(empty_space * emptyChars,i,end=" ")
            elif i in childrenArrows:
                charLen = len(i)
                emptyChars = (max_space - charLen) // 4 # divide by five or four
                print(empty_space * emptyChars,i,end=" ")
            elif i != "\n":
                charLen = len(i)
                emptyChars = (max_space - charLen) // 2
                print(empty_space * emptyChars, i, empty_space * emptyChars,end=" ")
            else:
                print(i)

    # print the tree graphically
    def printGraph(self):
        
        max_level = node.getMaxLevel()
        iterVar = 0

        while True:
            if iterVar < max_level:
                currLevel = game.printLevel(iterVar)
                print(currLevel)
                iterVar += 1
            else:
                break
    @classmethod
    def cleanupAge(self):
        
        # take in dict from server.json and level and assign ages accordingly

        diff_parent_child = 20 # min age diff between parent and child
        diff_sib = 2 # min age diff between siblings

        content = method.loadJSON("server.json")

        for i in content:
            curr_parent = i
            curr_children = node.getChildren(curr_parent)
            curr_age = node.getAge(curr_parent)
            



    def generateNodes(self,n):

        self.n = n * 2

        content = method.loadJSON("monarchs.json")

        all_first_names = content["firstNames"]["male"]
        all_first_names.extend(content["firstNames"]["female"])
        all_last_names = content["lastNames"]
        all_houses = content["houses"]
        all_titles = content["titles"]
        
        sample_first_name = random.sample(all_first_names,self.n)
        sample_last_name = random.choices(all_last_names,k=self.n)
        sample_first_name_parent = sample_first_name[:self.n//2]
        sample_last_name_parent = sample_last_name[:self.n//2]
        sample_first_name_child = sample_first_name[self.n//2:]
        sample_house = random.sample(all_houses,1)
        sample_title = random.sample(all_titles,self.n)
        sample_age = random.sample(range(1,100),self.n)
        sample_age.sort(reverse=True)

        zipped = zip(sample_first_name_parent,sample_last_name_parent,sample_title,sample_age)

        N = node()

        for i in zipped:
            name = i[0] + " " + i[1]
            N.addNode(name)
            N.addTitle(name,i[2])
            N.addAge(name,i[3])
            N.addHouse(name,sample_house)
            
            children_number = random.randint(0,len(sample_first_name_child)//2)
            children_population = sample_first_name_child[:children_number]
            children_population_mod = []

            for j in children_population:
                k = j + " " + i[1]
                children_population_mod.append(k)

            for i in children_population:
                if i in sample_first_name_child:
                    sample_first_name_child.remove(i)

            N.addChildren(name,children_population_mod)

            # content = method.loadJSON("server.json")
            # for a in content:
            #     parentAge = content[a]["age"]



N = node()
G = game()
# method.clearall()
# G.generateNodes(10)
G.cleanupAge()
