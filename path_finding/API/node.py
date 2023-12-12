class node:
    def __init__(self, center: dict, maze_indexes: dict):

        # format: center = {"coordinate": (x, y), "index": (i, j)} 
        self.center = center

        # format: maze_indexes = {"left": (i, j), "center": (i, j+1), "right": (i, j+2)}
        self.maze_indexes = maze_indexes
        
        self.parent = None

        # A* attributes
        self.g_cost = None
        self.f_cost = None
        self.h_cost = None

        # Dijkstra's attributes
        self.dist = float('inf')
    
    def find_center(self):
        return self.center
    
    def find_neighbours(self):
        pass