# Naam: Christiaan Posthuma
# Datum: vandaag 11 okt
# Versie: 1.0.0.0

########################################
import tkinter as tk  # importeer methodes voor keuzemenu vanuit tkinder module
import tkinter.filedialog as tkFile

openwindow = tk.Tk()   # opent een window voor het keuzemenu
openwindow.withdraw()   # haalt datzelfde window weer weg
##########################################

# Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand


def main():
    try:
        bestand = open("GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna").readlines()
        headers, sequences = lees_inhoud(bestand)

        searchterm = input("Enter a search term: ")
        for i in range(len(headers)):  # lengte headers=len sequences
            if searchterm in headers[i]:
                if is_dna(sequences[i]):
                    print("\n", headers[i])
                    knipt(sequences[i])
                    is_dna(sequences[i])

    except TypeError:
        print("TypeError: wrong type of input: sting given while float is needed")

    except:
        print("There was an unexcepted error")


def lees_inhoud(bestand):
    """
    Convert de inhoud van de fasta file naar 2 lijsten.
    Namelijk de headers en de sequenties

    :param bestand:
    :return list met Headers en een list met sequences:
    """
    try:
        headers, sequences = [], []
        seq = ""
        for line in bestand:
            line = line.strip()
            if line.startswith(">"):
                if seq != "":
                    sequences.append(seq)
                    seq = ""
                headers.append(line)
            else:
                seq += line
        sequences.append(seq)
        return headers, sequences

    except IOError:
        print("IOerror, file can not be read")
    except FileNotFoundError:
        print("FileNotFoundError: The file was not found, give an valid file, and try agian")


def is_dna(sequence):
    """
    Controleerd of de opgegeven seqenties in de lijst een DNA-sequentie is.

    :param sequence:
    :return True of False:
    """
    count = 0
    sequencex = sequence.upper()
    for letter in sequencex:
        if letter not in ["A", "C", "T", "G"]:
            count += 1
    if count > 0:
        return False
    else:
        return True


def knipt(sequence):
    """
    Kijkt welke enzymen in de sequenctie knipt.
    In het geval er een enzym knipt print het de header (uit de list)
        en daarna de enzymen die knippen.
    :param sequence:
    :return:
    """
    enzymfile = (open("enzymen.txt")).readlines()
    for regel in enzymfile:   # voor iedere regel in het gegeven bestand
        enzym, seq = regel.split()  # split de regels naar  enzymen  en code
        seq = seq.replace("^", "")       # vervangt de spaties met een ^
        enzymen = [[enzym, seq]]     # plakt ze achter elkaar
#            print(enzymen)
        for x in enzymen:   # loop voor ieder enzym, om te kijken of hij knipt in de seq
            if x[1] in sequence:                       # \
                print(x[0], "knipt in de sequenctie")
main()
