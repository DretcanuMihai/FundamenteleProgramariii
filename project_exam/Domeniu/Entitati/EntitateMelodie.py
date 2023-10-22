#modul ce contine definirea clasei melodie

class Melodie():
    def __init__(self,titlu, artist, gen, durata):
        """
        initializeaza o entitate de tip melodie cu titlu, artist, gen, durata
        :param titlu: string
        :param artist: string
        :param gen: string
        :param durata: intreg
        """
        self.__titlu=titlu
        self.__artist=artist
        self.__gen=gen
        self.__durata=durata

    def get_titlu(self):
        """
        returneaza titlul unei melodii
        :return: string
        """
        return self.__titlu
    def get_artist(self):
        """
        returneaza artistul unei melodii
        :return: string
        """
        return self.__artist
    def get_gen(self):
        """
        returneaza genul unei melodii
        :return: string
        """
        return self.__gen
    def get_durata(self):
        """
        returneaza durata unei melodii
        :return: intreg
        """
        return self.__durata
    def set_gen(self,gen_nou):
        """
        seteaza genul unei entitati melodie la gen_nou
        :param gen_nou: string
        :return: None - modificarea are loc in mod direct pe entitate
        """
        self.__gen=gen_nou
    def set_durata(self,durata_noua):
        """
        seteaza durata unei entitati melodie la durata_noua
        :param durata_noua: intreg
        :return: None - modificarea are loc in mod direct pe entitate
        """
        self.__durata=durata_noua
    def __str__(self):
        """
        supreascrie ce inseamna conversia string a unei entitati melodie
        formatul este "Melodie - titlu:*titlu* - artist:*artist* - gen:*gen* - durata:*durata* secunde"
        :return: string
        """
        return "Melodie - titlu:"+self.__titlu+" - artist:"+self.__artist+" - gen:"+self.__gen+" - durata:"+str(self.__durata)
    def __eq__(self, other):
        """
        supreascrie ce inseamna relatia de egalitate intre doua entitati melodie
        Doua entitati sunt egale daca au acelasi titlu si acelasi artist
        :param other: melodie
        :return: True/False - True daca sunt "egale", false in caz contrar
        """
        return self.__titlu==other.get_titlu() and self.__artist==other.get_artist()