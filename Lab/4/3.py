#Write a program in which a class named Account has private member variables named
#$account_no ,account_bal ,security_code. Use a public function to initialize the variables and print
#all data.

class Account():
    __accountNo = "000"
    __accountBal = 0.0
    __securityCode = 1234
    def setAccNo(self, accNo):
        self.__accountNo = accNo
    
    def setAccBal(self,accBal):
        self.__accountBal = accBal

    def setSecurityCode(self,securityCode):
        self.__securityCode = securityCode

    def setAll(self,aNo,aBal,secCode):
        self.__accountBal = aBal
        self.__accountNo = aNo
        self.__securityCode = secCode
        #An explicitly public function; req of Q
    def display(self):
        print(f"The account number of the account: {self.__accountNo}")
        print(f"The account total balance is: ",self.__accountBal)
        print(f"The security code for the account is: {self.__securityCode}\n")    

accDefault = Account()
accDefault.display()
acc = Account()
acc.setAccBal(12505.6)
acc.setAccNo("FUE08273")
acc.setSecurityCode(2546)
acc.display()

accSetAll = Account()
accSetAll.setAll("PFIU2913",5368.56,8584)
accSetAll.display()