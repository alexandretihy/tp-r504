def puissance(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError("Les deux nombres doivent être des entiers")
    
    if a == 0:
        if b < 0:
            raise ValueError("0 à une puissance négative est impossdef is_int(var):
    if type(var) != int:
        raise TypeError("Only integers are allowed")

def puissance(a, b):
    is_int(a)
    is_int(b)
    
    # 1. Gestion des cas où b est négatif
    if b < 0:
        if a == 0:
            raise ValueError("0 à une puissance négative est impossible")
        
        result = 1
        for i in range(-b):
            result *= a
        return 1 / result

    # 2. Cas où b >= 0 (y compris b = 0 et a = 0)
    if a == 0 and b > 0:
        return 0

    result = 1
    for i in range(b):
        result *= a
    return resultible")
        if b > 0:
            return 0
        return 1

    return a**b
