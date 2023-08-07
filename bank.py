class bank:
    def __init__(self,accnumb,balance):
        self._accnumb=accnumb
        self._balance=balance

    def withdraw(self,x):
        if x <= self._balance:
            self._balance = self._balance - x
            print(f'The current balance is {self._balance}')
        else:
            print('There isnt enough money')

obj=bank(76767,15000)
obj.withdraw(1000)