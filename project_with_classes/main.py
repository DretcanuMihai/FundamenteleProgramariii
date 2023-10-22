#functie principala ce porneste si asambleaza efectiv aplicatia

import unittest
from Teste.Teste_main import *
from Infrastructura.Repozitorii.RepozitoriuStudenti import RepozitoriuStudenti,RepozitoriuStudentiFisier,RepozitoriuStudentiDoarFisier
from Infrastructura.Repozitorii.RepozitoriuDiscipline import RepozitoriuDiscipline,RepozitoriuDisciplineFisier
from Infrastructura.Repozitorii.RepozitoriuNote import RepozitoriuNote,RepozitoriuNoteFisier
from Domeniu.Validatoare.Validator_Student import ValidatorStudent
from Domeniu.Validatoare.Validator_Disciplina import ValidatorDisciplina
from Domeniu.Validatoare.Validator_Nota import ValidatorNota
from Servicii.ServiciuStudenti import ServiciuStudenti
from Servicii.ServiciuDiscipline import SeriviciuDiscipline
from Servicii.ServiciuNote import ServiciuNote
from Prezentare.Interfata_Utilizator import Interfata_Utilizator

#initializarea si pornirea testarilor
if __name__ == '__main__':
    testare = ToateTestele()
    testare.ruleaza_teste()
    unittest.main(exit=False)

#crearea serviciilor

#fara fisier
#repo_stud=RepozitoriuStudenti()
#repo_dis=RepozitoriuDiscipline()
#repo_note=RepozitoriuNote()

#din fisier
#repo_stud=RepozitoriuStudentiFisier("studenti.txt")
repo_stud=RepozitoriuStudentiDoarFisier("student_2.txt")
repo_dis=RepozitoriuDisciplineFisier("discipline.txt")
repo_note=RepozitoriuNoteFisier("note.txt")

validator_stud=ValidatorStudent()
validator_dis=ValidatorDisciplina()
validator_note=ValidatorNota()
serviciu_stud=ServiciuStudenti(repo_stud,validator_stud)
serviciu_dis=SeriviciuDiscipline(repo_dis,validator_dis)
serviciu_note=ServiciuNote(repo_note,repo_stud,repo_dis,validator_note)
consola=Interfata_Utilizator(serviciu_stud, serviciu_dis,serviciu_note)
#consola.ruleaza()