# extractdata.py
# Script using Beautiful Soup to extract data from romanistik.de pages. 

from bs4 import BeautifulSoup
import re
import csv
import glob
import os


def extract_data(file):
    soup = BeautifulSoup(open(file))
    #extract title
    title = soup.find('title').text
    #extract datum 
    inhalt = soup.find('inhalt').text
    #identifier
    basename = os.path.basename(file)
    identifier = basename[:-5]
    print(identifier + "; " + inhalt)
    
    txtoutput = "./inhalt/" + identifier + ".txt"     # Builds filename for outputfile from original filenames.
    with open(txtoutput,"w") as output:                  # Writes selected text to TXT file in folder specified above.
        output.write(title + "\n" + inhalt)

def main(inputpath):
    for file in glob.glob(inputpath):
        extract_data(file)

main("./toextract/*.html")



"""
VERSION 0.2

def extract_data(file):
    soup = BeautifulSoup(open(file))
    #extract datum 
    datum = soup.find('date')
    datumstring = datum.contents[0]
    #extract kategorie 
    kategorie = soup.find(type="kategorie")
    kategoriestring = kategorie.contents[0]
    #extract title
    title = soup.find('title')
    titlestring = title.contents[0]
    #extract place
    place = soup.find(type="place")
    placestring = place.contents[0]
    #extract sprache
    sprache = soup.find(type="sprachen")
    sprachestring = sprache.contents[0]
    #extract disziplin
    disziplin = soup.find(type="disziplin")
    disziplinstring = disziplin.contents[0]
    #extract inhalt
    inhalt = soup.find('inhalt')
    inhaltstring = inhalt.contents[0]
    #identifier
    basename = os.path.basename(file)
    identifier = basename[:-5]
    print(identifier + "; " + kategoriestring + "; " + titlestring + "; " + placestring + "; " + sprachestring + "; " + disziplinstring + "; ")

def main(inputpath):
    for file in glob.glob(inputpath):
        extract_data(file)

main("./testextract/*.html")

"""



"""
VERSION 0.1
def extract_data(file):
    soup = BeautifulSoup(open(file))
    #show file
    #print(soup.prettify())
    #extract title
    titles = soup.find_all('title')
    for title in titles:
        titlestring = title.contents[0]
        print("Title: " + titlestring)
    #extract place
    places = soup.find_all(type="place")
    for place in places:
        placestring = place.contents[0]
        print("Ort: " + placestring)

def main(inputpath):
    for file in glob.glob(inputpath):
        extract_data(file)

main("./input/*.html")
"""
