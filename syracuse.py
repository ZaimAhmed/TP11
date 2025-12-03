def syracuse(n, res):
    if n <= 1:
        return res + [1]
    elif n % 2 == 0:
        return syracuse(n//2, res + [n])
    else:
        return syracuse(3*n+1, res + [n])
    
def test_syracuse():
    assert syracuse(3, []) == [3, 10, 5, 16, 8, 4, 2, 1]
    assert syracuse(1, []) == [1]
    assert syracuse(2, []) == [2, 1]
    assert syracuse(5, []) == [5, 16, 8, 4, 2, 1]

print(len(syracuse(97, [])))

def temps_de_vol(n):
    return len(syracuse(n, []))

def champion(n):
    temps_connus = {}
    maxi = 1
    n_champ = None
    for i in range(1, n):
        tmp_vol = temps_de_vol_avec_precalcul(i, temps_connus)
        if tmp_vol > maxi:
            maxi = tmp_vol
            n_champ = i
    return n_champ

def temps_de_vol_avec_precalcul(n, temps_connus):
    if n not in temps_connus.keys():
        temps_connus[n] = temps_de_vol(n)
    return temps_connus[n]

print(champion(100000))
