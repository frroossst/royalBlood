# dict fmt => {"parent" : nodes}
# 
# 

class Node():

    def __init__(self) -> None:
        pass

    def addChild(self,name):
        self.name = name
        print(f"{name} added to tree")

N = Node()
N.addChild("adhyan")