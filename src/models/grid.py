#!/usr/bin/env python3

import sys

class SudokuGrid:
    """Cette classe représente une grille de Sudoku.
    Toutes ces méthodes sont à compléter en vous basant sur la documentation fournie en docstring.
    """
    # 1er indice -> ligne / 2e -> colonne
    #Grille initial

    def __init__(self, initial_values_str):
        """
        Ce constructeur initialise une nouvelle instance de la classe SudokuGrid.
        Il doit effectuer la conversation de chaque caractère de la chaîne en nombre entier,
        et lever une exception si elle ne peut pas être interprétée comme une grille de Sudoku.
        :param initial_values_str: Une chaîne de caractères contenant **exactement 81 chiffres allant de 0 à 9**,
            où ``0`` indique une case vide
        :type initial_values_str: str
        """
        self.initial_grid = [0]*9 
        l = len(initial_values_str) 
        if l!=81 : 
            raise ValueError('La chaine de caractère est de longueur {} mais devrait être 81'.format(l))
        else:            
            for i in range(9):
                self.initial_grid[i]=[int(initial_values_str[j]) for j in range(i*9,(i*9)+9)]
        

    def __str__(self):
        """
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
        """
        Cette méthode extrait une ligne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param i: Numéro de la ligne à extraire, entre 0 et 8
        :type i: int
        :return: La liste des valeurs présentes à la ligne donnée
        :rtype: set of int
        """
        return self.initial_grid[i]

    def get_col(self, j):
        """
        Cette méthode extrait une colonne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param j: Numéro de la colonne à extraire, entre 0 et 8
        :type j: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """
        col = []
        for i in range(9):
            col.append(self.initial_grid[i][j])
        return col

    def get_region(self, reg_row, reg_col):
        """
        Cette méthode extrait les valeurs présentes dans une région donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param reg_row: Position verticale de la région à extraire, **entre 0 et 2**
        :param reg_col: Position horizontale de la région à extraire, **entre 0 et 2**
        :type reg_row: int
        :type reg_col: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """
        region = []
        for i in range(reg_row*3, (reg_row*3)+3):
            for j in range(reg_col*3, (reg_col*3)+3):
                region.append(self.initial_grid[i][j])
        return region

    def get_empty_pos(self):
        """
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
        """
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
        """
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