import sqlite3 as sql
import os
dosya = os.path.exists("D:\MyCodes\sqlite\veritabani.sqlite")


    

"""
    Veritabanı dosyasina baglanma / yeni oluşturma
vt1 = sql.connect("deneme.sqlite")      #(':memory:')/("") geçici veritabanı oluşturur.
vt = sql.connect("kitaplar.sqlite")
"""
vt = sql.connect("veritabani.sqlite")

"""
        imleç oluşturma
im = vt.cursor()
"""

im = vt.cursor()

#Ayni isme sahip bir tablo olusabilir. "already exist" hatasını almamak icin IF NOT EXİST
im.execute("CREATE TABLE IF NOT EXISTS adres_defteri('musteri isim' ,soyisim)")
im.execute("CREATE TABLE IF NOT EXISTS adress (a, b)")

#Tabloya veri eklemek :
if not dosya: # Busaydede her dosyaya bir kere yazılıyor
    im.execute("INSERT INTO adres_defteri VALUES('Ruchan', 'Yalçın')")

# Tabloya çoklu veri eklemek:
musteriler = [("Feyza","Gökbulut"), ("İsmail Fatih", "Demir"),
              ("Şerife","Yalçın"),("Talha","Çelik")]
for veri in musteriler:
    im.execute(""" INSERT INTO adres_defteri VALUES (? , ?) """, veri)
 
#Sütunların içerigini veritabanına islemek icin
vt.commit()

    
#Veritabanı içinde tablodan veri çekme SELECT veri FROM veritabanı
im.execute("SELECT * FROM adres_defteri")  # * hepsini seçiyor
im.execute("SELECT * FROM adres_defteri WHERE isim = 'Şerife'") # istediğimiz satırı seçiyor

#Seçilen verileri almak
veriler = im.fetchall()
tek_tek_veri = im.fetchone()
secili_veriler = im.fetchmany(8)
print(veriler)




vt.close()







