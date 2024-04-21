"""

it uses queue
it is a traversal technique to list down all the nodes in a graph.
Method 1-
    1- take any node from a graph
    2- it a node is connected twice then remove any one conenction
    3- now a spanning tree woul have been formed.
    4- now we have to just find the level order traversal of this tree
    5- and this traversal result would be the BFS answer

Method 2 -
    1- create a queue named explored_queue  which will have all nodes that are explored
    2- create a visited list

"""

import collections

def bfs(graph,startnode):

    visited=set()
    queue=collections.deque([startnode])

    # when we deque a element from a queue we will insert it into the visited set

    while queue:
        popedNode = queue.popleft()
        visited.add(popedNode)
        for i in graph[popedNode]:
            if i not in visited:
                queue.append(i)
                
    return visited

if __name__=="__main__":

    graph={
        0:[1,2,3],
        1:[0,2],
        2:[0,1],
        3:[0],
        4:[2]
    }

    nodetostart=0
    print(bfs(graph,nodetostart))