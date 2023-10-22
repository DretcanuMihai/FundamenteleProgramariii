#modul destinat clasei de repozitoriu melodii

from Domeniu.Entitati.EntitateMelodie import Melodie
from Exceptii.Exceptii import RepozitoriuMelodiiException

class RepozitoriuMelodii():
    def __init__(self,nume_fisier):
        """
        initialieaza un repozitoriu asociat fisierului aflat in ./BazeDate/nume_fisier
        :param nume_fisier: string
        """
        self.__cale_fisier="./BazeDate/"+nume_fisier
        self.__melodii=[]
        self.__incarca_din_fisier()

    def __incarca_din_fisier(self):
        """
        incarca in repozitoriu entitatile melodie din fisierul asociat
        :return: None - modifica in mod direct entitatea
        Daca apar erori la deschiderea si citirea fisierului, repozitoriul este initializat gol
        """
        try:
            fisier=open(self.__cale_fisier,"r")
            for linie in fisier:
                linie=linie.strip()
                if(linie!=""):
                    linie=linie.split(";")
                    melodie=Melodie(linie[0],linie[1],linie[2],int(linie[3]))
                    self.__melodii.append(melodie)
            fisier.close()
        except:
            try:
                fisier.close()
            except:
                pass
            self.__melodii=[]
            return
    def __incarca_in_fisier(self):
        """
        incarca in fisiserul asociat repozitoriului datele din repozitoriu
        :return: None
        Daca apar erori la incarcarea in fisier se va ridica un RepozitoriuMelodiiException cu mesjaul
        "Eroare: Salvarea in fisier a esuat;"
        """
        try:
            fisier=open(self.__cale_fisier,"w")
            for melodie in self.__melodii:
                de_scris=melodie.get_titlu()+";"+melodie.get_artist()+";"+melodie.get_gen()+";"+str(melodie.get_durata())+"\n"
                fisier.write(de_scris)
            fisier.close()
        except:
            try:
                fisier.close()
            except:
                pass
            raise RepozitoriuMelodiiException("Eroare: Salvarea in fisier a esuat;")
    def modificare_melodie(self,melodie):
        """
        modifica genul si durata unei melodii identificata prin artist si titlu
        :param melodie: melodie
        :return: None
        Daca nu exista melodia in repozitoriu, se va ridica un RepozitoriuMelodiiException cu mesajul
        "Eroare: Nu exista o melodie cu acest titlu si acest artist;"
        """
        for i in range(0,len(self.__melodii)):
            if self.__melodii[i]==melodie:
                self.__melodii[i].set_gen(melodie.get_gen())
                self.__melodii[i].set_durata(melodie.get_durata())
                self.__incarca_in_fisier()
                return
        raise RepozitoriuMelodiiException("Eroare: Nu exista o melodie cu acest titlu si acest artist;")
    def get_toate_melodiile(self):
        """
        returneaza o lista cu toate melodiile din repozitoriu
        :return: lista de melodii
        """
        return self.__melodii
    def adauga_melodie(self,melodie):
        """
        adauga o melodie in repozitoriu
        :param melodie: melodie
        :return: None
        Daca exista deja o melodie cu titlul si artistul respectiv, se va ridica un RepozitoriuMelodiiException cu mesajul
        "Eroare: Exista deja o melodie cu acest titlu si acest artist;"
        """
        if melodie in self.__melodii:
            raise RepozitoriuMelodiiException("Eroare: Exista deja o melodie cu acest titlu si acest artist;")
        self.__melodii.append(melodie)
        self.__incarca_in_fisier()