
import time
from datetime import date, datetime

def write_speed():

    """
    data -------------------------------------
        start_time = the time that write operation start
        finish_time = the time that write operation end
        text = the string that given by user and calculate the letter and word population
    result -----------------------------------------------
        wpm = words per minute
        ppm = pushes per minute
        total_time = the diffrence between start and finish
        words_list = splitted version of the text from blanks
    """
    
    words_list =[]

    start_time = datetime.now()

    text = input("Enter the text : ")

    finish_time = datetime.now()

    words_list = text.split(" ")
    total_time = (finish_time - start_time).seconds
    
    wpm = len(words_list) / (total_time/60)
    ppm = len(text) / (total_time/60)

    print("*"*40)
    print("{} Words in a minute.".format(wpm))
    print("{} letters in a minute.".format(ppm))
    

for i in reversed(range(1,4)):
    print(i)
    time.sleep(1)

write_speed()