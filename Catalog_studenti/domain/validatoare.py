from exceptii.erori import ValidError
class ValidatorStud:
    def __init__(self):
        pass
    def valideaza_student(self,stud):
        '''Functie care valideaza un student 
        input: un student 
        output: none
        raises: daca id<0 sau nume sir vid
        '''
        err=""
        if stud.get_id()<0:
            err+="Id invalid!\n"
        if stud.get_nume()=='':
            err+="Nume invalid!\n"
        if len(err)>0:
            raise ValidError(err)
    
    
class ValidatorDisci:
    
    
    def __init__(self):
        pass
    def valideaza_disciplina(self,disci):
        '''
        Functie care valideaza o disciplina 
        input: o disciplina
        output: none
        raises: daca id<0, nume/nume_prof sir vid
        '''
        err=""
        if disci.get_id()<0:
            err+="Id invalid!\n"
        if disci.get_nume()=="":
            err+="Nume invalid!\n"
        if disci.get_nume_prof()=="":
            err+="Nume de profesor invalid!\n"
        if len(err)>0:
            raise ValidError(err)
    



class ValidatorNota:
    
    
    def __init__(self):
        pass
    def valideaza_nota(self,nota):
        '''
        Functie care valideaza o nota
        input: o nota
        output: none
        raises: daca nota nu apartine [1,10]
        '''
        err=""
        if nota.get_nota()<1 or nota.get_nota()>10:
            err+="Nota invalida!\n"
        if len(err)>0:
            raise ValidError(err)
    



