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
        # if start and end points are same then return itselfs
        if start==end:
            return [path]
        # if origin itself is not present in graph then return empty listss
        if start not in self.graph_dict:
            return []
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths=self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)
                    
        return paths

    def get_shortest(self,start,end,path=[]):
        path = path +[start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        shortest_path =None

        for node in self.graph_dict[start]:
            if node not in path:
                sp= self.get_shortest(node,end,path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path=sp
                
        return shortest_path


if __name__ =='__main__':

    routes = [

        ("0", "1"),
        ("0", "2"),
        ("0", "3"),
        ("1", "3"),
        ("2", "3"),
        ("3", "2"),
        ("2", "4"),
        ("3", "4"),
        ("4", "6"),
        ("4", "5")
    ]

    start= "1"

    end= "6"


route_graph=Graph(routes)

print(f" Paths between {start} and {end} :" , route_graph.get_paths(start,end))
print(f"Shortest path between {start} and {end}:", route_graph.get_shortest(start,end))
