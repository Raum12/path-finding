Source: [micromouseonline/mazefiles](https://github.com/micromouseonline/mazefiles)
May be used with: [micromouseonline/micromouse_maze_tool](https://github.com/micromouseonline/micromouse_maze_tool)

The format used here is as follows:
- All posts are represented with the character `o`.

- All posts must be present in the grid even if there is no wall attached to them.

- Horizontal walls are represented with three `---`.

- Vertical walls are represented with a single `|`.

- The goal cells are marked with a `G` in the certer of the cell.

- The starting cell is marked with an `S` in the certer of the cell.

---
Here is an example of a 4x4 maze:
```
o---o---o---o---o
| G |           |
o   o   o   o---o
|       |       |
o---o---o---o   o
|               |
o   o---o---o   o
| S |           |
o---o---o---o---o
```
