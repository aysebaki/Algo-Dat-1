from typing import List, Tuple

# Using constants might make this more readable.
START = 'S'
EXIT = 'X'
VISITED = '.'
OBSTACLE = '#'
PATH = ' '


class MyMaze:
    """Maze object, used for demonstrating recursive algorithms."""

    def __init__(self, maze_str: str = ''):
        """Initialize Maze.

        Args:
            maze_str (str): Maze represented by a string,
            where rows are separated by newlines (\n).

        Raises:
            ValueError, if maze_str is empty.
        """
        if len(maze_str) == 0:
            raise ValueError
        else:
            # We internally treat this as a List[List[str]], as it makes indexing easier.
            self._maze = list(list(row) for row in maze_str.splitlines())
            self._row_range = len(self._maze)
            self._col_range = len(self._maze[0])
            self._exits: List[Tuple[int, int]] = []
            self._max_recursion_depth = 0

    def find_exits(self, start_row: int, start_col: int, depth: int = 0) -> bool:
        """Find and save all exits into `self._exits` using recursion, save 
        the maximum recursion depth into 'self._max_recursion_depth' and mark the maze.

        An exit is an accessible from S empty cell on the outer rims of the maze.

        Args:
            start_row (int): row to start from. 0 represents the topmost cell.
            start_col (int): column to start from; 0 represents the leftmost cell.
            depth (int): Depth of current iteration.

        Raises:
            ValueError: If the starting position is out of range or not walkable path.
        """
        if not (0 <= start_row < self._row_range and 0 <= start_col < self._col_range and self._maze[start_row][
            start_col] == " "):
            raise ValueError("The starting point couldn't be reached!")

        self._exits.clear()
        self._max_recursion_depth = 0
        if self._maze[start_row][(start_col + 1)] != START:
            self._maze[start_row][(start_col + 1)] = "."
            self.recursion_function(start_row, (start_col + 1), depth + 1)
        if 0 < start_row - 1 and start_row - 1 < len(self._maze):
            if self._maze[(start_row - 1)][start_col] == " ":
                if self._maze[(start_row - 1)][start_col] != START:
                    self._maze[(start_row - 1)][start_col] = "."
                self.recursion_function((start_row - 1), start_col, depth + 1)
        if 0 < start_col - 1 and start_col - 1 < len(self._maze[start_row]):
            if self._maze[start_row][(start_col - 1)] == " ":
                if self._maze[start_row][(start_col - 1)] != START:
                    self._maze[start_row][(start_col - 1)] = "."
                self.recursion_function(start_row, (start_col - 1), depth + 1)

        # Update the max recursion depth.
        self._max_recursion_depth = max(self._max_recursion_depth, depth)

    @property
    def exits(self) -> List[Tuple[int, int]]:
        """List of tuples of (row, col)-coordinates of currently found exits."""
        return self._exits

    @property
    def max_recursion_depth(self) -> int:
        """Return the maximum recursion depth after executing find_exits()."""
        return self._max_recursion_depth

    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self._maze)

    __repr__ = __str__