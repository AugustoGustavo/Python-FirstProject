class Main:
    pass

    print("testando o projeto")

    # class imports
    from Customer import Customer
    from Account import Account

    # insert data about the customer and your account bank
    customer1 = Customer("Gustavo", "(13)98156-2780")
    Customer1Account = Account(customer1.name, "46700-2", 0)


    # show data of the customers and your account balance
    print(Customer1Account.owner, "| Ac. Number: ", Customer1Account.num_account, "| Your Balance: ",
          Customer1Account.balance)