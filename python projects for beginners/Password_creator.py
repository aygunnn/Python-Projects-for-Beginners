import random
import string

"""Defining the list of characters that contains all characters can creating by the keyboard"""
characters_list = list(string.printable)

"""Asking to user for length of password"""
length_of_pasword = int(input("Kaç haneli bir şifre oluşturmak istiyorsunuz ? \n"))

"""Creating a empty list for adding choosen letters"""
password = []

"""Selecting characters from the characters_list randomly and appending theese to the password list. This operation depends on length_of_password variable"""
for i in range(length_of_pasword):
    password.append(random.choice(characters_list).strip())

"""Printing the password to console without the apostrophes"""
print("".join(password))

"""The password will be hard to remember. So create a text document and save the password."""
with open("şifre.txt","w",encoding="utf-8") as file :
    file.write("".join(password))