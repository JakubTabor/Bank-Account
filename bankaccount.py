class Results:

    def __init__(self, isSucces, message, value=None):
        self.isSucces = None
        self.message = "Welcome to Your bank"
        self.value = value

    def is_ok(self):
        return self.isSucces


class Good(Results):
    def __init__(self, isSucces, message, value=None):
        super().__init__(message, value)
        self.isSucces = True


class Error(Results):
    def __init__(self, isSucces, message, value=None):
        super().__init__(message, value)
        self.isSucces = False


class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        """Here it check if money is real"""
        self.balance += amount

    def try_withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            return Good("You can take the casch",  amount)

        return Error("not enough casch", amount)

    def __str__(self):
        return str(self.balance)


class minimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimumBalance=1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance

    def try_withdraw(self, amount):
        if (self.balance - amount > self.minimumBalance):
            return super().try_withdraw(amount)

        else:
            return Error("not enough casch, You take too much ", amount)


"""My_script"""
accountMin = minimumBalanceAccount(150, 100)

result = accountMin.try_withdraw(10)

if (result.is_ok()):
    print(result.message, " You can take your casch")

else:
    print(result.message, "Ups something goes wrong")
