"""
Name:
PID:
"""

import random


def generate_edges(size, connectedness):
    """
    DO NOT EDIT THIS METHOD
    Generates undirected edges between vertices to form a graph
    :return: A generator object that returns a tuple of the form (source ID, destination ID)
    used to construct an edge
    """
    assert connectedness <= 1
    random.seed(10)
    for i in range(size):
        for j in range(i + 1, size):
            if random.randrange(0, 100) <= connectedness * 100:
                w = random.randint(1, 20)
                yield [i, j, w]

class Graph:
    """
    Class representing a Graph
    """
    class Edge:
        """
        Class representing an Edge in the Graph
        """

        __slots__ = ['start', 'destination', 'weight']

        def __init__(self, start, destination, weight):
            """
            DO NOT EDIT THIS METHOD
            :param start: represents the starting vertex of the edge
            :param destination: represents the destination vertex of the edge
            :param weight: represents the weight of the edge
            """
            self.start = start
            self.destination = destination
            self.weight = weight

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: edge to compare
            :return: Bool, True if same, otherwise False
            """
            return self.start == other.start and \
                   self.destination.vertex_id == other.destination.vertex_id \
                   and self.weight == other.weight

        def __repr__(self):
            return f"Start: {self.start} Destination: {self.destination} Weight: {self.weight}"

        __str__ = __repr__

        def get_start(self):
            """
            Return the starting vertex of the edge
            """
            return self.start

        def get_destination(self):
            """
            Return the destination vertex of the edge
            """
            return self.destination.vertex_id

        def get_weight(self):
            """
            Returns the weight of the edge
            """
            return int(self.weight)

    class Vertex:
        """
        Class representing an Edge in the Graph
        """

        __slots__ = ['vertex_id', 'edges', 'visited']

        def __init__(self, vertex_id):
            """
            DO NOT EDIT THIS METHOD
            :param vertex_id: represents the unique identifier of the vertex
            """
            self.vertex_id = vertex_id
            self.edges = {}
            self.visited = False

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: vertex to compare
            :return: Bool, True if the same, False otherwise
            """
            return self.vertex_id == other.vertex_id and \
                   self.edges == other.edges and self.visited == other.visited

        def __repr__(self):
            return f"Vertex: {self.vertex_id}"

        __str__ = __repr__

        def degree(self):
            """
            Returns the degree of the vertex
            """
            return len(self.edges)

        def visit(self):
            """
            Sets the vertex’s visit value to true
            """
            self.visited = True

        def insert_edge(self, destination, weight):
            """
            Adds an edge representation into the edge map between the vertex and the given destination vertex.
            :param destination: The destination vertex
            :param weight: Weight of the edge
            :return:
            """
            edge = Graph().Edge(self.vertex_id, destination, weight)
            self.edges[destination.vertex_id] = edge

        def get_edge(self, destination):
            """
            Finds the specific edge that has the desired destination
            :param destination: Vertex.vertex_id
            :return: Edge
            """
            if destination in self.edges:
                return self.edges[destination]


        def get_edges(self):
            """
            Creates a list of the vertex’s edges.
            :return: list
            """
            edge_list = []
            for edge in self.edges.values():
                edge_list.append(edge.destination)
            return edge_list

    def __init__(self):
        """
        DO NOT EDIT THIS METHOD
        """
        self.adj_map = {}
        self.size = 0

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are Identical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        return self.adj_map == other.adj_map and self.size == other.size

    def add_to_graph(self, source, dest=None, weight=0):
        """
        Inserts a vertex into the graph and will create an edge.
        :param source: Source vertex
        :param dest: Destination vertex
        :param weight: Weight of the edge
        :return:
        """
        source_vertex = Graph().Vertex(source)
        if source not in self.adj_map:
            self.adj_map[source] = source_vertex
            self.size += 1

        if dest is not None:
            dest_vertex = Graph().Vertex(dest)
            if dest not in self.adj_map:
                self.adj_map[dest] = dest_vertex
                self.size += 1
            self.adj_map[source].insert_edge(dest_vertex, weight)
            self.adj_map[dest].insert_edge(source_vertex, weight)

    def construct_graph_from_file(self, filename):
        """
        Constructs a graph from the file
        :param filename: The filename
        :return:
        """
        fp = open(filename, "r")
        for line in fp:
            line_lst = line.strip().split()
            if len(line_lst) == 1:
                try:
                    source = int(line_lst[0])
                except:
                    source = line_lst[0]
                self.add_to_graph(source)
            elif len(line_lst) == 2:
                try:
                    source = int(line_lst[0])
                    dest = int(line_lst[1])
                except:
                    source = line_lst[0]
                    dest = line_lst[1]
                self.add_to_graph(source, dest)
            elif len(line_lst) == 3:
                try:
                    source = int(line_lst[0])
                    dest = int(line_lst[1])
                    weight = int(line_lst[2])
                except:
                    source = line_lst[0]
                    dest = line_lst[1]
                    weight = line_lst[2]
                self.add_to_graph(source, dest, weight)

    def get_vertex(self, vertex_id):
        """
        Creates a list of all the vertices in the graph
        :param vertex_id: The unique vertex_id
        :return: Vertex
        """
        if vertex_id in self.adj_map.keys():
            return self.adj_map[vertex_id]
        return None

    def get_vertices(self):
        """
        Creates a list of all the vertices in the graph
        :return: List[Vertex]
        """
        vertex_list = []
        if self.adj_map is not None:
            for vertex in self.adj_map:
                vertex_list.append(vertex)
        return vertex_list

    def bfs(self, start, target, path=None):
        """
        Performs a Breadth First Search on the graph
        :param start: Vertex.ID
        :param target: Vertex.ID
        :param path: List[Vertex.ID]
        :return: List[Vertex.ID]
        """
        # maintain a queue of paths
        queue = []
        # push the first path into the queue
        queue.append([start])
        while queue:
            # get the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            # path found
            if node == target:
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            adjacent_nodes = self.get_vertex(node).get_edges()
            for adjacent in adjacent_nodes:
                new_path = list(path)
                new_path.append(adjacent.vertex_id)
                queue.append(new_path)

    def dfs_paths(self, start, target, path, result):
        """
        Performs a Depth First Search on the graph recursively
        :param start: Vertex.ID
        :param target: Vertex.ID
        :param path: List[Vertex.ID]
        :param result: List[Vertex.ID]
        :return:
        """
        path += [start]
        if start == target:
            result.append(path)
        else:
            adjacent_edges = self.get_vertex(start).get_edges()
            for node in adjacent_edges:
                if node.vertex_id not in path:
                    self.dfs_paths(node.vertex_id, target, path[:], result)

    def dfs(self, start, target, path=None):
        """
        Performs a Depth First Search on the graph
        :param start: Vertex.ID
        :param target: Vertex.ID
        :param path: List[Vertex.ID]
        :return: List[Vertex.ID]
        """
        result = []
        self.dfs_paths(start, target, [], result)
        path.append(result[0])
        return result[0]

def quickest_route(filename, start, destination):
    """
    Finding the quickest route between start and destination
    :param filename: file used to construct the graph
    :param start: Vertex ID
    :param destination: Vertex ID
    :return: List [total weight, IDs of vertices in the path]
    """
    stu = Graph()
    stu.construct_graph_from_file(filename)

    if stu.get_vertex(start) is None:
        return []

    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node != destination:
        visited.add(current_node)
        destinations1 = stu.get_vertex(current_node).get_edges()
        destinations = []
        for dest in destinations1:
            destinations.append(dest.vertex_id)

        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = stu.get_vertex(current_node).get_edge(next_node).get_weight() + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return []
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    weight = 0
    for i, dest in enumerate(path):
        if i < len(path) - 1:
            weight = stu.get_vertex(path[i]).get_edge(path[i+1]).get_weight() + weight

    return [weight] + path
