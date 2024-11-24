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

print(f"Fiyat\t: \t{ilan1.fiyat}\nAdres\t: \t{ilan1.adres}\n\
İlan no\t: \t{ilan1.ilanNo}\nİlan Tarihi: \t{ilan1.ilanTarihi}")

class HayvanAlemi(Ilan): # (Ilan) Ilan sınıfından miras alma oluyor.
    Türü = ""
    Irkı = ""
    Yaşı = ""
    Cinsiyeti = ""
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
    def __init__(self,fiyat="---",no="1",adres="--",tarih="",tip="-",kimden="sahibinden"):
        super().__init__(fiyat,no,adres,tarih)
        self.EmlakTipi = tip
        self.kimdenDurumu = kimden


emlak1 = Emlak("2500000","8875","Çan/Denizli","2024-11-15","Ev","Uygun")
print("\n\n\nemlak1.EmlakTipi: ",emlak1.EmlakTipi)

class KiralikEv(Emlak):
    def __init__(self,fiyat="---",no="0",adres="--",tarih="",tip="-",kimden="emlakcıdan",depozito=0):
        super().__init__(fiyat,no,adres,tarih,tip,kimden)
        self.Depozitos = depozito

class SatilikEv(Emlak):
    def __init__(self,fiyat="---",no="0",adres="--",tarih="",tip="-",kimden="emlakcıdan",tapu="Sorunsuz"):
        super().__init__(fiyat,no,adres,tarih,tip,kimden)
        self.tapuDurumu = tapu

class Tasit(Ilan):
    pass

ilan4 = SatilikEv(tapu="İskansız",fiyat="1000000")
print ("ilan4 ilanNoı: ",ilan4.ilanNo)

print("ilan4.tapuDurumu : ",ilan4.tapuDurumu, "\nFiyat:",ilan4.fiyat)
# print("emlak1.tapuDurumu : ",emlak1.tapuDurumu, "\nFiyat:",emlak1.fiyat)
print("\nemlak1 Fiyat:",emlak1.fiyat)

