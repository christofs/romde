# cleanromde.py
# Function to clean up HTML scraped from archiv.romanistik.de. 
# Makes use of "re"; see: http://docs.python.org/2/library/re.html



#######################
# Import statements   #
#######################

import re
import glob
import os


#######################
# Functions           #
#######################

def removestuff(file,xmlmutandum):
    """ Removes the beginning and end of the files to leave just the actual content."""
    with open(file,"r") as mutandum:
        basename = os.path.basename(file)
        print(basename)
        mutandum = mutandum.read()
        mutandum = re.sub("[^#]*<div class=\"news-single-item\">","<item>",mutandum)
        mutandum = re.sub("<hr class=\"clearer\" />[^#]*","</item>",mutandum)
    with open(xmlmutandum,"w") as output:
        output.write(mutandum)
      
      
      
def cleanupabit(xmlmutandum):
    """ Removes unwanted stuff."""
    with open(xmlmutandum,"r") as mutandum:
        mutandum = mutandum.read()
        #Leerzeilen
        mutandum = re.sub("<p>&nbsp;</p>","",mutandum)
        #Semikolon (wegen CSV)
        mutandum = re.sub(";",",",mutandum)
        #Größer als in Kategorien
        mutandum = re.sub("&nbsp,&gt,&nbsp,","; ",mutandum)
        #Sonderzeichen
        mutandum = re.sub(""," ",mutandum)
        #<p> ohne Attribut (im Text)
        mutandum = re.sub("<p>","",mutandum)
        mutandum = re.sub("</p>","",mutandum)
        #Doppelte Zeilenumbrüche
        mutandum = re.sub("\n\n"," ",mutandum)        
        #Einfache Zeilenumbrüche
        mutandum = re.sub("\n"," ",mutandum)        
        #Kodierte Email
        mutandum = re.sub("<a href=\"javascript:linkTo_UnCryptMailto[^>]*>"," ",mutandum)
    with open(xmlmutandum,"w") as output:
        output.write(mutandum)
          
        
def renamestuff(xmlmutandum):
    """ Removes unwanted whitespace from the content of elements."""
    with open(xmlmutandum,"r") as mutandum:
        mutandum = mutandum.read()
        #kategorie
        mutandum = re.sub("<div class=\"news-catRootline\">","<div type=\"kategorie\">",mutandum)
        mutandum = re.sub(" <br />","",mutandum)
        mutandum = re.sub("<!-- Kategorie: Studium, Literaturwissenschaft, Medien/Kulturwissenschaft, Spanisch, Portugiesisch -->","",mutandum)
        #datum
        mutandum = re.sub("<div class=\"news-single-timedata\">","<date>",mutandum)
        mutandum = re.sub(" <!--[0-9][0-9]:[^#]*--></div>","</date>",mutandum)
        #titel
        mutandum = re.sub("<h2>","<title>",mutandum)
        mutandum = re.sub("</h2>","</title>",mutandum)   
        #ort     
        mutandum = re.sub(r"<li><span class='news-romde-single-label'>Ort:</span> ","<li type=\"place\">",mutandum)
        #disziplinen     
        mutandum = re.sub(r"<li><span class='news-romde-single-label'>Disziplinen:</span> ","<li type=\"disziplin\">",mutandum)
        #sprachen     
        mutandum = re.sub(r"<li><span class='news-romde-single-label'>Sprachen:</span> ","<li type=\"sprachen\">",mutandum)
        #beginn     
        mutandum = re.sub(r"<li><span class='news-romde-single-label'>Beginn:</span> ","<li type=\"beginn\">",mutandum)
        #ende     
        mutandum = re.sub(r"<li><span class='news-romde-single-label'>Ende:</span> ","<li type=\"ende\">",mutandum)
        #frist     
        mutandum = re.sub(r"<li><span class='news-romde-single-label'>Frist:</span> ","<li type=\"frist\">",mutandum)
        #autorin     
        mutandum = re.sub("<p class=\"news-single-author\">Von:&nbsp, ","<p type=\"autorin\">",mutandum)
        mutandum = re.sub("<p class=\"news-single-author\"> Von:&nbsp, ","<p type=\"autorin\">",mutandum)
        #redaktion     
        mutandum = re.sub(r"<p class=\"news-single-publisher\">Publiziert von: ","<p type=\"redaktion\">",mutandum)
        #frist     
        mutandum = re.sub(r"<li><span class='news-romde-single-label'>Frist:</span>","<li type=\"frist\">",mutandum)
        #text     
        mutandum = re.sub(r"</ul>","</ul>\n<inhalt>",mutandum)
        mutandum = re.sub(r"<p type=\"autorin\">","</inhalt>\n<p type=\"autorin\">",mutandum)
        #link     
        mutandum = re.sub(r"<a href='","<link>",mutandum)
        mutandum = re.sub(r"' target='_blank'>","</link>",mutandum)
        #arbeitszeit     
        mutandum = re.sub(r"<li><span class='news-romde-single-label'>Arbeitszeit:</span>","<li type=\"arbeitszeit\">",mutandum)
        #bezahlung     
        mutandum = re.sub(r"<li><span class='news-romde-single-label'>Bezahlung/Besoldungsklasse:</span>","<li type=\"bezahlung\">",mutandum)
        #befristung     
        mutandum = re.sub(r"<li><span class='news-romde-single-label'>Befristung:</span>","<li type=\"befristung\">",mutandum)
    with open(xmlmutandum,"w") as output:
        output.write(mutandum)


def write_output(file,xmlmutandum): 
    """Convenience function which saves transformed file to new filename. Needs to come last."""
    with open(xmlmutandum,"r") as mutandum:
        mutandum = mutandum.read()
    basename = os.path.basename(file)
    xmloutput = "./toextract/" + basename[:-5] + ".html"                       # Builds filename for outputfile from original filenames but correct extension.
    print(xmloutput)
    with open(xmloutput,"w") as output:
        output.write(mutandum)
        

#######################
# Main                #
#######################


def main(inputpath,xmlmutandum):
    for file in glob.glob(inputpath):
        removestuff(file,xmlmutandum)
        cleanupabit(xmlmutandum)
        renamestuff(xmlmutandum) 
        write_output(file,xmlmutandum)

            
main('./tocleanup/*.html',"MUTANDUM.xml")

