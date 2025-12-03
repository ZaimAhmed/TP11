ATM={'Armand':'Beatrice','Beatrice':'Cesar',
     'Cesar':'Dalida','Dalida':'Cesar',
     'Etienne':'Beatrice','Firmin':'Henri',
     'Gaston':'Beatrice','Henri':'Firmin',
     'Léo' : 'Léa'}

def couples(dico):
    """renvoie les couples dont l’amour estréciproque
    
    Args : - dico (dict) : un dictionnaire la valeur associée à chaque clé est le nom de l’élu·e de son cœur
    
    Returns : - couples (list), une liste de 2-uplet composé des amours réciproques"""
    couples = []
    for amoureux in dico:
        if dico[amoureux] in dico.keys() and dico[dico[amoureux]] == amoureux and (dico[amoureux], amoureux) not in couples:
            couples.append((amoureux, dico[amoureux]))
    return couples



assert (couples(ATM)) == [('Cesar', 'Dalida'), ('Firmin', 'Henri')]


def soupirant(dico, nom):
    """renvoie toutes les personnes qui sont amoureuses de la personne en question
    
    Args : - dico (dict) : un dictionnaire la valeur associée à chaque clé est le nom de l’élu·e de son cœur
           - nom (str) : la personne donnée
           
    Returns : - res (list) : une liste des persoone sont amoureuses de la personne en question"""
    res = []
    for amoureux, dulciné in dico.items():
        if dulciné == nom:
            res.append(amoureux)
    return res

print(soupirant(ATM, 'Cesar'))