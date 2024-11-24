class Ogrenci(): # Büyük veri tipi (sınıflar, nesnenin veri kalıbıdır)
    ad = "tanimsiz"
    tc = "yok"
    ortalamasi = 10

ogrenci1 = Ogrenci() # object initialization / yeni bir nesne oluşturma
ogrenci1.ad = "Sude" # bu ve sonraki 3 satır ile yeni nesne özellikleri ayarlanır.
ogrenci1.tc = "52365214754"
ogrenci1.ortalamasi = 99
ogrenci1.disiplinNotu = 100
print(ogrenci1.disiplinNotu)

ogrenci2 = Ogrenci()
ogrenci2.ad="Rahime"
ogrenci2.tc="41526385744"

print(ogrenci2.ortalamasi)

