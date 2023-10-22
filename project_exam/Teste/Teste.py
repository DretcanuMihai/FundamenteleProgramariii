#modul cu teste pentru tot ce tine de entitatea melodie

from Domeniu.Entitati.EntitateMelodie import Melodie
from Domeniu.Validatoare.ValidatorMelodie import ValidatorMelodie
from Exceptii.Exceptii import ValidatorMelodieException,RepozitoriuMelodiiException,ExportException,ValidatorAlteleException
from Infrastructura.Repozitorii.RepozitoriuMelodii import RepozitoriuMelodii
from Servicii.ServiciuMelodii import ServiciuMelodii
from FunctiiAjutatoare.Comparatori import comparator_1

import unittest

class TestDomeniu(unittest.TestCase):
    def setUp(self):
        self.__melodie=Melodie("Muzica","Dan Balan","Pop",300)

    def test_baze(self):
        self.assertEqual(self.__melodie.get_titlu(),"Muzica")
        self.assertEqual(self.__melodie.get_artist(),"Dan Balan")
        self.assertEqual(self.__melodie.get_gen(),"Pop")
        self.assertEqual(self.__melodie.get_durata(),300)
        self.assertEqual(self.__melodie,Melodie("Muzica","Dan Balan",None,None))
        self.assertNotEqual(self.__melodie, Melodie("Muzica", "Dan Bala", None, None))
        self.assertNotEqual(self.__melodie, Melodie("Muzic", "Dan Balan", None, None))
        self.assertNotEqual(self.__melodie, Melodie("Muzic", "Dan Bala", None, None))
        str1=str(self.__melodie)
        str2="Melodie - titlu:Muzica - artist:Dan Balan - gen:Pop - durata:300"
        self.assertEqual(str1,str2)
        self.__melodie.set_gen("Rock")
        self.__melodie.set_durata(240)
        self.assertEqual(self.__melodie.get_titlu(), "Muzica")
        self.assertEqual(self.__melodie.get_artist(), "Dan Balan")
        self.assertEqual(self.__melodie.get_gen(), "Rock")
        self.assertEqual(self.__melodie.get_durata(), 240)

class TestComparator(unittest.TestCase):
    def test_comparator1(self):
        m1=Melodie("abc","abc",None,None)
        m2=Melodie("bbc","abc",None,None)
        m3=Melodie("abc","acc",None,None)
        m4=Melodie("abc","abc",None,None)
        m5=Melodie("abc","aaa",None,None)
        m6=Melodie("aac","abc",None,None)
        f=comparator_1
        self.assertTrue(f(m1,m2))
        self.assertTrue(f(m1,m3))
        self.assertFalse(f(m1,m4))
        self.assertFalse(f(m1, m5))
        self.assertFalse(f(m1, m6))

class TestValidator(unittest.TestCase):
    def test_valideaza(self):
        validator=ValidatorMelodie()
        m1=Melodie("Muzica","Dan Balan","Pop",300)
        m2=Melodie("","","Roc",-1)
        er2=""
        er2+="Eroare: Titlul melodiei trebuie sa fie un sir nevid ce nu contine ';' ;\n"
        er2+="Eroare: Numele artistului trebuie sa fie un sir nevid ce nu contine ';' ;\n"
        er2+="Eroare: Genul melodiei trebuie sa fie unul din stringurile: 'Rock','Pop','Jazz','Altele' ;\n"
        er2+="Eroare: Durata melodiei trebuie sa fie un numar intreg strict pozitiv ;"
        m3=Melodie("Muzi;ca","Dan;Balan","Rock",0)
        er3=""
        er3+="Eroare: Titlul melodiei trebuie sa fie un sir nevid ce nu contine ';' ;\n"
        er3+="Eroare: Numele artistului trebuie sa fie un sir nevid ce nu contine ';' ;\n"
        er3+="Eroare: Durata melodiei trebuie sa fie un numar intreg strict pozitiv ;"
        m4=Melodie("Muzica","George","Jazz",1)
        m5=Melodie("Muzica","George","Altele",2)
        m6=Melodie("Muzica",";","Altele",3)
        er6="Eroare: Numele artistului trebuie sa fie un sir nevid ce nu contine ';' ;"
        validator.valideaza(m1)
        self.assertRaisesRegex(ValidatorMelodieException,er2,validator.valideaza,m2)
        self.assertRaisesRegex(ValidatorMelodieException,er3,validator.valideaza,m3)
        validator.valideaza(m4)
        validator.valideaza(m5)
        self.assertRaisesRegex(ValidatorMelodieException,er6,validator.valideaza,m6)

class TestRepozitoriu(unittest.TestCase):
    def setUp(self):
        fisier=open("./BazeDate/test_melodii.txt","w")
        de_scris="  \n\n  Test1;Artist1;Rock;1  \nTest2;Artist2;Pop;30\n \n \n Fain;Foarte Fain;Rock;120\n"
        fisier.write(de_scris)
        fisier.close()
        self.__repo=RepozitoriuMelodii("test_melodii.txt")
    def tearDown(self):
        pass
    def test_citire(self):
        repo=RepozitoriuMelodii("nu_exista.txt")
        l=repo.get_toate_melodiile()
        self.assertEqual(len(l),0)
        l=self.__repo.get_toate_melodiile()
        self.assertEqual(len(l),3)
        self.assertEqual(l[0].get_titlu(),"Test1")
        self.assertEqual(l[0].get_artist(),"Artist1")
        self.assertEqual(l[0].get_gen(),"Rock")
        self.assertEqual(l[0].get_durata(),1)
        self.assertEqual(l[2].get_titlu(),"Fain")
        self.assertEqual(l[2].get_artist(),"Foarte Fain")
        self.assertEqual(l[2].get_gen(),"Rock")
        self.assertEqual(l[2].get_durata(),120)
    def test_modifica_si_scrie(self):
        self.__repo.modificare_melodie(Melodie("Fain","Foarte Fain","Pop",2))
        l=self.__repo.get_toate_melodiile()
        self.assertEqual(len(l),3)
        self.assertEqual(l[0].get_titlu(),"Test1")
        self.assertEqual(l[0].get_artist(),"Artist1")
        self.assertEqual(l[0].get_gen(),"Rock")
        self.assertEqual(l[0].get_durata(),1)
        self.assertEqual(l[2].get_titlu(),"Fain")
        self.assertEqual(l[2].get_artist(),"Foarte Fain")
        self.assertEqual(l[2].get_gen(),"Pop")
        self.assertEqual(l[2].get_durata(),2)
        er="Eroare: Nu exista o melodie cu acest titlu si acest artist;"
        self.assertRaisesRegex(RepozitoriuMelodiiException,er, self.__repo.modificare_melodie,Melodie("T","Artist1","Rock",120))
        fisier=open("./BazeDate/test_melodii.txt","r")
        c=fisier.read()
        continut="Test1;Artist1;Rock;1\nTest2;Artist2;Pop;30\nFain;Foarte Fain;Pop;2\n"
        self.assertEqual(c,continut)
        fisier.close()
    def test_adauga(self):
        er="Eroare: Exista deja o melodie cu acest titlu si acest artist;"
        self.assertRaisesRegex(RepozitoriuMelodiiException,er,self.__repo.adauga_melodie,Melodie("Test1","Artist1","Pop",2))
        self.__repo.adauga_melodie(Melodie("George","Canta","Rock",2004))
        l=self.__repo.get_toate_melodiile()
        self.assertEqual(len(l),4)
        self.assertEqual(l[0].get_titlu(),"Test1")
        self.assertEqual(l[0].get_artist(),"Artist1")
        self.assertEqual(l[0].get_gen(),"Rock")
        self.assertEqual(l[0].get_durata(),1)
        self.assertEqual(l[3].get_titlu(),"George")
        self.assertEqual(l[3].get_artist(),"Canta")
        self.assertEqual(l[3].get_gen(),"Rock")
        self.assertEqual(l[3].get_durata(),2004)

class TestServiciu(unittest.TestCase):
    def setUp(self):
        fisier = open("./BazeDate/test_melodii.txt", "w")
        de_scris = "  \n  \n \n \n Fain;Foarte Fain;Rock;120\n\nTest2;Artist2;Pop;30\n  Test1;Artist1;Rock;1"
        fisier.write(de_scris)
        fisier.close()
        repo = RepozitoriuMelodii("test_melodii.txt")
        validator=ValidatorMelodie()
        self.__serviciu=ServiciuMelodii(repo,validator)
    def tearDown(self):
        pass
    def test_modifica(self):
        self.assertRaises(ValidatorMelodieException,self.__serviciu.modifica_melodie,";"," ","Pop",-1)
        self.assertRaises(RepozitoriuMelodiiException,self.__serviciu.modifica_melodie,"A","A","Pop",2)
        self.__serviciu.modifica_melodie("Test1","Artist1","Pop",2)
        l=self.__serviciu.get_melodii()
        self.assertEqual(len(l),3)
        self.assertEqual(l[0].get_titlu(),"Fain")
        self.assertEqual(l[0].get_artist(),"Foarte Fain")
        self.assertEqual(l[0].get_gen(),"Rock")
        self.assertEqual(l[0].get_durata(),120)
        self.assertEqual(l[2].get_titlu(),"Test1")
        self.assertEqual(l[2].get_artist(),"Artist1")
        self.assertEqual(l[2].get_gen(),"Pop")
        self.assertEqual(l[2].get_durata(),2)
    def test_export(self):
        er="Eroare:Numele fisierului trebuie sa nu fie vid;"
        er2="Eroare:Nu s-a putut realiza exportul;"
        self.assertRaisesRegex(ValidatorAlteleException,er,self.__serviciu.export,"")
        self.assertRaisesRegex(ExportException,er2,self.__serviciu.export,"fisier_gresit/csv/csv")
        self.__serviciu.export("text_melodii")
        fisier=open("./ExportData/text_melodii.csv","r")
        c=fisier.read()
        continut="Artist1,Test1,1,Rock\nArtist2,Test2,30,Pop\nFoarte Fain,Fain,120,Rock\n"
        self.assertEqual(c,continut)



if __name__=="__main__":
    unittest.main()