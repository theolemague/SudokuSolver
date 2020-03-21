#-*-coding: utf8-*-

import random

class SudokuSolver:
    """Cette classe permet d'explorer les solutions d'une grille de Sudoku pour la résoudre.
    Elle fait intervenir des notions de programmation par contraintes
    que vous n'avez pas à maîtriser pour ce projet."""

    def __init__(self, grid):
        """À COMPLÉTER
        Ce constructeur initialise une nouvelle instance de solver à partir d'une grille initiale.
        Il construit les ensembles de valeurs possibles pour chaque case vide de la grille,
        en respectant les contraintes définissant un Sudoku valide.
        :param grid: Une grille de Sudoku
        :type grid: SudokuGrid
        """
        self.grid = grid        # Grille de sudokus
        self.position = self.grid.get_empty_pos()    # List contenant les positions des cases vides
        self.possible_val = [[1,2,3,4,5,6,7,8,9] for i in range(len(self.position))]  # List contenant les valeur possibles des cases vides
        self.reduce_all_domains()   # Suppression des valeurs impossibles dans les cases vides
                    
        
    def is_valid(self):
        """À COMPLÉTER
        Cette méthode vérifie qu'il reste des possibilités pour chaque case vide
        dans la solution partielle actuelle.
        :return: Un booléen indiquant si la solution partielle actuelle peut encore mener à une solution valide
        :rtype: bool
        """
        for i in range(len(self.position)): # Pour chaque case vides
            if not self.possible_val[i]:    # Si la list est vide
                return False                # Il n'y a plus de possibilités -> la solution partielle est bloquée
        return True
            
    def is_solved(self):
        """À COMPLÉTER
        Cette méthode vérifie si la solution actuelle est complète,
        c'est-à-dire qu'il ne reste plus aucune case vide.
        :return: Un booléen indiquant si la solution actuelle est complète.
        :rtype: bool
        """
        if not self.position:   # Si la list est vide
            return True         # Le sudoku est fini
        else: return False

    def reduce_all_domains(self):
        """À COMPLÉTER
        Cette méthode devrait être appelée à l'initialisation
        et élimine toutes les valeurs impossibles pour chaque case vide.
        *Indication: Vous pouvez utiliser les fonction ``get_row``, ``get_col`` et ``get_region`` de la grille*
        """
        for i in range(len(self.position)): # Pour chaque case vide
            row = self.grid.get_row(self.position[i][0])    
            col = self.grid.get_col(self.position[i][1])
            region = self.grid.get_region(int(self.position[i][0]/3), int(self.position[i][1]/3))
            for j in range(1,10):   # Pour un chiffre de 1 à 9 compris
                if j in row or j in col or j in region: # Si ce chiffre apparait deja dans la ligne, la colonne ou la region
                    self.possible_val[i].remove(j)      # Supprimer ce chiffre des valeurs possibilités de la case vide

    def reduce_domains(self, last_i, last_j, last_v):
        """À COMPLÉTER
        Cette méthode devrait être appelée à chaque mise à jour de la grille,
        et élimine la dernière valeur affectée à une case
        pour toutes les autres cases concernées par cette mise à jour (même ligne, même colonne ou même région).
        :param last_i: Numéro de ligne de la dernière case modifiée, entre 0 et 8
        :param last_j: Numéro de colonne de la dernière case modifiée, entre 0 et 8
        :param last_v: Valeur affecté à la dernière case modifiée, entre 1 et 9
        :type last_i: int
        :type last_j: int
        :type last_v: int
        """
        del self.possible_val[self.position.index((last_i,last_j))] # Supprimer la list des possibilités de la case remplie précédemment
        self.position.remove((last_i,last_j))       # # Supprimer le tuple des positions de la case remplie précédemment
        
        for n in range(len(self.position)): # Pour chaque case vide
            i = self.position[n][0]
            j = self.position[n][1]
            if i==last_i or j==last_j or int(i/3)==int(last_i/3)and int(j/3)==int(last_j/3):
            # Si cette cas appartient à la ligne, la colonne ou la region de la case remplie précédemment
                if last_v in self.possible_val[n]: # Si la valeur ajouter est dans la list des possibilités
                    self.possible_val[n].remove(last_v) # Supprimer cette valeur
        
        
    def commit_one_var(self):
        """À COMPLÉTER
        Cette méthode cherche une case pour laquelle il n'y a plus qu'une seule possibilité.
        Si elle en trouve une, elle écrit cette unique valeur possible dans la grille
        et renvoie la position de la case et la valeur inscrite.
        :return: Le numéro de ligne, de colonne et la valeur inscrite dans la case
        ou ``None`` si aucune case n'a pu être remplie.
        :rtype: tuple of int or None
        """
        for i in range(len(self.possible_val)): # Pour chaque case vide
            if len(self.possible_val[i])==1:    # S'il ny a qu'une seule possibilité
                self.grid.write(self.position[i][0], self.position[i][1], self.possible_val[i][0]) # remplir la case
                return (int(self.position[i][0]), int(self.position[i][1]), int(self.possible_val[i][0]))
        return None # Aucune case vide n'a qu'une possibilité


    def solve_step(self):
        """À COMPLÉTER
        Cette méthode alterne entre l'affectation de case pour lesquelles il n'y a plus qu'une possibilité
        et l'élimination des nouvelles valeurs impossibles pour les autres cases concernées.
        Elle répète cette alternance tant qu'il reste des cases à remplir,
        et correspond à la résolution de Sudokus dits «simple».
        *Variante avancée: en plus de vérifier s'il ne reste plus qu'une seule possibilité pour une case,
        il est aussi possible de vérifier s'il ne reste plus qu'une seule position valide pour une certaine valeur
        sur chaque ligne, chaque colonne et dans chaque région*
        """
        blocked = False
        while (not blocked):
            try :
                i, j, v = self.commit_one_var() # Remplir une case avec 1 seule possibilité
                self.reduce_domains(i, j, v)    # Mettre à jour la grille
                i, j, v = self.line_check()     # Remplir la ligne ou la colonne avec la valeur pour laquelle il n'y a qu'une possibilité
                if i != -1:
                    self.reduce_domains(i, j, v)

            except TypeError:
                blocked = True
    
    def line_check(self):
        """
        Cette méthode vérifie dans les cases vides d'une ligne et d'une colonne si un nombre n'apparait qu'une seule fois.
        Si c'est le cas elle l'ecrit dans sa case correspondante et renvoie la position et la valeur écrite
        Sinon elle renvoi -1 a chaque valeur pour continuer la resolution
        :rtype: tuple of int or None
        """
        for i in range(9):
            row_index_list=[]
            col_index_list=[]
            for index in range(len(self.position)):
                if self.position[index][0]==i:
                    row_index_list.append(index)
                if self.position[index][1]==i:
                    col_index_list.append(index)
                
            for nb in range(9):
                row_app_nb = 0
                col_app_nb = 0
                for index in row_index_list:
                    if nb in self.possible_val[index]:
                        row_app_nb +=1
                        app_index = index
                        if row_app_nb > 1:
                            continue
                if row_app_nb == 1 :
                    self.grid.write(self.position[app_index][0], self.position[app_index][1], nb)
                    return (int(self.position[app_index][0]), int(self.position[app_index][1]), int(nb))
                
                for index in col_index_list:
                    if nb in self.possible_val[index]:
                        col_app_nb +=1
                        app_index = index
                        if col_app_nb > 1:
                            continue
                if col_app_nb == 1 :
                    self.grid.write(self.position[app_index][0], self.position[app_index][1], nb)
                    return (int(self.position[app_index][0]), int(self.position[app_index][1]), int(nb))
        return (-1,-1,-1)

    def branch(self):
        """À COMPLÉTER
        Cette méthode sélectionne une variable libre dans la solution partielle actuelle,
        et crée autant de sous-problèmes que d'affectation possible pour cette variable.
        Ces sous-problèmes seront sous la forme de nouvelles instances de solver
        initialisées avec une grille partiellement remplie.
        *Variante avancée: Renvoyez un générateur au lieu d'une liste.*
        *Variante avancée: Un choix judicieux de variable libre,
        ainsi que l'ordre dans lequel les affectations sont testées
        peut fortement améliorer les performances de votre solver.*
        :return: Une liste de sous-problèmes ayant chacun une valeur différente pour la variable choisie
        :rtype: list of SudokuSolver
        """
        min_index = 0
        for list_per_case in self.possible_val:
            if len(list_per_case)<len(self.possible_val[min_index]):
                min_index = self.possible_val.index(list_per_case)

        for i in range(len(self.possible_val[min_index])):
            new_grid = self.grid.copy()
            new_grid.write(self.position[min_index][0], self.position[min_index][1], self.possible_val[min_index][i])
            yield SudokuSolver(new_grid)
    
    def solve(self):
        """
        Cette méthode implémente la fonction principale de la programmation par contrainte.
        Elle cherche d'abord à affiner au mieux la solution partielle actuelle par un appel à ``solve_step``.
        Si la solution est complète, elle la retourne.
        Si elle est invalide, elle renvoie ``None`` pour indiquer un cul-de-sac dans la recherche de solution
        et déclencher un retour vers la précédente solution valide.
        Sinon, elle crée plusieurs sous-problèmes pour explorer différentes possibilités
        en appelant récursivement ``solve`` sur ces sous-problèmes.
        :return: Une solution pour la grille de Sudoku donnée à l'initialisation du solver
        (ou None si pas de solution)
        :rtype: SudokuGrid or None
        """
        self.solve_step()
        if self.is_solved():
            return self.grid
        else : 
            if self.is_valid() :
                subsolver = self.branch()
                for solver in subsolver:
                    grid = solver.solve()
                    if type(grid) is not type(None):
                        return grid
            else :
                return None  
        