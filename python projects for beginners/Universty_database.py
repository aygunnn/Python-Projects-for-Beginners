import sqlite3


class ÜniversiteVeriTabanı():

    def __init__(self):
        """
        Creating a boolian veriable that controls the game.
        """
        self.sistem_durumu = True

    def menü(self):
        """
        Printing a basic menu for the user to the console.
        """
        print("""
=======VERİ TABANI SİSTEMİ=========
 1 - Kayıt oluştur
 2 - Kayıt sil
 3 - Kayıt bilgileri güncelleme
 4 - Kayıtlı öğrencileri yazdır
 5 - Çıkış yap
 """)

    def seçim(self):
        """
        The choose function for the user from the menu. This function calls another functions depends on the choose.
        """
        seç = int(input("Seçimizi Giriniz : "))

        if seç == 1:
            self.kayıt()
        elif seç == 2:
            self.sil()
        elif seç == 3:
            self.düzenle()
        elif seç == 4:
            self.yazdır()
        elif seç == 5:
            self.çıkış()
        else:
            print("Lütfen 1-4 arası bir seçim yapınız...")

    def kayıt(self):
        """
        Create an account function. Asks the variables from the user abouth the student. Adds the student by this informations to the database.
        """
        isim = input("Öğrencinin adını giriniz : ")
        soyisim = input("Öğrencinin soyadını giriniz : ")
        cinsiyet = input("Öğrencinin cinsiyetini giriniz : ")
        fakülte = input("Öğrencinin fakültesini giriniz : ")

        with sqlite3.connect("Üniversite Veritabanı.db") as bağlantı:

            imleç = bağlantı.cursor()
            imleç.execute("CREATE TABLE IF NOT EXISTS Veritabanı_sistemi(İsim TEXT,Soyisim TEXT,Cinsiyet TEXT,Fakülte TEXT)")
            imleç.execute("INSERT INTO Veritabanı_sistemi VALUES('{}','{}','{}','{}')".format(isim, soyisim, cinsiyet, fakülte))
            bağlantı.commit()

        print("Öğrenci başarıyla kaydedildi...")

    def sil(self):
        """
        This function deletes the variables from the database. Asks the name and surname informations for search student and deletes him/her.
        """

        silinecek_ad = input("Silinecek öğrencinin adını giriniz : ")
        silinecek_soyad = input("Silinecek öğrencinin adını giriniz : ")

        with sqlite3.connect("Üniversite Veritabanı.db") as bağlantı:
            imleç = bağlantı.cursor()
            imleç.execute("DELETE FROM Veritabanı_sistemi WHERE İsim = '{}' and Soyisim = '{}'".format(silinecek_ad, silinecek_soyad))
            bağlantı.commit()

        print("Öğrencinin kaydı başarıyla silindi...")

    def düzenle(self):
        """
        This function arrange the students name, surname, gender and faculty information. Prints a menu for the choose.
        """

        düzenlenecek_kişinin_adı = input("Düzenlemek istediğiniz kişinini adını giriniz : ")
        seçim_yap = int(input("""
        ------Güncelleme-------
        1 - ADI
        2 - SOYADI
        3 - CİNSİYETİ
        4 - FAKÜLTESİ
        kişinin hangi bilgisini güncellemek istiyorsunuz : 
        """))

        if seçim_yap == 1:
            yeni_ad = input("Yeni ismi giriniz : ")
            with sqlite3.connect("Üniversite Veritabanı.db") as bağlantı:
                imleç = bağlantı.cursor()
                imleç.execute("UPDATE Veritabanı_sistemi SET İsim = '{}' WHERE İsim = '{}'".format(yeni_ad, düzenlenecek_kişinin_adı))
                bağlantı.commit()
            print("Kayıt başarıyla güncellendi...")

        elif seçim_yap == 2:
            yeni_soyad = input("Yeni soyismi giriniz : ")
            with sqlite3.connect("Üniversite Veritabanı.db") as bağlantı:
                imleç = bağlantı.cursor()
                imleç.execute("UPDATE Veritabanı_sistemi SET Soyisim = '{}' WHERE İsim = '{}'".format(yeni_soyad, düzenlenecek_kişinin_adı))
                bağlantı.commit()
            print("Kayıt başarıyla güncellendi...")

        elif seçim_yap == 3:
            yeni_cinsiyet = input("Yeni cinsiyeti giriniz : ")
            with sqlite3.connect("Üniversite Veritabanı.db") as bağlantı:
                imleç = bağlantı.cursor()
                imleç.execute("UPDATE Veritabanı_sistemi SET Cinsiyet = '{}' WHERE İsim = '{}'".format(yeni_cinsiyet, düzenlenecek_kişinin_adı))
                bağlantı.commit()
            print("Kayıt başarıyla güncellendi...")

        elif seçim_yap == 4:
            yeni_fakülte = input("Yeni fakülteyi giriniz : ")
            with sqlite3.connect("Üniversite Veritabanı.db") as bağlantı:
                imleç = bağlantı.cursor()
                imleç.execute("UPDATE Veritabanı_sistemi SET Fakülte = '{}' WHERE İsim = '{}'".format(yeni_fakülte, düzenlenecek_kişinin_adı))
                bağlantı.commit()
            print("Kayıt başarıyla güncellendi...")

        else:
            print("Lütfen 1-4 arası bir seçim yapınız!!!")

    def yazdır(self):
        """
        Prints the saved students in the database in order to the console.
        """

        with sqlite3.connect("Üniversite Veritabanı.db") as bağlantı:
            imleç = bağlantı.cursor()
            imleç.execute("SELECT * from Veritabanı_sistemi")

            for veri in imleç.fetchall():
                print("""
        İsim : {}
        Soyisim : {}
        Cinsiyet : {}
        Fakülte : {}
        """.format(veri[0], veri[1], veri[2], veri[3]))

            bağlantı.commit()

    def çıkış(self):
        """
        The basic "exit" function depends on a boolian expression.
        """
        print("Program sonlandırılıyor...")
        self.sistem_durumu = False


sistem = ÜniversiteVeriTabanı() # CREATING AN OBJECT FROM THE CLASS.

while sistem.sistem_durumu: # CODE RUNS UNDER CONDITIONS.
    sistem.menü()
    sistem.seçim()

