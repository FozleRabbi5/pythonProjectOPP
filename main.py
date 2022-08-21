class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details")
        print("")
        print("name", self.name)
        print("age", self.age)
        print("gender", self.gender)


class Bank(User):
    def __init__(self, name, age, gender):
        super(Bank, self).__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        # self.amount = amount
        self.balance = self.balance + amount
        return f"{self.name} has {self.balance} tk"

    def withdraw(self, withdrawamount):
        self.withdrawamount = withdrawamount

        if self.balance < withdrawamount:
            print(f"amount insufficiant and your amount {self.balance} ")
        else:
            self.balance = self.balance - withdrawamount
            return f"your remainig balance is {self.balance}"


    def view_balance(self):
        self.show_details()
        self.withdraw(self.withdrawamount)



johan = Bank("johan", 24, "male")
deposit_money = johan.deposit(200)
withdraw_money = johan.withdraw(100)
# print(deposit_money)
# print(withdraw_money)
# print(johan.balance)
details = johan.show_details()
print(details)


mithun = Bank("mithun", 24, "half-ladies")
deposite_of_mithun = mithun.deposit(500)
withdraw_money_mithun = mithun.withdraw(300)
# print(deposite_of_mithun)
# print(withdraw_money_mithun)
# print(mithun.balance)
