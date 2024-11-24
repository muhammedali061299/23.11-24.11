class Ilan():
    fiyat = "tanımsiz" # propty = özellik 
    ilanNo = "yok"
    adres = "---"
    ilanTarihi = "tanımlanmamış"
    def __init__(ilan,fiyati=fiyat,no=ilanNo,adresi=adres,tarih=ilanTarihi): # ilan = self
        ilan.fiyat = fiyati
        ilan.ilanNo = no
        ilan.adres = adresi
        ilan.ilanTarihi = tarih

ilan1 = Ilan("Ücretsiz Sahiplendirme","452","Çankaya/Ankara","2024-11-10")

# print(ilan1)
print(f"Fiyat\t: \t{ilan1.fiyat}\nAdres\t: \t{ilan1.adres}\n\
İlan no\t: \t{ilan1.ilanNo}\nİlan Tarihi: \t{ilan1.ilanTarihi}")

class HayvanAlemi(Ilan): # (Ilan) Ilan sınıfından miras alma oluyor.
    # fiyat = "tanımsiz" # Miras alma sayesinde bu ve sonraki 3 satırı tekrar yazmadık.
    # ilanNo = "yok"
    # adres = "---"
    # ilanTarihi = "tanımlanmamış"

    Türü = ""
    Irkı = ""
    Yaşı = ""
    Cinsiyeti = ""
    # def __init__(ilan,fiyati=fiyat,no=ilanNo,adresi=adres,tarih=ilanTarihi): # ilan = self
    def __init__(xx,fiyati="Ücretsiz Sahiplendirme",no="0",adresi="--",tarih="",tur="",irk="",yas=0,cins="Tanimsiz"): # ilan = self
        super().__init__(fiyati,no,adresi,tarih) # Sınıf yanındaki () ifadesi init fonksionunu çalıştıtrır
        xx.Türü = tur
        xx.Irkı = irk
        xx.Yaşı = yas
        xx.Cinsiyeti = cins

hayvan1 = HayvanAlemi("Sahiplendirme","8887","Merkez/KONYA","2024-11-11","Siyam","Kırma",2,"Ekek")
print("hayvan1.ilanNo: ",hayvan1.ilanNo)
print("hayvan1.Yaşı: ",hayvan1.Yaşı)

hayvan2 = HayvanAlemi()

class Emlak(Ilan):
    pass

class Tasit(Ilan):
    pass

