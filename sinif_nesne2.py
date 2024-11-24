class Ogrenci(): # Büyük veri tipi (sınıflar veri kalıbıdır)
    ad = "tanimsiz"
    tc = "yok"
    ortalamasi = 0

print(Ogrenci.ad)

print(type(Ogrenci))
print(type(Ogrenci.ad))

ogrenci1 = Ogrenci()
print(type(ogrenci1))
print(type(ogrenci1.ad))
print(ogrenci1.ad)
ogrenci1.ad = "M.Ali"
print(ogrenci1.ad)


ogrenci2 = Ogrenci()
ogrenci2.ad = "Ebru"
print("ogrenci2.ad: ",ogrenci2.ad)
print("ogrenci1.ad: ",ogrenci1.ad)
print(Ogrenci)

# sinav1 = 7
# sinav2 = 5
# sinav1 = 8
# ad = "Ömer"
# ortalama = (sinav1+sinav2)//2

# print(ortalama) 
# print(type(sinav1))
# print(type(ad))
# print(sinav2*ad)
# # print(sinav2/ad)