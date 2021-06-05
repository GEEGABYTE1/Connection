from vertex import Vertex

class Graph:
    def __init__(self, directed=False):
        self.directed = directed 
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print('Adding vertex {}'.format(vertex.value[0]))
        self.graph_dict[vertex.value[0]] = vertex 

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value[0]].add_edge(to_vertex.value[0], weight)
        if not self.directed:
            self.graph_dict[to_vertex.value[0]].add_edge(from_vertex.value[0], weight)
        
    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop()
            print(current_vertex)
            seen[current_vertex] = True 

            if current_vertex == end_vertex:
                print("Link found! ")
                return 
            else:
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()
                next_vertices = [vertex for vertex in next_vertices if not vertex in seen]
                start.extend(next_vertices)
        
        print("There is no link between the two modems")
        return  




