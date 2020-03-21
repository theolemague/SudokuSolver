#!/usr/bin/env python3

import sys
from grid import SudokuGrid

class PlaySudoku():

    def __init__(self):        
        try : 
            self.grid = SudokuGrid.from_file(sys.argv[1], int(sys.argv[2]))
        except IndexError:
            self.grid = SudokuGrid.from_stdin()
        self.initial_grid = self.grid.copy()

    def getValues(self):
        print(self.grid)    
        i, j, v = input("Entrez la position de la case (de 0 à 8) à modifier puis la valeur a mettre (ligne colonne valeur)\n").split()
        self.checkValues(i, j, v)
        
    def checkValues(self, i, j, v):
        impossible_val =[]
        try :
            tested_i = int(i)
            tested_j = int(j)
            row = self.grid.get_row(tested_i)
            col = self.grid.get_col(tested_j)
            region = self.grid.get_region(int(tested_i/3), int(tested_j/3))
            for nb in row:
                impossible_val.append(nb)
            for nb in col:
                impossible_val.append(nb)
            for nb in region:
                impossible_val.append(nb)
            
            if self.initial_grid.initial_grid[tested_i][tested_j]!=0:
                print("Impossible de modifier les valeurs initiales\n")
            elif int(v) in impossible_val:
                print("La valeur entrée est deja dans la ligne, la colonne ou la region\n")
            else:
                self.grid.write(tested_i,tested_j,int(v))

        except TypeError:
            print("Seuls les chiffres sont accepté")
        except IndexError:
            pass
            
    def checkFinish(self):
        for i in range(9):
            if 0 in self.grid.get_col(i):
                return False
        return True


def main():
    play = PlaySudoku()
    Finished = False
    while not Finished:
        play.getValues()
        Finished = play.checkFinish()
    print("Felicitation, sudoku fini !")
        
if __name__ == "__main__":
    main()