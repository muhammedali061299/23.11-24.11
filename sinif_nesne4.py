class Ogrenci(): # Büyük veri tipi (sınıflar, nesnenin veri kalıbıdır)
    ad = "tanimsiz"
    tc = "yok"
    ortalamasi = 10
    def __init__(xx,aa="---",bb=tc,cc=ortalamasi): # xx ifadesi yerine genelde self ifadesi kullanılır.
        xx.ad = aa
        xx.tc = bb
        xx.ortalamasi = cc

# ogrenci1 = Ogrenci() # object initialization / yeni bir nesne oluşturma
# ogrenci1.ad = "Sude" # bu ve sonraki 3 satır ile yeni nesne özellikleri ayarlanır.
# ogrenci1.tc = "52365214754"
# ogrenci1.ortalamasi = 99
ogrenci1 = Ogrenci("Sude","52365214754",98) # bu satır üstteki üç satırın yaptığı işi yapar.
ogrenci1.disiplinNotu = 100
print("ogrenci1.disiplinNotu: ",ogrenci1.disiplinNotu)

ogrenci2 = Ogrenci()
ogrenci2.ad="Rahime"
ogrenci2.tc="41526385744"

print("ogrenci2.ortalamasi : ",ogrenci2.ortalamasi)
print("ogrenci2.ad : ",ogrenci2.ad)

ogrenci3 = Ogrenci() # init'i çalıştırır
print("ogrenci3.ad : ",ogrenci3.ad)

ogrenci4 = Ogrenci # init fonksiyonu çalışmadan nesne oluşur. (tercih edilen bir şey değil)
print("ogrenci4.ad : ",ogrenci4.ad)
