from human import Human


faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade)+12)
#print(int(krediAdi))     Integer a çevirilemediği için hatalı
faiz = str(faiz)
print(type(faiz))

vade = 36 #int(input("Lütfen istediğiniz vade sayısını giriniz : "))
print(type(vade))
vade = vade + 12

# string interpolation
# Seçtiğiniz vade sonucu ortaya ıkan vade
print("Seçtiğiniz vade sonucu ortaya çıkan vade : " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade : {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade : {vade}")

isim = "Halit"
metin = "Merhaba {name}".format(name=123)
print(metin)


# f-string
metin = f"Hoşgeldiniz {1+1}"
print(metin)


# listeler
# döngüler
# fonksiyonlar

dizi = ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler))   #length
# print(krediler[3]) =>  hata verir out of range

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)


krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)

# for döngüsü
# i=0 i<10

for i in range(10):
    print("xxx")
    print(i)
print("*************************")

for i in range(5,11):
    print(i)

print("****************************")
for i in range(0,51,10):
    print(i)
print("******************************")
# for i in range(0.1,0,5):    hata verir. range fonksiyonu int değer kabul eder.
#     print(i)
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("********************")
for i in range(len(krediler)):
    print(krediler[i])
print("*************************")


# sonsuz döngü i yi arttırmazsak
i = 0
while i < 10:
    print("x")
    i += 1
print("y")


print("**************")
while True:
    print("X")
    break

print("********************")

i = 0
while i < len(krediler):
    print(krediler[i])
    i += 1  # Bu satırın nerede olduğuna göre çıktı değişir.
    if krediler[i] == "Konut Kredisi":
        break




# Fonksiyonlar

fiyat = 100
indirim = 20
# definition - fonksiyon tanımlama
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")


calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")


def calculateAndReturn(price, discount):
    return price-discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat+10)


def calculatePrice(price, discount):
    print(price-discount)

def calculatePriceAndReturn(price, discount):
    return price - discount

print("***********************************")
fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
print(f"159. satır : {fonk1}")
print(f"160. satır : {fonk2+50}")
print("*****************************")


# sınıflar => classes
# modules
# paket yönetimi

# Human sınıfı human.py dosyasına taşındı, bu sebeple import işlemi yapıldı ilk satırda

# instance => örnek  -- nesnelere ulaşabilmek için önce bir instance oluşturmalıyız.
human1 = Human("Enes")
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Halit")
human2.talk("Selam")
human2.walk()
print(human2)

Human("Melike").talk("Merhaba") # Bu şekilde de çalışır.

