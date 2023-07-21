#menu isimli bir dictionary olusturuldu.
#key degerleri yemeklerden, values degerleri fiyatlardan olusturuldu.
menu = {"adana kebap" : [15,"Euro"],
        "urfa kebap" : [15,"Euro"],
        "pilav ustu et doner":  [20,"Euro"],
        "mercimek corba" : [5, "Euro"],
        "patates kizartma" : [10, "Euro"],
        "baklava" : [8, "Euro"],
        "sutlac" : [6, "Euro"],
        "kadayif" : [7, "Euro"],
        "kola" : [3, "Euro"],
        "fanta" : [3, "Euro"],
        "ayran" : [2, "Euro"],
        "su" : [1, "Euro"],
        "cay" : [1,"Euro"]}

#Yemekler ve fiyatlar kullanicinin secim yapmasi icin ekrana basildi.
for k,v in menu.items():
    print(k, "=", v)

#Girdilerin tamamini tutmak icin yeni bir sozluk olusturuldu.
hesap =  {}

#Kullanicidan siparisleri istendi ve sozluge(hesap) eklendi.
#Siparisi tamamlamak icin cikis olusturuldu.
while  True:
    siparis = input("Lutfen bir yemek adi yazin.(Cikmak icin 'q' basin.):".lower())
    if siparis == "q":
        break
    print(menu.items())
    # for s,p in menu.items():
        # if siparis == s:
            # hesap[s] = {p[0]}
            # pass
        # elif siparis != s:
            # print("Lutfen menuden bir yemek secin!")
            # break
            


#Siparis tutarinin hesaplanmasi icin 
# keys ve values degerlerini tutacak iki farkli liste olusturuldu.
fyt = []
sprs = []
for y,f in hesap.items():
    fyt.append(f)
    sprs.append(y)

#Fiyat hesaplanmasi yapildi
fiyat = [list(x) for x in fyt]
tutar = 0
for t in fiyat:
    tutar += t[0]

#Verilen yemek siparisi ve toplam tutari ekrana basildi.
print("Sirasisleriniz:",sprs)
print("Tutar:",tutar," ", "Euro")
