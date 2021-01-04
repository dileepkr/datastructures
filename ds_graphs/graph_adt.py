class Vertex:
    def __init__(self, key) -> None:
        self.key = key
        self.neighbors = {}
        self.distance = 0
        self.predecessor = None
        self.color = 'white'
    
    #dictionary of vertex object: weight
    def add_neighbor(self, neighbor, weight=None):
        self.neighbors[neighbor] = weight
    
    def get_connections(self):
        return self.neighbors.keys()
    
    def get_weight(self, neighbor):
        if neighbor in self.neighbors:
            return self.neighbors[neighbor]
        else:
            raise KeyError(f"Requested key {neighbor} not found in {self.key}'s neighbors")
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        if not color or isinstance(color, str):
            self.color = color
        else:
            raise TypeError(f"invalid color assigned to vertex color")

    def get_predecessor(self):
        return self.predecessor
    
    def set_predecessor(self, pred_vertex):
        if not pred_vertex or isinstance(pred_vertex, Vertex):
            self.predecessor = pred_vertex
        else:
            raise TypeError(f"Invalid type assigned to vertex predecessor")

    def get_distance(self):
        return self.distance
    
    def set_distance(self, distance):
        if isinstance(distance, int):
            self.distance = distance
        else:
            raise TypeError(f"Invalid distance assigned to vertex distance")

    def get_key(self):
        return self.key

    def __str__(self) -> str:
        return f"{self.key} neighbors: {[f'{vert}: {weight}, ' for vert, weight in self.neighbors.items()]}"

class Graph:
    def __init__(self) -> None:
        #vertices is a dictionary mapping vertex_name:vertex_obj
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex

    def add_edge(self, from_key, to_key, weight=None):
        '''
        Given from and to vertex keys, 
        1. Create vertex objects in vertices dictionary  
        2. Add to_vertex as a neighbor to the from_vertex
        '''
        if from_key not in self.vertices.keys():
            self.add_vertex(Vertex(from_key))
        if to_key not in self.vertices.keys():
            self.add_vertex(Vertex(to_key))
        self.vertices[from_key].add_neighbor(
            self.vertices[to_key],
            weight
        )

    def get_vertex(self, key):
        if key in self.vertices.keys():
            return self.vertices[key]
        else:
            raise KeyError(f"Vertex {key} not found in graph")

    def get_vertices(self):
        return self.vertices.keys()

    def __contains__(self, key):
        return key in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(Vertex(i))
    
    print(g.vertices)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    
    for vertex in g:
        for neighbor in vertex.get_connections():
            print("({} -> {})".format(vertex.key, neighbor.key))