class node:
    def __init__(self, center: dict, maze_indexes: dict, parent=None, g_cost=None, f_cost=None, h_cost=None):

        # format: center = {"coordinate": (x, y), "index": (i, j)} 
        self.center = center

        # format: maze_indexes = {"left": (i, j), "center": (i, j+1), "right": (i, j+2)}
        self.maze_indexes = maze_indexes
        
        self.parent = parent

        self.g_cost = g_cost
        self.f_cost = f_cost 
        self.h_cost = h_cost
    
    def find_center(self):
        return self.center
    
    def find_neighbours(self):
        pass