kor = int(input("Írd be a korodat "))

while kor < 0:
    print(f"A korod nem lehet negatív")
    kor = int(input("Írd be a korodat"))
    
print(f"Te {kor} éves vagy")