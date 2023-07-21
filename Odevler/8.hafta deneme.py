










class Hesap:
    def __init__(self,hesap_numarasi,hesap_sahibi,bakiye):
        self.hesap_numarasi = hesap_numarasi
        self.hesap_sahibi = hesap_sahibi
        self.bakiye = bakiye


    def para_yatirma(self,miktar):
        self.bakiye += miktar
        return (f"Toplam bakiye {self.bakiye}")

    def para_cekme(self,miktar):
        self.bakiye -= miktar
        return (f"Kalan bakiye {self.bakiye}")
    
    def bakiye_sorgulama(self):
        return (f"Mevcut Bakiyeniz:{self.bakiye}")
    
class Banka(Hesap):
    def __init__(self, hesap_numarasi, hesap_sahibi, bakiye,hesap_listesi):
        super().__init__(hesap_numarasi, hesap_sahibi, bakiye,)
        self.hesap_listesi = hesap_listesi

    def hesap_ekle(self):
        hesap_numarasi = input("Hesap numaranizi girin:")
        baslangic = input("Baslangic bakiyesini girin:")
        musteriler = [obj for obj in globals().values() if isinstance(obj,Hesap)]
        for x in musteriler:
            if hesap_numarasi == x:
                print("Bu hesab numarasi kullanilmaktadir! Baska bir hesap numarasi Girin")
            else:
                self.hesap_numarasi2 = hesap_numarasi
                self.bakiye2 = baslangic
    
    
    def hesap_kaldir(self):
        hesap_kaldir = input("Hesap numaranizi girin:")
        musteriler = [obj for obj in globals().values() if isinstance(obj,Hesap)]
        for x in musteriler:
            if hesap_kaldir == x:
                x = 0

    def toplam_bakiye(self):
        return(f"Toplam bakiyeniz: {self.bakiye + self.bakiye2}")
    
musteri1 = Hesap(2222,"Ali",1000)













# print(musteri1)
# def menu():
#         secim = int(input("""
#         #HOSGELDINIZ#
#         -------------
#         BIR ISLEM SECINIZ:
#         1-)Hesap Olustur

#         2-)Hesap Kaldir

#         3-)Para Yatirma

#         4-)Para Cekme

#         5-)bakiye sorgulama

#         6-)Cikis
        
#         """))
#         if secim == 6:
#             quit
#         elif secim == 1:
#             Hesap.hesap_ekle()
#         elif secim == 2:
#             Hesap.hesap_kaldir()
#         elif secim == 3:
#             Hesap.para_yatirma()
#         elif secim == 4:
#             Hesap.para_yatirma()
#         elif secim == 5:
#             Hesap.bakiye_sorgulama()


# print(menu())