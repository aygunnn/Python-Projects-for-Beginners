import time

class TTT():

    def __init__(self):
        """
        In this function defining a "move" variable, a condition for the game and a basic board.
        """

        self.sira = 0
        self.oyun = True
        self.tahta = [["   ","   ","   "],["   ","   ","   "],["   ","   ","   "]]

    def oyunuGoster(self):
        """
        Prints the board to the console.
        """
        for satır in self.tahta:
            print(satır)

    def siraKimde(self):
        """
        Defines the player depends on the number of moves.
        """
        
        if self.sira %2 == 0 :
            self.oyuncu1Sec()

        else :
            self.oyuncu2Sec()

    def oyuncu1Sec(self):
        """
        Player_1 choosing a spot for placing the sign of himself/herself ("X"). Controls the line and column by the function named "doluMU"
        If the board allows the operation, player_1 signs this spot.
        """
        
        print("1. OYUNCU SEÇİM YAPIYOR...")

        satir = int(input("SATIRI SEÇİNİZ :  "))
        if satir < 4 and satir > 0 :
            sutun = int(input("SÜTUNU SEÇİNİZ :  "))
            if sutun < 4 and sutun > 0 :
                if self.doluMu(satir-1,sutun-1) == False :
                    self.tahta[satir-1][sutun-1] = "X"
                    self.sira += 1
                else :
                    print("BU KONUM DOLU..!")
            else :
                print("YANLIŞ BİR KONUM SEÇTİNİZ..!")
        else :
            print("YANLIŞ BİR KONUM SEÇTİNİZ..!")

    def oyuncu2Sec(self):
        """
        Player_2 choosing a spot for placing the sign of himself/herself ("O"). Controls the line and column by the function named "doluMU"
        If the board allows the operation, player_1 signs this spot.
        """

        print("2. OYUNCU SEÇİM YAPIYOR...")

        satir = int(input("SATIRI SEÇİNİZ :  "))
        if satir < 4 and satir > 0 :
            sutun = int(input("SÜTUNU SEÇİNİZ :  "))
            if sutun < 4 and sutun > 0 :
                if self.doluMu(satir-1,sutun-1) == False :
                    self.tahta[satir-1][sutun-1] = "O"
                    self.sira += 1
                else :
                    print("BU KONUM DOLU..!")
            else :
                print("YANLIŞ BİR KONUM SEÇTİNİZ..!")
        else :
            print("YANLIŞ BİR KONUM SEÇTİNİZ..!")

    def doluMu(self,sat,sut):
        """
        Controls the line and columns abouth the emptyness situations.
        """
        
        if self.tahta[sat][sut] == "   ":
            return False
        elif self.tahta[sat][sut] != "   ":
            return True
    
    def kontrol(self):
        """
        This function controls the game on horizonal, vertical and cross axises. Prints the winner if there is one. Returns a boolian expression.
        """
        
        # DİKEY KONTROL
        if [self.tahta[0][0],self.tahta[1][0],self.tahta[2][0]] == ["X","X","X"] :
            print("1. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        elif [self.tahta[0][0],self.tahta[1][0],self.tahta[2][0]]== ["O","O","O"] :
            print("2. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        elif [self.tahta[0][1],self.tahta[1][1],self.tahta[2][1]]== ["X","X","X"] :
            print("1. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        elif [self.tahta[0][1],self.tahta[1][1],self.tahta[2][1]]== ["O","O","O"] :
            print("2. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        elif [self.tahta[0][2],self.tahta[1][2],self.tahta[2][2]] == ["X","X","X"] :
            print("1. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        elif [self.tahta[0][2],self.tahta[1][2],self.tahta[2][2]] == ["O","O","O"]:
            print("2. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)

        #YATAY KONTROL
        elif [self.tahta[0][0],self.tahta[0][1],self.tahta[0][2]]== ["X","X","X"] :
            print("1. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        elif [self.tahta[0][0],self.tahta[0][1],self.tahta[0][2]]== ["O","O","O"]:
            print("2. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        elif [self.tahta[1][0],self.tahta[1][1],self.tahta[1][2]]== ["X","X","X"] :
            print("1. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        elif [self.tahta[1][0],self.tahta[1][1],self.tahta[1][2]]== ["O","O","O"]:
            print("2. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        elif [self.tahta[2][0],self.tahta[2][1],self.tahta[2][2]]== ["X","X","X"] :
            print("1. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        elif [self.tahta[2][0],self.tahta[2][1],self.tahta[2][2]]== ["O","O","O"]:
            print("2. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)

        #ÇAPRAZ KONTROL
        elif [self.tahta[0][0],self.tahta[1][1],self.tahta[2][2]]== ["X","X","X"] :
            print("1. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        elif [self.tahta[0][0],self.tahta[1][1],self.tahta[2][2]] == ["O","O","O"]:
            print("2. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        elif [self.tahta[0][2],self.tahta[1][1],self.tahta[2][0]] == ["X","X","X"] :
            print("1. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        elif [self.tahta[0][2],self.tahta[1][1],self.tahta[2][0]] == ["O","O","O"] :
            print("2. OYUNCU KAZANDI")
            self.oyun = False
            time.sleep(20)
        
    def full(self):
        """
        This function controls the board. If there is not a empty slot and if there is not a winner tat means board is full.
        Returns boolian expression.
        """

        liste = []

        for i in self.tahta:
            for j in i :
                liste.append(j)

        if "   " not in liste :
            return True
        else :
            return False
                
    def oyunDurumu(self):
        """
        Basic function that returns the boolian variable name like "oyun". By this function we can control game situation easyly.
        """
        return self.oyun
        


oyun = TTT() # CREATING A GAME OBJECT

while oyun.oyunDurumu() : # GAME RUNS UNDER CONDITIONS

    oyun.oyunuGoster()
    oyun.siraKimde()
    oyun.kontrol()
    
    if oyun.full(): 
        print("TAHTA DOLDU. KAZANAN YOK...")
        print("20 SANİYE SONRA OYUN KAPANACAK")
        time.sleep(20)
    else :
        pass
    