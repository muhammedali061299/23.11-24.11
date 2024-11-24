# veritabanı sistemine bağlanmak için gerekli kodlar.
import mysql.connector

try:
  vts = mysql.connector.connect( # vts = veritabanı sistemi
    host="localhost", # Veritabanı sistemi adı (instance).
    user="root", # Veritabanı kullanıcı adı
    password="1234" # Veritabanı sistemi(instance) şifresi
  )
  print("Bağlantı tamam:")
  print(vts)

  try:
    secilen = vts.cursor()
    secilen.execute("CREATE DATABASE pythondersleri1")
    print("Veritabanı oluşturuldu.")

  except mysql.connector.Error as hata:
    print(f"Veri tabanı oluşturulamadı. Hata : {hata}")  


except:
  print("Veritabanına bağlanırken bir hata oluştu.")
# veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.

