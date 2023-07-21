from random import randint

def rollDice(sayi):
    zar =[["bir",0],["iki",0],["uc",0],["dort",0],["bes",0],["alti",0]]

    sayi = 5000

    while sayi > 0:
        gelen_sayi = randint(1,6)
        sayi -= 1
        if gelen_sayi == 1:
            zar[gelen_sayi-1][1] += 1
        elif gelen_sayi == 2:
            zar[gelen_sayi-1][1] += 1 
        elif gelen_sayi == 3:
            zar[gelen_sayi-1][1] += 1 
        elif gelen_sayi == 4:
            zar[gelen_sayi-1][1] += 1 
        elif gelen_sayi == 5:
            zar[gelen_sayi-1][1] += 1 
        elif gelen_sayi == 6:
            zar[gelen_sayi-1][1] += 1 

    print("Zar'in 1 gelme olasiligi:",float(zar[0][1]/100))
    print("Zar'in 2 gelme olasiligi:",float(zar[1][1]/100))
    print("Zar'in 3 gelme olasiligi:",float(zar[2][1]/100))
    print("Zar'in 4 gelme olasiligi:",float(zar[3][1]/100))
    print("Zar'in 5 gelme olasiligi:",float(zar[4][1]/100))
    print("Zar'in 6 gelme olasiligi:",float(zar[5][1]/100))