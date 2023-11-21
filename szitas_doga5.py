nev=input("Írd be a nevedet: ")
kor=int(input("Írd be az életkorodat: "))

if 0<=kor<=3:
    print(f"0-tól 3 év:A legfiatalabb kiskorú!")
if 4<=kor<=6:
    print(f"4-től 6 év:Óvodás korban van!")
if 7<=kor<=18:
    print(f"7-től 18 év:Érettségi előtt álló ifjú!")
if 19<=kor<=25:
    print(f"19-től 25 év:Egyetemita vagy ifjú munkavállaló!")
if 26<=kor<=65:
    print(f"26-tól 65 év:Aktív dologozó ember!")
if 66<=kor<=100:
    print(f"66-tól 100 év:Megérdemelt nyugdíjas éveit élvezi!")
else:
    print(f"Ritka mint a fehér holló")
