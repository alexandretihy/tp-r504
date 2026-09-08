print("Hello, World!")

import fonctions as f

while True:
    a = input("nombre a : ")
    b = input("nombre b : ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        pass

    res = f.puissance(a, b)

    print (res)
