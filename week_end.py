### Total = 152
### Pierre : 38 => doit recevoir 7,6
### Marie : 54 =>  doir recevoir 23,6
### Anna : 52 => doit recevoir 21,6
### Beatrice : 8 => doit verser 22,4
### Sacha : 0 => doit verser 22,4

week_end_mai = {"Pierre" : [12, 70, 10], "Paul" : [100], "Marie" : [15], "Anna" : []}
week_end_juin = {"Pierre" : [15, 12, 8, 3], "Marie" : [20, 34] , "Anna" : [52], "Beatrice" : [8], "Sacha" : []}

def total(week_end):
    """renvoie le total des dépenses du week-end
    
    Args : - week_end (dico) : le dictionnaire avec les dépenses de chaque personne durant le week-end sous la forme {nom : dépenses}, nom (str), dépenses (list)
    
    Returns : - res (int) : le total de toutes les dépenses"""
    res = 0
    for dépenses in week_end.values(): #dépenses : list
        for dépense in dépenses: #dépense : int
            res += dépense
    return res


def test_total():
    assert total(week_end_mai) == 207 
    assert total(week_end_juin) == 152


def total_personne(week_end, nom):
    """renvoie le total des dépenses du week-end d'une personne
    
    Args : - week_end (dico) : le dictionnaire avec les dépenses de chaque personne durant le week-end sous la forme {nom : dépenses}, nom (str), dépenses (list)
           - nom (str) : le nom de la personne         
    
    Returns : - res (int) : le total de toutes les dépenses de la personne"""
    res = 0
    for dépense in week_end[nom]:
        res += dépense
    return res


def test_total_personne():
    assert total_personne(week_end_mai, "Pierre") == 92 
    assert total_personne(week_end_juin, "Sacha") == 0

def moyenne(week_end):
    """renvoie la moyenne que chaque dépenses
    
    Args : - week_end (dico) : le dictionnaire avec les dépenses de chaque personne durant le week-end sous la forme {nom : dépenses}, nom (str), dépenses (list)
    
    Returns : -res (float) : la moyenne"""
    return total(week_end) / len(week_end)

def test_moyenne():
    assert moyenne(week_end_mai) == 207 / 4
    assert moyenne(week_end_juin) == 152 / 5


def affiche_bilan_financier(week_end):
    """renvoie le bilan de financier du week-end
    
    Args : - week_end (dico) : le dictionnaire avec les dépenses de chaque personne durant le week-end sous la forme {nom : dépenses}, nom (str), dépenses (list)
    
    Returns : - print : un affichage des transactions qui doivent se faire par personne"""
    moy = moyenne(week_end)
    for personne in week_end:
        res = moy - total_personne(week_end, personne)
        if res > 0 :
            print(personne, "doit recevoir", res)
        elif res < 0:
            print(personne, "doit verser", -res)
        else:
            print(personne, "ne doit rien")
            
            
affiche_bilan_financier(week_end_mai)
affiche_bilan_financier(week_end_juin)