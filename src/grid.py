#!/usr/bin/env python3

import sys

class SudokuGrid:
    """Cette classe représente une grille de Sudoku.
    Toutes ces méthodes sont à compléter en vous basant sur la documentation fournie en docstring.
    """
    # 1er indice -> ligne / 2e -> colonne
       #Grille initial
    

    @classmethod
    def from_file(cls, filename, line):
        nb_line = 0
        with open(filename) as grid:    
            lines = grid.readlines()    #List des lignes du fichier
        grid.close()
        nb_line = len(lines)        
        if (line-1)>nb_line:
            sys.exit("Le numéro de ligne max est "+str(nb_line))
        return cls(lines[line-1].strip('\n'))
        """À COMPLÉTER!
        Cette méthode de classe crée une nouvelle instance de grille
        à partir d'une ligne contenue dans un fichier.
        Pour retourner une nouvelle instance de la classe, utilisez le premier argument ``cls`` ainsi::
            return cls(arguments du constructeur)

        :param filename: Chemin d'accès vers le fichier à lire
        :param line: Numéro de la ligne à lire
        :type filename: str
        :type line: int
        :return: La grille de Sudoku correspondant à la ligne donnée dans le fichier donné
        :rtype: SudokuGrid
        """

    @classmethod
    def from_stdin(cls):
        """À COMPLÉTER!
        Cette méthode de classe crée une nouvelle instance de grille
        à partir d'une ligne lu depuis l'entrée standard (saisi utilisateur).
        *Variante avancée: Permettez aussi de «piper» une ligne décrivant un Sudoku.*
        :return: La grille de Sudoku correspondant à la ligne donnée par l'utilisateur
        :rtype: SudokuGrid
        """
        input_values_str = input("Entrez les 81 valeurs du sudoku (de 0 à 9)\n")
        return cls(input_values_str) # s'il y a des erreurs de saisie elle seront retrouver dans le constructeur
        
        

    def __init__(self, initial_values_str):
        self.initial_grid = [0]*9 
        if len(initial_values_str)!=81 : 
            raise ValueError("La chaine de caractère n'est pas de la bonne longueur")
        else:            
            for i in range(9):
                self.initial_grid[i]=[int(initial_values_str[j]) for j in range(i*9,(i*9)+9)]
        
        """À COMPLÉTER!
        Ce constructeur initialise une nouvelle instance de la classe SudokuGrid.
        Il doit effectuer la conversation de chaque caractère de la chaîne en nombre entier,
        et lever une exception si elle ne peut pas être interprétée comme une grille de Sudoku.
        :param initial_values_str: Une chaîne de caractères contenant **exactement 81 chiffres allant de 0 à 9**,
            où ``0`` indique une case vide
        :type initial_values_str: str
        """

    def __str__(self):
        """À COMPLÉTER!
        Cette méthode convertit une grille de Sudoku vers un format texte pour être affichée.
        :return: Une chaîne de caractère (sur plusieurs lignes...) représentant la grille
        :rtype: str
        """
        grid_string = ""
        for i in range(9):
            for j in range(9):
                grid_string += str(self.initial_grid[i][j])+" "
                if j==2 or j==5:
                    grid_string+=" "
            grid_string +="\n"
            
        return grid_string

    def get_row(self, i):
        for val in self.initial_grid[i]:
            yield val
        
        """À COMPLÉTER!
        Cette méthode extrait une ligne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param i: Numéro de la ligne à extraire, entre 0 et 8
        :type i: int
        :return: La liste des valeurs présentes à la ligne donnée
        :rtype: list of int
        """

    def get_col(self, j):
        col = []
        for i in range(9):
            col.append(self.initial_grid[i][j])
            yield self.initial_grid[i][j]
        """À COMPLÉTER!
        Cette méthode extrait une colonne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param j: Numéro de la colonne à extraire, entre 0 et 8
        :type j: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """

    def get_region(self, reg_row, reg_col):
        for i in range(reg_row*3, (reg_row*3)+3):
            for j in range(reg_col*3, (reg_col*3)+3):
                yield self.initial_grid[i][j]
        

        """À COMPLÉTER!
        Cette méthode extrait les valeurs présentes dans une région donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param reg_row: Position verticale de la région à extraire, **entre 0 et 2**
        :param reg_col: Position horizontale de la région à extraire, **entre 0 et 2**
        :type reg_row: int
        :type reg_col: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """

    def get_empty_pos(self):
        """À COMPLÉTER!
        Cette méthode renvoit la position des cases vides dans la grille de Sudoku,
        sous la forme de tuples ``(i,j)`` où ``i`` est le numéro de ligne et ``j`` le numéro de colonne.
        *Variante avancée: Renvoyez un générateur sur les tuples de positions ``(i,j)`` au lieu d'une liste*
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of tuple of int
        """
        result = []
        for i in range(9):
            for j in range(9):
                if self.initial_grid[i][j]==0:
                    result.append((i,j))
        return result
        
        

    def write(self, i, j, v):
        """À COMPLÉTER!
        Cette méthode écrit la valeur ``v`` dans la case ``(i,j)`` de la grille de Sudoku.
        *Variante avancée: Levez une exception si ``i``, ``j`` ou ``v``
        ne sont pas dans les bonnes plages de valeurs*
        *Variante avancée: Ajoutez un argument booléen optionnel ``force``
        qui empêche d'écrire sur une case non vide*
        :param i: Numéro de ligne de la case à mettre à jour, entre 0 et 8
        :param j: Numéro de colonne de la case à mettre à jour, entre 0 et 8
        :param v: Valeur à écrire dans la case ``(i,j)``, entre 1 et 9
        """
        if i not in range(9) or j not in range(9) or v not in range(1,10):
            raise IndexError("Les valeurs ne sont pas bonnes (de 0 à 8)")
        else :
            self.initial_grid[i][j]=v
        

    def copy(self):
        """À COMPLÉTER!
        Cette méthode renvoie une nouvelle instance de la classe SudokuGrid,
        copie **indépendante** de la grille de Sudoku.
        Vous pouvez utiliser ``self.__class__(argument du constructeur)``.
        *Variante avancée: vous pouvez aussi utiliser ``self.__new__(self.__class__)``
        et manuellement initialiser les attributs de la copie.*
        """
        values_string=""
        for i in range(9):
            for j in range(9):
                values_string += str(self.initial_grid[i][j])
        return self.__class__(values_string)