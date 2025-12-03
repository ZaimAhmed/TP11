""" Matrices : API n 3 """


def matrice(nb_lignes, nb_colonnes, valeur_par_defaut):
    """crée une nouvelle matrice en mettant la valeur par défaut dans chacune de ses cases.

    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut : La valeur que prendra chacun des éléments de la matrice

    Returns:
        une nouvelle matrice qui contient la valeur par défaut dans chacune de ses cases
    """
    m = []
    for i in range(nb_lignes):
        m.append([valeur_par_defaut]*nb_colonnes)
    return m


def set_val(la_matrice, ligne, colonne, nouvelle_valeur):
    """permet de modifier la valeur de l'élément qui se trouve à la ligne et à la colonne
    spécifiées. Cet élément prend alors la valeur nouvelle_valeur

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)
        nouvelle_valeur : la nouvelle valeur que l'on veut mettre dans la case

    Returns:
        None
    """
    la_matrice[ligne][colonne] = nouvelle_valeur

def get_nb_lignes(la_matrice):
    """permet de connaître le nombre de lignes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de lignes de la matrice
    """
    return len(la_matrice)

def get_nb_colonnes(la_matrice):
    """permet de connaître le nombre de colonnes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de colonnes de la matrice
    """
    return len(la_matrice[0])

def get_val(la_matrice, ligne, colonne):
    """permet de connaître la valeur de l'élément de la matrice dont on connaît
    le numéro de ligne et le numéro de colonne.

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)

    Returns:
        la valeur qui est dans la case située à la ligne et la colonne spécifiées
    """
    return la_matrice[ligne][colonne]

# Fonctions pour l'affichage

def affiche_ligne_separatrice(la_matrice, taille_cellule=4):
    """fonction auxilliaire qui permet d'afficher (dans le terminal)
    une ligne séparatrice

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    print()
    for _ in range(get_nb_colonnes(la_matrice) + 1):
        print('-' * taille_cellule + '+', end = '')
    print()


def affiche(la_matrice, taille_cellule=4):
    """permet d'afficher une matrice dans le terminal

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    nb_colonnes = get_nb_colonnes(la_matrice)
    nb_lignes = get_nb_lignes(la_matrice)
    print(' '*taille_cellule+'|', end='')
    for indice in range(nb_colonnes):
        print(str(indice).center(taille_cellule) + '|', end = '')
    affiche_ligne_separatrice(la_matrice, taille_cellule)
    for ind in range(nb_lignes):
        print(str(ind).rjust(taille_cellule) + '|', end = '')
        for ind_j in range(nb_colonnes):
            print(str(get_val(la_matrice, ind, ind_j)).rjust(taille_cellule) + '|', end='')
        affiche_ligne_separatrice(la_matrice, taille_cellule)
    print()


# Ajouter ici les fonctions supplémentaires, sans oublier de compléter le fichier
def get_ligne(matrice, ligne):
    """renvoie sous la forme d'une liste la ligne de la matrice dont le numéro est spécifié.
    
    Args:
       matrice : une matrice
       ligne : la ligne de la matrice que l'on souhaite traitée
       
    Returns:
       li (list) : une liste représentant la ligne de la matrice"""
    if ligne >= 0 and ligne < get_nb_lignes(matrice):
        return matrice[ligne]

def get_colonne(matrice, colonne):
    """renvoie sous la forme d'une liste la colonne de la matrice dont le numéro est spécifié.
    
    Args:
       matrice : une matrice
       colonne : la colonne de la matrice que l'on souhaite traitée
       
    Returns:
       col (list) : une liste représentant la colonne de la matrice"""
    if colonne >= 0 and colonne < get_nb_colonnes(matrice):
        col = []
        for i in range(get_nb_lignes(matrice)):
            col.append(matrice[i][colonne])
        return col
# tests_API_matrice.py avec des fonctions de tests
