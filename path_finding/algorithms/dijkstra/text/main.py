import sys, time, os

sys.path.append('../../../../')
from path_finding.API import API


def main():
    if len(sys.argv) != 2:
        print("USAGE ERROR: python main.py maze_file_path")
        return None

    file = sys.argv[1]

    maze, max_x, max_y = API.init(file)
    coord_space = API.map_nodes(maze)

    key_nodes = API.find_key_nodes(maze, coord_space)
    start_coords = key_nodes['start']['coordinate']
    end_coords = key_nodes['goal']['coordinate']

    for node in coord_space:
        if node.center['coordinate'] == start_coords:
            start = node
        if node.center['coordinate'] == end_coords:
            end = node

    start_time = time.time()
    path = API.dijkstra(start, end, coord_space, maze)

    API.mark_path(path, maze)
    end_time = time.time() 

    API.visualise(maze)
    print(f"Execution time: {end_time - start_time}")


main()