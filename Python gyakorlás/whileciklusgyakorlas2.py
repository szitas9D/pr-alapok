név = input("Kérek egy nevet ")

while név == "":
    print(f"Nem írtál be nevet, kérem a nevedet!")
    név = input("Kérek egy nevet ")

print(f"Jó napot {név}")
