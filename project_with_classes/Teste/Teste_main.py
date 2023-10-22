#modulul principal de testare ce va apela celelalte module de testare

from Teste.Teste_Student import TesteStudent, TestCaseStudentDomeniu, TestCaseStudentValidator,TestCaseStudentRepozitoriu,TestCaseStudentServiciu,TestCaseStudentRepozitoriuFisier
from Teste.Teste_functii_siruri_de_caractere import TesteFunctiiSiruriCaractere, TestCaseSiruriCaractere
from Teste.Teste_Disciplina import TesteDisciplina,TestCaseDisciplinaDomeniu,TestCaseDisciplinaValidator,TestCaseDisciplinaRepozitoriu,TestCaseDisciplinaServiciu,TestCaseDisciplinaRepozitoriuFisier
from Teste.Teste_Nota import TesteNota,TestCaseNotaDomeniu,TestCaseNotaValidator,TestCaseNotaRepozitoriu,TestCaseNotaServiciu,TestCaseNotaRepozitoriuFisier
from Teste.Teste_functii_de_sortare import TestCaseSortari
from Teste.Teste_functii_de_comparare import TestCaseComparatori

class ToateTestele:
    def __init__(self):
        self.__teste_siruri_de_caractere=TesteFunctiiSiruriCaractere()
        self.__teste_student=TesteStudent()
        self.__teste_disciplina=TesteDisciplina()
        self.__teste_nota=TesteNota()
    def ruleaza_teste(self):
        self.__teste_siruri_de_caractere.ruleaza_teste()
        self.__teste_student.ruleaza_teste()
        self.__teste_disciplina.ruleaza_teste()
        self.__teste_nota.ruleaza_teste()