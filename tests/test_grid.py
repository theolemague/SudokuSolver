#!/usr/bin/env python3

import unittest
import unittest.mock
import random
import sys

import os
sys.path.append(os.path.abspath('.')+'/src')


from models.grid import SudokuGrid


class TestSudokuGrid(unittest.TestCase):
    def setUp(self):
        self._grid = SudokuGrid("349000000000000700000509002200095007001000400800720005100402000008000000000000376")

    def test_init(self):
        with self.assertRaises(ValueError):
            grid = SudokuGrid("123456xyz"*9)
        with self.assertRaises(ValueError):
            grid = SudokuGrid("123456abc"*9)
        with self.assertRaises(ValueError):
            grid = SudokuGrid("123456")
        with self.assertRaises(ValueError):
            grid = SudokuGrid("12345678"*11)

    def test_from_file(self):
        with open('src/sudokus.txt') as grids : 
            for i, _ in enumerate(grids):
                pass
            grids.seek(0)
            grid = grids.readlines()[random.randint(0, i)].replace('\n','')
        g = SudokuGrid(grid)


    def test_str(self):
        grid_str = str(self._grid)

    def test_get_row(self):
        self.assertEqual(list(self._grid.get_row(1)),
                [0, 0, 0, 0, 0, 0, 7, 0, 0])
        self.assertEqual(list(self._grid.get_row(4)),
                [0, 0, 1, 0, 0, 0, 4, 0, 0])

    def test_get_col(self):
        self.assertEqual(list(self._grid.get_col(4)),
                [0, 0, 0, 9, 0, 2, 0, 0, 0])
        self.assertEqual(list(self._grid.get_col(5)),
                [0, 0, 9, 5, 0, 0, 2, 0, 0])

    def test_get_region(self):
        self.assertEqual(list(self._grid.get_region(0, 0)),
                [3, 4, 9, 0, 0, 0, 0, 0, 0])
        self.assertEqual(list(self._grid.get_region(2, 2)),
                [0, 0, 0, 0, 0, 0, 3, 7, 6])

    def test_empty_pos(self):
        self.assertEqual(set(self._grid.get_empty_pos()),
                {(7, 3), (4, 7), (1, 3), (4, 8), (5, 6), (6, 6), (8, 0), (7, 7), (0, 7), (2, 1), (6, 2), (3, 7),
                    (0, 3), (5, 1), (8, 5), (4, 0), (1, 2), (6, 7), (3, 3), (5, 5), (8, 1), (7, 6), (4, 4), (1, 5),
                    (3, 6), (2, 2), (0, 4), (4, 1), (1, 1), (6, 4), (3, 2), (2, 6), (8, 2), (7, 1), (4, 5), (1, 4),
                    (7, 5), (0, 5), (1, 0), (0, 8), (2, 7), (7, 8), (8, 3), (7, 0), (6, 8), (6, 1), (3, 1), (5, 7),
                    (7, 4), (0, 6), (1, 8), (2, 0), (4, 3), (1, 7), (5, 2), (2, 4), (8, 4)})

    def test_write(self):
        for _ in range(4):
            i, j = random.choice(list(self._grid.get_empty_pos()))
            val = random.randint(1, 9)
            self._grid.write(i, j, val)
            self.assertEqual(list(self._grid.get_row(i))[j], val)

    def test_copy(self):
        grid = self._grid.copy()
        for i in range(9):
            self.assertEqual(list(grid.get_row(i)), list(self._grid.get_row(i)))
        i, j = random.choice(list(self._grid.get_empty_pos()))
        val = random.randint(1, 9)
        grid.write(i, j, val)
        self.assertEqual(list(self._grid.get_row(i))[j], 0)

if __name__ == "__main__":
    unittest.main()
