#feladat_009_2
"""
Kérjünk be két egész számot, szám1 és szám2.
Hasonlítsuk össze a két számot, és írassuk ki, hogy a szám1 kisebb mint a szám2, vagy a szám2 kisebb mint a szám1,vagy a szám1 egyenlő szám2-vel.
"""

szam1 = input("Kérek egy egész számot")
szam1 = int(szam1)
szam2 = input("Kérek egy másik egész számot")
szam2 = int(szam2)

if szam1 < szam2 :
    print(f"A szám1 kisebb mint a szám2")


if szam2 < szam1 :
    print(f"A szám2 kisebb mint a szám1")

elif szam1 == szam2 :
    print(f"A szám1 egyenlő a szám2-vel")

#-----------------

if szam1 < szam2:
    print(f"A szám1 kisebb mint a szám2")
elif szam2 < szam1:
    print(f"A szám2 kisebb mint a szám 1")
elif szam1 == szam2:
    print(f"A szám1 egyenlő a szám2-vel")