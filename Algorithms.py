import numpy as np

def DFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    #TODO:
    path=[]
    visited={}
    parent={}
    # Set the visited value of start node to visited
    new_node_visited = {start: -1}
    visited.update(new_node_visited)

	# Add the start node to the stack
    stack = [start]
    
    while len(stack) != 0:
        # Get a new node
        node = stack.pop()
        if node not in visited or node == start:
            path.append(node)
            adjacent_note=[]
            for x in range (0, len(matrix)):
                # Check is route exists and the node isn't visited
                if matrix[node][x] >= 1 and x not in visited:
                    new_node = {x: node}
                    parent.update(new_node)
                    adjacent_note.append(x)
            
            [stack.append(node) for node in reversed(adjacent_note)]
            if node != start:
                new_node_visited = {node: parent[node]}
                visited.update(new_node_visited)
                # Stack is empty or the node is end, break        
                if node == end:
                    break
                if len(adjacent_note) == 0:
                    path.append(parent[node])
                    
    return visited, path

def BFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    #TODO:
    path=[]
    visited={}
    parent={}
    # Set the visited value of start node to visited
    new_node_visited = {start: -1}
    visited.update(new_node_visited)

	# Add the start node to the queue
    q = queue.Queue()
    q.put(start)
    
    while q.empty() == False:
        # Get a new node
        node = q.get()
        if node not in visited or node == start:
            path.append(node)
            adjacent_note = True
            for x in range (0, len(matrix)):
                # Check is route exists and the node isn't visited
                if matrix[node][x] >= 1 and x not in visited:    
                    new_node = {x: node}
                    parent.update(new_node)
                    q.put(x)
                    adjacent_note = False

            if node != start:
                new_node_visited = {node: parent[node]}
                visited.update(new_node_visited)
                # Stack is empty or the node is end, break        
                if node == end:
                    break
                if adjacent_note == True:
                    path.append(parent[node])
    
    return visited, path

def UCS(matrix, start, end, pos):
    """
    Uniform Cost Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    parent={}
    # Set the visited value of start node to visited
    new_node_visited = {start: -1}
    parent.update(new_node_visited)

	# Add the start node to the queue
    q = [(start, -1)]
    
    while len(q) != 0:
        # Get a new node
        node = q.pop()[0]
        if node in visited:
            pass

        else:
            if node == end:
                print("Goal is found")
                new_node_visited = {node: parent[node]}
                visited.update(new_node_visited)
                path.append(node)
                try:
                    while node != start:
                        node = visited[node]
                        path.append(node)
                except:
                    break
                path.reverse()
                break
            
            else:
                for x in range (0, len(matrix)):
                    # Check is route exists and the node isn't visited
                    if matrix[node][x] >= 1 and x not in visited:
                        
                        #update parent
                        new_node = {x: node}
                        parent.update(new_node)
                        
                        #caculate distance between two coordinates, using the mahattan
                        distance = abs(pos[start][0] - pos[x][0]) + abs(pos[start][1] - pos[x][1])
                        q.append((x, distance))
    
                q.sort(key=lambda tup: tup[1], reverse=True)
                new_node_visited = {node: parent[node]}
                visited.update(new_node_visited)
    
    return visited, path

def Best_First_Search(matrix, start, end):
    """
    Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    parent={}
    # Set the visited value of start node to visited
    new_node_visited = {start: -1}
    parent.update(new_node_visited)

	# Add the start node to the queue
    q = [(start, -1)]
    
    while len(q) != 0:
        # Get a new node
        node = q.pop()[0]
        if node in visited:
            pass

        else:
            if node == end:
                print("Goal is found")
                new_node_visited = {node: parent[node]}
                visited.update(new_node_visited)
                path.append(node)
                try:
                    while node != start:
                        node = visited[node]
                        path.append(node)
                except:
                    break
                path.reverse()
                break
            
            else:
                for x in range (0, len(matrix)):
                    # Check is route exists and the node isn't visited
                    if matrix[node][x] >= 1 and x not in visited:
                        
                        #update parent
                        new_node = {x: node}
                        parent.update(new_node)
                        q.append((x, matrix[node][x]))
    
                q.sort(key=lambda tup: tup[1], reverse=True)
                new_node_visited = {node: parent[node]}
                visited.update(new_node_visited)
    
    return visited, path

def Astar(matrix, start, end, pos):
    """
    A star algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    parent={}
    # Set the visited value of start node to visited
    new_node_visited = {start: -1}
    parent.update(new_node_visited)

	# Add the start node to the queue
    q = [(start, -1)]
    
    while len(q) != 0:
        # Get a new node
        node = q.pop()[0]
        if node in visited:
            pass

        else:
            if node == end:
                print("Goal is found")
                new_node_visited = {node: parent[node]}
                visited.update(new_node_visited)
                path.append(node)
                try:
                    while node != start:
                        node = visited[node]
                        path.append(node)
                except:
                    break
                path.reverse()
                break
            
            else:
                for x in range (0, len(matrix)):
                    # Check is route exists and the node isn't visited
                    if matrix[node][x] >= 1 and x not in visited:
                        
                        #update parent
                        new_node = {x: node}
                        parent.update(new_node)
                        
                        #caculate distance between two coordinates, using the mahattan
                        distance = abs(pos[start][0] - pos[x][0]) + abs(pos[start][1] - pos[x][1]) + matrix[node][x]
                        q.append((x, distance))
    
                q.sort(key=lambda tup: tup[1], reverse=True)
                new_node_visited = {node: parent[node]}
                visited.update(new_node_visited)
    
    return visited, path

def Prim(matrix):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    edges: list
        List of founded edges in spanning tree (sort by search order)
        example: [[1,2],[3,4],[4,5]]
    """
    # TODO: 
    edges=[]
    n_v=matrix.shape[0]
    np.random.seed(0)
    start_v=np.random.randint(0,n_v-1)

    vertices = set()
    vertices.add(start_v)
    while len(vertices) != len(matrix[0]):
        crossing = set()
        for v in vertices:
            for k in range(len(matrix[0])):
                if k not in vertices and matrix[v][k] != 0:
                    crossing.add((v, k))
        # find the edge with the smallest weight in crossing
        edge = sorted(crossing, key=lambda e:matrix[e[0]][e[1]])[0]
        edges.append(edge)
        # add the new vertex into vertices
        vertices.add(edge[1])
    
    return edges

def Kruskal(matrix):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
   edges: list
        List of founded edges in spanning tree (sort by search order)
        example: [(1,2),(3,4),(4,5)]
    """ 
    # TODO: 
    edges=[]
    parent_node = {}
    rank = {}
    def convert_matrix_to_vertex(matrix):
        graph = {}
        vertices= []
        edges = set()
        for i in range(0, len(matrix[0])):
            vertices.append('{}'.format(i))
            for j in range(0, len(matrix[0])):
                if matrix[i][j] > 0:
                    new_edege = (matrix[i][j], '{}'.format(i), '{}'.format(j))
                    edge_visited = (matrix[i][j], '{}'.format(j), '{}'.format(i))
                    if edge_visited not in edges:
                        edges.add(new_edege)
        graph.update({'vertices': vertices, 'edges': edges})
        return graph
    
    def make_set(vertex):
        parent_node[vertex] = vertex
        rank[vertex] = 0
    
    def find(vertex):
        if parent_node[vertex] != vertex:
            parent_node[vertex] = find(parent_node[vertex])
        return parent_node[vertex]
    def union(vertex1, vertex2):
        root1 = find(vertex1)
        root2 = find(vertex2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent_node[root2] = root1
            else:
                parent_node[root1] = root2
                if rank[root1] == rank[root2]: rank[root2] += 1
                
    graph = convert_matrix_to_vertex(matrix)
    for vertex in graph['vertices']:
        make_set(vertex)
    edges_list = list(graph['edges'])
    edges_list.sort()
    for edge in edges_list:
        weight, vertex1, vertex2 = edge
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            edges.append((int(vertex1), int(vertex2))) 
    
    return edges


def ConnectedComponents(matrix):
    """
     Connected Components
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    
    Returns
    ---------------------
   edges: list
        example: [
            [4,6],[5,6],[6,7]], // component 1
            [[1,3],[1,2],[2,0]],  // component 2
            [[9,10],[9,11],[8,10]  // component 3
        ]
    """ 
    # TODO: 
    edges=[]
    visited = [ False for i in range(0, matrix[0].size) ]
    
    def DFS(result, visited, node, edges_list):
     
        # Mark the current vertex as visited
        visited[node] = True

        for i in range(0, len(edges_list)):
            if node == edges_list[i][0]:
                if visited[edges_list[i][1]] == False:
                    result.append([node, edges_list[i][1]])
                # Update the list
                    result = DFS(result, visited, edges_list[i][1], edges_list)
                    
        return result

    def convert_matrix_to_vertex(matrix):
        graph = {}
        vertices= []
        edges = set()
        for i in range(0, len(matrix[0])):
            vertices.append('{}'.format(i))
            for j in range(0, len(matrix[0])):
                if matrix[i][j] > 0:
                    new_edege = (i, j)
                    edge_visited = (j, i)
                    if edge_visited not in edges:
                        edges.add(new_edege)
        graph.update({'vertices': vertices, 'edges': edges})
        return graph
    
    graph = convert_matrix_to_vertex(matrix)
    edges_list = list(graph['edges'])
    edges_list.sort()
    
    # node start = 0
    for i in range(0, len(matrix[0])):
        if visited[i] == False:
            result = []
            result = DFS(result, visited, i, edges_list)
            if result == []:
                edges.append(i)
            else:
                edges.append(result)
    
    # edges=[
    #     [[4,6],[5,6],[6,7]],
    #     [[1,3],[1,2],[2,0]],
    #     [[9,10],[9,11],[8,10]]
    # ]
    return edges
