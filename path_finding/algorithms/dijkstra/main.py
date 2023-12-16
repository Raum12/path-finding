import sys, time

sys.path.append('../../../')
from path_finding.API import API

def main():
    if len(sys.argv) >= 2:
        try:
            f = open(sys.argv[1])
        except FileNotFoundError:
            print("\nUSAGE: python main.py maze_file_path")
            print("\nTo perform unit tests: python main.py maze_file_path --unittest number_of_test_iterations\n")

            return 1
        
        file = sys.argv[1]

    if len(sys.argv) == 2:
        maze, coord_space, start, end, max_x, max_y = API.init(file)

        start_time = time.time()
        path = API.dijkstra(start, end, coord_space, maze)
        end_time = time.time() 

        API.mark_path(path, maze)
        
        API.visualise(maze)
        print(f"Execution time: {end_time - start_time}")

    elif len(sys.argv) > 2 and sys.argv[2] == "--unittest":

        if len(sys.argv) == 4:
            API.unit_test(int(sys.argv[3]), API.dijkstra, file)
        
        else:
            print("\nUSAGE: python main.py maze_file_path --unittest number_of_test_iterations\n")
    
    else:
        print("\nUSAGE: python main.py maze_file_path")
        print("\nTo perform unit tests: python main.py maze_file_path --unittest number_of_test_iterations\n")
    
        return None
    
if __name__ == "__main__":
    main()
