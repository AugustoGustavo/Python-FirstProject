class Main:
    pass

    print("testing the project")

    # class imports
    from Customer import Customer
    from Account import Account

    # insert data about the customer and your account bank
    customer1 = Customer()
    customer1.set_name("Gustavo")
    customer1.set_telephone("(13)98156-XXXX")

    customer1_account = Account()
    customer1_account.set_owner(customer1.get_name())
    customer1_account.set_num_account("46700-2")
    customer1_account.balance = 0

    # show data of the customers and your account balance
    print(customer1_account.get_owner(), "| Ac. Number: ", customer1_account.get_num_account(), "| Your Balance: ",
          customer1_account.balance)
