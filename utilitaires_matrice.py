""" Fonctions utilitaires pour manipuler les matrices """

import API_matrice3 as matrice_util

def nb_occ(mat, val):
    """retourne le nombre de fois où val est dans la matrice mat"""
    occ = 0
    for i in range(matrice_util.get_nb_lignes(mat)):
        for j in range(matrice_util.get_nb_colonnes(mat)):
            if matrice_util.get_val(mat, i, j) == val:
                occ += 1
    return occ

def get_ligne(matrice, ligne):
    """renvoie sous la forme d'une liste la ligne de la matrice dont le numéro est spécifié.
    
    Args:
       matrice : une matrice
       ligne : la ligne de la matrice que l'on souhaite traitée
       
    Returns:
       li (list) : une liste représentant la ligne de la matrice"""
    nb_col = matrice_util.get_nb_colonnes(matrice)
    nb_li = matrice_util.get_nb_lignes(matrice)
    li = []
    if ligne >= 0 and ligne < nb_li:
        for i in range(ligne*nb_col, (ligne*nb_col)+nb_col):
            li.append(matrice_util.get_val(matrice, i, ligne))
        return li
    return None


def get_colonne(matrice, colonne):
    """renvoie sous la forme d'une liste la colonne de la matrice dont le numéro est spécifié.
    
    Args:
       matrice : une matrice
       colonne : la colonne de la matrice que l'on souhaite traitée
       
    Returns:
       col (list) : une liste représentant la colonne de la matrice"""
    nb_col = matrice_util.get_nb_colonnes(matrice)
    nb_li = matrice_util.get_nb_lignes(matrice)
    col = []
    if colonne >= 0 and colonne < nb_col:
        for i in range(colonne, (nb_li*nb_col), nb_col):
            col.append(matrice_util.get_val(matrice, colonne, i))
        return col
    return None