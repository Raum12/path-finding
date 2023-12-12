from .node import node
import sys, time, statistics


def read_maze(maze, filename):
    maze_file = open(filename, "r")
    columns = maze_file.readlines()

    for column in columns:
        column = column.strip()
        row = [i for i in column]
        maze.append(row)

def unit_test(loops: int, algorithm, file):
    print(f"\nstarting unit test of length {loops}...\n")

    sum = 0
    max = None
    min = None
    set = []

    unittest_start = time.time()

    for i in range(loops):
        maze, coord_space, start, end, max_x, max_y = init(file)
        run_string = f"Run {i+1}"
        
        print(f"{run_string}:")

        start_time = time.time()
        algorithm(start, end, coord_space, maze)
        end_time = time.time()

        time_elapsed = end_time - start_time
        sum += time_elapsed
        set.append(time_elapsed)

        if max is None or time_elapsed > max:
            max = time_elapsed
            max_run = run_string
        
        if min is None or time_elapsed < min:
            min = time_elapsed
            min_run = run_string

        print(f"Finished in: {time_elapsed}s")
        print("-------------------------------------\n")
    
    unittest_end = time.time()
    print(f"Unittest took: {unittest_end - unittest_start}s")
    print(f"Mean: {sum/loops}s | Standard deviation: {statistics.stdev(set)}s | Min({min_run}): {min}s | Max({max_run}): {max}s\n")


def validate(maze, index: tuple):
    """Checks whether a given index has an 'o' character above it"""

    if maze[index[0]-1][index[1]] == "o":
        return False
    else:
        return True


def map_nodes(maze):
    """maps all traversable nodes' center coordinates to index in the maze array"""
    coord_space = []
    x_count = 0
    y_count = 0

    for i, row in enumerate(maze):
        x_count = 0

        if row[0] == "o":
            continue
        
        for j in range(len(row)):
            if not (validate(maze, (i, j)) and validate(maze, (i, j+1)) and validate(maze, (i, j+2))):
                continue
            
            if row[j] == ' ' and row[j+1] in [' ', 'G', 'S'] and row[j+2]:
                # find the center coordinate
                center = {
                    "coordinate": (x_count, y_count),
                    "index": (i, j+1)
                }
                maze_indexes = {
                    "left": (i, j),
                    "center": (i, j+1),
                    "right": (i, j+2)
                }

                coord_space.append(node(center=center, maze_indexes=maze_indexes))
                x_count += 1

        y_count += 1

    return coord_space
                
        
def visualise(maze, max_x=None, max_y=None):
    if max_x is not None and max_y is not None:
        print(f"Width: {max_x + 1}")
        print(f"Height: {max_y + 1}")

    for row in maze:
        print(''.join(row))
    print('\n')


def init(file):
    maze = []
    read_maze(maze, file)

    coord_space = map_nodes(maze)

    max_x = 0
    max_y = 0
    for coord in map_nodes(maze):
        to_check = coord.center['coordinate']

        if to_check[0] > max_x:
            max_x = to_check[0]

        if to_check[1] > max_y:
            max_y = to_check[1]

    # find key nodes

    key_nodes = find_key_nodes(maze, coord_space)
    start_coords = key_nodes['start']['coordinate']
    end_coords = key_nodes['goal']['coordinate']

    for node in coord_space:
        if node.center['coordinate'] == start_coords:
            start = node
        if node.center['coordinate'] == end_coords:
            end = node


    return maze, coord_space, start, end, max_x, max_y


def find_key_nodes(maze, coord_space):
    """finds the start and goal nodes in the maze"""
    goal_index = 0
    start_index = 0

    for i, row in enumerate(maze):
        for j, column in enumerate(row):
            if maze[i][j] == "S":
                start_index = (i, j)
            elif maze[i][j] == "G":
                goal_index = (i, j)

            if goal_index != 0 and start_index != 0:
                for node in coord_space:
                    if node.center['index'] == start_index:
                        start_coord = node.center['coordinate']

                    if node.center['index'] == goal_index:
                        goal_coord = node.center['coordinate']

                return {
                    "start": {"coordinate": start_coord, "index": start_index},
                    "goal": {"coordinate": goal_coord, "index": goal_index}
                }
    
    print("MAZE FORMAT ERROR: start and/or goal nodes not marked")
    sys.exit()


def mark_path(path, maze):
    for node in path:
        index = node.center['index']

        if maze[index[0]][index[1]] == ' ':
            maze[index[0]][index[1]] = "*"


def get_neighbours(node, maze, coord_space):
    x, y = node.center['coordinate']
    neighbours = []

    possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in possible_moves:
        new_x, new_y = x + dx, y + dy
        new_coords = (new_x, new_y)

        for possible_neighbour in coord_space:
            left = node.maze_indexes["left"]
            right = node.maze_indexes["right"]
            center = node.maze_indexes["center"]

            left_index = maze[left[0]][left[1]]
            right_index = maze[right[0]][right[1]]

            if new_coords == possible_neighbour.center['coordinate']:
                if new_coords[0] > x:
                    if maze[right[0]][right[1] + 1] == ' ': 
                        neighbours.append(possible_neighbour)

                if new_coords[0] < x:
                    if maze[left[0]][left[1] - 1] == ' ':
                        neighbours.append(possible_neighbour)
                
                if new_coords[1] > y:
                    if maze[center[0] + 1][center[1]] == ' ':
                        neighbours.append(possible_neighbour)
                
                if new_coords[1] < y:
                    if maze[center[0] - 1][center[1]] == ' ':
                        neighbours.append(possible_neighbour)

    return neighbours


def manhattan_distance(point: node, end: node):
    point_coords = point.center['coordinate']
    end_coords = end.center['coordinate']

    return abs(point_coords[0] - end_coords[0]) + abs(point_coords[1] - end_coords[1])


## a* implementation ##
def a_star(start: node, end: node, coord_space, maze):
    open_set = [start]
    closed_set = []

    start.f_cost = manhattan_distance(start, end)
    start.g_cost = 0
    start.h_cost = start.f_cost + start.g_cost

    path_found = False

    current = None

    while not path_found:
        current = min(open_set, key=lambda node: node.f_cost)

        if current.center['coordinate'] == end.center['coordinate']:
            path = []

            while current is not None:
                path.append(current)
                current = current.parent
            
            return path[::-1]
        
        open_set.remove(current)
        closed_set.append(current)

        for neighbour in get_neighbours(current, maze, coord_space):
            if neighbour.g_cost is None or current.g_cost + 1 < neighbour.g_cost:
                neighbour.f_cost = manhattan_distance(neighbour, end)
                neighbour.g_cost = current.g_cost + 1

                if neighbour in closed_set:
                    neighbour.parent = current

                elif neighbour in open_set:
                    neighbour.parent = current 

                elif neighbour not in open_set and neighbour not in closed_set:
                    neighbour.parent = current 
                    open_set.append(neighbour)

    # path not found
    return None 

# use manhattan for edge length 
def dijkstra(start: node, end: node, coord_space, maze):
    queue = [] # Q
    empty_set = [] # S

    start.dist = 0

    for coord in coord_space:
        queue.append(coord)

    while len(queue) != 0:
        current = min(queue, key=lambda node: node.dist)
        queue.remove(current)
        empty_set.append(current)

        for neighbour in get_neighbours(current, maze, coord_space):
            tentative_dist = current.dist + manhattan_distance(current, neighbour)

            if tentative_dist < neighbour.dist:
                neighbour.dist = tentative_dist
                neighbour.parent = current

    path = []
    current = end
    
    while current.parent is not None:
        path.append(current)
        current = current.parent 

    return path[::-1] 