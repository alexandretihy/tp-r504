def puissance(a, b):
    if not type(a) is int:
           raise TypeError("Les deux nombres doivent être des entiers")
    if not type(b) is int:
           raise TypeError("Les deux nombres doivent être des entiers")
    return a**b

def puissance(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError("Les deux nombres doivent être des entiers")
    
    if a == 0:
        if b < 0:
            raise ValueError("0 à une puissance négative est indéfini")
        if b > 0:
            return 0
        return 1

    return a**b




