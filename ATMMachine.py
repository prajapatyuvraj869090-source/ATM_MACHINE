 # ATM Machine

# class Bank_Account :
#     def __init__(self, Name, Account_Number, Pin, Balance):
#         self.Name = Name
#         self.Account_Number = Account_Number
#         self.Pin = Pin 
#         self.Balance = Balance
#         self.Transition = []

#     def display_Detail(self):
#         print("Name : ", self.Name)
#         print("Account_Number : ", self.Account_Number)
#         print("Pin : ", self.Pin)
#         print("Balance : ", self.Balance)


#     def add_Bank_Account():
#         print("add New Account")

#         Name = input("Enter Your Name : ", )
#         Account_Number = input("Enter Your Account Number : ", )
#         Pin = input("Enter Your Pin : ", )
#         Balance = input("Enter Your Bank Balance : ", )

#     BankAcc = BankAcc(Name, Account_Number, Pin, Balance)
#     list.appent(BankAcc)        

#     print("Account Added Successfully")



# ==============================
# ATM MACHINE
# ==============================

class BankAccount:

    def __init__(self, name, account_number, pin, balance):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transactions = []

    # Check Balance
    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance}")

    # Deposit Money
    def deposit(self):

        try:
            amount = float(input("Enter amount to deposit: "))

            if amount <= 0:
                print("Please enter a positive amount.")
                return

            self.balance += amount

            self.transactions.append(f"Deposited ₹{amount}")

            print(f"₹{amount} deposited successfully!")

        except ValueError:
            print("Please enter a valid amount.")

    # Withdraw Money
    def withdraw(self):

        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Please enter a positive amount.")

            elif amount > self.balance:
                print("Insufficient Balance!")

            else:
                self.balance -= amount

                self.transactions.append(f"Withdrawn ₹{amount}")

                print(f"₹{amount} withdrawn successfully!")

        except ValueError:
            print("Please enter a valid amount.")

    # Transaction History
    def show_transactions(self):

        if len(self.transactions) == 0:
            print("\nNo transactions yet.")

        else:
            print("\n===== Transaction History =====")

            for transaction in self.transactions:
                print(transaction)


# ==============================
# Creating Account
# ==============================

account = BankAccount(
    "Yuvraj",
    "123456789",
    "1234",
    5000
)


# ==============================
# PIN LOGIN
# ==============================

attempts = 3

while attempts > 0:

    entered_pin = input("Enter your PIN: ")

    if entered_pin == account.pin:
        print(f"\nWelcome, {account.name}!")
        break

    else:
        attempts -= 1
        print(f"Wrong PIN! Attempts left: {attempts}")

else:
    print("Too many wrong attempts. Account blocked.")
    exit()


# ==============================
# ATM MENU
# ==============================

while True:

    print("\n========== ATM ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")
    print("==========================")

    choice = input("Enter your choice: ")

    if choice == "1":

        account.check_balance()

    elif choice == "2":

        account.deposit()

    elif choice == "3":

        account.withdraw()

    elif choice == "4":

        account.show_transactions()

    elif choice == "5":

        print("\nThank you for using the ATM!")
        break

    else:

        print("Invalid choice! Please try again.")

    