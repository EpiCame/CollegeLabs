from domain.entitati import Student, Disciplina, Nota, StudGradesDTO, StudAvgDTO, DisciAvgDTO
from math import ceil
from random import randint, choice
import sys
import string
from exceptii.erori import RepoError

class ServiceStud:
    
    def __init__(self, repoStud, valid_stud):
        self.__repoStud = repoStud
        self.__valid_stud = valid_stud
    def adauga_student(self,s_id,nume):
        student = Student(s_id,nume)
        self.__valid_stud.valideaza_student(student)
        self.__repoStud.adauga(student)
    def cauta_student(self,s_id):
        stud_aux=Student(s_id,'search')
        self.__valid_stud.valideaza_student(stud_aux)
        return self.__repoStud.cauta(stud_aux)
    def modifica_student(self,s_id,newname):
        stud_to_modify = Student(s_id,"search")
        self.__valid_stud.valideaza_student(stud_to_modify)
        x=self.__repoStud.cauta(stud_to_modify)
        modified_stud=Student(x.get_id(),newname)
        self.__valid_stud.valideaza_student(modified_stud)
        self.__repoStud.modifica(x,modified_stud)
    def sterge_student(self,s_id):
        stud_to_delete = Student(s_id, 'delete')
        self.__valid_stud.valideaza_student(stud_to_delete)
        self.__repoStud.sterge(stud_to_delete)
    def afiseaza_studenti(self):
        return self.__repoStud.get_all()
    def calculeaza_id_maxim(self):
        list=self.__repoStud.get_all()
        maxi=0
        for x in list:
            if x.get_id()>maxi:
                maxi=x.get_id()
        return maxi
    def adauga_stud_random(self,nr,min_id):
        last_id=min_id
        while nr:
            id=last_id+1
            last_id=id
            letters = string.ascii_lowercase
            len_name=randint(5,16)
            nume=''
            while len_name>0:
                litera=choice(letters)
                nume+=litera
                len_name=len_name-1
            stud=Student(id,nume)
            self.__repoStud.adauga(stud)
            nr=nr-1
class ServiceDisci:
    
    
    def __init__(self, repoDisci, valid_disci):
        self.__repoDisci = repoDisci
        self.__valid_disci = valid_disci
    def adauga_disciplina(self,d_id, nume, nume_prof):
        disci_aux=Disciplina(d_id,nume,nume_prof)
        self.__valid_disci.valideaza_disciplina(disci_aux)
        self.__repoDisci.adauga(disci_aux)
    def cauta_disciplina(self,d_id):
        disci_aux=Disciplina(d_id,'search','search')
        self.__valid_disci.valideaza_disciplina(disci_aux)
        return self.__repoDisci.cauta(disci_aux)
    def modifica_nume_disciplina(self,d_id,newname):
        disci_to_modify = Disciplina(d_id,"search",'search')
        self.__valid_disci.valideaza_disciplina(disci_to_modify)
        x=self.__repoDisci.cauta(disci_to_modify)
        modified_disci=x 
        modified_disci.set_nume(newname)
        self.__valid_disci.valideaza_disciplina(modified_disci)
        self.__repoDisci.modifica(x,modified_disci)
    def modifica_nume_profesor(self,d_id,newname):
        disci_to_modify = Disciplina(d_id,"search",'search')
        self.__valid_disci.valideaza_disciplina(disci_to_modify)
        x=self.__repoDisci.cauta(disci_to_modify)
        modified_disci=x 
        modified_disci.set_nume_prof(newname)
        self.__valid_disci.valideaza_disciplina(modified_disci)
        self.__repoDisci.modifica(x,modified_disci)
    def sterge_disciplina(self,d_id):
        disci_to_delete = Disciplina(d_id, 'delete','delete')
        self.__valid_disci.valideaza_disciplina(disci_to_delete)
        self.__repoDisci.sterge(disci_to_delete)
    def afiseaza_discipline(self):
        return self.__repoDisci.get_all()
        
    



class ServiceNote(object):
    
    
    def __init__(self, repoNote, repoStud, repoDisci, valid_nota):
        self.__repoNote = repoNote
        self.__repoStud = repoStud
        self.__repoDisci = repoDisci
        self.__valid_nota = valid_nota
    def adauga_nota(self,s_id,d_id, nota):
        stud_aux=Student(s_id,'search')
        stud=self.__repoStud.cauta(stud_aux)
        disci_aux=Disciplina(d_id, 'search', 'search')
        disci=self.__repoDisci.cauta(disci_aux)
        nota=Nota(stud,disci,nota)
        self.__valid_nota.valideaza_nota(nota)
        self.__repoNote.adauga(nota)
    def completeaza_note(self):
        note=self.__repoNote.get_all()
        for nota in note:
            stud_aux=nota.get_stud()
            disci_aux=nota.get_disci()
            try:
                stud=self.__repoStud.cauta(stud_aux)
                try:    
                    disci=self.__repoDisci.cauta(disci_aux)
                    nota.set_nume_stud(stud.get_nume())
                    nota.set_nume_disci(disci.get_nume())
                    nota.set_nume_prof(disci.get_nume_prof())
                except RepoError:
                    self.__repoNote.sterge(nota)
            except RepoError:
                self.__repoNote.sterge(nota)
    def afiseaza_note(self):
        note=self.__repoNote.get_all()
        return note
    def sterge_note_student(self, s_id):
        note=self.__repoNote.get_all()
        for nota in note:
            if nota.get_stud().get_id()==s_id:
                self.__repoNote.sterge(nota)
    def sterge_note_disciplina(self,d_id):
        note=self.__repoNote.get_all()
        for nota in note:
            if nota.get_disci().get_id()==d_id:
                self.__repoNote.sterge(nota)
    def get_stud_ord(self,d_id):
        note=self.__repoNote.get_all()
        situatie={}
        for nota in note:
            if nota.get_disci().get_id()==d_id:
                if nota.get_stud().get_id() not in situatie:
                    situatie[nota.get_stud().get_id()]=[]
                situatie[nota.get_stud().get_id()].append(nota.get_nota())
        rez=[]
        for item in situatie.items():
            aux_stud=Student(item[0],'')
            x=self.__repoStud.cauta(aux_stud)
            item[1].sort()
            stud=StudGradesDTO(x.get_nume(),item[1])
            rez.append(stud)
        rez.sort(key=lambda x:x.get_nume(), reverse=False)
        return rez[:]
    def get_stud_medie(self):
        note=self.__repoNote.get_all()
        situatie={}
        for nota in note:
            if nota.get_stud().get_id() not in situatie:
                situatie[nota.get_stud().get_id()]=[]
            situatie[nota.get_stud().get_id()].append(nota.get_nota())
        rez=[]
        for item in situatie.items():
            aux_stud=Student(item[0],'')
            x=self.__repoStud.cauta(aux_stud)
            stud=StudAvgDTO(x.get_nume(),sum(item[1])/len(item[1]))
            rez.append(stud)
        rez.sort(key=lambda x:x.get_medie(), reverse=True)
        nr=len(rez)*20/100
        nr=ceil(nr)
        return rez[:nr]
    def get_disci_medie(self):
        note=self.__repoNote.get_all()
        situatie={}
        for nota in note:
            if nota.get_disci().get_id() not in situatie:
                situatie[nota.get_disci().get_id()]=[]
            situatie[nota.get_disci().get_id()].append(nota.get_nota())
        discipline=self.__repoDisci.get_all()
        for disci in discipline:
            if disci.get_id() not in situatie:
                situatie[disci.get_id()]=[0]
        rez=[]
        for item in situatie.items():
            aux_disci=Disciplina(item[0],'','')
            x=self.__repoDisci.cauta(aux_disci)
            disci=DisciAvgDTO(x.get_nume(),sum(item[1])/len(item[1]))
            rez.append(disci)
        rez.sort(key=lambda x:x.get_medie(), reverse=True)
        i=0
        j=0
        for i in range(0,len(rez)-1):
            for j in range(i+1,len(rez)):
                if rez[i].get_medie()==rez[j].get_medie() and rez[i].get_nume()>rez[j].get_nume():
                    aux=rez[i]
                    rez[i]=rez[j]
                    rez[j]=aux 
        return rez[:]
        
        
            
                
    



