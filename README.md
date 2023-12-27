# Text-based maze solver

This repository allows you to select different algorithms and heuristic combinations to solve a maze via the command line. Then, it outputs a visual representation of the solution that was found. Currently, it supports Manhattan and Euclidean heuristics along with A* and Dijkstra's algorithms; however, the API is designed to support [new configurations of your own heuristic functions and algorithms](#configure-your-own-heuristic-function-or-algorithm) aswell.

In the `src/tools/api.py` file, you will find implementations of Dijkstra's algorithm and the A* algorithm used for solving the text file mazes in the `mazes` directory. 

The directory named `src/mazes` contains text files that represent various mazes. However, this implementation supports the use of additional text files beyond those found in this specific directory. Any file that follows the format described in `mazes/format.md` will work correctly (source: [mackorone's maze files repository](https://github.com/micromouseonline/mazefiles)). You may find these in [mackorone's maze files repository](https://github.com/micromouseonline/mazefiles); any file obtained from this repository will be compatible.

It is important to note that if the files sourced from this repository do not already include a start node designated as `S` and a goal node labeled `G`, you will need to manually add these characters to the files to ensure their compatibility with the implementation.

-----
# Usage
## Standard maze solve

Enter the `src` directory and run the following:

```
python main.py {maze_file_path} {algorithm} {heuristic_function}
```

The video below demonstrates this more clearly for the A* algorithm.

https://github.com/Raum490/path-finding/assets/116556858/9198e724-5624-4fb7-bf81-e37b37dea3f4

Please note, however, that you may also solve with Dijkstra's algorithm or use a different heuristic function. The current [map dictionary](https://github.com/Raum490/path-finding/blob/main/src/tools/mapper.py) contains the following keys which may be used in the command line: 

```
import tools.api as api

map = {
    "manhattan": api.manhattan_distance,
    "euclidean": api.euclidean_distance,
    "a_star": api.a_star,
    "dijkstra": api.dijkstra
}
```

For more details, read through this [section](#configure-your-own-heuristic-function-or-algorithm).

## Unit tests
This will allow you to solve a maze multiple times with a specific algorithm and heuristic function. Then it will output the:
1. Mean
2. Standard Deviation
3. Minimum
4. Maximum
   
of the run

Enter the `src` directory and run the following to perform unit tests:

```
python main.py {maze_file_path} {algorithm} {heuristic_function} --unittest {number_of_test_iterations}
```

The video below demonstrates this more clearly for the A* algorithm.

https://github.com/Raum490/path-finding/assets/116556858/d88ef7be-09cc-4335-88c1-15dec58369b1

To use other algorithms like Dijkstra or other heuristic functions like euclidean, simply replace a_star with its key in the [map dictionary](https://github.com/Raum490/path-finding/blob/main/src/tools/mapper.py). 

## Configure your own heuristic function or algorithm

To configure your own algorithm implementation or heuristic function to work on the command line:
1. implement either function in the `src/tools/api.py` file (refer to manhattan_distance, euclidean_distance, a_star or dijkstra functions for more details)
2. add the function to the map dictionary in `src/tools/mapper.py` with a key of your choice

Now, to use your new configuration, go back to the `src` directory and run the following:

```
python main.py {maze_file_path} {algorithm_key_in_map_dictionary} {heuristic_function_key_in_map_dictionary}
```

You may also alternatively run unit tests with your new config - the process is exactly the same as the one described in the unit tests section. 
