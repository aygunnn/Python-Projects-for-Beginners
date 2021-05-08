"""
This application gets informations by the BeautifulSoup library from the target url. By the Requests module
Connect the url and get the html content from the url. Than work on this content easyly.
"""
import requests
from bs4 import BeautifulSoup

print("Getting the informatin...")
"""Detect the target URL."""
link = "https://www.imdb.com/chart/top/"

"""Take all htmla codes from the target URL."""
html_content = requests.get(link).content

"""Parse the content as like as a web site for work on it easyly."""
organized_content = BeautifulSoup(html_content,"html.parser")

"""Finding the list of films in the html content by entry level html knowledge."""
films_list = organized_content.find("tbody",{"class":"lister-list"}).find_all("tr")



"""Create a text that contains the wanted attiributes of the movies."""
with open("IMDB Movies.txt","w",encoding="utf-8") as file:
    for film in films_list:
        name = film.find("td",{"class":"titleColumn"}).find("a").text
        year = film.find("td",{"class":"titleColumn"}).find("span").text
        rating = film.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text

        file.write(f"{name} --- {year} --- {rating}\n")
