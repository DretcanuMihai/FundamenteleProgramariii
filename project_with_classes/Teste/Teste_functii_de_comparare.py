
from Infrastructura.Functii_Ajutatoare.functii_de_comparare import comparare_medie_alfabetic_profesori,comparare_medie_id,comparare_valoare_id,comparare_nume_id
from Domeniu.Entitati.Entitate_Student import Student
from Domeniu.Entitati.Entitate_Nota import Nota
import unittest

class TestCaseComparatori(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        """
        cred ca-i ultimul set
        :return:
        """
    def test_comparare_nume_id(self):
        f=comparare_nume_id
        l = [Student(2, "George George"), None]
        l1 = [Student(1, "George Georg"), None]
        l2 = [Student(1, "George George"), None]
        l3 = [Student(2, "George George"), None]
        l4 = [Student(3, "George George"), None]
        l5 = [Student(1, "George Georgee"), None]
        self.assertEqual(f(l,l1),1)
        self.assertEqual(f(l, l2), 1)
        self.assertEqual(f(l, l3), 0)
        self.assertEqual(f(l, l4), -1)
        self.assertEqual(f(l, l5), -1)
    def test_comparare_valoare_id(self):
        f=comparare_valoare_id
        l=[Student(2, "George George"), Nota(None,None,7.5)]
        l1= [Student(2, "George George"), Nota(None,None,7.4)]
        l2= [Student(3, "George George"), Nota(None,None,7.5)]
        l3= [Student(2, "George George"), Nota(None,None,7.5)]
        l4= [Student(1, "George George"), Nota(None,None,7.5)]
        l5= [Student(2, "George George"), Nota(None,None,7.6)]
        self.assertEqual(f(l, l1), 1)
        self.assertEqual(f(l, l2), 1)
        self.assertEqual(f(l, l3), 0)
        self.assertEqual(f(l, l4), -1)
        self.assertEqual(f(l, l5), -1)
    def test_comparare_medie_id(self):
        f=comparare_medie_id
        l=[Student(2,"George George"),7.0]
        l1= [Student(2, "Very Nice"), 6.9]
        l2= [Student(3, "George George"), 7.0]
        l3= [Student(2, "George George"), 7.0]
        l4= [Student(1, "George George"), 7.0]
        l5= [Student(2, "George George"), 7.1]
        self.assertEqual(f(l, l1), 1)
        self.assertEqual(f(l, l2), 1)
        self.assertEqual(f(l, l3), 0)
        self.assertEqual(f(l, l4), -1)
        self.assertEqual(f(l, l5), -1)
    def test_comparare_medie_alfabetic_profesori(self):
        f=comparare_medie_alfabetic_profesori
        l=["Azlad Boabe",7.5]
        l1= ["Azlad Boabe", 7.4]
        l2= ["Azlad Boabee", 7.5]
        l3= ["Azlad Boabe", 7.5]
        l4= ["Azlad Boab", 7.5]
        l5= ["Azlad Boabe", 7.6]
        self.assertEqual(f(l, l1), 1)
        self.assertEqual(f(l, l2), 1)
        self.assertEqual(f(l, l3), 0)
        self.assertEqual(f(l, l4), -1)
        self.assertEqual(f(l, l5), -1)