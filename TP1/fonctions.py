def is_int(var):
    if type(var) != int:
        raise TypeError("Les deux nombres doivent être des entiers")

def puissance(a, b):
    # 1. Vérification des types
    is_int(a)
    is_int(b)

    # 2. Cas particulier : base égale à 0
    if a == 0:
        if b < 0:
            raise ValueError("0 à une puissance négative est impossible")
        if b > 0:
            return 0
        return 1

    # 3. Calcul par boucle for
    res = 1
    nb_iterations = b if b >= 0 else -b

    for i in range(nb_iterations):
        res *= a

    # 4. Si l'exposant était négatif, on renvoie l'inverse
    if b < 0:
        return 1 / res

    return res
