def json_kayit(bilgi,dosya_adi="/Users/ahmetmesutcelem/VIT/Odevler/students.json"):
    with open(dosya_adi,"w") as d:
        json.dump(ogrenciler,d,indent=4)