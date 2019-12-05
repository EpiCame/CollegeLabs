from exceptii.erori import RepoError, ValidError
class Console(object):
    
    
    def __init__(self, srv_stud, srv_disci, srv_note):
        self.__srv_stud = srv_stud
        self.__srv_disci = srv_disci
        self.__srv_note = srv_note
        self.__commands={'adauga_stud':self.__ui_add_stud,
                         'adauga_stud_random':self.__ui_add_random_studs,
                        'cauta_stud':self.__ui_cauta_stud,
                        'modifica_nume_stud':self.__ui_modif_stud,
                        'sterge_stud':self.__ui_sterge_stud,
                        'afiseaza_studenti':self.__ui_print_stud,
                        'adauga_disci':self.__ui_add_disci,
                        'cauta_disci':self.__ui_cauta_disci,
                        'modifica_nume_disci':self.__ui_modif_nume_disci,
                        'modifica_nume_prof':self.__ui_modif_nume_prof,
                        'sterge_disci':self.__ui_sterge_disci,
                        'adauga_nota':self.__ui_add_note,
                        'afiseaza_discipline':self.__ui_print_disci,
                        'afiseaza_note': self.__ui_print_note,
                        'statistica_disciplina':self.__ui_stat_disci,
                        'statistica_medie_stud':self.__ui_stat_medie,
                        'statistica_medie_disci':self.__ui_stat_medie_disci
                        }
        
    def __ui_stat_medie_disci(self,parametrii):
        if len(parametrii)!=0:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            self.__srv_note.completeaza_note()
            disci_ord=self.__srv_note.get_disci_medie()
            if len(disci_ord)>0:
                for disci in disci_ord:
                    print(str(disci))
            else:
                print(f'Nu exista studenti adaugati.')
        except ValueError as ve:
            print("Id-ul disciplinei trebuie sa fie un numar intreg!")
    def __ui_add_random_studs(self,parametrii):
        if len(parametrii)!=1:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            nr_stud=int(parametrii[0])
            min_id=self.__srv_stud.calculeaza_id_maxim()
            self.__srv_stud.adauga_stud_random(nr_stud,min_id)
        except ValueError as ve:
            print("Numarul de studenti trebuie sa fie intreg!\n")
    def __ui_stat_medie(self,parametrii):
        if len(parametrii)!=0:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            self.__srv_note.completeaza_note()
            stud_ord=self.__srv_note.get_stud_medie()
            if len(stud_ord)>0:
                for stud in stud_ord:
                    print(str(stud))
            else:
                print(f'Nu exista studenti adaugati.')
        except ValueError as ve:
            print("Id-ul disciplinei trebuie sa fie un numar intreg!")
    def __ui_stat_disci(self,parametrii):
        if len(parametrii)!=1:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            d_id=int(parametrii[0])
            self.__srv_note.completeaza_note()
            stud_ord=self.__srv_note.get_stud_ord(d_id)
            if len(stud_ord)>0:
                for stud in stud_ord:
                    print(str(stud))
            else:
                print(f'Nu exista note la disciplina cu id: {d_id}.')
        except ValueError as ve:
            print("Id-ul disciplinei trebuie sa fie un numar intreg!")
            
    def __ui_print_note(self, parametrii):
        '''
        functie care afiseaza toate notele din repository
        input: parametrii-lista vida 
        ouput: lista cu note in format str
        '''
        if len(parametrii)>0:
            raise ValueError("Numar de parametrii invalid!\n")
        self.__srv_note.completeaza_note()
        list=self.__srv_note.afiseaza_note()
        if len(list)==0:
            print("Nu exista discipline adaugate!\n")
        else:
            for x in list:
                print(str(x))
    def __ui_add_note(self,parametrii):
        '''
        functie care adauga un student in repository 
        input: parametrii- o lista cu 3 int 
        output: none
        '''
        if len(parametrii)!=3:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            s_id=int(parametrii[0])
        except ValueError as ve:
            print("Id-ul studentului trebuie sa fie un numar intreg!")
        try:
            d_id=int(parametrii[1])
        except ValueError as ve:
            print("Id-ul disciplinei trebuie sa fie un numar intreg!")
        try:
            nota=int(parametrii[2])
        except ValueError as ve:
            print("Nota trebuie sa fie un numar intreg!")
        self.__srv_note.adauga_nota(s_id,d_id,nota)
    def __ui_print_disci(self,parametrii):
        '''
        functie care afiseaza toate disciplinele din repository
        input: parametrii-lista vida 
        ouput: lista cu discipline in format str
        '''
        if len(parametrii)>0:
            raise ValueError("Numar de parametrii invalid!\n")
        list=self.__srv_disci.afiseaza_discipline()
        if len(list)==0:
            print("Nu exista discipline adaugate!\n")
        else:
            for x in list:
                print(str(x))
    def __ui_print_stud(self,parametrii):
        '''
        functie care afiseaza toti studentii din repository
        input: parametrii-lista vida 
        ouput: lista cu studenti in format str
        '''
        if len(parametrii)>0:
            raise ValueError("Numar de parametrii invalid!\n")
        list=self.__srv_stud.afiseaza_studenti()
        if len(list)==0:
            print("Nu exista studenti adaugati!\n")
        else:
            for x in list:
                print(str(x))
    def __ui_add_stud(self,parametrii):
        '''
        functie care adauga un student in repository 
        input: parametrii- o lista cu un int si un string
        output: none
        '''
        if len(parametrii)!=2:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            s_id=int(parametrii[0])
        except ValueError as ve:
            print("Id-ul trebuie sa fie un numar intreg!")
        nume=parametrii[1]
        self.__srv_stud.adauga_student(s_id,nume)
    def __ui_cauta_stud(self,parametrii):
        '''
        functie care cauta un student
        input: parametrii- o lista cu un int 
        output: un student in cazul in care a fost gasit 
        '''
        if len(parametrii)!=1:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            id=int(parametrii[0])
            x=self.__srv_stud.cauta_student(id)
            print(str(x))
        except ValueError as ve:
            print("Id-ul trebuie sa fie un numar intreg!")
        
    def __ui_modif_stud(self,parametrii):
        '''
        functie care modifica un numele unui student
        input: parametrii- o lista cu un int si un string 
        output:none 
        '''
        if len(parametrii)!=2:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            id=int(parametrii[0])
            newname=parametrii[1]
            self.__srv_stud.modifica_student(id, newname)
        except ValueError as ve:
            print("Id-un trebuie sa fie un numar intreg!\n")
    def __ui_sterge_stud(self,parametrii):
        '''
        functie care sterge un student 
        input:parametrii- o lista cu un int
        output: none'''
        if len(parametrii)!=1:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            id=int(parametrii[0])
            self.__srv_stud.sterge_student(id)
            self.__srv_note.sterge_note_student(id)
        except ValueError as ve:
            print("Id-ul trebuie sa fie un numar intreg!\n")
    def __ui_add_disci(self,parametrii):
        '''
        functie care adauga o disciplina in repository
        input: parametrii- o lista cu un int, si doua stringuri 
        output:none
        '''
        if len(parametrii)!=3:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            id=int(parametrii[0])
            nume=parametrii[1]
            nume_prof=parametrii[2]
            self.__srv_disci.adauga_disciplina(id,nume,nume_prof)
        except ValueError as ve:
            print("Id-ul trebuie sa fie un numar intreg!\n")
    def __ui_cauta_disci(self,parametrii):
        '''
        functie care cauta o disciplina
        input: parametrii- o lista cu un int 
        output: o disciplina in cazul in care a fost gasita 
        '''
        if len(parametrii)!=1:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            id=int(parametrii[0])
            x=self.__srv_disci.cauta_disciplina(id)
            print(str(x))
        except ValueError as ve:
            print("Id-ul trebuie sa fie un numar intreg!")
    def __ui_modif_nume_disci(self,parametrii):
        '''
        functie care modifica numele unei discipline
        input: parametrii- o lista cu un int si un string 
        output:none 
        '''
        if len(parametrii)!=2:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            id=int(parametrii[0])
            newname=parametrii[1]
            self.__srv_disci.modifica_nume_disciplina(id, newname)
        except ValueError as ve:
            print("Id-un trebuie sa fie un numar intreg!\n")
    def __ui_modif_nume_prof(self,parametrii):
        '''
        functie care modifica numele unui profesor asociat unei discipline
        input: parametrii- o lista cu un int si un string 
        output:none 
        '''
        if len(parametrii)!=2:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            id=int(parametrii[0])
            newname=parametrii[1]
            self.__srv_disci.modifica_nume_profesor(id, newname)
        except ValueError as ve:
            print("Id-un trebuie sa fie un numar intreg!\n")
    def __ui_sterge_disci(self,parametrii):
        '''
        functie care sterge o disciplina
        input:parametrii- o lista cu un int
        output: none'''
        if len(parametrii)!=1:
            raise ValueError("Numar de parametrii invalid!\n")
        try:
            id=int(parametrii[0])
            self.__srv_disci.sterge_disciplina(id)
            self.__srv_note.sterge_note_disciplina(id)
        except ValueError as ve:
            print("Id-ul trebuie sa fie un numar intreg!\n")
    def run(self):
        while True:
            cmd=input(">>>")
            if cmd=='exit':
                return
            cmd.strip()
            comanda=cmd.split()
            nume_comanda=comanda[0]
            parametrii=comanda[1:]
            if nume_comanda in self.__commands:
                try:
                    self.__commands[nume_comanda](parametrii)
                except ValueError as ve:
                    print("Valoare numarică invalidă!\n")
                except ValidError as vale:
                    print(str(vale))
                except RepoError as repe:
                    print(str(repe))
            else:
                print("Comanda Invalida!!!")
    
    



