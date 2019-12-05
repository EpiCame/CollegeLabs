from tests.teste import Teste, StudentsTests, DisciplinaTests, NoteTests, RapoarteTests
from infrastructura.repos import FileRepo
from domain.validatoare import ValidatorStud,ValidatorDisci,ValidatorNota
from business.services import ServiceStud,ServiceDisci,ServiceNote
from presentation.console import Console 
from domain.entitati import Student,Disciplina,Nota
stud_test=StudentsTests()
disci_test=DisciplinaTests()
note_test=NoteTests()
stats_test=RapoarteTests()
teste=Teste(stud_test,disci_test,note_test,stats_test)
teste.run_tests()
repoStud=FileRepo('fisier_stud.txt',Student.read_line,Student.write_line)
repoDisci=FileRepo('fisier_disci.txt',Disciplina.read_line,Disciplina.write_line)
repoNote=FileRepo('fisier_note.txt',Nota.read_line, Nota.write_line)
valid_stud=ValidatorStud()
valid_disci=ValidatorDisci()
valid_nota=ValidatorNota()
srv_stud=ServiceStud(repoStud,valid_stud)
srv_disci=ServiceDisci(repoDisci,valid_disci)
srv_note=ServiceNote(repoNote,repoStud,repoDisci,valid_nota)
ui=Console(srv_stud,srv_disci,srv_note)
ui.run()