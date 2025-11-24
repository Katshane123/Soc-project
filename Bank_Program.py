# Python banking Program 
# Author : cyberKAT123

def show_balance(balance):
    print("------------------")
    print(f"Balance is: R{balance:.2f}")


def deposit():
    print("------------------")
    amount = float(input('Enter the amount you want to deposit: '))

    if amount < 0:
        print("Please enter a valid amount")
        return 0
    else:
        return amount


def withdraw(balance):
    print("------------------")
    amount = float(input('Enter the amount you want to withdraw: '))
    if amount > balance:
        print("------------------")
        print("Insufficent funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("------------------")
        print('Banking program')
        print("------------------")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("------------------")
        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Not valid, Enter your choice(1-4): ")

    print("Have a nice day!!!")

if __name__ == "__main__":
    main()
    
