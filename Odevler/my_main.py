import my_dice

try:
    tekrar = int(input("Tekrar sayisini girin:"))
except ValueError:
    print("Pozitif bir sayi girin!")
except:
    print("Hata Olustu!")

my_dice.rollDice(tekrar)