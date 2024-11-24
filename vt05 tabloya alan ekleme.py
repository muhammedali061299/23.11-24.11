# veritabanı sistemine bağlanmak için gerekli kodlar.
import mysql.connector

try:
  vts = mysql.connector.connect( # vts = veritabanı sistemi
    host="localhost", # Veritabanı sistemi adı (instance).
    user="root", # Veritabanı kullanıcı adı
    password="1234", # Veritabanı sistemi(instance) şifresi
    database="ots"
  )
  print("Bağlantı tamam:")  

  try:
    secilen = vts.cursor()
    # secilen.execute("CREATE TABLE ogrenciler (ad VARCHAR(50), telefon VARCHAR(30))")
    # secilen.execute("ALTER TABLE ogrenciler ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    secilen.execute("ALTER TABLE ogrenciler ADD COLUMN sehir VARCHAR(20)")
    print("Tablo oluşturuldu.")

  except mysql.connector.Error as hata:
    print(f"Tablo oluşturulamadı. Hata : {hata}")  


except:
  print("Veritabanına bağlanırken bir hata oluştu.")
# veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.

