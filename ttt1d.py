from random import randrange

def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    return pole[:cislo_policka] + symbol + pole[cislo_policka+1:]

def tah_pocitace(herni_pole):
    "Dostane řetězec s herním polem, vybere pozici a vrátí herní pole se zaznamenaným tahem počítače"
    if "-" not in herni_pole:
        print("Všechna políčka už jsou obsazena. Hra dopadla následovně: ")
        return herni_pole
        
    if "x-" in herni_pole:
        pozice = herni_pole.index("x-")
        # print(pozice)
        return tah(herni_pole, pozice+1, 'o')
    elif "-x" in herni_pole: 
        pozice = herni_pole.index("-x")
        return tah(herni_pole, pozice, 'o')
    elif "o-" in herni_pole:
        pozice = herni_pole.index("o-")
        return tah(herni_pole, pozice+1, 'o')
    elif "-o" in herni_pole:
        pozice = herni_pole.index("-o")
        return tah(herni_pole, pozice, 'o')
    else:
        while True:
            pozice = randrange(0,19)
            if herni_pole[pozice] != "-":
                continue
            else: 
                return tah(herni_pole, pozice, "o")
        
print(tah_pocitace("--------x-"))
print(tah_pocitace("--o--xx---"))
print(tah_pocitace("----xo---x"))
print(tah_pocitace("xxo-------"))
print(tah_pocitace("oxoxoxoxox"))