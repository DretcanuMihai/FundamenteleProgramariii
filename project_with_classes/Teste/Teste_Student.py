#modul ce contine clasa pentru testarile functiilor ce lucreaza pe entitatea de tip student

from Domeniu.Entitati.Entitate_Student import Student
from Domeniu.Validatoare.Validator_Student import ValidatorStudent
from Infrastructura.Repozitorii.RepozitoriuStudenti import RepozitoriuStudenti,RepozitoriuStudentiFisier
from Servicii.ServiciuStudenti import ServiciuStudenti
from Exceptii.exceptii import ValidatorStudentException,RepStudException
import unittest

class TestCaseStudentDomeniu(unittest.TestCase):
    def setUp(self):
        self.stud1=Student(1,"Dan Daniel")
        self.stud1_cheie=Student(1,None)
        self.stud1_alta_cheie=Student(2,None)
        self.stud2=Student(3,"Ciu Ciu")
    def tearDown(self):
        """
        BFMV
        :return:HT
        """
    def testget(self):
        self.assertTrue(self.stud1.get_id()==1)
        self.assertTrue(self.stud1.get_nume()=="Dan Daniel")
    def testset(self):
        self.stud1.set_nume("Dor Dorin")
        self.assertTrue(self.stud1.get_id() == 1)
        self.assertTrue(self.stud1.get_nume() == "Dor Dorin")
    def testequ(self):
        self.assertTrue(self.stud1==self.stud1_cheie,"id-uri egale")
        self.assertFalse(self.stud1==self.stud1_alta_cheie,"id-uri diferite")
    def teststr(self):
        self.assertTrue(str(self.stud1)=="Student - ID:1; Nume:Dan Daniel")
        self.assertTrue(str(self.stud2) == "Student - ID:3; Nume:Ciu Ciu")

class TestCaseStudentValidator(unittest.TestCase):
    def setUp(self):
        self.validator=ValidatorStudent()
    def tearDown(self):
        """
        BFMV
        :return:HT
        """
    def test_validare(self):
        erori=""
        erori = erori + "Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
        erori = erori + "Eroare: numele trebuie sa fie un string de doua cuvinte pentru care doar prima litera este" \
                        " cu majuscula, despartite printr-un spatiu;"
        er1=erori
        erori=""
        erori = erori + "Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;"
        er2=erori
        erori=""
        erori = erori + "Eroare: numele trebuie sa fie un string de doua cuvinte pentru care doar prima litera este" \
                        " cu majuscula, despartite printr-un spatiu;"
        er3=erori
        ex1=Student(0,"John")
        ex2=Student(100000,"Bong")
        ex3=Student(-1,"Ping Pong")
        ex4=Student(123456,"Ba Ban")
        ex5=Student(1,"####")
        ex6=Student(12345,"Incaundiscurspentruromania Mersispotify")
        self.assertRaisesRegex(ValidatorStudentException,er1,self.validator.validare,ex1)
        self.assertRaisesRegex(ValidatorStudentException, er1, self.validator.validare, ex2)
        self.assertRaisesRegex(ValidatorStudentException, er2, self.validator.validare, ex3)
        self.assertRaisesRegex(ValidatorStudentException, er2, self.validator.validare, ex4)
        self.assertRaisesRegex(ValidatorStudentException, er3, self.validator.validare, ex5)
        self.validator.validare(ex6)
    def test_validare_id(self):
        erori=""
        erori = erori + "Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;"
        er=erori
        self.assertRaisesRegex(ValidatorStudentException,er,self.validator.validare_id,0)
        self.assertRaisesRegex(ValidatorStudentException, er, self.validator.validare_id, 100000)
        self.validator.validare_id(123)

class TestCaseStudentRepozitoriu(unittest.TestCase):
    def setUp(self):
        self.repo=RepozitoriuStudenti()
        self.st1=Student(2,"Un Pachet")
        self.repo.adauga(self.st1)
        self.st2=Student(5,"Douazeci Douazeci")
        self.repo.adauga(self.st2)
        self.er1="Eroare:Nu exista un student cu acest ID;"
        self.er2="Eroare:Exista deja un student cu ID-ul respectiv;"
    def tearDown(self):
        """
        BFMV
        :return:HT
        """
    def test_cauta(self):
        self.assertEqual(self.repo.cauta(5).get_id(),self.st2.get_id())
        self.assertEqual(self.repo.cauta(5).get_nume(), self.st2.get_nume())
        self.assertEqual(self.repo.cauta(2).get_id(), self.st1.get_id())
        self.assertEqual(self.repo.cauta(2).get_nume(), self.st1.get_nume())
        self.assertRaisesRegex(RepStudException,self.er1,self.repo.cauta,1)

    def test_adauga_si_get_studenti(self):
        self.assertRaisesRegex(RepStudException,self.er2,self.repo.adauga,self.st2)
        self.assertEqual(len(self.repo),2)
        self.assertEqual(self.repo.cauta(5).get_id(),self.st2.get_id())
        self.assertEqual(self.repo.cauta(5).get_nume(), self.st2.get_nume())
        self.assertEqual(self.repo.cauta(2).get_id(), self.st1.get_id())
        self.assertEqual(self.repo.cauta(2).get_nume(), self.st1.get_nume())
        self.assertEqual(self.repo.get_studenti(),[self.st1,self.st2])
        self.repo.adauga(Student(1,"Boabe Cantarete"))
        self.assertEqual(len(self.repo),3)
        self.assertEqual(self.repo.cauta(5).get_id(),self.st2.get_id())
        self.assertEqual(self.repo.cauta(5).get_nume(), self.st2.get_nume())
        self.assertEqual(self.repo.cauta(2).get_id(), self.st1.get_id())
        self.assertEqual(self.repo.cauta(2).get_nume(), self.st1.get_nume())
        self.assertEqual(self.repo.cauta(1).get_id(), 1)
        self.assertEqual(self.repo.cauta(1).get_nume(), "Boabe Cantarete")
        self.assertEqual(self.repo.get_studenti(), [self.st1, self.st2,self.repo.cauta(1)])

    def test_sterge(self):
        self.repo.sterge(5)
        self.assertEqual(len(self.repo),1)
        self.assertEqual(self.repo.cauta(2).get_id(), self.st1.get_id())
        self.assertEqual(self.repo.cauta(2).get_nume(), self.st1.get_nume())
        self.assertRaisesRegex(RepStudException,self.er1,self.repo.sterge,1)

    def test_modifica(self):
        self.repo.modifica(Student(2,"Incaozi Incadouazecisipatrudeore"))
        self.assertEqual(len(self.repo),2)
        self.assertEqual(self.repo.cauta(5).get_id(),self.st2.get_id())
        self.assertEqual(self.repo.cauta(5).get_nume(), self.st2.get_nume())
        self.assertEqual(self.repo.cauta(2).get_id(), self.st1.get_id())
        self.assertEqual(self.repo.cauta(2).get_nume(), "Incaozi Incadouazecisipatrudeore")

class TestCaseStudentRepozitoriuFisier(TestCaseStudentRepozitoriu):
    def setUp(self):
        fisier=open("./Infrastructura/Repozitorii/BazeDeDate/TestBazeDeDate/test_rep_stud.txt", "w")
        fisier.write("2;Un Pachet\n5;Douazeci Douazeci\n   \n")
        fisier.close()
        self.repo=RepozitoriuStudentiFisier("TestBazeDeDate/test_rep_stud.txt")
        self.er1="Eroare:Nu exista un student cu acest ID;"
        self.er2="Eroare:Exista deja un student cu ID-ul respectiv;"
        self.st1 = Student(2, "Un Pachet")
        self.st2 = Student(5, "Douazeci Douazeci")
    def tearDown(self):
        """
        inca putin si-i gata
        :return:
        """
    def test_no_read(self):
        repo=RepozitoriuStudentiFisier("/TestBazeDeDate/nu_exista.txt")
        self.assertEqual(repo.get_studenti(),[])

class TestCaseStudentServiciu(unittest.TestCase):
    def setUp(self):
        repo = RepozitoriuStudenti()
        self.st1 = Student(2, "Un Pachet")
        repo.adauga(self.st1)
        self.st2 = Student(5, "Douazeci Douazeci")
        repo.adauga(self.st2)
        validator=ValidatorStudent()
        self.srv=ServiciuStudenti(repo,validator)
    def tearDown(self):
        """
        BFMV
        :return:HT
        """
    def test_adauga(self):
        self.assertRaises(ValidatorStudentException,self.srv.adauga,0,"Oopsie Doopsie")
        self.assertRaises(RepStudException,self.srv.adauga,2,"Doi Pacheti")
        self.srv.adauga(3,"Hai Iar")
        self.assertEqual(self.srv.get_studenti(),[self.st1,self.st2,Student(3,"Hai Iar")])
        self.assertEqual(self.srv.numar_studenti(),3)

    def test_cauta(self):
        self.assertRaises(ValidatorStudentException,self.srv.cauta,-1)
        self.assertRaises(RepStudException,self.srv.cauta,3)
        self.assertEqual(self.srv.cauta(5),self.st2)

    def test_sterge(self):
        self.assertRaises(ValidatorStudentException,self.srv.sterge,123456)
        self.assertRaises(RepStudException,self.srv.sterge,1)
        self.srv.sterge(2)
        self.assertEqual(self.srv.numar_studenti(),1)
        self.assertEqual(self.srv.get_studenti(),[self.st2])

    def test_modifica(self):
        self.assertRaises(ValidatorStudentException,self.srv.modifica,0,"ciu")
        self.assertRaises(RepStudException,self.srv.modifica,1,"Nu Da")
        self.srv.modifica(2,"Da Dan")
        self.assertEqual(self.srv.cauta(2).get_id(),2)
        self.assertEqual(self.srv.cauta(2).get_nume(),"Da Dan")

class TesteStudent:
    def __gen_ex1(self):
        stud=Student(123,"Aciobanitei Andrei")
        return stud
    def __gen_ex2(self):
        stud=Student(245, "Lazar Luca")
        return stud
    def __gen_ex3(self):
        stud=Student(-123,"andrei")
        return stud
    def __gen_ex4(self):
        stud=Student(100000,"L zar #")
        return stud
    def __gen_ex5(self):
        stud=Student(1,"Mazar  Slab")
        return stud
    def __gen_ex6(self):
        stud=Student(123, "Buliga Matei")
        return stud
    def __gen_ex7(self):
        stud=Student(245, "Pop Luca")
        return stud
    def __gen_ex8(self):
        stud=Student(122, "Buli Matei")
        return stud
    def __gen_ex9(self):
        stud=Student(22, "Sandu Dab")
        return stud

    def __test_domeniu(self):
        stud1=self.__gen_ex1()
        assert stud1.get_id()==123
        assert stud1.get_nume()=="Aciobanitei Andrei"
        assert str(stud1)=="Student - ID:123; Nume:Aciobanitei Andrei"
        stud0=Student(123,None)
        assert stud0==stud1
        stud0=Student(24,None)
        assert not(stud0==stud1)
        stud1.set_nume("Buiciuc Gabriel")
        assert stud1.get_nume()=="Buiciuc Gabriel"
        assert not(stud1=="ASD")
        stud2=self.__gen_ex2()
        assert stud2.get_id()==245
        assert stud2.get_nume()=="Lazar Luca"
        assert str(stud2) == "Student - ID:245; Nume:Lazar Luca"
        stud0=Student(1,None)
        assert not(stud0==stud2)
        stud0=Student(245,None)
        assert stud0==stud2
        stud1.set_nume("Pop Luke")
        assert stud1.get_nume()=="Pop Luke"
        assert not(stud1==0)

    def __test_validare(self):
        stud1=self.__gen_ex1()
        stud2=self.__gen_ex2()
        stud3=self.__gen_ex3()
        stud4=self.__gen_ex4()
        stud5=self.__gen_ex5()
        validator=ValidatorStudent()
        validator.validare(stud1)
        validator.validare_id(stud1.get_id())
        validator.validare(stud2)
        validator.validare_id(stud1.get_id())
        try:
            validator.validare(stud3)
            assert False
        except ValidatorStudentException as er:
            eroare="Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
            eroare=eroare+"Eroare: numele trebuie sa fie un string de doua cuvinte pentru care doar prima litera" \
                          " este cu majuscula, despartite printr-un spatiu;"
            assert str(er)==eroare
        try:
            validator.validare_id(stud3.get_id())
            assert False
        except ValidatorStudentException as er:
            eroare="Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;"
            assert str(er)==eroare
        try:
            validator.validare(stud4)
            assert False
        except ValidatorStudentException as er:
            eroare="Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
            eroare=eroare+"Eroare: numele trebuie sa fie un string de doua cuvinte pentru care doar prima litera" \
                          " este cu majuscula, despartite printr-un spatiu;"
            assert str(er)==eroare
        try:
            validator.validare_id(stud4.get_id())
            assert False
        except ValidatorStudentException as er:
            eroare="Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;"
            assert str(er)==eroare
        try:
            validator.validare(stud5)
            assert False
        except ValidatorStudentException as er:
            eroare="Eroare: numele trebuie sa fie un string de doua cuvinte pentru care doar prima litera este" \
                   " cu majuscula, despartite printr-un spatiu;"
            assert str(er)==eroare

    def __test_repozitoriu(self):
        repo=RepozitoriuStudenti()
        assert len(repo)==0
        lista=repo.get_studenti()
        assert lista==[]
        try:
            repo.cauta(123)
            assert False
        except RepStudException as er:
            assert str(er)=="Eroare:Nu exista un student cu acest ID;"
        stud1=self.__gen_ex1()
        repo.adauga(stud1)
        assert len(repo)==1
        stud_cautat=repo.cauta(123)
        assert stud_cautat.get_id()==123
        assert stud_cautat.get_nume()=="Aciobanitei Andrei"
        lista=repo.get_studenti()
        assert lista==[stud1]
        try:
            repo.cauta(124)
            assert False
        except RepStudException as er:
            assert str(er) == "Eroare:Nu exista un student cu acest ID;"
        try:
            repo.cauta(1)
            assert False
        except RepStudException as er:
            assert str(er) == "Eroare:Nu exista un student cu acest ID;"
        stud0=Student(123,"a b")
        try:
            repo.adauga(stud0)
            assert False
        except RepStudException as eroare:
            assert str(eroare)=="Eroare:Exista deja un student cu ID-ul respectiv;"
        stud2=self.__gen_ex2()
        repo.adauga(stud2)
        assert len(repo)==2
        stud_cautat=repo.cauta(123)
        assert stud_cautat.get_id()==123
        assert stud_cautat.get_nume()=="Aciobanitei Andrei"
        stud_cautat=repo.cauta(245)
        assert stud_cautat.get_id()==245
        assert stud_cautat.get_nume()=="Lazar Luca"
        lista=repo.get_studenti()
        assert lista==[stud1,stud2]
        repo.sterge(123)
        assert len(repo)==1
        stud_cautat=repo.cauta(245)
        assert stud_cautat.get_id()==245
        assert stud_cautat.get_nume()=="Lazar Luca"
        lista=repo.get_studenti()
        assert lista==[stud2]
        try:
            repo.sterge(123)
            assert False
        except RepStudException as eroare:
            assert str(eroare)=="Eroare:Nu exista un student cu acest ID;"
        repo.sterge(245)
        assert len(repo)==0
        try:
            repo.sterge(245)
            assert False
        except RepStudException as eroare:
            assert str(eroare)=="Eroare:Nu exista un student cu acest ID;"
        repo.adauga(stud1)
        repo.adauga(stud2)
        stud3=self.__gen_ex6()
        stud4=self.__gen_ex7()
        repo.modifica(stud3)
        assert len(repo)==2
        stud_cautat=repo.cauta(123)
        assert stud_cautat.get_id()==123
        assert stud_cautat.get_nume()=="Buliga Matei"
        stud_cautat=repo.cauta(245)
        assert stud_cautat.get_id()==245
        assert stud_cautat.get_nume()=="Lazar Luca"
        repo.modifica(stud4)
        assert len(repo)==2
        stud_cautat=repo.cauta(123)
        assert stud_cautat.get_id()==123
        assert stud_cautat.get_nume()=="Buliga Matei"
        stud_cautat=repo.cauta(245)
        assert stud_cautat.get_id()==245
        assert stud_cautat.get_nume()=="Pop Luca"
        stud5=self.__gen_ex8()
        stud6=self.__gen_ex9()
        try:
            repo.modifica(stud5)
            assert False
        except RepStudException as eroare:
            assert str(eroare)=="Eroare:Nu exista un student cu acest ID;"
        try:
            repo.modifica(stud6)
            assert False
        except RepStudException as eroare:
            assert str(eroare)=="Eroare:Nu exista un student cu acest ID;"

    def __test_serviciu(self):
        repo=RepozitoriuStudenti()
        validator=ValidatorStudent()
        serviciu=ServiciuStudenti(repo,validator)
        assert serviciu.numar_studenti()==0
        lista=serviciu.get_studenti()
        assert lista==[]
        serviciu.adauga(1,"Ciorba Sandu")
        assert serviciu.numar_studenti()==1
        stud_cautat1=serviciu.cauta(1)
        assert stud_cautat1.get_id()==1
        assert stud_cautat1.get_nume()=="Ciorba Sandu"
        lista=serviciu.get_studenti()
        assert lista==[stud_cautat1]
        try:
            serviciu.adauga(1,"Ciorb Sand")
            assert False
        except RepStudException as eroare:
            assert str(eroare)=="Eroare:Exista deja un student cu ID-ul respectiv;"
        try:
            serviciu.adauga(0,"tEst Be st")
            assert False
        except ValidatorStudentException as er:
            eroare="Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
            eroare=eroare+"Eroare: numele trebuie sa fie un string de doua cuvinte pentru care doar prima litera" \
                          " este cu majuscula, despartite printr-un spatiu;"
            assert str(er)==eroare
        assert serviciu.numar_studenti()==1
        serviciu.adauga(441,"Brothers Fratii")
        assert serviciu.numar_studenti()==2
        stud_cautat2=serviciu.cauta(441)
        assert stud_cautat2.get_id()==441
        assert stud_cautat2.get_nume()=="Brothers Fratii"
        lista=serviciu.get_studenti()
        assert lista==[stud_cautat1,stud_cautat2]
        try:
            serviciu.cauta(2)
            assert False
        except RepStudException as er:
            assert str(er) == "Eroare:Nu exista un student cu acest ID;"
        try:
            serviciu.cauta(0)
            assert False
        except ValidatorStudentException as eroare:
            assert str(eroare)=="Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;"
        serviciu.modifica(1, "Supa Sandu")
        assert serviciu.numar_studenti()==2
        stud_cautat=serviciu.cauta(1)
        assert stud_cautat.get_id()==1
        assert stud_cautat.get_nume()=="Supa Sandu"
        serviciu.modifica(441,"Treime Accepto")
        assert serviciu.numar_studenti()==2
        stud_cautat=serviciu.cauta(441)
        assert stud_cautat.get_id()==441
        assert stud_cautat.get_nume()=="Treime Accepto"
        try:
            serviciu.modifica(2, "Tuica Damigean")
            assert False
        except RepStudException as eroare:
            assert str(eroare)=="Eroare:Nu exista un student cu acest ID;"
        try:
            serviciu.modifica(100000, "Astaiibun aStanui")
            assert False
        except ValidatorStudentException as er:
            eroare="Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
            eroare=eroare+"Eroare: numele trebuie sa fie un string de doua cuvinte pentru care doar prima litera" \
                          " este cu majuscula, despartite printr-un spatiu;"
            assert eroare==str(er)
        serviciu.sterge(441)
        assert serviciu.numar_studenti()==1
        try:
            serviciu.sterge(2)
            assert False
        except RepStudException as eroare:
            assert str(eroare)=="Eroare:Nu exista un student cu acest ID;"
        try:
            serviciu.sterge(-5)
            assert False
        except ValidatorStudentException as eroare:
            assert str(eroare)=="Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;"
        serviciu.sterge(1)
        assert serviciu.numar_studenti()==0

    def ruleaza_teste(self):
        self.__test_domeniu()
        self.__test_validare()
        self.__test_repozitoriu()
        self.__test_serviciu()