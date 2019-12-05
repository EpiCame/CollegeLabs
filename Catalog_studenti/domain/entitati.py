class Student():
    def __init__(self,s_id,nume):
        self.__s_id=s_id 
        self.__nume=nume 
        
    def get_id(self):
        '''
        retureaza id_ul unui student
        '''
        return int(self.__s_id)
    
    def get_nume(self):
        '''
        returneaza numele unui student
        '''
        return self.__nume
    
    def set_nume(self,newname):
        '''
        seteaza numele unui student la newname
        input:newname- string 
        output:none
        '''
        self.__nume=newname 
    def change(self,other):
        '''
        modifica studentul cu other
        '''
        self.set_nume(other.get_nume())
    def __eq__(self,other):
        '''
        verifica daca doi studenti sunt identici
        input: other- un student 
        output: True, daca sunt identici, respectiv False daca nu 
        '''
        return int(self.__s_id)==int(other.__s_id) 
    
    def __str__(self):
        '''
        retureaza un student in formatul "id: nume"
        '''
        return str(self.__s_id)+": "+self.__nume
    def read_line(linie):
        '''
        preia o linie din fisier si o transforma in student
        input: string
        output: student
        '''
        stud_camp= linie.split()
        stud= Student(stud_camp[0],stud_camp[1])
        return stud
    def write_line(stud):
        '''
        preia un student si il transforma intr-o linie de fisier
        input: un student
        output: un string 
        '''
        return str(stud.get_id())+' '+stud.get_nume()
class Disciplina():
    def __init__(self,d_id,nume,nume_prof):
        self.__d_id = d_id
        self.__nume = nume
        self.__nume_prof = nume_prof
    def get_id(self):
        '''
        returneaza id-ul unei discipline'''
        return int(self.__d_id)
    def get_nume(self):
        '''
        returneaza numele unei discipline 
        '''
        return self.__nume
    def get_nume_prof(self):
        '''
        returneaza numele profesorului
        '''
        return self.__nume_prof
    def set_nume(self,newname):
        '''
        seteaza numele unei discipline la newname
        input:newname- string 
        output:none
        '''
        self.__nume=newname 
    def set_nume_prof(self,newname):
        '''
        seteaza numele unui profesor la newname
        input:newname- string 
        output:none
        '''
        self.__nume_prof=newname 
    def __str__(self):
        '''
        returneaza o disciplina in formatul "id: nume, nume_prof"
        '''
        return str(self.get_id())+": "+str(self.get_nume())+', '+str(self.get_nume_prof())
    def __eq__(self,other):
        '''
        verifica daca 2 discipline sunt identice 
        input: other- o disciplina
        output: True- daca sunt identice, respectiv False daca nu
        '''
        return int(self.get_id())==int(other.get_id())
    def change(self,other):
        '''
        modifica disciplina cu other
        '''
        self.__nume=other.get_nume()
        self.__nume_prof=other.get_nume_prof()
    def read_line(linie):
        '''
        preia o linie din fisier si o transforma in sdisciplina
        input: string
        output: disciplina
        '''
        disci_camp= linie.split()
        disci= Disciplina(disci_camp[0],disci_camp[1],disci_camp[2])
        return disci
    def write_line(disci):
        '''
        preia o disciplina si o transforma intr-o linie de fisier
        input: o disciplina
        output: un string 
        '''
        return str(disci.get_id())+' '+disci.get_nume()+' '+disci.get_nume_prof()
class Nota():
    def __init__(self,stud,disci,nota):
        self.__stud = stud
        self.__disci = disci
        self.__nota = nota
        
    def get_stud(self):
        '''
        returneaza studentul care a primit nota 
        output: un student
        '''
        return self.__stud
    def get_disci(self):
        '''
        returneaza disciplina la care s a dat nota
        output: o disciplina
        '''
        return self.__disci
    def get_nota(self):
        '''
        returneaza nota
        output: int
        '''
        return int(self.__nota)
    def set_nota(self,nota):
        '''
        seteaza valoarea notei la o noua valoare
        input: nota int
        output: none
        '''
        self.__nota=nota 
    def change(self,other):
        '''
        modifica nota cu other
        '''
        self.__nota=other.get_nota()
    def set_nume_stud(self,nume):
        self.__stud.set_nume(nume)
    def set_nume_disci(self,nume):
        self.__disci.set_nume(nume)
    def set_nume_prof(self,nume):
        self.__disci.set_nume_prof(nume)
    def __eq__(self,other):
        '''
        verifica daca 2 note sunt indentice 
        output:True daca sunt identice, False- daca nu sunt identice 
        '''
        return (self.__stud.__eq__(other.__stud) and
                self.__disci.__eq__(other.__disci) and 
                self.get_nota()==other.get_nota())
    def __str__(self):
        '''
        returneaza o nota in format: "nume_stud, nume_disci, nota
        output: string
        '''
        return self.__stud.get_nume()+' are nota '+str(self.get_nota())+' la disciplina '+self.__disci.get_nume()
    def read_line(linie):
        '''
        preia o linie din fisier si o transforma in nota
        input: string
        output: nota
        '''
        nota_camp= linie.split()
        id_s = nota_camp[0]
        id_d = nota_camp[1]
        val = nota_camp[2]
        stud=Student(id_s,'')
        disci=Disciplina(id_d,'','')
        nota=Nota(stud,disci,val)
        return nota
    def write_line(nota):
        '''
        preia o nota si o transforma intr-o linie de fisier
        input: o nota
        output: un string 
        '''
        return str(nota.get_stud().get_id())+' '+str(nota.get_disci().get_id())+' '+str(nota.get_nota())
class StudGradesDTO:
    def __init__(self,nume, note):
        self.__nume = nume
        self.__note = note
    def get_nume(self):
        
        return self.__nume 
    def get_note(self):
        
        return self.__note 
    def __str__(self):
        st=''
        st+=self.__nume+' are notele: '
        for x in self.__note:
            st+=str(x)+' '
        return st 
class StudAvgDTO:
    
    def __init__(self,nume,medie):
        self.__nume = nume
        self.__medie = medie
    def get_nume(self):
        
        return self.__nume 
    def get_medie(self):
        
        return int(self.__medie)
    def __str__(self):
        return self.__nume+' '+str(self.__medie)
class DisciAvgDTO: 
    def __init__(self,nume, medie ):
        self.__nume = nume
        self.__medie = medie
    def get_nume(self):
        return self.__nume 
    def get_medie(self):
        return int(self.__medie)
    def __str__(self):
        return self.__nume+' '+str(self.__medie)
    
    
        
    

