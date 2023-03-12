print("Kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)
# string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)
# int, integr => tam sayı
vade = 36
ekVade = 6
vade2 = "36"

# float, decimal, double
aylikOdeme = 200.50

# bool, boolean => true veya false
yukselisteMi = True

# Matematiksel opertatörler

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

# *
print(5 * 5)
print(vade * 2)
print(vade * ekVade)
print(10 * 10)

# /
print(5 / 5)
print(vade / 2)
print(vade / ekVade)
print(10 / 2)


yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operatörü -- bölme işleminden kalan
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)


# Mantıksal operatörler
print(1 == 1)
print(1 == 2)

# CTRL K + CTRL C  => Block yorum satırı
print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)


print(1 != 1)
print(1 != 2)

# or ve and keyword leri


print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)


# Karar yapıları
# if else 
sayi1 = 15
sayi2 = 15
# sayi1 sayi2 den büyükse ekrana sayi1 daha büyük yazdır

# indent  çok önemli
if sayi1 <= sayi2:
    print("sayi1 sayi2'den küçüktür")
# eğer if bloğuna girmezse
elif sayi1 == sayi2:
    print("iki sayı eşittir")
# eğer if ve else if bloklarından hiçbirine girmez ise
else:
    print("sayi1 sayi2'den büyüktür")

print("***************************")

if sayi1 <= sayi2:
    print("Sayı 1 Sayı 2 den küçüktür")
if sayi1 == sayi2:
    print("iki sayı eşittir")
else:
    print("sayi1 sayi2'den büyüktür")

print("Burası if bloğunun dışıdır")


