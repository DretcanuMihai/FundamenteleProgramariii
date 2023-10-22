#modul ce contine clasa pentru testarile functiilor ce lucreaza pe entitatea de tip student

from Domeniu.Entitati.Entitate_Disciplina import Disciplina
from Domeniu.Validatoare.Validator_Disciplina import ValidatorDisciplina
from Infrastructura.Repozitorii.RepozitoriuDiscipline import RepozitoriuDiscipline,RepozitoriuDisciplineFisier
from Servicii.ServiciuDiscipline import SeriviciuDiscipline
from Exceptii.exceptii import ValidatorDisciplinaException, RepDisException
import unittest

class TestCaseDisciplinaDomeniu(unittest.TestCase):
    def setUp(self):
        self.ex1=Disciplina(1,"Calatorit","Oops Nuputem")
        self.ex2=Disciplina(10,"Bere","Dorin Bere")
        self.ex1_cheie=Disciplina(1,None,None)
        self.ex1_altacheie=Disciplina(2,None,None)
    def tearDown(self):
        """
        Asta da gandac de bucatarie mare
        :return:
        """
    def test_get(self):
        self.assertEqual(self.ex1.get_id(),1)
        self.assertEqual(self.ex1.get_nume(),"Calatorit")
        self.assertEqual(self.ex1.get_nume_prof(),"Oops Nuputem")

    def test_set(self):
        self.ex1.set_nume("Mancat")
        self.assertEqual(self.ex1.get_id(),1)
        self.assertEqual(self.ex1.get_nume(),"Mancat")
        self.assertEqual(self.ex1.get_nume_prof(),"Oops Nuputem")
        self.ex1.set_nume_prof("Ba Putem")
        self.assertEqual(self.ex1.get_id(),1)
        self.assertEqual(self.ex1.get_nume(),"Mancat")
        self.assertEqual(self.ex1.get_nume_prof(),"Ba Putem")
    def test_equ(self):
        self.assertTrue(self.ex1==self.ex1_cheie)
        self.assertFalse(self.ex1==self.ex1_altacheie)
    def test_str(self):
        self.assertEqual(str(self.ex1),"Disciplina - ID:1; Nume:Calatorit; Nume profesor:Oops Nuputem")
        self.assertEqual(str(self.ex2),"Disciplina - ID:10; Nume:Bere; Nume profesor:Dorin Bere")

class TestCaseDisciplinaValidator(unittest.TestCase):
    def setUp(self):
        self.validator=ValidatorDisciplina()
    def tearDown(self):
        """
        Album nou Ghost in var alui 2021
        :return:
        """
    def test_validare(self):
        ex1=Disciplina(0,"a","a")
        ex2=Disciplina(1000,"a","A")
        ex3=Disciplina(0,"A","a")
        ex4=Disciplina(0,"A","A")
        ex5=Disciplina(1,"a","a")
        ex6=Disciplina(1,"a","A")
        ex7=Disciplina(1,"A","a")
        ex8=Disciplina(1,"A","A A")
        erori=""
        erori = erori + "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
        erori = erori + "Eroare: numele disciplinei trebuie sa fie un string nenul de cuvinte pentru care doar prima" \
                        " litera incepe cu majusculta, iar cuvintele sunt despartite cu cate un spatiu;\n"
        erori = erori + "Eroare: numele profesorului trebuie sa fie un string de doua cuvinte pentru care doar prima" \
                        " litera este cu majuscula, despartite printr-un spatiu"
        er1=erori
        erori=""
        erori = erori + "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
        erori = erori + "Eroare: numele disciplinei trebuie sa fie un string nenul de cuvinte pentru care doar prima" \
                        " litera incepe cu majusculta, iar cuvintele sunt despartite cu cate un spatiu;"
        er2=erori
        erori=""
        erori = erori + "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
        erori = erori + "Eroare: numele profesorului trebuie sa fie un string de doua cuvinte pentru care doar prima" \
                        " litera este cu majuscula, despartite printr-un spatiu"
        er3=erori
        erori=""
        erori = erori + "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        er4=erori
        erori=""
        erori = erori + "Eroare: numele disciplinei trebuie sa fie un string nenul de cuvinte pentru care doar prima" \
                        " litera incepe cu majusculta, iar cuvintele sunt despartite cu cate un spatiu;\n"
        erori = erori + "Eroare: numele profesorului trebuie sa fie un string de doua cuvinte pentru care doar prima" \
                        " litera este cu majuscula, despartite printr-un spatiu"
        er5=erori
        erori=""
        erori = erori + "Eroare: numele disciplinei trebuie sa fie un string nenul de cuvinte pentru care doar prima" \
                        " litera incepe cu majusculta, iar cuvintele sunt despartite cu cate un spatiu;"
        er6=erori
        erori=""
        erori = erori + "Eroare: numele profesorului trebuie sa fie un string de doua cuvinte pentru care doar prima" \
                        " litera este cu majuscula, despartite printr-un spatiu"
        er7=erori
        self.assertRaisesRegex(ValidatorDisciplinaException,er1,self.validator.validare,ex1)
        self.assertRaisesRegex(ValidatorDisciplinaException, er2, self.validator.validare, ex2)
        self.assertRaisesRegex(ValidatorDisciplinaException, er3, self.validator.validare, ex3)
        self.assertRaisesRegex(ValidatorDisciplinaException, er4, self.validator.validare, ex4)
        self.assertRaisesRegex(ValidatorDisciplinaException, er5, self.validator.validare, ex5)
        self.assertRaisesRegex(ValidatorDisciplinaException, er6, self.validator.validare, ex6)
        self.assertRaisesRegex(ValidatorDisciplinaException, er7, self.validator.validare, ex7)
        self.validator.validare(ex8)

    def test_validare_id(self):
        er="Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        self.assertRaisesRegex(ValidatorDisciplinaException,er,self.validator.validare_id,0)
        self.assertRaisesRegex(ValidatorDisciplinaException, er, self.validator.validare_id, 1000)
        self.validator.validare_id(5)

class TestCaseDisciplinaRepozitoriu(unittest.TestCase):
    def setUp(self):
        self.repo=RepozitoriuDiscipline()
        self.dis1=Disciplina(5,"Batut Din Palme","High Five")
        self.repo.adauga(self.dis1)
        self.dis2=Disciplina(3,"Citit In Palma","Vitoria Lipan")
        self.repo.adauga(self.dis2)
        self.er1="Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        self.er2="Eroare:Exista deja o disciplina cu id-ul respectiv;"
    def tearDown(self):
        """
        Zwei Schritte vor
        :return:
        """
    def test_cauta(self):
        self.assertRaisesRegex(RepDisException,self.er1,self.repo.cauta,1)
        c=self.repo.cauta(3)
        self.assertEqual(c.get_id(),3)
        self.assertEqual(c.get_nume(),"Citit In Palma")
        self.assertEqual(c.get_nume_prof(),"Vitoria Lipan")
    def test_adauga(self):
        dis=Disciplina(3,"Hura","Ora Oraoraora")
        self.assertRaisesRegex(RepDisException,self.er2,self.repo.adauga,dis)
        self.assertEqual(len(self.repo),2)
        self.assertEqual(self.repo.get_discipline(),[self.dis1,self.dis2])
        self.repo.cauta(3)
        self.repo.cauta(5)
        dis3=Disciplina(1,"Slipknotareala","Theo G")
        self.repo.adauga(dis3)
        self.assertEqual(len(self.repo),3)
        self.assertEqual(self.repo.get_discipline(),[self.dis1,self.dis2,dis3])
        self.repo.cauta(3)
        self.repo.cauta(5)
        c3=self.repo.cauta(1)
        self.assertEqual(c3.get_id(),dis3.get_id())
        self.assertEqual(c3.get_nume(),dis3.get_nume())
        self.assertEqual(c3.get_nume_prof(),dis3.get_nume_prof())
    def test_sterge(self):
        self.assertRaisesRegex(RepDisException,self.er1,self.repo.sterge,1)
        self.assertEqual(len(self.repo), 2)
        self.assertEqual(self.repo.get_discipline(), [self.dis1, self.dis2])
        self.repo.cauta(3)
        self.repo.cauta(5)
        self.repo.sterge(5)
        self.assertEqual(len(self.repo), 1)
        self.assertEqual(self.repo.get_discipline(), [self.dis2])
        self.repo.cauta(3)
    def test_modifica(self):
        dis=Disciplina(1,"Inot","Inotatorul American")
        self.assertRaisesRegex(RepDisException,self.er1,self.repo.modifica,dis)
        dis=Disciplina(3,"Inot","Inotatorul American")
        self.repo.modifica(dis)
        self.assertEqual(len(self.repo), 2)
        self.assertEqual(self.repo.get_discipline(), [self.dis1, dis])
        self.repo.cauta(3)
        self.repo.cauta(5)
        c=self.repo.cauta(3)
        self.assertEqual(c.get_id(),3)
        self.assertEqual(c.get_nume(), "Inot")
        self.assertEqual(c.get_nume_prof(), "Inotatorul American")

class TestCaseDisciplinaRepozitoriuFisier(TestCaseDisciplinaRepozitoriu):
    def setUp(self):
        fisier=open("./Infrastructura/Repozitorii/BazeDeDate/TestBazeDeDate/test_rep_dis.txt","w")
        fisier.write("5;Batut Din palme;High Five\n\n   \n3;Citit In Palma;Vitoria Lipan\n  ")
        fisier.close()
        self.repo=RepozitoriuDisciplineFisier("TestBazeDeDate/test_rep_dis.txt")
        self.dis1=Disciplina(5,"Batut Din Palme","High Five")
        self.dis2=Disciplina(3,"Citit In Palma","Vitoria Lipan")
        self.er1="Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        self.er2="Eroare:Exista deja o disciplina cu id-ul respectiv;"
    def tearDown(self):
        """
        aproape aproape
        :return:
        """
    def test_no_read(self):
        repo=RepozitoriuDisciplineFisier("TestBazeDeDate/nu_exista.txt")
        self.assertEqual(repo.get_discipline(),[])

class TestCaseDisciplinaServiciu(unittest.TestCase):
    def setUp(self):
        repo=RepozitoriuDiscipline()
        validator=ValidatorDisciplina()
        self.srv=SeriviciuDiscipline(repo,validator)
        self.srv.adauga(1,"Somn","Mos Alprazolam")
        self.srv.adauga(2,"Somnd","Mos Ketamina")
        self.dis1=Disciplina(1,"Somn","Mos Alprazolam")
        self.dis2=Disciplina(2,"Somnd","Mos Ketamina")
    def tearDown(self):
        """
        Und dreizehn zuruck
        :return:
        """
    def test_cauta(self):
        self.assertRaises(ValidatorDisciplinaException,self.srv.cauta,0)
        self.assertRaises(RepDisException,self.srv.cauta,3)
        c=self.srv.cauta(1)
        self.assertEqual(c.get_id(),1)
        self.assertEqual(c.get_nume(),"Somn")
        self.assertEqual(c.get_nume_prof(),"Mos Alprazolam")
    def test_adauga(self):
        self.assertRaises(ValidatorDisciplinaException,self.srv.adauga,1,"ddd","ZZZAAAAAAA")
        self.assertRaises(RepDisException,self.srv.adauga,1,"Hahaha","Acum Miesomn")
        self.assertEqual(self.srv.numar_discipline(),2)
        self.assertEqual(self.srv.get_discipline(),[self.dis1,self.dis2])
        dis3=Disciplina(3,"Istoria Lui Luca Lazar","Dretcanu Mihai")
        self.srv.adauga(3,"Istoria Lui Luca Lazar","Dretcanu Mihai")
        self.assertEqual(self.srv.numar_discipline(),3)
        self.assertEqual(self.srv.get_discipline(),[self.dis1,self.dis2,dis3])
    def test_sterge(self):
        self.assertRaises(ValidatorDisciplinaException,self.srv.sterge,0)
        self.assertRaises(RepDisException,self.srv.sterge,3)
        self.srv.sterge(1)
        self.assertEqual(self.srv.numar_discipline(),1)
        self.assertEqual(self.srv.get_discipline(),[self.dis2])
    def test_modifica(self):
        self.assertRaises(ValidatorDisciplinaException,self.srv.modifica,0,"d",":(")
        self.assertRaises(RepDisException,self.srv.modifica,3,"A","B C")
        self.srv.modifica(1,"Bine Bine","Foarte Bine")
        c=self.srv.cauta(1)
        self.assertEqual(c.get_id(),1)
        self.assertEqual(c.get_nume(),"Bine Bine")
        self.assertEqual(c.get_nume_prof(),"Foarte Bine")


class TesteDisciplina:
    def __gen_ex1(self):
        dis=Disciplina(1,"Matematica","Ciudin Ionela")
        return dis
    def __gen_ex2(self):
        dis=Disciplina(3, "Fizica", "Balauca Cristina")
        return dis
    def __gen_ex3(self):
        dis=Disciplina(100, "Educatie Fizica", "Pomparau Gabriel")
        return dis
    def __gen_ex4(self):
        dis=Disciplina(0,"BOABOLOGIE","Dretca nu Mihai")
        return dis
    def __gen_ex5(self):
        dis=Disciplina(999,"A","N B")
        return dis
    def __gen_ex6(self):
        dis=Disciplina(1000,"Corect","Dar Nu Chiar")
        return dis
    def __gen_ex7(self):
        dis=Disciplina(999,"##", "shoo")
        return dis
    def __gen_ex8(self):
        dis=Disciplina(1000,"nu","Macar Atat")
        return dis
    def __test_domeniu(self):
        dis1=self.__gen_ex1()
        assert dis1.get_id()==1
        assert dis1.get_nume()=="Matematica"
        assert dis1.get_nume_prof()=="Ciudin Ionela"
        assert str(dis1)=="Disciplina - ID:1; Nume:Matematica; Nume profesor:Ciudin Ionela"
        dis2=self.__gen_ex2()
        assert dis2.get_id()==3
        assert dis2.get_nume()=="Fizica"
        assert dis2.get_nume_prof()=="Balauca Cristina"
        assert str(dis2)=="Disciplina - ID:3; Nume:Fizica; Nume profesor:Balauca Cristina"
        dis3=self.__gen_ex3()
        assert dis3.get_id()==100
        assert dis3.get_nume()=="Educatie Fizica"
        assert dis3.get_nume_prof()=="Pomparau Gabriel"
        assert str(dis3)=="Disciplina - ID:100; Nume:Educatie Fizica; Nume profesor:Pomparau Gabriel"
        dis1.set_nume("Analiza Matematica")
        assert dis1.get_id()==1
        assert dis1.get_nume()=="Analiza Matematica"
        assert dis1.get_nume_prof()=="Ciudin Ionela"
        dis1.set_nume_prof("Ciudin Ion")
        assert dis1.get_id()==1
        assert dis1.get_nume()=="Analiza Matematica"
        assert dis1.get_nume_prof()=="Ciudin Ion"
        dis2.set_nume("Mecanica")
        assert dis2.get_id()==3
        assert dis2.get_nume()=="Mecanica"
        assert dis2.get_nume_prof()=="Balauca Cristina"
        dis2.set_nume_prof("Chitac Dan")
        assert dis2.get_id()==3
        assert dis2.get_nume()=="Mecanica"
        assert dis2.get_nume_prof()=="Chitac Dan"
        dist=Disciplina(1,None,None)
        assert dist==dis1
        assert dist!=dis2
        assert dist!=1
        assert dist!="asd"
        dis1.set_nume("Geografie")
        dis1.set_nume_prof("Gabriela Voinea")
        assert dis1==dist
        dist=Disciplina(100,None,None)
        assert dist!=dis1
        assert dist!=dis2
        assert dist==dis3

    def __test_validator(self):
        validator=ValidatorDisciplina()
        dis1=self.__gen_ex1()
        dis2=self.__gen_ex2()
        dis3=self.__gen_ex3()
        dis4=self.__gen_ex4()
        dis5=self.__gen_ex5()
        validator.validare(dis1)
        validator.validare_id(dis1.get_id())
        validator.validare(dis2)
        validator.validare_id(dis2.get_id())
        validator.validare(dis3)
        validator.validare_id(dis3.get_id())
        try:
            validator.validare(dis4)
            assert False
        except ValidatorDisciplinaException as er:
            erori=""
            erori=erori+"Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
            erori=erori+"Eroare: numele disciplinei trebuie sa fie un string nenul de cuvinte pentru care doar prima" \
                        " litera incepe cu majusculta, iar cuvintele sunt despartite cu cate un spatiu;\n"
            erori=erori+"Eroare: numele profesorului trebuie sa fie un string de doua cuvinte pentru care doar prima" \
                        " litera este cu majuscula, despartite printr-un spatiu"
            assert erori==str(er)
        validator.validare(dis5)
        dis6=self.__gen_ex6()
        dis7=self.__gen_ex7()
        dis8=self.__gen_ex8()
        try:
            validator.validare(dis6)
            assert False
        except ValidatorDisciplinaException as er:
            erori=""
            erori=erori+"Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
            erori=erori+"Eroare: numele profesorului trebuie sa fie un string de doua cuvinte pentru care doar prima" \
                        " litera este cu majuscula, despartite printr-un spatiu"
            assert erori==str(er)
        try:
            validator.validare_id(dis6.get_id())
            assert False
        except ValidatorDisciplinaException as er:
            erori="Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
            assert erori==str(er)
        try:
            validator.validare(dis7)
            assert False
        except ValidatorDisciplinaException as er:
            erori=""
            erori=erori+"Eroare: numele disciplinei trebuie sa fie un string nenul de cuvinte pentru care doar prima" \
                        " litera incepe cu majusculta, iar cuvintele sunt despartite cu cate un spatiu;\n"
            erori=erori+"Eroare: numele profesorului trebuie sa fie un string de doua cuvinte pentru care doar prima" \
                        " litera este cu majuscula, despartite printr-un spatiu"
            assert erori==str(er)
        try:
            validator.validare(dis8)
            assert False
        except ValidatorDisciplinaException as er:
            erori=""
            erori=erori+"Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
            erori=erori+"Eroare: numele disciplinei trebuie sa fie un string nenul de cuvinte pentru care doar prima" \
                        " litera incepe cu majusculta, iar cuvintele sunt despartite cu cate un spatiu;"
            assert erori==str(er)
        try:
            validator.validare_id(dis8.get_id())
            assert False
        except ValidatorDisciplinaException as er:
            erori="Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
            assert erori==str(er)

    def __test_repozitoriu(self):
        repo=RepozitoriuDiscipline()
        assert len(repo)==0
        assert repo.get_discipline()==[]
        dis1=self.__gen_ex1()
        repo.adauga(dis1)
        assert len(repo)==1
        assert repo.get_discipline()==[dis1]
        dis_cautata=repo.cauta(1)
        assert dis_cautata.get_id()==dis1.get_id()
        assert dis_cautata.get_nume()==dis1.get_nume()
        assert dis_cautata.get_nume_prof()==dis1.get_nume_prof()
        try:
            repo.cauta(2)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        try:
            repo.adauga(dis1)
            assert False
        except RepDisException as er:
            assert str(er)=="Eroare:Exista deja o disciplina cu id-ul respectiv;"
        dis2=self.__gen_ex2()
        repo.adauga(dis2)
        assert len(repo)==2
        assert repo.get_discipline()==[dis1,dis2]
        dis_cautata=repo.cauta(1)
        assert dis_cautata.get_id()==dis1.get_id()
        assert dis_cautata.get_nume()==dis1.get_nume()
        assert dis_cautata.get_nume_prof()==dis1.get_nume_prof()
        dis_cautata=repo.cauta(3)
        assert dis_cautata.get_id()==dis2.get_id()
        assert dis_cautata.get_nume()==dis2.get_nume()
        assert dis_cautata.get_nume_prof()==dis2.get_nume_prof()
        try:
            repo.cauta(100)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        try:
            repo.adauga(dis2)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Exista deja o disciplina cu id-ul respectiv;"
        try:
            repo.adauga(dis1)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Exista deja o disciplina cu id-ul respectiv;"
        dis1=self.__gen_ex1()
        dis1.set_nume("Ghost Scot Album Nou")
        dis1.set_nume_prof("Forge Tobias")
        repo.modifica(dis1)
        assert len(repo)==2
        assert repo.get_discipline()==[dis1,dis2]
        dis_cautata=repo.cauta(1)
        assert dis_cautata.get_id()==dis1.get_id()
        assert dis_cautata.get_nume()==dis1.get_nume()
        assert dis_cautata.get_nume_prof()==dis1.get_nume_prof()
        dis_cautata=repo.cauta(3)
        assert dis_cautata.get_id()==dis2.get_id()
        assert dis_cautata.get_nume()==dis2.get_nume()
        assert dis_cautata.get_nume_prof()==dis2.get_nume_prof()
        dist=Disciplina(10,"Salut Lume","Lazarluca Aici")
        try:
            repo.modifica(dist)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        dist=Disciplina(101,"Piraterie Si Jefuit Insule Cu","Mircea Gabi")
        try:
            repo.modifica(dist)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        dis2=self.__gen_ex2()
        dis2.set_nume("Nu Domn Politist")
        dis2.set_nume_prof("Nam Beut")
        repo.modifica(dis2)
        assert len(repo)==2
        assert repo.get_discipline()==[dis1,dis2]
        dis_cautata=repo.cauta(1)
        assert dis_cautata.get_id()==dis1.get_id()
        assert dis_cautata.get_nume()==dis1.get_nume()
        assert dis_cautata.get_nume_prof()==dis1.get_nume_prof()
        dis_cautata=repo.cauta(3)
        assert dis_cautata.get_id()==dis2.get_id()
        assert dis_cautata.get_nume()==dis2.get_nume()
        assert dis_cautata.get_nume_prof()==dis2.get_nume_prof()
        repo.sterge(1)
        assert len(repo)==1
        assert repo.get_discipline()==[dis2]
        dis_cautata=repo.cauta(3)
        assert dis_cautata.get_id()==dis2.get_id()
        assert dis_cautata.get_nume()==dis2.get_nume()
        assert dis_cautata.get_nume_prof()==dis2.get_nume_prof()
        dis3=self.__gen_ex3()
        repo.adauga(dis3)
        try:
            repo.sterge(1)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        repo.sterge(100)
        assert len(repo) == 1
        assert repo.get_discipline() == [dis2]
        dis_cautata = repo.cauta(3)
        assert dis_cautata.get_id() == dis2.get_id()
        assert dis_cautata.get_nume() == dis2.get_nume()
        assert dis_cautata.get_nume_prof() == dis2.get_nume_prof()
        repo.sterge(3)
        assert len(repo)==0
        assert repo.get_discipline()==[]
        try:
            repo.sterge(3)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        try:
            repo.sterge(5)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Nu exista o disciplina cu ID-ul respectiv;"

    def __test_serviciu(self):
        repo=RepozitoriuDiscipline()
        validator=ValidatorDisciplina()
        serv=SeriviciuDiscipline(repo,validator)
        assert serv.numar_discipline()==0
        assert serv.get_discipline()==[]
        serv.adauga(1,"Gramateca", "Lazar Luca")
        dis1=serv.cauta(1)
        assert serv.numar_discipline()==1
        assert serv.get_discipline()==[dis1]
        assert dis1.get_id()==1
        assert dis1.get_nume()=="Gramateca"
        assert dis1.get_nume_prof()=="Lazar Luca"
        try:
            serv.adauga(1,"Gresit-am In Viata","De Siggy Ztardust si Popandaii Aerieni")
            assert False
        except ValidatorDisciplinaException as er:
            eroare=""
            eroare=eroare+"Eroare: numele disciplinei trebuie sa fie un string nenul de cuvinte pentru care doar" \
                          " prima litera incepe cu majusculta, iar cuvintele sunt despartite cu cate un spatiu;\n"
            eroare=eroare+"Eroare: numele profesorului trebuie sa fie un string de doua cuvinte pentru care doar prima" \
                          " litera este cu majuscula, despartite printr-un spatiu"
            assert str(er)==eroare
        try:
            serv.adauga(1, "Vjtdgkdwqjoppamdatcucapuldetastaturaxcvxctiiisqs","Domn Profesor")
            assert False
        except RepDisException as er:
            assert str(er)=="Eroare:Exista deja o disciplina cu id-ul respectiv;"
        try:
            serv.cauta(2)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        serv.adauga(5,"Meteoreologie Subterana", "Popandau Dominic")
        dis1=serv.cauta(1)
        dis2=serv.cauta(5)
        assert serv.numar_discipline()==2
        assert serv.get_discipline()==[dis1,dis2]
        assert dis1.get_id()==1
        assert dis1.get_nume()=="Gramateca"
        assert dis1.get_nume_prof()=="Lazar Luca"
        assert dis2.get_id()==5
        assert dis2.get_nume()=="Meteoreologie Subterana"
        assert dis2.get_nume_prof()=="Popandau Dominic"
        serv.adauga(100,"Papucologie Pentru Psihici","Palton Paprika")
        dis1=serv.cauta(1)
        dis2=serv.cauta(5)
        dis3=serv.cauta(100)
        try:
            serv.cauta(2)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        try:
            serv.cauta(3)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        assert serv.numar_discipline()==3
        assert serv.get_discipline()==[dis1,dis2,dis3]
        assert dis1.get_id()==1
        assert dis1.get_nume()=="Gramateca"
        assert dis1.get_nume_prof()=="Lazar Luca"
        assert dis2.get_id()==5
        assert dis2.get_nume()=="Meteoreologie Subterana"
        assert dis2.get_nume_prof()=="Popandau Dominic"
        assert dis3.get_id()==100
        assert dis3.get_nume()=="Papucologie Pentru Psihici"
        assert dis3.get_nume_prof()=="Palton Paprika"
        try:
            serv.adauga(1001,"Las12", "Gata cu exemplele de genul asta")
            assert False
        except ValidatorDisciplinaException as er:
            eroare = ""
            eroare=eroare+"Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
            eroare = eroare + "Eroare: numele disciplinei trebuie sa fie un string nenul de cuvinte pentru care doar" \
                              " prima litera incepe cu majusculta, iar cuvintele sunt despartite cu cate un spatiu;\n"
            eroare = eroare + "Eroare: numele profesorului trebuie sa fie un string de doua cuvinte pentru care doar prima" \
                              " litera este cu majuscula, despartite printr-un spatiu"
            assert str(er) == eroare
        try:
            serv.cauta(0)
            assert False
        except ValidatorDisciplinaException as er:
            assert str(er)=="Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        try:
            serv.cauta(-1)
            assert False
        except ValidatorDisciplinaException as er:
            assert str(er)=="Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        dis1=serv.cauta(1)
        dis2=serv.cauta(5)
        dis3=serv.cauta(100)
        assert serv.get_discipline()==[dis1,dis2,dis3]
        assert dis1.get_id()==1
        assert dis1.get_nume()=="Gramateca"
        assert dis1.get_nume_prof()=="Lazar Luca"
        assert dis2.get_id()==5
        assert dis2.get_nume()=="Meteoreologie Subterana"
        assert dis2.get_nume_prof()=="Popandau Dominic"
        assert dis3.get_id()==100
        assert dis3.get_nume()=="Papucologie Pentru Psihici"
        assert dis3.get_nume_prof()=="Palton Paprika"
        serv.modifica(1,"Gramatik", "Luca Lazar")
        dis1=serv.cauta(1)
        dis2=serv.cauta(5)
        dis3=serv.cauta(100)
        assert serv.get_discipline()==[dis1,dis2,dis3]
        assert dis1.get_id()==1
        assert dis1.get_nume()=="Gramatik"
        assert dis1.get_nume_prof()=="Luca Lazar"
        assert dis2.get_id()==5
        assert dis2.get_nume()=="Meteoreologie Subterana"
        assert dis2.get_nume_prof()=="Popandau Dominic"
        assert dis3.get_id()==100
        assert dis3.get_nume()=="Papucologie Pentru Psihici"
        assert dis3.get_nume_prof()=="Palton Paprika"
        serv.modifica(100,"Astept", "Asteapta Bine")
        dis1=serv.cauta(1)
        dis2=serv.cauta(5)
        dis3=serv.cauta(100)
        assert serv.get_discipline()==[dis1,dis2,dis3]
        assert dis1.get_id()==1
        assert dis1.get_nume()=="Gramatik"
        assert dis1.get_nume_prof()=="Luca Lazar"
        assert dis2.get_id()==5
        assert dis2.get_nume()=="Meteoreologie Subterana"
        assert dis2.get_nume_prof()=="Popandau Dominic"
        assert dis3.get_id()==100
        assert dis3.get_nume()=="Astept"
        assert dis3.get_nume_prof()=="Asteapta Bine"
        try:
            serv.modifica(3,"Bine", "B B")
            assert False
        except RepDisException as er:
            assert str(er)=="Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        try:
            serv.modifica(0,"Hapciu","Sanatate")
            assert False
        except ValidatorDisciplinaException as er:
            eroare=""
            eroare=eroare+"Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
            eroare = eroare + "Eroare: numele profesorului trebuie sa fie un string de doua cuvinte pentru care doar prima" \
                              " litera este cu majuscula, despartite printr-un spatiu"
            assert str(er)==eroare
        try:
            serv.modifica(1,"Hapciu","Sanatate")
            assert False
        except ValidatorDisciplinaException as er:
            eroare=""
            eroare = eroare + "Eroare: numele profesorului trebuie sa fie un string de doua cuvinte pentru care doar prima" \
                              " litera este cu majuscula, despartite printr-un spatiu"
            assert str(er)==eroare
        try:
            serv.modifica(77, "Salut", "H I")
            assert False
        except RepDisException as er:
            assert str(er)=="Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        serv.modifica(100,"Student", "Nui Student")
        dis1=serv.cauta(1)
        dis2=serv.cauta(5)
        dis3=serv.cauta(100)
        assert serv.get_discipline()==[dis1,dis2,dis3]
        assert dis1.get_id()==1
        assert dis1.get_nume()=="Gramatik"
        assert dis1.get_nume_prof()=="Luca Lazar"
        assert dis2.get_id()==5
        assert dis2.get_nume()=="Meteoreologie Subterana"
        assert dis2.get_nume_prof()=="Popandau Dominic"
        assert dis3.get_id()==100
        assert dis3.get_nume()=="Student"
        assert dis3.get_nume_prof()=="Nui Student"
        serv.sterge(1)
        dis2=serv.cauta(5)
        dis3=serv.cauta(100)
        assert serv.get_discipline()==[dis2,dis3]
        try:
            serv.cauta(1)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        assert dis2.get_id()==5
        assert dis2.get_nume()=="Meteoreologie Subterana"
        assert dis2.get_nume_prof()=="Popandau Dominic"
        assert dis3.get_id()==100
        assert dis3.get_nume()=="Student"
        assert dis3.get_nume_prof()=="Nui Student"
        serv.sterge(100)
        dis2=serv.cauta(5)
        assert serv.get_discipline()==[dis2]
        try:
            serv.cauta(100)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        assert dis2.get_id()==5
        assert dis2.get_nume()=="Meteoreologie Subterana"
        assert dis2.get_nume_prof()=="Popandau Dominic"
        try:
            serv.sterge(100)
            assert False
        except RepDisException as er:
            assert str(er)=="Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        try:
            serv.sterge(0)
            assert False
        except ValidatorDisciplinaException as er:
            assert str(er)=="Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        try:
            serv.sterge(1000)
            assert False
        except ValidatorDisciplinaException as er:
            assert str(er)=="Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        try:
            serv.sterge(4)
            assert False
        except RepDisException as er:
            assert str(er)=="Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        serv.sterge(5)
        assert serv.get_discipline()==[]
        assert serv.numar_discipline()==0
        try:
            serv.cauta(5)
            assert False
        except RepDisException as er:
            assert str(er) == "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        try:
            serv.sterge(5)
            assert False
        except RepDisException as er:
            assert str(er)=="Eroare:Nu exista o disciplina cu ID-ul respectiv;"


    def ruleaza_teste(self):
        self.__test_domeniu()
        self.__test_validator()
        self.__test_repozitoriu()
        self.__test_serviciu()