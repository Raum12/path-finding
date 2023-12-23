# Text-based maze solver

The `API` directory contains implementations of the A* algorithm and Dijkstra's algorithm for solving mazes through custom text file representations. The A* algorithm uses a Manhattan heuristic; however, you may choose to use a different heuristic function - this may be done by declaring your own function in the `API.py` file under the API directory.

Users can interact with these algorithms and the maze-solving API by using the specified custom text file format to represent mazes. Moreover, the API is designed to support modifications or enhancements to the algorithms by updating the code within the API.py file, allowing you to experiment with different heuristic functions as mentioned earlier or to potentially introduce other algorithms within the API structure.

The directory named `maze_files` contains text files that represent various mazes. However, this implementation supports the use of additional text files beyond those found in this specific directory. Any file conforming to the format described in `maze_files/format.md` will work correctly (source: [mackorone's maze files repository](https://github.com/micromouseonline/mazefiles)). You may find these in [mackorone's maze files repository](https://github.com/micromouseonline/mazefiles); any file obtained from this repository will be compatible.

It is important to note that if the files sourced from this repository do not already include a start node designated as `S` and a goal node labeled `G`, you will need to manually add these characters to the files to ensure their compatibility with the implementation.

-----
# Standard maze solve

Run the following command in either the dijkstra or a-star directories:

```
python main.py {maze file directory}
```

https://github.com/Raum12/path-finding/assets/116556858/1825ecbb-7c4c-4aad-85c0-15dd366ff6eb

https://github.com/Raum12/path-finding/assets/116556858/42fdd2a9-b627-4186-9c43-d80234554d2b

-----
# Unit tests
Run the following command in either the dijkstra or a-star directory (depending on which algorithm you want to test):

```
python main.py {maze file directory} --unittest {number of unittest iterations}
```

The video below demonstrates this more clearly for Dijkstra's algorithm.

https://github.com/Raum12/path-finding/assets/116556858/57b583fe-82ef-4520-8387-f008d1632834
