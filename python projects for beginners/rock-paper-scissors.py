import random
import time

class RPS():

    def __init__(self):
        """
        Defining the variables for the game.
        """

        self.skorPC = 0
        self.skorOyuncu = 0
        self.oyunDurumu = True


    def menu(self):
        """
        Printing a menu to console for the user make a choice
        """
        print("""
        
        1 - TAŞ
        2 - KAĞIT
        3 - MAKAS

        """)


    def sec(self):
        """
        Choosing funtion for the user from the menu. Returns the string expression. Closes the game when selecting uncorrectly.
        """

        sec = int(input("Seçim yap : \n"))

        if sec == 1 :
            return "TAŞ"
        elif sec == 2 :
            return "KAĞIT"
        elif sec == 3 :
            return "MAKAS"
        else:
            print("Yanlış bir seçim yaptınız...")
            self.oyunDurumu = False
            return self.oyunDurumu


    def bilgisayaraSectir(self):
        """
        Playing against the computer. So this function makes a choose in the name of computer. Returns a string expression.
        """

        secenekler = ["TAŞ", "KAĞIT", "MAKAS"]
        secilen = random.choice(secenekler)
        return secilen


    def karsilastir(self):
        """
        This function calls "sec" (CHOOSE) and "bilgisayaraSectir" (CHOOSE FOR THE COMPUTER) function. After this, compare the returned expressions.
        Updates scores. Returns the string expression abouth the score.
        """

        ben = self.sec()
        pc = self.bilgisayaraSectir()

        if ben == "TAŞ":

            if pc == "TAŞ":
                return print("TAŞ - TAŞ ---> BERABERLİK\nDURUM {} - {}".format(self.skorOyuncu,self.skorPC))
            elif pc == "KAĞIT":
                self.skorPC += 1
                return print("TAŞ - KAĞIT ---> BİLGİSAYAR KAZANDI\nDURUM {} - {}".format(self.skorOyuncu,self.skorPC))
            elif pc == "MAKAS":
                self.skorOyuncu += 1
                return print("TAŞ - MAKAS ---> OYUNCU KAZANDI\nDURUM {} - {}".format(self.skorOyuncu,self.skorPC))

        elif ben == "KAĞIT":

            if pc == "TAŞ":
                self.skorOyuncu += 1
                return print("KAĞIT - TAŞ ---> OYUNCU KAZANDI\nDURUM {} - {}".format(self.skorOyuncu,self.skorPC))
            elif pc == "KAĞIT":
                return print("KAĞIT - KAĞIT ---> BERABERLİK\nDURUM {} - {}".format(self.skorOyuncu,self.skorPC))
            elif pc == "MAKAS":
                self.skorPC += 1
                return print("KAĞIT - MAKAS ---> BİLGİSAYAR KAZANDI\nDURUM {} - {}".format(self.skorOyuncu,self.skorPC))

        elif ben == "MAKAS":

            if pc == "TAŞ":
                self.skorPC += 1
                return print("MAKAS - TAŞ ---> BİLGİSAYAR KAZANDI\nDURUM {} - {}".format(self.skorOyuncu,self.skorPC))
            elif pc == "KAĞIT":
                self.skorOyuncu += 1
                return print("MAKAS - KAĞIT ---> OYUNCU KAZANDI\nDURUM {} - {}".format(self.skorOyuncu,self.skorPC))
            elif pc == "MAKAS":
                return print("MAKAS - MAKAS ---> BERABERLİK\nDURUM {} - {}".format(self.skorOyuncu,self.skorPC))


    def oyunKontrol(self):
        """
        This function checks the scores. Controls the limits of the scores and define the winner. Retruns boolian expression.
        """

        if self.skorOyuncu == 5:
            print("Oyuncu Kazandı...")
            time.sleep(10)
            self.oyunDurumu = False
            return self.oyunDurumu

        elif self.skorPC == 5:
            print("Oyuncu Kazandı...")
            time.sleep(10)
            self.oyunDurumu = False
            return self.oyunDurumu

        else:
            return self.oyunDurumu


oyun = RPS() # CREATING AN OBJECT FROM THE CLASS

while oyun.oyunKontrol(): # GAME RUNS UNDER THE CONDITIONS

    oyun.menu()
    oyun.karsilastir()
