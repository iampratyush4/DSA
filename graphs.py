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

if __name__ =='__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

route_graph=Graph(routes)