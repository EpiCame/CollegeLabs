from domain.entitati import Student,Disciplina,Nota
from domain.validatoare import ValidatorStud, ValidatorDisci, ValidatorNota
from business.services import ServiceNote
from exceptii.erori import ValidError,RepoError
from infrastructura.repos import FileRepo 
from utils.fileutils import clear_file
import unittest 
class StudentsTests(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    def __test_create_student(self):
        stud1=Student(10,'Bogdan')
        self.assertEqual(stud1.get_id(),10)
        self.assertEqual(stud1.get_nume(),'Bogdan')
        self.assertEqual(str(stud1),'10: Bogdan')
        stud1.set_nume('Marius')
        self.assertEqual(stud1.get_nume(),'Marius')
        stud2=Student(10,'Alex')
        self.assertTrue(stud1==stud2)
        self.__student=stud1 
    def __test_valid_student(self):
        valid_stud=ValidatorStud()
        valid_stud.valideaza_student(self.__student)
        self.__stud_id_invalid = Student(-15,"Hagi")
        self.__stud_nume_invalid = Student(10,"")
        self.__stud_invalid = Student(-1,"")
        with self.assertRaises(ValidError):
            valid_stud.valideaza_student(self.__stud_id_invalid)
        with self.assertRaises(ValidError):
            valid_stud.valideaza_student(self.__stud_nume_invalid)
        with self.assertRaises(ValidError):
            valid_stud.valideaza_student(self.__stud_invalid)
        self.__validStudent = valid_stud
    def __test_repo_student(self):
        clear_file('test.txt')
        self.__repo=FileRepo('test.txt',Student.read_line,Student.write_line)
        self.assertEqual(self.__repo.size(),0)
        self.__repo.adauga(self.__student)
        self.assertEqual(self.__repo.size(),1)
        self.assertEqual(self.__repo.get_all(),[self.__student])
        with self.assertRaises(RepoError):
            self.__repo.adauga(self.__student)
        x=self.__repo.cauta(self.__student)
        self.assertEqual(x,self.__student)
        self.__student_inexistent=Student(1,'roman')
        with self.assertRaises(RepoError):
            x=self.__repo.cauta(self.__student_inexistent)
        self.__stud_to_modify=self.__student
        self.__modified_stud=self.__student
        self.__modified_stud.set_nume('fish')
        self.__repo.modifica(self.__stud_to_modify,self.__modified_stud)
        self.assertEqual(self.__student.get_nume(),'fish')
        with self.assertRaises(RepoError):
            self.__repo.sterge(self.__student_inexistent)
        self.__repo.sterge(self.__student)
        self.assertEqual(self.__repo.size(),0)
        self.__repo.adauga(self.__student)
        self.assertEqual(self.__repo.size(),1)
    def run_stud_tests(self):
        self.__test_create_student()
        self.__test_valid_student()
        self.__test_repo_student()
class DisciplinaTests(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    def __test_create_disciplina(self):
        disci=Disciplina(10,'info','neagu')
        self.assertEqual(disci.get_id(),10)
        self.assertEqual(disci.get_nume(),'info')
        self.assertEqual(disci.get_nume_prof(),'neagu')
        disci.set_nume('mate')
        self.assertEqual(disci.get_nume(),'mate')
        disci.set_nume_prof('coada')
        self.assertEqual(disci.get_nume_prof(),'coada')
        disci1=Disciplina(10,'info','neagu')
        self.assertTrue(disci==disci1)
        self.__disciplina=disci 
    def __test_valid_disciplina(self):
        valid_disci=ValidatorDisci()
        valid_disci.valideaza_disciplina(self.__disciplina)
        self.__disci_id_invalid=Disciplina(-10,'heh','ehe')
        self.__disci_nume_invalid=Disciplina(9,'','gabi')
        self.__disci_nume_prof_invalid=Disciplina(9,'Fp','')
        self.__disci_invalid=Disciplina(-2,'','')
        with self.assertRaises(ValidError):
            valid_disci.valideaza_disciplina(self.__disci_id_invalid)
            valid_disci.valideaza_disciplina(self.__disci_nume_invalid)
            valid_disci.valideaza_disciplina(self.__disci_nume_prof_invalid)
            valid_disci.valideaza_disciplina(self.__disci_invalid)
    def __test_repo_disciplina(self):
        clear_file('test.txt')
        self.__repo=FileRepo('test.txt',Disciplina.read_line,Disciplina.write_line)
        self.assertEqual(self.__repo.size(),0)
        self.__repo.adauga(self.__disciplina)
        self.assertEqual(self.__repo.size(),1)
        self.assertEqual(self.__repo.get_all(),[self.__disciplina])
        with self.assertRaises(RepoError):
            self.__repo.adauga(self.__disciplina)
        x=self.__repo.cauta(self.__disciplina)
        self.assertEqual(x,self.__disciplina)
        self.__disci_inexistenta=Disciplina(1,'roman','')
        with self.assertRaises(RepoError):
            x=self.__repo.cauta(self.__disci_inexistenta)
        self.__disci_to_modify=self.__disciplina
        self.__modified_disci=self.__disciplina
        self.__modified_disci.set_nume('geogra')
        self.__modified_disci.set_nume_prof('georgian')
        self.__repo.modifica(self.__disci_to_modify,self.__modified_disci)
        self.assertEqual(self.__disciplina.get_nume(),'geogra')
        self.assertEqual(self.__disciplina.get_nume_prof(),'georgian')
        with self.assertRaises(RepoError):
            self.__repo.sterge(self.__disci_inexistenta)
        self.__repo.sterge(self.__disciplina)
        assert(self.__repo.size()==0)
    def run_disci_tests(self):
        self.__test_create_disciplina()
        self.__test_valid_disciplina()
        self.__test_repo_disciplina()
class NoteTests(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    def __test_creeaza_nota(self):
        self.__student=Student(10,'Bogdan')
        self.__disciplina=Disciplina(1,'info','neagu')
        nota=Nota(self.__student,self.__disciplina,7)
        self.assertEqual(nota.get_stud(),self.__student)
        self.assertEqual(nota.get_disci(),self.__disciplina)
        self.assertEqual(nota.get_nota(),7)
        self.assertEqual(str(nota),self.__student.get_nume()+' are nota 7 la disciplina '+self.__disciplina.get_nume())
        nota2=Nota(self.__student,self.__disciplina,9)
        self.assertFalse(nota==nota2)
        nota.set_nota(9)
        self.assertEqual(nota.get_nota(),9)
        self.assertTrue(nota==nota2)
        self.__nota=nota
    def __test_valideaza_nota(self):
        valid_nota=ValidatorNota()
        valid_nota.valideaza_nota(self.__nota)
        self.__nota_invalida=Nota(self.__student,self.__disciplina,-5)
        with self.assertRaises(ValidError):
            valid_nota.valideaza_nota(self.__nota_invalida)
    def __test_repo_note(self):
        clear_file('test.txt')
        self.__repo=FileRepo('test.txt',Nota.read_line,Nota.write_line)
        self.assertEqual(self.__repo.size(),0)
        self.__repo.adauga(self.__nota)
        self.assertEqual(self.__repo.size(),1)
        self.assertEqual(self.__repo.get_all(),[self.__nota])
        with self.assertRaises(RepoError):
            self.__repo.adauga(self.__nota)
        x=self.__repo.cauta(self.__nota)
        self.assertEqual(x,self.__nota)
        stud=Student(20,'')
        disci=Disciplina(20,'','')
        self.__nota_inexistenta=Nota(stud,disci,4)
        with self.assertRaises(RepoError):
            x=self.__repo.cauta(self.__nota_inexistenta)
        self.__nota_to_modify=self.__nota
        self.__modified_nota=self.__nota
        self.__modified_nota.set_nota(5)
        self.__repo.modifica(self.__nota_to_modify,self.__modified_nota)
        self.assertEqual(self.__nota.get_nota(),5)
        with self.assertRaises(RepoError):
            self.__repo.sterge(self.__nota_inexistenta)
        self.__repo.sterge(self.__nota)
        assert(self.__repo.size()==0)
    def run_note_tests(self):
        self.__test_creeaza_nota()
        self.__test_valideaza_nota()
        self.__test_repo_note()
class RapoarteTests(unittest.TestCase):
    def __init__(self):
        self.__repo_stud=FileRepo("fisier_stud.txt",Student.read_line,Student.write_line)
        self.__repo_disci=FileRepo("fisier_disci.txt",Disciplina.read_line,Disciplina.write_line)
        self.__repo_note=FileRepo("fisier_note.txt",Nota.read_line,Nota.write_line)
        self.__valid_nota=ValidatorNota
        self.__srv_note=ServiceNote(self.__repo_note,self.__repo_stud,self.__repo_disci,self.__valid_nota)
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    def __test_statistica_disciplina(self):
        '''
        testeaza:lista de studenți și notele lor la o disciplină dată, ordonat: alfabetic după nume, după notă.
        '''
        list=self.__srv_note.get_stud_ord(3)
        assert(str(list[0]),'codrin are notele: 3 ')
        assert(str(list[1])=='cosmin are notele: 6 8 ')
    def __test_statistica_medie_studenti(self):
        '''
        testeaza:Primi 20% din studenți ordonat dupa media notelor la toate disciplinele (nume și notă)
        '''
        list=self.__srv_note.get_stud_medie()
        assert(str(list[0])=='adriana 8.0')
        assert(str(list[1])=='cosmin 7.0')
    def run_stats_tests(self):
        self.__test_statistica_disciplina()
        self.__test_statistica_medie_studenti()
        
class Teste():
    def __init__(self,stud_tests,disci_tests,note_tests,rapo_tests):
        self.__stud_tests = stud_tests
        self.__disci_tests = disci_tests
        self.__note_tests = note_tests
        self.__rapo_tests= rapo_tests
    def run_tests(self):
        self.__stud_tests.run_stud_tests()
        self.__disci_tests.run_disci_tests()
        self.__note_tests.run_note_tests()
        self.__rapo_tests.run_stats_tests()

   
    



