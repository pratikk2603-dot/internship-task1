print("welcome to kiran bank")
balance=10000
while True:
    print("\n1.check balance")
    print("2.deposit money")
    print("3.withdraw money")
    print("4.exit")
    choice=int(input("enter choice:"))
    if choice==1:
        print("current balance:",balance)
    elif choice==2:
        amount=int(input("enter deposit amount:"))
        if amount>0:
            balance=balance+amount
            print("deposit successful")
            print("updated balance:",balance)
        else:
            print("transaction failed:amount must be greater than zero")
    elif choice == 3:
        amount = int(input("enter withdrawal amount:"))
        if amount<= 0:
            print("transaction failed: amount must be greater than zero")
        elif amount > balance:
            print("transaction failed: insufficient balance")
            print("current balance:",balance)
        else:
            balance=balance-amount
            print("withdrawal successful")
            print("updated balance:",balance)
    elif choice == 4:
        print("thank you for banking with us. goodbye!")
        break
    else:
        print("invalid choice.please select 1 to 4")
        