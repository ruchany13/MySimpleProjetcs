import sqlite3
vt = sqlite3.connect("D:\MyCodes\sqlite\kitaplar.sqlite")
im = vt.cursor()

def veri_alma_fetchal():
    im.execute("SELECT name FROM sqlite_master")  # Veritabanındaki tabloların şemları sqlite master daolur
    tables = im.fetchall()
    print(tables)
    im.execute("SELECT * FROM kitaplar")
    veriler = im.fetchall()
    print(veriler)



def veri_alma_fetchone():
    im.execute("SELECT * FROM kitaplar")
    i = 0
    while i<5:
        print(im.fetchone())  # Verieleri teker teker alıyor
        i += 1

#veri_alma_fetchone()

def veri_alma_fetchmany():
    im.execute("SELECT * FROM kitaplar")
    print(im.fetchmany(3))  # istediğimiz kadar veriyi çekebiliyoruz

    
#veri_alma_fetchmany()


def veri_suzme():
    
    im.execute("UPDATE kitaplar SET Yazar = 'Ahmet' WHERE Yazar = 'Rıfat Ilgaz' AND KitapAdi = 'Hayat'")
    vt.commit()
    im.execute("SELECT * FROM kitaplar WHERE Yazar = 'Hma'")
    veri = im.fetchall()
    print(veri)
    


def veri_ekleme():
    table_name = "kitaplar"
    data = ("Yaşam", "Ahmet","35")
    ex = """INSERT INTO {} VALUES(?,?,?)""".format(table_name)
    print(ex)
    im.execute(ex, data)
    vt.commit()


veri_ekleme()

veri_suzme()

