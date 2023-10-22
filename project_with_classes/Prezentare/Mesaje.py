#modul cu o clasa de mesaje de afisat

class Mesaje():
    def start(self):
        print("-------------------------------------------------------------------------------------------\n"
              "Aplicatie pornita;\nPentru a vedea o lista cu comenzile posibile introduceti 'meniu'")
    def meniu(self):
        print("Meniu:\n"
              "0.'exit' - opreste aplicatia\n"
              "1.'meniu' - afiseaza meniul\n"
              "2.'afisare_studenti' - afiseaza studentii din repozitoriu\n"
              "3.'adauga_student' - adauga un student in repozitoriu\n"
              "4.'cauta_student' - cauta un student in repozitoriu dupa id\n"
              "5.'modifica_student' - modifica datele unui student in repozitoriu\n"
              "6.'sterge_student' - sterge un student din repozitoriu dupa id\n"
              "7.'afisare_discipline' - afiseaza disciplinele din repozitoriu\n"
              "8.'adauga_disciplina' - adauga o disciplina in repozitoriu\n"
              "9.'cauta_disciplina' - cauta o disciplina in repozitoriu dupa id\n"
              "10.'modifica_disciplina' - modifica datele unei discipline in repozitoriu\n"
              "11.'sterge_disciplina' - sterge o disciplina din repozitoriu dupa id\n"
              "12.'afisare_note' - afiseaza toate notele din repozitoriu\n"
              "13.'adauga_nota' - adauga o nota in repozitoriu de note\n"
              "14.'raport_note_alfabetic' - afiseaza notele elevilor la o disciplina, ordonate alfabetic\n"
              "15.'raport_note_descrescator' - afiseaza notele elevilor la o disciplina, ordonate descrescator\n"
              "16.'raport_20_la_suta' - afiseaza primii 20% din elevi dupa media la toate disciplinele la care au"
              "nota\n"
              "17.'raport_profesori_medie' - afiseaza profesorii in ordine descrescatoare dupa media notelor oferite"
              )
    def comanda_nerecunoscuta(self):
        print("Eroare:Comanda nerecunoscuta - introduceti comanda 'meniu' pentru a vedea o lista cu comenzile posibile")
    def exit(self):
        print("Iesire din aplicatie...")
    def date_invalide(self):
        print("Eroare:Tipul datelor introduse este invalid;")
    def succes(self):
        print("Operatia asupra repozitoriului a fost realizata cu succes;")
    def rep_stud_gol(self):
        print("Repozitoriu de studenti gol;")
    def rep_dis_gol(self):
        print("Repozitoriu de discipline gol;")
    def rep_note_gol(self):
        print("Repozitoriu de note gol;")
    def stud_cautat_inexistent(self):
        print("Studentul cautat nu exista;")
    def dis_cautata_inexistenta(self):
        print("Disciplina cautata nu exista;")