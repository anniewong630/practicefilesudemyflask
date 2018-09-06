####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.




class Account:
    #attributes: owner, balance
    
    #constructor
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    #methods
    #As an added requirement, withdrawals may not exceed the available balance.
    def deposit(self, balance):
        self.balance += balance
        print('Depositing: $' + str(balance))


    def withdraw(self, balance):
        if balance > self.balance:
            print( 'Withdrawals may not exceed the available balance.')
        else:
            self.balance -= balance
            print('Withdrawing: $' + str(balance))

    def __repr__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}" 

    def printCurrentBalance(self):
        print('Current Balance: $' + str(self.balance))



# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)


# 3. Show the account owner attribute
print(acct1.owner)




# 4. Show the account balance attribute
print(acct1.balance)




# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.printCurrentBalance()




acct1.withdraw(75)
acct1.printCurrentBalance()



# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
acct1.printCurrentBalance()


# ## Good job!
