#!/usr/bin/env python3

from models.grid import SudokuGrid
from models.solver import SudokuSolver
import time
import multiprocessing
    
def solve_all(running_times, result, file):
    with open(file) as grids : 
        for i,grid in enumerate(grids):
            g = SudokuGrid(grid.replace("\n",""))
            start = time.monotonic()
            solver = SudokuSolver(g)
            result.append(solver.solve())
            running_times.append(1000*(time.monotonic() - start))
            print("\r[{: <40}] ({:.0%})".format("="*int(40*i/244), i/244), end="")


def solve(data, typeSource):
    if typeSource == "sudoku" : 
        try :
            g = SudokuGrid(data)
            start = time.monotonic()
            solver = SudokuSolver(g)
            solved = solver.solve()
            print(solved)
            print("Soduku solved in {:.3f}ms".format(1000*(time.monotonic() - start)))
            
        except : 
            print("Wrong data source")
    else :
        manager = multiprocessing.Manager()
        running_times = manager.list()
        results = manager.list()
        p = multiprocessing.Process(target=solve_all, args=(running_times, results, data))
        print("Starting solver on {} with a time-out of 2min...".format(data))
        p.start()
        p.join(120)

        if p.is_alive():
            print("\nTime-out!")
            p.terminate()
            p.join()
        else:
            print()

        n_runs = len(running_times)
        result_fname = (data.rsplit(".")[0]+"_solved.txt")
        with open(result_fname, "w+") as r :
            for s in results :
                r.write(str(s) + "\n\n")

        print("Number of completed run: {}".format(n_runs))
        print("Running times statistics: min = {:.3f}ms, average = {:.3f}ms, max = {:.3f}ms".format(
            min(running_times), sum(running_times) / n_runs, max(running_times)))
        print("Results are stored in : {}".format(result_fname))