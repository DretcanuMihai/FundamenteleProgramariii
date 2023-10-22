#modul pentru testele legate de entitatea nota

from Domeniu.Entitati.Entitate_Nota import Nota
from Domeniu.Validatoare.Validator_Nota import ValidatorNota
from Infrastructura.Repozitorii.RepozitoriuNote import RepozitoriuNote,RepozitoriuNoteFisier
from Infrastructura.Repozitorii.RepozitoriuDiscipline import RepozitoriuDiscipline
from Infrastructura.Repozitorii.RepozitoriuStudenti import RepozitoriuStudenti
from Servicii.ServiciuNote import ServiciuNote
from Domeniu.Entitati.Entitate_Student import Student
from Domeniu.Entitati.Entitate_Disciplina import Disciplina
from Exceptii.exceptii import ValidatorNotaException,RepNoteException, RepDisException,RepStudException

import unittest

class TestCaseNotaDomeniu(unittest.TestCase):

    def setUp(self):
        self.ex1=Nota(3,10,5.77)
    def tearDown(self):
        """
        DUHB
        :return:
        """
    def test_get(self):
        self.assertEqual(self.ex1.get_id_student(),3)
        self.assertEqual(self.ex1.get_id_disciplina(),10)
        self.assertEqual(self.ex1.get_valoare(),5.77)
    def test_equ(self):
        self.assertTrue(self.ex1==Nota(3,10,None))
        self.assertFalse(self.ex1==Nota(3,1,None))
        self.assertFalse(self.ex1==Nota(1,10,None))
        self.assertFalse(self.ex1==Nota(1,1,None))
    def test_str(self):
        self.assertEqual(str(self.ex1),"Nota:5.77")
        self.assertEqual(str(Nota(1,1,10.0)),"Nota:10.00")

class TestCaseNotaValidator(unittest.TestCase):
    def setUp(self):
        self.validator=ValidatorNota()
    def tearDown(self):
        """
        whatsername
        :return:
        """
    def test_validare(self):
        erori=""
        erori = erori + "Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
        erori = erori + "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
        erori = erori + "Eroare: valoarea notei trebuie sa fie un float mai mare sau egal cu 1 si mai mic sau egal" \
                        " cu 10;"
        er1=erori
        erori=""
        erori = erori + "Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
        erori = erori + "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        er2=erori
        erori=""
        erori = erori + "Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
        erori = erori + "Eroare: valoarea notei trebuie sa fie un float mai mare sau egal cu 1 si mai mic sau egal" \
                        " cu 10;"
        er3=erori
        erori=""
        erori = erori + "Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;"
        er4=erori
        erori=""
        erori = erori + "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
        erori = erori + "Eroare: valoarea notei trebuie sa fie un float mai mare sau egal cu 1 si mai mic sau egal" \
                        " cu 10;"
        er5=erori
        erori=""
        erori = erori + "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        er6=erori
        erori=""
        erori = erori + "Eroare: valoarea notei trebuie sa fie un float mai mare sau egal cu 1 si mai mic sau egal" \
                        " cu 10;"
        er7=erori
        ex1=Nota(0,0,0)
        ex2=Nota(100000,1000,1.0)
        ex3=Nota(123456,1,0.99)
        ex4=Nota(-1,1,1.00)
        ex5=Nota(1,-1,0)
        ex6=Nota(3,1234,7.77)
        ex7=Nota(4,123,10.01)
        ex8=Nota(1,1,1.00)
        self.assertRaisesRegex(ValidatorNotaException,er1,self.validator.validare,ex1)
        self.assertRaisesRegex(ValidatorNotaException, er2, self.validator.validare, ex2)
        self.assertRaisesRegex(ValidatorNotaException, er3, self.validator.validare, ex3)
        self.assertRaisesRegex(ValidatorNotaException, er4, self.validator.validare, ex4)
        self.assertRaisesRegex(ValidatorNotaException, er5, self.validator.validare, ex5)
        self.assertRaisesRegex(ValidatorNotaException, er6, self.validator.validare, ex6)
        self.assertRaisesRegex(ValidatorNotaException, er7, self.validator.validare, ex7)
        self.validator.validare(ex8)
    def test_validare_id_stud(self):
        er="Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;"
        self.assertRaisesRegex(ValidatorNotaException,er,self.validator.validare_id_stud,0)
        self.assertRaisesRegex(ValidatorNotaException, er, self.validator.validare_id_stud, -5)
        self.assertRaisesRegex(ValidatorNotaException, er, self.validator.validare_id_stud, 100000)
        self.assertRaisesRegex(ValidatorNotaException, er, self.validator.validare_id_stud, 123456)
        self.validator.validare_id_stud(123)
    def test_validare_id_dis(self):
        er="Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        self.assertRaisesRegex(ValidatorNotaException,er,self.validator.validare_id_dis,0)
        self.assertRaisesRegex(ValidatorNotaException, er, self.validator.validare_id_dis, -1)
        self.assertRaisesRegex(ValidatorNotaException, er, self.validator.validare_id_dis, 1000)
        self.assertRaisesRegex(ValidatorNotaException, er, self.validator.validare_id_dis, 1234)
        self.validator.validare_id_dis(10)

class TestCaseNotaRepozitoriu(unittest.TestCase):
    def setUp(self):
        self.repo=RepozitoriuNote()
        self.nota1=Nota(1,1,7.77)
        self.repo.adauga_nota(self.nota1)
        self.nota2=Nota(3,13,2.34)
        self.repo.adauga_nota(self.nota2)
        self.er1="Eroare:Exista deja o nota atribuita studentului respectiv la disciplina selectata;"
        self.er2="Eroare:Nu exista nota cautata;"
    def tearDown(self):
        """
        Overcompensate
        :return:
        """
    def test_cauta_nota(self):
        self.assertRaisesRegex(RepNoteException,self.er2,self.repo.cauta_nota,2,2)
        self.assertRaisesRegex(RepNoteException, self.er2, self.repo.cauta_nota,3,1)
        self.assertRaisesRegex(RepNoteException, self.er2, self.repo.cauta_nota,1,3)
        c=self.repo.cauta_nota(1,1)
        self.assertEqual(c.get_id_student(),1)
        self.assertEqual(c.get_id_disciplina(),1)
        self.assertEqual(c.get_valoare(),7.77)

    def test_adauga_nota(self):
        self.assertRaisesRegex(RepNoteException,self.er1,self.repo.adauga_nota,Nota(1,1,3))
        self.assertEqual(len(self.repo),2)
        self.assertEqual(self.repo.get_all(),[self.nota1,self.nota2])
        nota3=Nota(1,3,3.33)
        self.repo.adauga_nota(nota3)
        self.assertEqual(len(self.repo),3)
        self.assertEqual(self.repo.get_all(),[self.nota1,self.nota2,nota3])
    def test_sterge_nota(self):
        self.assertRaisesRegex(RepNoteException,self.er2,self.repo.sterge_nota,1,3)
        self.assertEqual(len(self.repo), 2)
        self.assertEqual(self.repo.get_all(), [self.nota1, self.nota2])
        self.repo.sterge_nota(1,1)
        self.assertEqual(len(self.repo),1)
        self.assertEqual(self.repo.get_all(),[self.nota2])

class TestCaseNotaRepozitoriuFisier(TestCaseNotaRepozitoriu):
    def setUp(self):
        fisier=open("./Infrastructura/Repozitorii/BazeDeDate/TestBazeDeDate/test_rep_note.txt","w")
        fisier.write("  \n1;1;7.77   \n\n   3;13;2.34\n")
        fisier.close()
        self.repo=RepozitoriuNoteFisier("TestBazeDeDate/test_rep_note.txt")
        self.nota1=Nota(1,1,7.77)
        self.nota2=Nota(3,13,2.34)
        self.er1="Eroare:Exista deja o nota atribuita studentului respectiv la disciplina selectata;"
        self.er2="Eroare:Nu exista nota cautata;"
    def tearDown(self):
        """
        Intr-un final
        :return:
        """
    def test_no_read(self):
        repo=RepozitoriuNoteFisier("TestBazeDeDate/nu_exista.txt")
        self.assertEqual(repo.get_all(),[])

class TestCaseNotaServiciu(unittest.TestCase):
    def setUp(self):
        self.repo_stud=RepozitoriuStudenti()
        self.stud1=Student(1,"Giorgi Cluni")
        self.stud2=Student(2,"Black Garfield")
        self.repo_stud.adauga(self.stud1)
        self.repo_stud.adauga(self.stud2)
        self.repo_dis=RepozitoriuDiscipline()
        self.dis1=Disciplina(1,"Baut","Ivanov M")
        self.dis2=Disciplina(2,"Reclame","Spotify Premium")
        self.repo_dis.adauga(self.dis1)
        self.repo_dis.adauga(self.dis2)
        self.repo_note=RepozitoriuNote()
        self.nota11=Nota(1,1,4.00)
        self.nota21=Nota(2,1,10.00)
        self.repo_note.adauga_nota(self.nota11)
        self.repo_note.adauga_nota(self.nota21)
        self.validator=ValidatorNota()
        self.srv1=ServiciuNote(self.repo_note,self.repo_stud,self.repo_dis,self.validator)
    def tearDown(self):
        """
        Stiind ca voi avea de testat iar rapoartele si stergerile de studenti si discipline, ma cuprinde o stare de
        "l'appel du vide"
        :return:
        """
    def test_adauga_nota(self):
        self.assertRaises(ValidatorNotaException,self.srv1.adauga_nota,-1,0,1.1)
        self.assertRaises(RepStudException,self.srv1.adauga_nota,3,1,1.1)
        self.assertRaises(RepDisException,self.srv1.adauga_nota,1,3,1.1)
        self.assertRaises(RepNoteException,self.srv1.adauga_nota,1,1,1.1)
        self.assertEqual(self.srv1.nr_note(),2)
        self.assertEqual(self.srv1.get_all(),[self.nota11,self.nota21])
        self.assertEqual(self.srv1.get_all_for_print(),[[self.nota11,self.stud1,self.dis1],[self.nota21,self.stud2,self.dis1]])
        self.srv1.adauga_nota(1,2,8.90)
        nota12=Nota(1,2,8.90)
        self.assertEqual(self.srv1.nr_note(),3)
        self.assertEqual(self.srv1.get_all(),[self.nota11,self.nota21,nota12])
        self.assertEqual(self.srv1.get_all_for_print(),[[self.nota11,self.stud1,self.dis1],[self.nota21,self.stud2,self.dis1],[nota12,self.stud1,self.dis2]])

    def test_sterge_student(self):
        self.assertRaises(ValidatorNotaException,self.srv1.sterge_student,0)
        self.assertRaises(RepStudException,self.srv1.sterge_student,3)
        self.assertEqual(self.srv1.nr_note(),2)
        self.assertEqual(self.srv1.get_all(),[self.nota11,self.nota21])
        self.assertEqual(self.srv1.get_all_stud(),[self.stud1,self.stud2])
        self.srv1.adauga_nota(1,2,10.0)
        self.srv1.sterge_student(1)
        self.assertEqual(self.srv1.nr_note(),1)
        self.assertEqual(self.srv1.get_all(),[self.nota21])
        self.assertEqual(self.srv1.get_all_stud(),[self.stud2])
    def test_sterge_disciplina(self):
        self.assertRaises(ValidatorNotaException,self.srv1.sterge_disciplina,1000)
        self.assertRaises(RepDisException,self.srv1.sterge_disciplina,3)
        self.assertEqual(self.srv1.nr_note(),2)
        self.assertEqual(self.srv1.get_all(),[self.nota11,self.nota21])
        self.assertEqual(self.srv1.get_all_dis(),[self.dis1,self.dis2])
        self.srv1.adauga_nota(1,2,6.55)
        self.srv1.sterge_disciplina(1)
        self.assertEqual(self.srv1.nr_note(),1)
        self.assertEqual(self.srv1.get_all(),[Nota(1,2,6.55)])
        self.assertEqual(self.srv1.get_all_dis(),[self.dis2])
    def test_raport_disciplina_alfabetic(self):
        self.repo_stud.adauga(Student(5,"Giorgi Cluni"))
        self.repo_stud.adauga(Student(4,"Giorgi Cluni"))
        self.repo_stud.adauga(Student(3,"Zburatorul Eminescian"))
        stud3=Student(3,"Zburatorul Eminescian")
        stud4=Student(4,"Giorgi Cluni")
        stud5=Student(5,"Giorgi Cluni")
        self.srv1=ServiciuNote(self.repo_note,self.repo_stud,self.repo_dis,self.validator)
        self.assertRaises(ValidatorNotaException,self.srv1.raport_disciplina_aflabetic,0)
        self.assertRaises(RepDisException,self.srv1.raport_disciplina_aflabetic,3)
        self.assertEqual(self.srv1.raport_disciplina_aflabetic(1),[self.dis1,[self.stud2,self.nota21],
                                    [self.stud1,self.nota11],[stud4,None],[stud5,None],[stud3,None]])
        self.assertEqual(self.srv1.raport_disciplina_aflabetic(2),[self.dis2,[self.stud2,None],
                                    [self.stud1,None],[stud4,None],[stud5,None],[stud3,None]])
        self.srv1.sterge_student(1)
        self.srv1.sterge_student(2)
        self.srv1.sterge_student(3)
        self.srv1.sterge_student(4)
        self.srv1.sterge_student(5)
        self.assertEqual(self.srv1.raport_disciplina_aflabetic(1),[self.dis1])

    def test_raport_disciplina_descrescator_black_box(self):
        self.assertRaises(ValidatorNotaException,self.srv1.raport_disciplina_descrescator,0)
        self.assertRaises(RepDisException, self.srv1.raport_disciplina_descrescator, 3)
        stud3=Student(3,"Compania Giuco")
        self.repo_stud.adauga(stud3)
        self.srv1=ServiciuNote(self.repo_note,self.repo_stud,self.repo_dis,self.validator)
        self.assertEqual(self.srv1.raport_disciplina_descrescator(1),[self.dis1, [self.stud2, self.nota21], [self.stud1,
                        self.nota11],[stud3,None]])
        self.srv1.sterge_student(3)
        self.assertEqual(self.srv1.raport_disciplina_descrescator(1),[self.dis1,[self.stud2,self.nota21],[self.stud1,
                        self.nota11]])
        self.assertEqual(self.srv1.raport_disciplina_descrescator(2),[self.dis2,[self.stud1,None],[self.stud2,None]])
        self.srv1.adauga_nota(1,2,10.0)
        self.assertEqual(self.srv1.raport_disciplina_descrescator(2),[self.dis2,[self.stud1,Nota(1,2,10.0)],
                                                                      [self.stud2,None]])
        self.srv1.sterge_student(2)
        self.assertEqual(self.srv1.raport_disciplina_descrescator(1),[self.dis1,[self.stud1,self.nota11]])
        self.srv1.sterge_student(1)
        self.assertEqual(self.srv1.raport_disciplina_descrescator(1),[self.dis1])
        self.assertEqual(self.srv1.raport_disciplina_descrescator(2),[self.dis2])

    def test_raport_disciplina_descrescator(self):
        stud10=Student(10,"Aluat Ceva")
        stud6=Student(6,"Quite Punk")
        stud8=Student(8,"The Offspring")
        stud7=Student(7,"Cinco Cinco")
        self.repo_stud.adauga(stud10)
        self.repo_stud.adauga(stud6)
        self.repo_stud.adauga(stud8)
        self.repo_stud.adauga(stud7)
        self.srv1=ServiciuNote(self.repo_note,self.repo_stud,self.repo_dis,self.validator)
        self.srv1.adauga_nota(10,1,3.0)
        self.assertRaises(ValidatorNotaException,self.srv1.raport_disciplina_descrescator,1000)
        self.assertRaises(RepDisException,self.srv1.raport_disciplina_descrescator,5)
        self.assertEqual(self.srv1.raport_disciplina_descrescator(1),[self.dis1,[self.stud2,self.nota21],[self.stud1,
                        self.nota11],[stud10,Nota(10,1,3.0)],[stud6,None],[stud7,None],[stud8,None]])
        self.assertEqual(self.srv1.raport_disciplina_descrescator(2),[self.dis2,[self.stud1,None],[self.stud2,None],
                        [stud6,None],[stud7,None],[stud8,None],[stud10,None]])
        self.srv1.sterge_student(1)
        self.srv1.sterge_student(2)
        self.srv1.sterge_student(6)
        self.srv1.sterge_student(7)
        self.srv1.sterge_student(8)
        self.srv1.sterge_student(10)
        self.assertEqual(self.srv1.raport_disciplina_descrescator(1),[self.dis1])

    def test_raport_20_la_suta(self):
        stud3=Student(3,"Orlando Blu")
        stud5=Student(5,"Test Test")
        stud4=Student(4,"Nu Asteptam")
        self.repo_stud.adauga(stud3)
        self.repo_stud.adauga(stud5)
        self.repo_stud.adauga(stud4)
        self.srv1=ServiciuNote(self.repo_note,self.repo_stud,self.repo_dis,self.validator)
        self.srv1.adauga_nota(2,2,9.50)
        self.assertEqual(self.srv1.raport_20_la_suta(),[[self.stud2,9.75]])
        self.repo_stud.adauga(Student(6,"Prea Mult"))
        self.srv1 = ServiciuNote(self.repo_note, self.repo_stud, self.repo_dis, self.validator)
        self.assertEqual(self.srv1.raport_20_la_suta(), [[self.stud2, 9.75],[self.stud1,4.00]])
        self.srv1.sterge_student(1)
        self.srv1.sterge_student(2)
        self.srv1.sterge_student(3)
        self.srv1.sterge_student(4)
        self.srv1.sterge_student(5)
        self.srv1.sterge_student(6)
        self.assertEqual(self.srv1.raport_20_la_suta(),[])

    def test_raport_profesori_descrescator(self):
        dis3=Disciplina(3,"Matematica","Ivanov M")
        dis4=Disciplina(4,"Spaniola","Heroes Delsilencio")
        dis5=Disciplina(5,"Literatura","Maremotor Muzicuta")
        dis6=Disciplina(6,"Minerit","Tarna Cop")
        self.repo_dis.adauga(dis3)
        self.repo_dis.adauga(dis4)
        self.repo_dis.adauga(dis5)
        self.repo_dis.adauga(dis6)
        self.srv1=ServiciuNote(self.repo_note,self.repo_stud,self.repo_dis,self.validator)
        self.srv1.adauga_nota(1,4,8.00)
        self.srv1.adauga_nota(1,3,1.00)
        self.assertEqual(self.srv1.raport_profesori_descrescator(),[["Heroes Delsilencio",8.00],["Ivanov M",5.00],
                        ["Maremotor Muzicuta",0.0],["Spotify Premium",0.0],["Tarna Cop",0.0]])
        self.srv1.sterge_disciplina(1)
        self.srv1.sterge_disciplina(2)
        self.srv1.sterge_disciplina(3)
        self.srv1.sterge_disciplina(4)
        self.srv1.sterge_disciplina(5)
        self.srv1.sterge_disciplina(6)
        self.assertEqual(self.srv1.raport_profesori_descrescator(),[])




class TesteNota:
    def __gen_ex1(self):
        nota=Nota(1,1,7.76)
        return nota
    def __gen_ex2(self):
        nota=Nota(1,3,1.00)
        return nota
    def __gen_ex3(self):
        nota=Nota(100,455,10.00)
        return nota
    def __gen_ex4(self):
        nota=Nota(0,0,10.01,)
        return nota
    def __gen_ex5(self):
        nota=Nota(1,1000,9.99)
        return nota
    def __gen_ex6(self):
        nota=Nota(45,100, 0.99)
        return nota
    def __gen_ex7(self):
        nota=Nota(100000,33,1.01)
        return nota
    def __test_domeniu(self):
        nota1=self.__gen_ex1()
        nota2=self.__gen_ex2()
        nota3=self.__gen_ex3()
        assert nota1.get_id_student()==1
        assert nota1.get_id_disciplina()==1
        assert abs(nota1.get_valoare()-7.76)<0.00001
        assert nota2.get_id_student() == 1
        assert nota2.get_id_disciplina() == 3
        assert abs(nota2.get_valoare() - 1.00)< 0.00001
        assert nota3.get_id_student()==100
        assert nota3.get_id_disciplina()==455
        assert abs(nota3.get_valoare()-10)<0.00001
        notaT=Nota(1,1,7.76)
        assert notaT==nota1
        assert notaT!=nota2
        assert notaT!=nota3
        notaT=Nota(1,3,3)
        assert notaT!=nota1
        assert notaT==nota2
        assert notaT!=nota3
        notaT=Nota(100,455,None)
        assert notaT!=nota1
        assert notaT!=nota2
        assert notaT==nota3
        assert str(nota1)=="Nota:7.76"
        assert str(nota2)=="Nota:1.00"
        assert str(nota3)=="Nota:10.00"

    def __test_validator(self):
        validator=ValidatorNota()
        nota1=self.__gen_ex1()
        nota2=self.__gen_ex2()
        nota3=self.__gen_ex3()
        nota4=self.__gen_ex4()
        nota5=self.__gen_ex5()
        nota6=self.__gen_ex6()
        nota7=self.__gen_ex7()
        validator.validare(nota1)
        try:
            validator.validare(nota4)
            assert False
        except ValidatorNotaException as er:
            erori=""
            erori=erori+"Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
            erori = erori + "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
            erori=erori+"Eroare: valoarea notei trebuie sa fie un float mai mare sau egal cu 1 si mai mic sau egal" \
                        " cu 10;"
            assert str(er)==erori
        try:
            validator.validare(nota5)
            assert False
        except ValidatorNotaException as er:
            erori=""
            erori = erori + "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
            assert str(er)==erori
        validator.validare(nota2)
        try:
            validator.validare(nota6)
            assert False
        except ValidatorNotaException as er:
            erori=""
            erori=erori+"Eroare: valoarea notei trebuie sa fie un float mai mare sau egal cu 1 si mai mic sau egal" \
                        " cu 10;"
            assert str(er)==erori
        try:
            validator.validare(nota7)
            assert False
        except ValidatorNotaException as er:
            erori=""
            erori=erori+"Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;"
            assert str(er)==erori
        validator.validare(nota3)
        validator.validare_id_dis(1)
        validator.validare_id_dis(999)
        validator.validare_id_stud(555)
        validator.validare_id_stud(99999)
        try:
            validator.validare_id_dis(0)
            assert False
        except ValidatorNotaException as er:
            assert str(er)=="Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        try:
            validator.validare_id_dis(1000)
            assert False
        except ValidatorNotaException as er:
            assert str(er)=="Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        try:
            validator.validare_id_stud(0)
            assert False
        except ValidatorNotaException as er:
            assert str(er)=="Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;"
        try:
            validator.validare_id_stud(11234567)
            assert False
        except ValidatorNotaException as er:
            assert str(er)=="Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;"

    def __test_repo(self):
        repo=RepozitoriuNote()
        assert len(repo)==0
        assert repo.get_all()==[]
        try:
            repo.cauta_nota(1,1)
            assert False
        except RepNoteException as er:
            assert str(er)=="Eroare:Nu exista nota cautata;"
        nota1=self.__gen_ex1()
        nota2=self.__gen_ex2()
        nota3=self.__gen_ex3()
        repo.adauga_nota(nota1)
        assert len(repo)==1
        assert repo.get_all()==[nota1]
        notac=repo.cauta_nota(1,1)
        assert notac.get_id_student()==1
        assert notac.get_id_disciplina()==1
        assert notac.get_valoare()==7.76
        try:
            repo.adauga_nota(nota1)
            assert False
        except RepNoteException as er:
            assert str(er)=="Eroare:Exista deja o nota atribuita studentului respectiv la disciplina selectata;"
        repo.adauga_nota(nota3)
        assert len(repo)==2
        assert repo.get_all()==[nota1,nota3]
        notac=repo.cauta_nota(1,1)
        assert notac.get_id_student()==1
        assert notac.get_id_disciplina()==1
        assert notac.get_valoare()==7.76
        notac=repo.cauta_nota(100,455)
        assert notac.get_id_student()==100
        assert notac.get_id_disciplina()==455
        assert notac.get_valoare()==10.00
        nota3p=Nota(100,455,8.00)
        try:
            repo.adauga_nota(nota3p)
            assert False
        except RepNoteException as er:
            assert str(er)=="Eroare:Exista deja o nota atribuita studentului respectiv la disciplina selectata;"
        repo.adauga_nota(nota2)
        assert len(repo)==3
        assert repo.get_all()==[nota1,nota3,nota2]
        notac=repo.cauta_nota(1,1)
        assert notac.get_id_student()==1
        assert notac.get_id_disciplina()==1
        assert notac.get_valoare()==7.76
        notac=repo.cauta_nota(100,455)
        assert notac.get_id_student()==100
        assert notac.get_id_disciplina()==455
        assert notac.get_valoare()==10.00
        notac=repo.cauta_nota(1,3)
        assert notac.get_id_student()==1
        assert notac.get_id_disciplina()==3
        assert notac.get_valoare()==1.00
        repo.sterge_nota(100,455)
        assert len(repo)==2
        assert repo.get_all()==[nota1,nota2]
        notac=repo.cauta_nota(1,1)
        assert notac.get_id_student()==1
        assert notac.get_id_disciplina()==1
        assert notac.get_valoare()==7.76
        notac=repo.cauta_nota(1,3)
        assert notac.get_id_student()==1
        assert notac.get_id_disciplina()==3
        assert notac.get_valoare()==1.00
        try:
            repo.sterge_nota(100,455)
            assert False
        except RepNoteException as er:
            assert str(er)=="Eroare:Nu exista nota cautata;"
        repo.sterge_nota(1,1)
        assert len(repo)==1
        assert repo.get_all()==[nota2]
        notac=repo.cauta_nota(1,3)
        assert notac.get_id_student()==1
        assert notac.get_id_disciplina()==3
        assert notac.get_valoare()==1.00
        try:
            repo.sterge_nota(10,30)
            assert False
        except RepNoteException as er:
            assert str(er)=="Eroare:Nu exista nota cautata;"
        repo.sterge_nota(1,3)
        assert len(repo)==0
        assert repo.get_all()==[]
        try:
            repo.cauta_nota(1, 3)
            assert False
        except RepNoteException as er:
            assert str(er) == "Eroare:Nu exista nota cautata;"
        try:
            repo.cauta_nota(1, 1)
            assert False
        except RepNoteException as er:
            assert str(er) == "Eroare:Nu exista nota cautata;"

    def __test_serviciu(self):
        repo_note=RepozitoriuNote()
        repo_stud=RepozitoriuStudenti()
        stud1=Student(1,None)
        stud2=Student(2,None)
        stud3=Student(3,None)
        repo_stud.adauga(stud1)
        repo_stud.adauga(stud2)
        repo_stud.adauga(stud3)
        repo_dis=RepozitoriuDiscipline()
        dis1=Disciplina(1,None,None)
        dis2=Disciplina(2,None,None)
        dis3=Disciplina(3,None,None)
        repo_dis.adauga(dis1)
        repo_dis.adauga(dis2)
        repo_dis.adauga(dis3)
        validator=ValidatorNota()
        srv=ServiciuNote(repo_note,repo_stud,repo_dis,validator)
        assert srv.nr_note()==0
        assert srv.get_all()==[]
        assert srv.get_all_for_print()==[]
        try:
            srv.adauga_nota(-1,1000, -5)
            assert False
        except ValidatorNotaException as er:
            erori = ""
            erori = erori + "Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
            erori = erori + "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
            erori = erori + "Eroare: valoarea notei trebuie sa fie un float mai mare sau egal cu 1 si mai mic sau egal" \
                            " cu 10;"
            assert str(er)==erori
        srv.adauga_nota(1,1,1.0)
        nota1=Nota(1,1,1.0)
        assert srv.nr_note()==1
        l=srv.get_all()
        assert l==[nota1]
        assert l[0].get_id_student()==1
        assert l[0].get_id_disciplina()==1
        assert l[0].get_valoare()==1.0
        assert srv.get_all_stud()==[stud1,stud2,stud3]
        assert srv.get_all_dis()==[dis1,dis2,dis3]
        assert srv.get_all_for_print()==[[nota1,stud1,dis1]]
        try:
            srv.adauga_nota(1,1,2.0)
            assert False
        except RepNoteException as er:
            assert str(er)=="Eroare:Exista deja o nota atribuita studentului respectiv la disciplina selectata;"
        try:
            srv.adauga_nota(9,0, 10.01)
            assert False
        except ValidatorNotaException as er:
            erori = ""
            erori = erori + "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
            erori = erori + "Eroare: valoarea notei trebuie sa fie un float mai mare sau egal cu 1 si mai mic sau egal" \
                            " cu 10;"
            assert str(er)==erori
        try:
            srv.adauga_nota(4,4, 4)
            assert False
        except RepStudException as er:
            erori = ""
            erori=erori+"Eroare:Nu exista un student cu acest ID;"
            assert str(er)==erori
        try:
            srv.adauga_nota(1,4, 4)
            assert False
        except RepDisException as er:
            erori = ""
            erori=erori+"Eroare:Nu exista o disciplina cu ID-ul respectiv;"
            assert str(er)==erori
        srv.adauga_nota(2,3,4.5)
        nota2=Nota(2,3,4.5)
        assert srv.nr_note()==2
        l=srv.get_all()
        assert l==[nota1,nota2]
        assert l[0].get_id_student()==1
        assert l[0].get_id_disciplina()==1
        assert l[0].get_valoare()==1.0
        assert l[1].get_id_student()==2
        assert l[1].get_id_disciplina()==3
        assert l[1].get_valoare()==4.5
        assert srv.get_all_stud()==[stud1,stud2,stud3]
        assert srv.get_all_dis()==[dis1,dis2,dis3]
        assert srv.get_all_for_print()==[[nota1,stud1,dis1],[nota2,stud2,dis3]]

        srv.sterge_student(3)
        assert srv.nr_note()==2
        l=srv.get_all()
        assert l==[nota1,nota2]
        assert l[0].get_id_student()==1
        assert l[0].get_id_disciplina()==1
        assert l[0].get_valoare()==1.0
        assert l[1].get_id_student()==2
        assert l[1].get_id_disciplina()==3
        assert l[1].get_valoare()==4.5
        assert srv.get_all_stud()==[stud1,stud2]
        assert srv.get_all_dis()==[dis1,dis2,dis3]
        assert srv.get_all_for_print()==[[nota1,stud1,dis1],[nota2,stud2,dis3]]
        srv.sterge_disciplina(2)
        assert srv.nr_note()==2
        l=srv.get_all()
        assert l==[nota1,nota2]
        assert l[0].get_id_student()==1
        assert l[0].get_id_disciplina()==1
        assert l[0].get_valoare()==1.0
        assert l[1].get_id_student()==2
        assert l[1].get_id_disciplina()==3
        assert l[1].get_valoare()==4.5
        assert srv.get_all_stud()==[stud1,stud2]
        assert srv.get_all_dis()==[dis1,dis3]
        assert srv.get_all_for_print()==[[nota1,stud1,dis1],[nota2,stud2,dis3]]
        try:
            srv.sterge_student(3)
            assert False
        except RepStudException as er:
            assert str(er)=="Eroare:Nu exista un student cu acest ID;"
        try:
            srv.sterge_student(-1)
            assert False
        except ValidatorNotaException as er:
            assert str(er)=="Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;"
        try:
            srv.sterge_disciplina(2)
            assert False
        except RepDisException as er:
            assert str(er)=="Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        try:
            srv.sterge_disciplina(1000)
            assert False
        except ValidatorNotaException as er:
            assert str(er)=="Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        srv.sterge_student(1)
        assert srv.nr_note()==1
        l=srv.get_all()
        assert l==[nota2]
        assert l[0].get_id_student()==2
        assert l[0].get_id_disciplina()==3
        assert l[0].get_valoare()==4.5
        assert srv.get_all_stud()==[stud2]
        assert srv.get_all_dis()==[dis1,dis3]
        assert srv.get_all_for_print()==[[nota2,stud2,dis3]]
        srv.sterge_disciplina(3)
        assert srv.nr_note()==0
        l=srv.get_all()
        assert l==[]
        assert srv.get_all_stud()==[stud2]
        assert srv.get_all_dis()==[dis1]
        assert srv.get_all_for_print()==[]
        repo_stud=RepozitoriuStudenti()
        stud1=Student(1,"Daniel Daniel")
        stud2=Student(2,"Dorin Doreste")
        stud3=Student(3,"Daniel Dan")
        stud4=Student(4,"Daniel Daniel")
        repo_stud.adauga(stud1)
        repo_stud.adauga(stud2)
        repo_stud.adauga(stud3)
        repo_stud.adauga(stud4)
        repo_dis=RepozitoriuDiscipline()
        dis1=Disciplina(1,"Distractie Distractiva","Mary Juana")
        dis2=Disciplina(2,"Assertul Din Teste Face","Zbrr Zbrr")
        dis3=Disciplina(3,"Disciplina Disciplinatorie","Domnul Domnisor")
        repo_dis.adauga(dis1)
        repo_dis.adauga(dis2)
        repo_dis.adauga(dis3)
        repo_note=RepozitoriuNote()
        validator=ValidatorNota()
        srv=ServiciuNote(repo_note,repo_stud,repo_dis,validator)
        assert srv.raport_disciplina_aflabetic(1)==[dis1,[stud3,None],[stud1,None],[stud4,None],[stud2,None]]
        assert srv.raport_disciplina_descrescator(1)==[dis1,[stud1,None],[stud2,None],[stud3,None],[stud4,None]]
        assert srv.raport_20_la_suta()==[[stud1,0.0]]
        try:
            srv.raport_disciplina_aflabetic(1000)
            assert False
        except ValidatorNotaException as er:
            assert str(er)=="Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        try:
            srv.raport_disciplina_aflabetic(55)
            assert False
        except RepDisException as er:
            assert str(er)=="Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        try:
            srv.raport_disciplina_descrescator(-1)
            assert False
        except ValidatorNotaException as er:
            assert str(er)=="Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        try:
            srv.raport_disciplina_descrescator(10)
            assert False
        except RepDisException as er:
            assert str(er)=="Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        srv.adauga_nota(1,1,5.00)
        srv.adauga_nota(2,3,4.40)
        srv.adauga_nota(2,1,5.00)
        srv.adauga_nota(3,1,4.13)
        srv.adauga_nota(4,1,7.70)
        nota1=Nota(1,1,5.00)
        nota2=Nota(2,3,4.40)
        nota3=Nota(2,1,5.00)
        nota4=Nota(3,1,4.13)
        nota5=Nota(4,1,7.70)
        assert srv.raport_disciplina_aflabetic(1) == [dis1, [stud3, nota4], [stud1, nota1], [stud4,nota5], [stud2,nota3]]
        assert srv.raport_disciplina_aflabetic(3) == [dis3, [stud3, None], [stud1, None], [stud4, None], [stud2, nota2]]
        assert srv.raport_disciplina_descrescator(1)==[dis1,[stud4,nota5],[stud1,nota1],[stud2,nota3],[stud3,nota4]]
        assert srv.raport_disciplina_descrescator(3)==[dis3,[stud2,nota2],[stud1,None],[stud3,None],[stud4,None]]
        assert srv.raport_20_la_suta()==[[stud4,7.70]]
        repo_stud=RepozitoriuStudenti()
        stud1=Student(1,"Daniel Daniel")
        stud2=Student(2,"Dorin Doreste")
        stud3=Student(3,"Daniel Dan")
        stud4=Student(4,"Daniel Daniel")
        stud5 = Student(5, "Eaniel Eaniel")
        stud6 = Student(6, "Faniel Faniel")
        stud7 = Student(7, "Ganiel Ganiel")
        stud8 = Student(8, "Haniel Haniel")
        stud9 = Student(9, "Ianiel Ianiel")
        stud10 = Student(10, "Janiel Janiel")
        repo_stud.adauga(stud1)
        repo_stud.adauga(stud2)
        repo_stud.adauga(stud3)
        repo_stud.adauga(stud4)
        repo_stud.adauga(stud5)
        repo_stud.adauga(stud6)
        repo_stud.adauga(stud7)
        repo_stud.adauga(stud8)
        repo_stud.adauga(stud9)
        repo_stud.adauga(stud10)
        repo_dis=RepozitoriuDiscipline()
        dis1=Disciplina(1,"Distractie Distractiva","Mary Juana")
        dis2=Disciplina(2,"Assertul Din Teste Face","Zbrr Zbrr")
        dis3=Disciplina(3,"Disciplina Disciplinatorie","Domnul Domnisor")
        repo_dis.adauga(dis1)
        repo_dis.adauga(dis2)
        repo_dis.adauga(dis3)
        repo_note=RepozitoriuNote()
        nota11=Nota(1,1,10.0)
        nota12=Nota(1,2,10.0)
        nota13=Nota(1,3,10.0)
        nota23=Nota(2,3,5.55)
        nota41=Nota(4,1,9.00)
        nota42=Nota(4,2,9.77)
        nota43=Nota(4,3,9.20)
        nota53=Nota(5,3,9.00)
        repo_note.adauga_nota(nota11)
        repo_note.adauga_nota(nota12)
        repo_note.adauga_nota(nota13)
        repo_note.adauga_nota(nota23)
        repo_note.adauga_nota(nota41)
        repo_note.adauga_nota(nota42)
        repo_note.adauga_nota(nota43)
        repo_note.adauga_nota(nota53)
        validator=ValidatorNota()
        srv=ServiciuNote(repo_note,repo_stud,repo_dis,validator)
        assert srv.raport_20_la_suta()==[[stud1,10.0],[stud4,9.32]]
        repo_stud=RepozitoriuStudenti()
        repo_dis=RepozitoriuDiscipline()
        repo_note=RepozitoriuNote()
        validator=ValidatorNota()
        srv=ServiciuNote(repo_note,repo_stud,repo_dis,validator)
        assert srv.raport_20_la_suta()==[]
        assert srv.raport_profesori_descrescator()==[]
        repo_stud=RepozitoriuStudenti()
        stud1 = Student(1, "A A")
        stud2 = Student(2, "B B")
        stud3 = Student(3, "C C")
        stud4 = Student(4, "D D")
        stud5 = Student(5, "E E")
        repo_stud.adauga(stud1)
        repo_stud.adauga(stud2)
        repo_stud.adauga(stud3)
        repo_stud.adauga(stud4)
        repo_stud.adauga(stud5)
        dis1= Disciplina(1,"A", "Ap Ap")
        dis2=Disciplina(2,"B","Bp Bp")
        dis3=Disciplina(3,"C","Cp Cp")
        dis4=Disciplina(4,"D","Ap Ap")
        dis5=Disciplina(5,"E","Ap Ap")
        repo_dis=RepozitoriuDiscipline()
        repo_dis.adauga(dis1)
        repo_dis.adauga(dis2)
        repo_dis.adauga(dis3)
        repo_dis.adauga(dis4)
        repo_dis.adauga(dis5)
        nota1 = Nota(1,1,7)
        nota2=Nota(1,3,3)
        nota3=Nota(2,3,10)
        nota4=Nota(5,5,2)
        nota5=Nota(4,5,3)
        nota6=Nota(5,3,10)
        repo_note=RepozitoriuNote()
        repo_note.adauga_nota(nota1)
        repo_note.adauga_nota(nota2)
        repo_note.adauga_nota(nota3)
        repo_note.adauga_nota(nota4)
        repo_note.adauga_nota(nota5)
        repo_note.adauga_nota(nota6)
        validator=ValidatorNota()
        srv=ServiciuNote(repo_note,repo_stud,repo_dis,validator)
        assert srv.raport_profesori_descrescator()==[["Cp Cp",7.67],["Ap Ap",4.0],["Bp Bp",0.0]]
        nota1=Nota(1,1,5)
        nota2=Nota(2,1,5)
        nota3=Nota(1,2,5)
        nota4=Nota(2,2,5)
        nota5=Nota(1,3,5)
        nota6=Nota(2,3,5)
        repo_note=RepozitoriuNote()
        repo_note.adauga_nota(nota1)
        repo_note.adauga_nota(nota2)
        repo_note.adauga_nota(nota3)
        repo_note.adauga_nota(nota4)
        repo_note.adauga_nota(nota5)
        repo_note.adauga_nota(nota6)
        validator=ValidatorNota()
        srv=ServiciuNote(repo_note,repo_stud,repo_dis,validator)
        assert srv.raport_profesori_descrescator() == [["Ap Ap", 5.0], ["Bp Bp", 5.0], ["Cp Cp", 5.0]]

    def ruleaza_teste(self):
        self.__test_domeniu()
        self.__test_validator()
        self.__test_repo()
        self.__test_serviciu()