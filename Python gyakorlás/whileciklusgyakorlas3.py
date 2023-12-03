étel = input("Kérek egy ételt mit szeretsz (a q-val kiléphetsz) ")
while not étel == "q":
    print(f"Te az {étel}-t szereted")
    étel = input("Kérek egy másik ételt mit szeretsz (a q-val kiléphetsz) ")

print(f"Viszlát")
