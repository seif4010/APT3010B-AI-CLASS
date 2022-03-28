class ShortestPath:
    def shortest_path(graph, node1, node2):
        path_list = [[node1]]
        path_index = 0
    # To keep track of previously visited nodes
        previous_nodes = {node1}
        if node1 == node2:
            return path_list[0]
            
        while path_index < len(path_list):
            current_path = path_list[path_index]
            last_node = current_path[-1]
            next_nodes = graph[last_node]
            # Search goal node
            if node2 in next_nodes:
                current_path.append(node2)
                return current_path
            # Add new paths
            for next_node in next_nodes:
                if not next_node in previous_nodes:
                    new_path = current_path[:]
                    new_path.append(next_node)
                    path_list.append(new_path)
                    # To avoid backtracking
                    previous_nodes.add(next_node)
            # Continue to next path in list
            path_index += 1
        # No path is found
        return []

# Driver program
graph = {}

graph[1] = {"S", "G"}
graph[2] = {"S", 1, 3}
graph[3] = {"G", 4}
graph[4] = {4, 5, 3}
graph[5] = {1, 2, 4}
graph[6] = {4}
graph[7] = {2, 1}

print("THe Shortest path from node S to G is: ")
graph.shortest_path(graph, 1, 7)