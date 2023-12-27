import tools.api as api
from tools.mapper import map
import time, os

def log_command_line_structure():
    print(
        "\nUSAGE: python main.py {maze_file_path} {algorithm} {heuristic_function}"
    )
    
    print(
        "\nTo perform unit tests: python main.py {maze_file_path} {algorithm} {heuristic_function} --unittest {number_of_test_iterations}\n"
    )
    
    
def handle_command_line(command_line_args: list):
    try:
        f = open(command_line_args[1])
    except OSError:
        print(f"python: can't open file {command_line_args[1]}")
        log_command_line_structure()

        return 1
        
        
    file = command_line_args[1]
    algorithm = command_line_args[2]
    heuristic_function = command_line_args[3]
    
    
    if heuristic_function not in map or algorithm not in map:
        print("invalid heuristic function or algorithm")
        
        return 1
    else:
        algorithm = map[command_line_args[2]]
        heuristic_function = map[command_line_args[3]]
    
    
    if len(command_line_args) == 4:
        maze, coord_space, start, end, max_x, max_y = api.init(file)
        
        start_time = time.time()
        path = algorithm(
            start=start, 
            end=end, 
            heuristic_function=heuristic_function, 
            coord_space=coord_space, 
            maze=maze
        )
        end_time = time.time() 

        api.mark_path(path, maze)
        
        api.visualise(maze)
        print(f"Execution time: {end_time - start_time}")
    
    elif len(command_line_args) == 6 and command_line_args[4] == "--unittest":
        loops = int(command_line_args[5])
        
        if isinstance(loops, int):
            api.unit_test(loops, algorithm, heuristic_function, file)
        else:
            raise ValueError("")
        
    else:
        log_command_line_structure()
        
        return 1
    
    return 0
        