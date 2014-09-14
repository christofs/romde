#!/usr/bin/env python3
# Filename: cleanromde_pers.py

"""
# Function to clean up HTML scraped from romanistik.de/pers. 
# Makes use of "re"; see: http://docs.python.org/2/library/re.html
"""


#######################
# Import statements   #
#######################

from bs4 import BeautifulSoup
import csv
import re
import glob
import os


#######################
# Functions           #
#######################

     
def extract_persdata(file):
    soup = BeautifulSoup(open(file))
    basename = os.path.basename(file)
    identifier = str(basename[:-5])
    print(identifier)

    ### extract name 
    persname = soup.find('persname').text
    persname = str(persname)
    print("persname: " + persname)

    ### extract university 
    persuni = soup.find('persuni').text
    persuni = str(persuni)
    print("persuni: " + persuni)

    ### extract location 
    persadd = soup.find('persadd').text
    if len(persadd) < 2:
        persadd = re.sub(r'\n',r'##NA##',persadd)
    persadd = re.sub(r'\n\n',r'\n', persadd)
    persadd = re.sub(r'\n',r' ', persadd)
    persadd = str(persadd)
    print("persadd: " + persadd)

    ### extract website 
    website = soup.find('website').text
    #website = "<a href=\""+website+"\">www</a>"
    website = str(website)
    print("website: " + website)

    ### extract date person joined 
    joindate = soup.find('joindate').text
    joindate = str(joindate)
    print("persname: " + joindate)


    
    #### put together results
    rowstring = identifier + "\t" + persname + "\t" + website + "\t" + persuni + " -- " + persadd + "\t" + joindate
    print(rowstring)
    outputfile = "pers-data_v2.csv"   
    csv_output = open(outputfile, 'a', newline='\n') 
    csvwriter = csv.writer(csv_output)
    csvwriter.writerow([rowstring])
    csv_output.close()

  

#######################
# Main                #
#######################


def main(inputpath):
    for file in glob.glob(inputpath):
        extract_persdata(file)
            
main('./cleaned/*.html')

