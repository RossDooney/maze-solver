import unittest
from mazes import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 50, 50)
        self.assertEqual(
            len(m._cells),
            num_cols,
        )
        self.assertEqual(
            len(m._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m._cells),
            num_cols,
        )
        self.assertEqual(
            len(m._cells[0]),
            num_rows,
        )

    def test_exit_enterence_exists(self):
        num_cols = 10
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m._cells[0][0].has_left_wall,
            False,
        )
        self.assertEqual(
            m._cells[num_cols - 1][num_rows - 1].has_right_wall,
            False,
        )

    def test_visited_reset(self):
        num_cols = 10
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(
                    m._cells[i][j].visited,
                    False,
                )


if __name__ == "__main__":
    unittest.main()
