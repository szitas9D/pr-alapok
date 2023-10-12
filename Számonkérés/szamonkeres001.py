#Szitás Attila 10.D 1. csoport
#szamonkeres001.py
"""
Bekérek egy jegyet 1-5 írassuk ki a megadott jegyet értékkel és szövegesen,ha nem megfelelő jegyet adtam akkor írja ki a jegy értékét és mellé hogy nem megfelelő jegy
"""
jegy = input("Kérek egy jegyet 1 és 5 között")
jegy = int(jegy)
if jegy == 5 :
    print(f"A jegyed {jegy}-ös példás értékelést ér")
if jegy == 4 :
    print(f"A jegyed {jegy}-es jó értékelést ér")
if jegy == 3 :
    print(f"A jegyed {jegy}-as közepes értékelést ér")
if jegy == 2 :
    print(f"A jegyed {jegy}-es, elégséges értékelést ér")
if jegy == 1 :
    print(f"A jegyed {jegy}-es elégtelen értékelést ér")

