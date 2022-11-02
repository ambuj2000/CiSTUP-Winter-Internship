"""
Enter the solution for Q2 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""


def bidirectional_dij(source: int, destination: int, graph_object) -> int:
    """
    Bi-directional Dijkstra's algorithm.
    Args:
        source (int): Source stop id
        destination (int): destination stop id
        graph_object: python object containing network information
    Returns:
        shortest_path_distance (int): length of the shortest path.
    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1

    try:
        		
    	
    	def bidirectional_search(self, source, destination):
    		
    		self.source_queue.append(source)
    		self.source_visited[source] = True
    		self.source_parent[source] = -1
    		
    		self.last_node_queue.append(destination)
    		self.last_node_visited[destination] = True
    		self.last_node_parent[destination] = -1
    
    		while self.source_queue and self.last_node_queue:
    			
    		
    			self.breadth_fs(direction = 'forward')
    			
    			self.breadth_fs(direction = 'backward')
    				
    			intersecting_node = self.is_intersecting()
    			
    			if intersecting_node != -1:
    				print("Path exists between {} and {}".format(source, destination))
    				print("Intersection at : {}".format(intersecting_node))
    				self.path_st(intersecting_node,
    								source, destination)
    				exit(0)
    		return shortest_path_distance

       # return shortest_path_distance
    except:
        return shortest_path_distance
