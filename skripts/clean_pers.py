#!/usr/bin/env python3
# Filename: cleanromde_pers.py

"""
# Function to clean up HTML scraped from romanistik.de/pers. 
# Makes use of "re"; see: http://docs.python.org/2/library/re.html
"""


#######################
# Import statements   #
#######################

import re
import glob
import os


#######################
# Functions           #
#######################

def clean_romdepers(file):
    """ Removes the beginning and end of the files to leave just the actual content."""
    with open(file,"r") as mutandum:
        mutandum = mutandum.read()
        basename = os.path.basename(file)
        identifier = basename[0:4]
        #print(identifier)
        
        ### Simplify the file
        mutandum = re.sub("[^#]*<h2>","<h2>",mutandum)
        mutandum = re.sub("<footer>[^#]*","",mutandum)
        #print(mutandum)
        
        ### Identify data
        mutandum = re.sub(r'<h2>([^#]*)</h2>',r'<persname>\1</persname>',mutandum)
        mutandum = re.sub(r'Institution</dt>\n<dd>([^#]*)</dd>\n<dt>Adresse',r'Institution</dt>\n<persuni>\1</persuni>\n<dt>Adresse',mutandum)
        mutandum = re.sub(r'Adresse</dt>\n<dd>([^#]*?)</dd>\n<dt>([Status|E-Mail|Webseite])',r'Adresse</dt>\n<persadd>\1</persadd>\n<dt>\2',mutandum)
        mutandum = re.sub(r'Webseite</dt>\n<dd>([^#]*?)</dd>\n<dt>([Status|E-Mail])',r'Webseite</dt>\n<website>\1</website>\n<dt>\2',mutandum)
        #print(mutandum)
       
        ### Supply missing entries
        if "<dt>Hochschule / Institution</dt>" not in mutandum: 
            mutandum = re.sub(r'</persname>\n', r'</persname>\n<dt>Hochschule / Institution</dt>\n<persuni>##NA##</persuni>', mutandum)
        if "<dt>Adresse</dt>" not in mutandum: 
            mutandum = re.sub(r'</persname>\n', r'</persname>\n<dt>Adresse</dt>\n<persaddress>##NA##</persaddress>', mutandum)
        if "<dt>Webseite</dt>" not in mutandum: 
            mutandum = re.sub(r'</persname>\n', r'</persname>\n<dt>Webseite</dt>\n<website>##NA##</website>', mutandum)
       
        ### Write new file to target folder
        xmloutput = "./cleaned/" + basename[:-5] + ".html" 
        print(xmloutput)
        with open(xmloutput,"w") as output:
            output.write(mutandum)

 
      
#######################
# Main                #
#######################


def main(inputpath):
    for file in glob.glob(inputpath):
        clean_romdepers(file)
            
main('./pers/*.html')

