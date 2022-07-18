class Account:
    def __init__(self):

        # starting, declaring and setting vars of this class to private
        self.__balance = None
        self.__num_account = None
        self.__owner = None

    # define the getter and setter methods
    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner = owner

    def get_num_account(self):
        return self.__num_account

    def set_num_account(self, num_account):
        self.__num_account = num_account

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            print("The negative values it not accept")
            exit()
        else:
            self.__balance = balance

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            print("Withdraw money successful")
        else:
            print("No balance")

    def deposit(self, value):
        self.balance += value

    def extract(self):
        print("Customer: ", self.get_owner(), " | Your current balance: ", self.balance)
