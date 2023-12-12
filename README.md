# Path Finding

Contains A* algorithm (manhattan heuristic; however, this can easily be changed by creating a euclidean_distance function in the API.py file for example) and Dijkstra's algorithm implementations using a custom text file maze solving API.

The maze_files directory contains txt files which represent mazes. They are to be used with any txt file which follows the format laid out in maze_files/format.md; the source of this format is [mackorone's maze files](https://github.com/micromouseonline/mazefiles) from micro mouse online. Hence, any maze files foudn there will work with this repository. Please note however that you will need to add a goal node, `G`, and start node, `S`, if not already present in those files.

----
# Text Implementations

### Standard maze solve

Run the following command in either the dijkstra or a-star directories:
`python main.py {maze file directory}`


#### A* Algorithm with Manhattan Heuristic (text implementation):
https://github.com/Raum12/path-finding/assets/116556858/d044ae0f-345f-40e4-88ea-8eb7c239622b


#### Dijkstra's Algorithm (text implementation):
https://github.com/Raum12/path-finding/assets/116556858/e304d47b-f419-4389-81d5-9e9f7a2afdc4

-----
## Unit tests
Run the following command in either the dijkstra or a-star directories:
`python main.py {maze file directory} --unittest {number of unittest iterations}`


https://github.com/Raum12/path-finding/assets/116556858/9ac0a037-b9c1-4710-afab-977b41feee95

https://github.com/Raum12/path-finding/assets/116556858/5f05abe0-175f-4777-a176-92dad235ea95
