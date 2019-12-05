from exceptii.erori import RepoError
from domain.entitati import Student, Disciplina, Nota
class Repo:
    
    def __init__(self):
        self._entitati=[]
    def size(self):
        return len(self._entitati)
    def adauga(self,other):
        list = self.get_all()
        for x in list:
            if x.__eq__(other)==True:
                raise RepoError("Id existent!\n")
        self._entitati.append(other)
    def cauta(self,cheie):
        if cheie not in self._entitati:
            raise RepoError("Id inexistent!\n")
        for x in self._entitati:
            if x==cheie:
                return x 
    def modifica(self,other,new):
        other.change(new)
    def sterge(self,other):
        try:
            self._entitati.remove(other) 
        except:
            raise RepoError("Id inexistent!\n")
    def get_all(self):
        return self._entitati[:]
    
class FileRepo(Repo):
    def __init__(self, nume_fisier,read_line,write_line):
        self.__nume_fisier = nume_fisier
        self._read_line = read_line
        self._write_line = write_line
        Repo.__init__(self)
        self.__read_all_from_file()

    def __read_all_from_file(self):
        self._entitati=[]
        with open(self.__nume_fisier,'r') as f:
            continut=f.read()
        lines=continut.split('\n')
        for line in lines:
            if line.strip() == '':
                continue
            self._entitati.append(self._read_line(line)) 
    def __write_all_to_file(self):
        with open(self.__nume_fisier,'w') as f:
            for x in self._entitati:
                f.write(self._write_line(x))
                f.write('\n')
    def adauga(self, student):
        Repo.adauga(self, student)
        self.__write_all_to_file()
    def modifica(self, other, new):
        Repo.modifica(self, other, new)
        self.__write_all_to_file()
    def sterge(self, other):
        Repo.sterge(self, other)
        self.__write_all_to_file()

