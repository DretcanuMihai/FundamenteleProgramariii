#modul ce contine clasa pentru testarile functiilor de sortare de liste

import unittest
from Infrastructura.Functii_Ajutatoare.functii_de_sortare import FunctiiSortare

class TestCaseSortari(unittest.TestCase):
    def setUp(self):
        self.l1=[]
        self.l2=[2]
        self.l3=[1,2,3]
        self.l4=[2,3,1]
        self.l5=[1,2,3,1,1,3,2,2]
        self.l5c=[1,2,3,1,1,3,2,2]
    def tearDown(self):
        """
        dedic acest tearDown tuturor sortarilor recursive
        :return:
        """
    def test_quicksort(self):
        f=FunctiiSortare().quicksort
        f(self.l1)
        self.assertEqual(self.l1,[])
        f(self.l2)
        self.assertEqual(self.l2,[2])
        f(self.l3)
        self.assertEqual(self.l3,[1,2,3])
        f(self.l4)
        self.assertEqual(self.l4,[1,2,3])
        f(self.l5)
        self.assertEqual(self.l5,[1,1,1,2,2,2,3,3])
        f(self.l5c,reversed=True)
        self.assertEqual(self.l5c,[3,3,2,2,2,1,1,1])

    def test_gnomesort(self):
        f=FunctiiSortare().gnomesort
        f(self.l1)
        self.assertEqual(self.l1,[])
        f(self.l2)
        self.assertEqual(self.l2,[2])
        f(self.l3)
        self.assertEqual(self.l3,[1,2,3])
        f(self.l4)
        self.assertEqual(self.l4,[1,2,3])
        f(self.l5)
        self.assertEqual(self.l5,[1,1,1,2,2,2,3,3])
        f(self.l5c,reversed=True)
        self.assertEqual(self.l5c,[3,3,2,2,2,1,1,1])

    def test_gnomesort_v2(self):
        f=FunctiiSortare().gnomesort_v2
        f(self.l1,comparator1=lambda x,y:1 if(x%2>y%2) else 0 if(x%2==y%2) else -1)
        self.assertEqual(self.l1,[])
        f(self.l2,comparator1=lambda x,y:1 if(x%2>y%2) else 0 if(x%2==y%2) else -1)
        self.assertEqual(self.l2,[2])
        f(self.l3,comparator1=lambda x,y:1 if(x%2>y%2) else 0 if(x%2==y%2) else -1)
        self.assertEqual(self.l3,[2,1,3])
        f(self.l4,comparator1=lambda x,y:1 if(x%2>y%2) else 0 if(x%2==y%2) else -1)
        self.assertEqual(self.l4,[2,1,3])
        f(self.l5,comparator1=lambda x,y:1 if(x%2>y%2) else 0 if(x%2==y%2) else -1)
        self.assertEqual(self.l5,[2,2,2,1,1,1,3,3])
        f(self.l5c,reversed=True,comparator1=lambda x,y:1 if(x%2>y%2) else 0 if(x%2==y%2) else -1)
        self.assertEqual(self.l5c,[3,3,1,1,1,2,2,2])