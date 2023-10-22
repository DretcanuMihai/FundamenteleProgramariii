from Domeniu.Entitati.EntitateMelodie import Melodie
from Exceptii.Exceptii import ExportException,ValidatorAlteleException,RandomException
from FunctiiAjutatoare.Comparatori import comparator_1
from random import randint

class ServiciuMelodii():
    def __init__(self,repo,validator):
        """
        initializeaza un serviciu de melodii cu un repozitoriu si un validator
        :param repo: RepozitoriuMelodii
        :param validator: ValidatorMelodie
        """
        self.__repo=repo
        self.__validator=validator

    def modifica_melodie(self,titlu,artist,gen,durata):
        """
        modifica o melodie identificata dupa titlu si artist cu genul si durata specificata
        :param titlu: string
        :param artist: string
        :param gen: string
        :param durata: intreg
        :return: None
        Daca melodia nu este valida, se va ridica un ValidatorMelodieException cu mesajele specifice, ultimul '\n' fiind
        eliminat:
        "Eroare: Titlul melodiei trebuie sa fie un sir nevid ce nu contine ';' ;\n"
        "Eroare: Numele artistului trebuie sa fie un sir nevid ce nu contine ';' ;\n"
        "Eroare: Genul melodiei trebuie sa fie unul din stringurile: 'Rock','Pop','Jazz','Altele' ;\n"
        "Eroare: Durata melodiei trebuie sa fie un numar intreg strict pozitiv ;\n"
        Daca melodia este valida, dar aceasta nu exista in repozitoriu, se va ridica un RepozitoriuMelodiiException cu
        mesajul : "Eroare: Nu exista o melodie cu acest titlu si acest artist;"
        """
        melodie=Melodie(titlu,artist,gen,durata)
        self.__validator.valideaza(melodie)
        self.__repo.modificare_melodie(melodie)
    def get_melodii(self):
        """
        returneaza o lista cu toate melodiile din repozitoriul asociat serviciului
        :return: lista de melodii
        """
        return self.__repo.get_toate_melodiile()

    def export(self,nume_fisier):
        """
        exporteaza datele din repozitoriu intr-un fisier csv localizat intr-un fisier ./ExportData/nume_fisier.csv
        :param nume_fisier: string
        :return: None
        Daca numele fisierul este vid se va ridica un ValidatorAlteleException cu mesajul
        "Eroare:Numele fisierului trebuie sa nu fie vid;"
        Daca numele fisierului e valid dar apar erori la crearea fisierului,se va ridica un ValidatorAlteleException
        cu mesajul:
        "Eroare:Nu s-a putut realiza exportul;"
        """
        if(nume_fisier==""):
            raise ValidatorAlteleException("Eroare:Numele fisierului trebuie sa nu fie vid;")
        try:
            fisier=open("./ExportData/"+nume_fisier+".csv","w")
            melodii=self.__repo.get_toate_melodiile()
            for i in range(0,len(melodii)-1):
                for j in range(i+1,len(melodii)):
                    if(comparator_1(melodii[j],melodii[i])):
                        melodii[j],melodii[i]=melodii[i],melodii[j]
            for melodie in melodii:
                de_scris=melodie.get_artist()+","+melodie.get_titlu()+","+str(melodie.get_durata())+","+melodie.get_gen()+"\n"
                fisier.write(de_scris)
            fisier.close()
        except:
            raise ExportException("Eroare:Nu s-a putut realiza exportul;")
    def generator(self,numar,lista):
        """
        functie ce genereaza aleator un numar "numar" de melodii ce sunt adaugate in repozitoriu
        functia returneaza numarul de elemente adaugate
        :param numar: intreg
        :param lista: string
        :return: intreg
        Daca lista nu are indeajunse elemente despartite prin virgula pentru generare, se va ridica un RandomException
        cu mesajul "Eroare:Lista trebuie sa contina un numar par, nenul de elemente;"
        """
        lista=lista.split(",")
        if(len(lista)%2!=0 or len(lista)==0):
            raise RandomException("Eroare:Lista trebuie sa contina un numar par, nenul de elemente;")
        mid=len(lista)//2
        titluri=lista[0:mid]
        artisti=lista[mid:]
        genuri=["Pop","Rock","Jazz","Altele"]
        nr=0
        for i in range(0,numar):
            melodie=Melodie(titluri[randint(0,mid-1)],artisti[randint(0,mid-1)],genuri[randint(0,3)],randint(1950,2022))
            try:
                self.__repo.adauga_melodie(melodie)
                nr+=1
            except:
                pass
        return nr