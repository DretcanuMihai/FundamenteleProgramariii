#modul ce contine clasa pentru testarile functiilor ce lucreaza cu siruri de caractere

from Infrastructura.Functii_Ajutatoare.functii_siruri_de_caractere import FunctiiSiruriCaractere
import unittest

class TestCaseSiruriCaractere(unittest.TestCase):
    def setUp(self):
        self.ex1=""
        self.ex2p1="#asdd"
        self.ex2p2="~dd"
        self.ex3="D"
        self.ex4p1="AddA"
        self.ex4p2="Dzz~"
        self.ex5="Corect"
        self.ex6="Dum Dum Dum"
        self.ex7="Dum Dum"
        self.ex8="Dum #f"
        self.ex9="dd Dum"
        self.ex10="zbbrr factesteleunit"
        self.f=FunctiiSiruriCaractere()

    def tearDown(self):
        """
        BFMV
        :return:HT
        """
    def test_nume_corect(self):
        self.assertTrue(self.f.nume_corect(self.ex1)==False, "Cazul sir vid")
        self.assertTrue(self.f.nume_corect(self.ex2p1) == False,"T sau F - prim caracter")
        self.assertTrue(self.f.nume_corect(self.ex2p2) == False, "F sau T - prim caracter")
        self.assertTrue(self.f.nume_corect(self.ex3) == True,"Cazul cand e de o litera si nu intra in for")
        self.assertTrue(self.f.nume_corect(self.ex4p1) == False,"T sau F - un caracter nu e litera mica")
        self.assertTrue(self.f.nume_corect(self.ex4p2) == False, "F sau T - un caracter nu e litera mica")
        self.assertTrue(self.f.nume_corect(self.ex5) == True,"Ajunge la sfarsit")

    def test_fn_corect(self):
        self.assertTrue(self.f.fn_corect(self.ex1)==False, "Nr. cuvinte mai mic ca 2")
        self.assertTrue(self.f.fn_corect(self.ex6) == False, "Nr. cuvinte mai mare ca 2")
        self.assertTrue(self.f.fn_corect(self.ex7) == True, "T si T - verificarea celor 2 cuvinte")
        self.assertTrue(self.f.fn_corect(self.ex8) == False, "T si F - verificarea celor 2 cuvinte")
        self.assertTrue(self.f.fn_corect(self.ex9) == False, "F si T - verificarea celor 2 cuvinte")
        self.assertTrue(self.f.fn_corect(self.ex10) == False, "F si F - verificarea celor 2 cuvinte")

    def test_fd_corect(self):
        self.assertTrue(self.f.fd_corect(self.ex1)==False,"Cuvant vid - split bizar")
        self.assertTrue(self.f.fd_corect(self.ex8) == False, "Unul din cuvinte nu e bun")
        self.assertTrue(self.f.fd_corect(self.ex6)==True,"Toate cuvintele valide - ar trebui sa poata iesi din for")

class TesteFunctiiSiruriCaractere:
    def __test_nume_corect(self, functii):
        test=functii.nume_corect
        assert test("")==False
        assert test("A")==True
        assert test("a")==False
        assert test("Stefan")==True
        assert test(" Stefan")==False
        assert test("nu")==False
        assert test("AAndrei")==False
        assert test("#")==False

    def __test_fn_corect(self, functii):
        test=functii.fn_corect
        assert test("")==False
        assert test("A")==False
        assert test("AB")==False
        assert test(" A A")==False
        assert test(" Denis Da")==False
        assert test("A A ")==False
        assert test("A  A")==False
        assert test("#as Dan")==False
        assert test("Dan Dan Dan")==False
        assert test("Gabriel POmparau")==False
        assert test("GAbriel Pomparau")==False
        assert test("Andrei Aciobanitei")==True
        assert test("A B")==True

    def __test_fd_correct(self, functii):
        test=functii.fd_corect
        assert test("")==False
        assert test(" ")==False
        assert test("     ")==False
        assert test("A")==True
        assert test("A A A")==True
        assert test("#")==False
        assert test("A # A")==False
        assert test("A A #")==False
        assert test("a")==False
        assert test("A a")==False
        assert test("A  A")==False
        assert test("Analiza Matematica")==True
        assert test("AnaliZa Matematica")==False
        assert test("AnalizA Matematica")==False
        assert test("Analiza MatematicA")==False
        assert test("Introduceti Boabologia In Scoli")==True

    def ruleaza_teste(self):
        functii=FunctiiSiruriCaractere()
        self.__test_nume_corect(functii)
        self.__test_fn_corect(functii)
        self.__test_fd_correct(functii)