def deposit():
    while True:
        amount = input("what would youlike to deposit? $" )
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")   
        else:
            print("Try again.")
    return amount

deposit()