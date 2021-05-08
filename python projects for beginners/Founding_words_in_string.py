"""
This application can 
    1- Print all words in the text
    2- Print all diffrent words in the text
    3- Print "how many words in this text"
    4- Print "how many diffrent words in this text"
    5- Sort all words 
    6- Find a word in the text
    7- Find how many times a word repeat
"""

class Metin():

    def __init__(self):
        """
        This function opens the text. Assings all the written things in the text to a variable. Turn this variable to a list and strips all the members of
        this list. Creates a List that contains all words an creates a Set that contains just diffrent words in the text.
        """

        with open("Nissan_GTR.txt","r",encoding="utf-8") as gtr :

            yazanlar = gtr.read()

            kelimeler = yazanlar.split() # içine bir şey yazmazsak boşluklardan ayırır

            self.sade_kelimeler = []

            for i in kelimeler :
                i.strip(".")
                i.strip(",")
                i.strip(":")
                i.strip(" ")

                self.sade_kelimeler.append(i)

            self.kelimeler_kümesi = set()

            for i in self.sade_kelimeler :
                    self.kelimeler_kümesi.add(i)

    def farklılar(self):
        """
        Prints the diffrent words in the text by the Set of words
        """

        print(self.kelimeler_kümesi)

    def farklıkelimesayısı(self):
        """
        This function prints how many diffrent words in the text. Set object has not got "len" methot. So do this with
        for loop.
        """

        farklı_kelimeler_listesi=[]

        for i in self.kelimeler_kümesi :
            farklı_kelimeler_listesi.append(i)

        print("Bu metinde {} farklı kelime geçmektedir...".format(len(farklı_kelimeler_listesi)))

    def toplamkelimesayısı(self):
        """
        In this basic function, it prints the len of all words.
        """

        print("Bu metinde {} kelime vardır...".format(len(self.sade_kelimeler)))

    def geçiyormu(self):
        """
        This function searches the word by given from user, in the text. Asks the word first.
        """

        kelime = input("Kelimenizi giriniz : ")

        if (kelime in self.sade_kelimeler):
            print("{} kelimesi metinde {} defa geçmektedir...".format(kelime,self.sade_kelimeler.count(kelime)))
        else :
            print("{} kelimesi bu metinde geçmemektedir...".format(kelime))

    def kelimeler(self):
        """
        This function prints all words
        """
        print("Kelimelerin Hepsi : \n",self.sade_kelimeler)

    def kelimelerisırala(self):
        """
        This function sorts the all words by alphabet
        """

        self.sade_kelimeler.sort()
        print(self.sade_kelimeler)

    def tekrar(self):
        """
        This fonction searches the given word in the text and prints how many times that word pass in this text.
        """

        kelimes=dict()

        for i in self.sade_kelimeler:
            if i in kelimes :
                kelimes[i] += 1
            else :
                kelimes[i] = 1

        for kelime,sayı in kelimes.items() :
            print("{} kelimesi {} defa geçiyor...".format(kelime,sayı))
            print("==========================================")

    



metin = Metin() # CREATING AN OBJECT FROM THE CLASS

print("""

            METİN İŞLEMLERİ SİSTEMİ
==================================================
0 - ÇIKIŞ

1 - TÜM KELİMELERİ BASIR
2 - FARKLI KELİMELERİ BASTIR
3 - TOPLAM KAÇ KELİMEDEN OLUŞTUĞUNU BUL
4 - KAÇ FARKLI KELİMEDEN OLUŞTUĞUNU BUL
5 - TÜM KELİMELERİ ALFABETİK OLARAK SIRALI BASTIR
6 - BİR KELİMEYİ METİNDE ARA
7 - KELİMENİN KAÇ DEFA TEKRAR ETTİĞİNİ BASTIR
===================================================

""") # PRINTING A MENU FOR THE USER

while True : # STARTS A INFINITE LOOP CONTAINS THE FUNCTIONS OF OBJECT. IT CAN BE BREAK BY "0".

    x=int(input("Bir işlem seçiniz : "))

    if x == 1 :
        metin.kelimeler()
    elif x == 2 :
        metin.farklılar()

    elif x == 3 :
        metin.toplamkelimesayısı()

    elif x == 4 :
        metin.farklıkelimesayısı()

    elif x == 5 :
        metin.kelimelerisırala()

    elif x == 6 :
        metin.geçiyormu()
    
    elif x == 7 :
        metin.tekrar()

    elif x == 0 :
        print("Çıkış yapılıyor...")
        break

    else : 
        print("Yanlış bir işlem seçtiniz...")

