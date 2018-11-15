# Naam: Christiaan Posthuma
# Datum: vandaag 11 okt
# Versie: 1.0.0.0

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

########################################
import tkinter as tk    #importeer methodes voor keuzemenu vanuit tkinder module
import tkinter.filedialog as tkFile

openwindow = tk.Tk()   #opent een window voor het keuzemenu
openwindow.withdraw()   #haalt datzelfde window weer weg(alleen nodig om het keuzemenu te weergeven
##########################################


# Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
"""
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """
def Main():
    bestand = open(tkFile.askopenfilename(),"r").readlines()
    headers, sequences = lees_inhoud(bestand)

    searchterm= input("Enter a search term: ")
    for i in range(len(headers)):        #lengte headers=len sequences
        if searchterm in headers[i]:
            if is_dna(sequences[i]) == True:                   
                print("\n",headers[i])
                knipt(sequences[i])
                is_dna(sequences[i])
                
            
    

    # schrijf hier de rest van de code nodig om de aanroepen te doen
    
    
def lees_inhoud(bestand):
    
       
    """
    Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
    Lever twee lijsten op:
        - headers = [] met daarin alle headers
        - seqs = [] met daarin alle sequenties behorend bij de headers
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """

    headers, sequences= [],[]
    seq = ""
    for line in bestand:
        line=line.strip()
        if line.startswith(">"):
            if seq != "":
                sequences.append(seq)
                seq = ""
            headers.append(line)
        else:
            seq += line
    sequences.append(seq)
    return headers, sequences
     
    

    
def is_dna(sequence):
    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """
    count = 0

    sequencex =  sequence.upper()   
    for letter in sequencex:
        if not letter in ["A","C","T","G"]:
            count += 1
    if count > 0:
        
        return False
    else:
        return True
            

def knipt(sequence):
    """
    Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken

    Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
    """
    enzymfile = (open ("enzymen.txt")).readlines()
    for regel in enzymfile: #voor iedere regel in het gegeven bestand
        enzym, seq = regel.split()  #split de regels met de enzymen in een ezym en de code
        seq = seq.replace("^","")       #vervangt de spaties met een ^
        enzymen = [[enzym,seq]]     # plakt ze achter elkaar
##            print(enzymen)
        for x in enzymen:             #  een loop voor ieder enzym, om te kijken of hij knipt    #loopt voor beide sequenties
            if x[1] in sequence:                       #\
                print(x[0],"knipt in de sequenctie")       #\> dit stuk geeft weer of het wel of niet knipt
            
##        
Main()
