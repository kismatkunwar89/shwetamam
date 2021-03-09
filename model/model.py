class User:
    def __init__(self,uname,address,email,gender,phoneno,roomno,date):
        self.__username=uname
        self.__address = address
        self.__email = email
        self.__gen = gender
        self.__pno = phoneno
        self.__rno=roomno
        self.__date=date

    def set_username(self,uname):
        self.__username=uname

    def get_username(self):
        return self.__username

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_gender(self,gender):
        self.__gen = gender

    def get_gender(self):
        return self.__gen

    def set_pno(self,phoneno):
        self.__pno = phoneno

    def get_pno(self):
        return self.__pno


    def set_rno(self, roomno):
        self.__rno = roomno

    def get_rno(self):
        return self.__rno

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date