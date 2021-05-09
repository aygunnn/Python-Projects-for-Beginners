import random
import time


class Blackjack():

    def __init__(self):
        """
        Main class of application. Game variables defined.
        """
        self.toplam1 = 0
        self.toplam2 = 0
        self.hamle = 0


    def kartSec(self):
        """
        "Card choose" function. Randomly select a card in cards list. Controls it and returns the value.
        """

        kartlar = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Q", "K", "J"] 
        kart = random.choice(kartlar)

        if kart == "A":
            sec = int(input("AS kartı, değer seçiniz (1 veya 10) \n\n"))
            return sec
        elif type(kart) != int:
            return 10
        else:
            return kart


    def sıraKımde(self):
        """
        "Detect the next player" function. Define the next player depends on number of moves. Retruns the function that "Switch_players" function.
        """

        if self.hamle % 2 == 0:
            return self.oyuncuDegis1()
        else:
            return self.oyuncuDegis2()


    def kontrol(self):
        """
        "Controls the game". The function that controls the win or loose situations. Reaching the top limits or passed it already etc. Returns boolian
        variable to "Control" function.
        """

        if self.toplam1 > 21:
            print("1. OYUNCU KAYBETTİ...\n\n")
            time.sleep(15)
            return False

        elif self.toplam2 > 21:
            print("2. OYUNCU KAYBETTİ...\n\n")
            time.sleep(15)
            return False
        
        elif self.toplam1 == 21:
            print("1. OYUNCU KAZANDI..!")
            time.sleep(15)
            return False

        elif self.toplam2 == 21:
            print("2. OYUNCU KAZANDI..!")
            time.sleep(15)
            return False

        else:
            return True


    def kartIste(self):
        """
        The function that draw a card. Asks the player first, than draws a card name of a player. Returns the "Choose card" function, 0 or "wrong choose"
        massage depends on selection.
        """

        ıste = input("Kart istiyor musunuz  (E/H)    ")
        ıste = ıste.capitalize()

        if ıste == "E":
            return self.kartSec()
        elif ıste == "H":
            return 0
        else:
            print("Yanlış bir seçim yaptınız...")


    def oyuncuDegis2(self):
        """
        Collect the scores of player_2. Increase the number of moves for pass to the next player. Prints the score of player_2 at end of all tours.
        """

        print("\n2. OYUNCUNUN SIRASI...\n")

        self.toplam2 += self.kartIste()

        
        print("2. OYUNCU TOPLAMI {}\n\n".format(self.toplam2))
        self.hamle += 1


    def oyuncuDegis1(self):
        """
        Collect the scores of player_2. Increase the number of moves for pass to the next player. Prints the score of player_2 at end of all tours.
        """

        print("\n1. OYUNCUNUN SIRASI...\n")

        self.toplam1 += self.kartIste()

        
        print("1. OYUNCU TOPLAMI {}\n\n".format(self.toplam1))
        self.hamle += 1




# OYUN BURDA ÇALIŞTIRILDI ## GAME RUNS AT HERE #

oyun = Blackjack() # CREATING AN OBJECT FROM THIS CLASS

while oyun.kontrol(): # CONDITION COMES FROM A FUNCTION THAT CONTROLS THE GAME SITUATION

    oyun.sıraKımde() 

"""
But there is a logical error here. Everybody knows this game. If you pick a card from the deck, you dont put it back the deck. In this game there is
a mistake abouth that. Every time you pick a card, cards coming from the same list, same member of cards list. But number of cards have to reduced after
every pick time.
"""

"""
I don't fix this on purpose. This code gives you an idea abouth my level at past. So how can i fix this mistake;
    1- We can detect more lists name of "Red_cards","Black_cards" and more Card_lists
    2- Than we select this list randomly when a card picking.
    3- We can delete the choosen card at the list.
"""
