
def bankFlow(fnc):

    def helper(amt):
        print("Logging into the server.....")
        fnc(amt)
        print("logging out of the server.....")
        print("-" * 60)

    return helper




@bankFlow
def deposit(amt):
    print(f"Amount {amt} credited into the accout ending ####")

@bankFlow
def withdraw(amt):
    print(f"Amount {amt} debited from the account ending ####")


deposit(50000)
withdraw(15000)



"""

@bankFlow               # deposit = bankFlow(deposit)
def deposit(amt):
    print(f"Amount {amt} credited into the accout ending ####")

@bankFlow
def withdraw(amt):
    print(f"Amount {amt} debited from the account ending ####")

withdraw(15000)
deposit(50000)

"""