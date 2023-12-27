# Text-based maze solver

In the `src/tools/api.py` file, you will find implementations of A* and Dijkstra's algorithms used for solving mazes represented by text files in the `mazes` directory. This repository allows you to choose different algorithms and heuristics to solve one of the mazes via the command line. Currently, it supports only Manhattan and Euclidean heuristics along with A* and Dijkstra's algorithms; however, the API is designed to support [new configurations of your own heuristic functions and algorithms](#configure-your-own-heuristic-function-or-algorithm).

The directory named `src/mazes` contains text files that represent various mazes. However, this implementation supports the use of additional text files beyond those found in this specific directory. Any file that follows the format described in `mazes/format.md` will work correctly (source: [mackorone's maze files repository](https://github.com/micromouseonline/mazefiles)). You may find these in [mackorone's maze files repository](https://github.com/micromouseonline/mazefiles); any file obtained from this repository will be compatible.

It is important to note that if the files sourced from this repository do not already include a start node designated as `S` and a goal node labeled `G`, you will need to manually add these characters to the files to ensure their compatibility with the implementation.

-----
# Usage
## Standard maze solve

Enter the `src` directory and run the following:

```
python main.py {maze_file_path} {algorithm} {heuristic_function}
```

https://github.com/Raum12/path-finding/assets/116556858/1825ecbb-7c4c-4aad-85c0-15dd366ff6eb

https://github.com/Raum12/path-finding/assets/116556858/42fdd2a9-b627-4186-9c43-d80234554d2b

## Unit tests
Enter the `src` directory and run the following to perform unit tests:

```
python main.py {maze_file_path} {algorithm} {heuristic_function} --unittest {number_of_test_iterations}
```

The video below demonstrates this more clearly for Dijkstra's algorithm.

https://github.com/Raum12/path-finding/assets/116556858/57b583fe-82ef-4520-8387-f008d1632834

## Configure your own heuristic function or algorithm

To configure your own algorithm implementation or heuristic function to work on the command line:
1. implement either function in the `src/tools/api.py` file (refer to manhattan_distance, euclidean_distance, a_star or dijkstra functions for more details)
2. add the function to the map dictionary in `src/tools/mapper.py` with a key of your choice

Now, to use your new configuration, go back to the `src` directory and run the following:

```
python main.py {maze_file_path} {algorithm_key_in_map_dictionary} {heuristic_function_key_in_map_dictionary}
```

You may also alternatively run unit tests with your new config - the process is exactly the same as the one described in the unit tests section. 
