
def dfs(visited,graph,startnode):
    if startnode not in visited:
        print(startnode)
        visited.add(startnode)
        for neighbor in graph[startnode]:
            dfs(visited,graph,neighbor)



if __name__=="__main__":

    graph={
        'A':['B','C','D'],
        'B':['E'],
        'C':['D','E'],
        
        'D':[],
        'E':[]
    }
    visited=set()

    nodetostart='A'
    print(dfs(visited,graph,nodetostart))