# attribute dict fmt => {"parent" : [{"children" : []}, {"name" : "NAME"} ], {"age" : int}, {"marriage" : }, {"house" : }, {...}}
# tree dict fmt => {"parent" : [child0,child1], "child0" : None, "child1" : None, ...}

import json



class Algorithm():

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
                Algorithm.DFS(visited, graph, neighbour)

        return visited

class Node():

    def __init__(self) -> None:
        pass

    