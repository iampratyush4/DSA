"""
types of graphs -
    1-directed
    2-undirected
    3-weighted graphs(ex- distance ,weights etc)
"""

class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print("Graph dict is" , self.graph_dict)

    def get_paths(self,start,end,path=[]):
        path =path + [start]
        # if start and end points are same then return itself
        if start==end:
            return [path]
        # if origin itself is not present in graph then return empty list
        if start not in self.graph_dict:
            return []
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths=self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)
                    
        return paths



if __name__ =='__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    start="Mumbai"
    end="New York"


route_graph=Graph(routes)
print(f" Paths between {start} and {end} :" , route_graph.get_paths(start,end))
