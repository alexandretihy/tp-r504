def puissance(a, b):
    if not type(a) is int:
           raise TypeError("Les deux nombres doivent être des entiers")
    if not type(b) is int:
           raise TypeError("Les deux nombres doivent être des entiers")
    return a**b




