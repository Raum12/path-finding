import mms.API as API, sys
from queue import PriorityQueue

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()


x_max = API.mazeWidth() - 1
x_min = 0
y_max = API.mazeHeight() - 1
y_min = 0


def manhattan_distance(point, end):
    return abs(point[0] - end[0]) + abs(point[1] - end[1])


def a_star(start, end):
    open_set = PriorityQueue()
    open_set.put((0, start))
    log("start node added to open set")

    parent = {}
    g_cost = {start: 0}
    f_cost = {start: manhattan_distance(start, end)}

    while not open_set.empty():
        current = open_set.get()[1] # get the node itself, in index 1 of the tuple
        log(f"{current} has become the current node")
        if current == end:
            path = []

            while current in parent:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        for next in get_neighbours(current):
            log(f"Neighbours of {current}: {get_neighbours(current)}") 
            tentative_g_cost = g_cost[current] + 1 # each step has a cost of 1

            if tentative_g_cost < g_cost.get(next, float('inf')): 
                # if next not present positive infinity returned as default value
                # because: if the next has not been encountered before: the algorithm treats it as if it has infinite cost - until a better (lower) cost is determined
                parent[next] = current
                g_cost[next] = tentative_g_cost
                f_cost[next] = tentative_g_cost + manhattan_distance(next, end)
                open_set.put((f_cost[next], next))

    return None # path not found

def get_neighbours(node):
    x, y = node
    neighbours = []

    
    for direction in ["up", "right", "down", "left"]:
        if direction == "up":
            if not API.wallFront() and y < y_max:
                neighbours.append((x, y + 1))

            if not API.wallBack() and y > y_min:
                neighbours.append((x, y - 1))

            if not API.wallLeft() and x > x_min:
                neighbours.append((x - 1, y))

            if not API.wallRight() and x < x_max:
                neighbours.append((x + 1, y))
        
        if direction == "right":
            if not API.wallFront() and x < x_max:
                neighbours.append((x + 1, y))

            if not API.wallBack() and x > x_min:
                neighbours.append((x - 1, y))

            if not API.wallLeft() and y < y_max:
                neighbours.append((x, y + 1))

            if not API.wallRight() and y > y_min:
                neighbours.append((x, y - 1)) 
        
        if direction == "down": 
            if not API.wallFront() and y > y_min:
                neighbours.append((x, y - 1))
            
            if not API.wallBack() and y < y_max:
                neighbours.append((x, y + 1))
            
            if not API.wallLeft() and x < x_max:
                neighbours.append((x + 1, y))

            if not API.wallRight() and x > x_min:
                neighbours.append((x - 1, y))
        
        if direction == "left":
            if not API.wallFront() and x > x_min:
                neighbours.append((x - 1, y))
            
            if not API.wallBack() and x < x_max:
                neighbours.append((x + 1, y))
            
            if not API.wallLeft() and y > y_min:
                neighbours.append((x, y - 1))
            
            if not API.wallRight() and y < y_max:
                neighbours.append((x, y + 1))

def main():
    log(f"Maze Height: {y_max}\nMaze Width: {x_max}")
    start_node = (0, 0)
    end_node = (8, 8)

    path = a_star(start_node, end_node)

    if path:
        log("Running path...")
        API.setColor(0, 0, "G")
        API.setText(8, 8, "B")
        API.setText(0, 0, "start")
        API.setText(8,8, "end")

        for next_node in path:
            x, y = next_node
            current_x, current_y = start_node
            
            # move to next node
            if x > current_x:
                API.turnRight()
                API.moveForward()
            
            if x < current_x:
                API.turnLeft()
                API.moveForward()
            
            if y > current_y:
                API.moveForward()
            
            if y < current_y:
                API.turnLeft()
                API.turnLeft()
                API.moveForward()
            
            start_node = next_node

main()