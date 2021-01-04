from ds_graphs.graph_adt import Graph

class Color:
    WHITE = "white"
    GRAY = 'gray'
    BLACK = 'black'

class DFSGraph(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.time = 0
    
    def dfs(self):
        for vertex in self:
            vertex.set_color(Color.WHITE)
            vertex.set_predecessor(-1)
        for vertex in self:
            if vertex.get_color() == Color.WHITE:
                self.dfs_visit(vertex)
    
    def dfs_visit(self, start_vertex):
        start_vertex.set_color(Color.GRAY)
        self.time += 1
        start_vertex.set_discovery(self.time)
        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_color() == Color.WHITE:
                next_vertex.set_predecessor(start_vertex)
                self.dfs_visit(next_vertex)
        start_vertex.set_color(Color.BLACK)
        self.time += 1
        start_vertex.set_finish(self.time)
