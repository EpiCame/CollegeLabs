class RepoError(Exception):
    def __init__(self,err):
        self.__err=err 
    def get_err(self):
        return self.__err
    def __str__(self):
        return self.__err
        


class ValidError(Exception):
    def __init__(self,err):
        self.__err=err 
    def get_err(self):
        return self.__err
    def __str__(self):
        return self.__err
        

