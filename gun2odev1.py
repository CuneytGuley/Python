ogrenciler = ["Burak Yavaş", "Altan Ejder", "Mehmet Uluğ"]
def ogrenciListesiYazdir():
    for i in range(len(ogrenciler)):
        print(ogrenciler[i])

ogrenciListesiYazdir()
print("**************************************")

def ogrenciEkle(isim,soyisim):
    ogrenciler.append(f"{isim} {soyisim}")
    ogrenciListesiYazdir()

ogrenciEkle("Oya", "Balkır")
print("**************************************")

def ogrenciSil(isim, soyisim):
    ogrenciler.remove(f"{isim} {soyisim}")
    ogrenciListesiYazdir()

ogrenciSil("Oya", "Balkır")
print("**************************************")

def cokluOgrenciEkle():
    ogrenci1 = input("1.ci öğrencinin isim ve soyisim giriniz : ")
    ogrenci2 = input("2.ci öğrencinin isim ve soyisim giriniz : ")
    ogrenci3 = input("3.ci öğrencinin isim ve soyisim giriniz : ")
    ogrenciler.extend([f"{ogrenci1}", f"{ogrenci2}", f"{ogrenci3}"])
    ogrenciListesiYazdir()

cokluOgrenciEkle()
print("**************************************")

def ogrenciNoBul(isim, soyisim):
    ogrenciNo = ogrenciler.index(f"{isim} {soyisim}")
    print(f"Örencinin Numarası : {ogrenciNo}" )

ogrenciNoBul("Altan", "Ejder")
print("***********************************")




