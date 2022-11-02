"""
CiSTUP Internship: Round 1
Enter the solution for Q1 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""


def Dij_generator():
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.
    Returns:
        graph_object: variable containing network information.
    """
    graph_object = None
    try:
        open('ChicagoSketch_net.tntp','r')
        return graph_object
    except:
        return graph_object


def Q1_dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.
    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information
    Returns:
        shortest_path_distance (int): length of the shortest path.
    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1
    try:
        for u,v,w in graph_object:   #traversing in the graph_object network to find start node, end node and weight
            graph_object[u].append((v,w))
        minHeap=[(0,source)]#using the min heap
        vis=set()
        while minHeap:
            w1,n1=heapq.heappop(minHeap)
            if n1 in vis:  #checking if the node  is visited earlier or not
                continue
            vis.add(n1)
            shortest_path_distance=max(shortest_path_distance,w1)
            for n2,w2 in graph_object[n1]:
                if n2 not in vis:
                    heapq.heappush(minHeap,(w1+w2,n2))
        
        return shortest_path_distance
    except:
        return shortest_path_distance
