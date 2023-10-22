#modul ce contine clasa de validator pentru entitatea melodie

from Exceptii.Exceptii import ValidatorMelodieException

class ValidatorMelodie():
    def valideaza(self,melodie):
        """
        functie ce valideaza o melodie daca aceasta este valida
        :param melodie: melodie
        :return: None
        Functia va ridicica un ValidatorMelodieException cu unele din mesjaele de mai jos, dupa caz, daca melodia nu
        este valida
        "Eroare: Titlul melodiei trebuie sa fie un sir nevid ce nu contine ';' ;\n"
        "Eroare: Numele artistului trebuie sa fie un sir nevid ce nu contine ';' ;\n"
        "Eroare: Genul melodiei trebuie sa fie unul din stringurile: 'Rock','Pop','Jazz','Altele' ;\n"
        "Eroare: Durata melodiei trebuie sa fie un numar intreg strict pozitiv ;\n"
        Ultimul '\n' va fi sters din eroare
        """
        erori=""
        titlu=melodie.get_titlu()
        nume=melodie.get_artist()
        gen=melodie.get_gen()
        durata=melodie.get_durata()
        if(titlu=="" or ';' in titlu):
            erori+="Eroare: Titlul melodiei trebuie sa fie un sir nevid ce nu contine ';' ;\n"
        if(nume=="" or ";" in nume):
            erori+="Eroare: Numele artistului trebuie sa fie un sir nevid ce nu contine ';' ;\n"
        if(gen not in ["Rock","Pop","Jazz","Altele"]):
            erori+="Eroare: Genul melodiei trebuie sa fie unul din stringurile: 'Rock','Pop','Jazz','Altele' ;\n"
        if durata<=0:
            erori+="Eroare: Durata melodiei trebuie sa fie un numar intreg strict pozitiv ;\n"
        if(len(erori)>0):
            erori=erori[0:-1]
            raise ValidatorMelodieException(erori)

