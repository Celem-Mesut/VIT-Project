class Hesap:
    def __init__(self, hesap_numarasi, bakiye):
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        self.bakiye += miktar
        print("İşlem başarıyla tamamlandı. Yeni bakiye:", self.bakiye)

    def para_cek(self, miktar):
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            print("İşlem başarıyla tamamlandı. Yeni bakiye:", self.bakiye)
        else:
            print("Hesapta yeterli bakiye yok.")

    def bakiye_sorgula(self):
        print("Toplam bakiye:", self.bakiye)


class Banka:
    def __init__(self):
        self.hesaplar = {}

    def hesap_olustur(self, hesap_numarasi, baslangic_bakiyesi):
        self.hesaplar[hesap_numarasi] = Hesap(
            hesap_numarasi, baslangic_bakiyesi)
        print("Hesap başarıyla oluşturuldu!")

    def hesap_kaldir(self, hesap_numarasi):
        del self.hesaplar[hesap_numarasi]
        print("Hesap başarıyla kaldırıldı.")

    def islem(self):
        while True:
            print("""
            Bankacılık sistemine hoş geldiniz!
            Lütfen bir seçenek seçin:
            1. Hesap oluştur
            2. Para yatırma
            3. Para çekme
            4. Hesap kaldırma
            5. Toplam bakiye sorgulama
            6. Çıkış
            """)

            secenek = input("Seçenek: ")

            if secenek == "1":
                hesap_numarasi = input("Hesap numarasını girin: ")
                baslangic_bakiyesi = float(
                    input("Başlangıç bakiyesini girin: "))
                self.hesap_olustur(hesap_numarasi, baslangic_bakiyesi)

            elif secenek == "2":
                hesap_numarasi = input("Hesap numarasını girin: ")
                miktar = float(input("Yatırılacak miktarı girin: "))
                self.hesaplar[hesap_numarasi].para_yatir(miktar)

            elif secenek == "3":
                hesap_numarasi = input("Hesap numarasını girin: ")
                miktar = float(input("Çekilecek miktarı girin: "))
                self.hesaplar[hesap_numarasi].para_cek(miktar)

            elif secenek == "4":
                hesap_numarasi = input("Hesap numarasını girin: ")
                self.hesap_kaldir(hesap_numarasi)

            elif secenek == "5":
                hesap_numarasi = input("Hesap numarasını girin: ")
                self.hesaplar[hesap_numarasi].bakiye_sorgula()

            elif secenek == "6":
                print("Programdan çıkılıyor...")
                break

            else:
                print("Geçersiz bir seçenek girdiniz, lütfen tekrar deneyin.")


uygulama = Banka()
uygulama.islem()