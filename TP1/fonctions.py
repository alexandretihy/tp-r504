def puissance(a, b):
    if not type(a) is int:
           raise TypeError("Les deux nombres doivent être des entiers")
    if not type(b) is int:
           raise TypeError("Les deux nombres doivent être des entiers")
    return a**b

def puissance(a, b):
    if not type(a) is int or not type(b) is int:        raise TypeError("Les deux nombres doivent être des entiers")
    
    if a == 0:
        if b < 0:
            raise ValueError("0 à une puissance négative est indéfini")
        if b > 0:
            return 0
      def puissance(a, b):

    if type(a) != int or type(b) != int:
        raise TypeError("Les deux nombres doivent être des entiers")
    

    if a == 0:
        if b < 0:
            raise ValueError("Puissance négative impossible pour 0")
        if b > 0:
            return 0
        return 1


    res = 1
    

    nb_iterations = b if b >= 0 else -b

    for i in range(nb_iterations):
        res = res * a


    if b < 0:
        return 1 / res

    return res



