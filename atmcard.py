                         #  practic question
#Q. create account class with two attributes-balance and account numb. 
#   create methood for debit, creadit and printing the blance.
pin= int(input("please enter your pin: ",  )  ) 
if ( pin == 1196 ):
    print ( "thank you for using HBL atm" )
    
else:
    print(   "please correct your password " ,  )

class Account:
    
    def __init__(self, blance, acc):
        self.blance      = blance
        self.account_no  = acc
        print("total blance: ", self.get_blance() )
        print("..................................")
        # debit methood
    def debit( self, amount ):
        self.blance -= amount
        print("Rs:", amount, " was debit")
        print("total blance: ", self.get_blance() )
        print("..................................")

    def creadit( self, amount ):
        self.blance += amount
        print("Rs:", amount, " was creadit") 
        print("total blance: ", self.get_blance() ) 
        print("..................................")
        print("Thank you for using HBL atm ")

    def get_blance(self):
        return self.blance  

acc1 =  Account (35000, 1196)

acc1.debit (int (input( "Debit: ", )))
acc1.creadit (int(input("Creadit: ")))