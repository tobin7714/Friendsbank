# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
accounts = ["joey", "chandler", "ross", "monica", "rachel", "phoebe"]
pin = ["1089", "3374", "1477", "5678", "4534", "9030"]
balance = [34500, 88000, 4000, 14000, 200000, 76000]

print("WELCOME TO F.R.I.E.N.D.S ATM")
name = input("Enter your name: ")
name = name.lower()
pinI = input("Enter your pin: ")
if name in accounts and pinI in pin:
    s = accounts.index(name)
    if s == pin.index(pinI):
        print("How may i help you?")
        print("1) Cash Deposit\n2) Cash Withdrawal\n3) Check balance")
        help = int(input("Enter the digit of your option: "))
        b = balance[s]
        if help == 1:
            deposit = int(input("Enter the amount of deposit: "))
            b = b + deposit
            print("Your money has been successfully deposited", name)
            print("your account balance is", b)
        elif help == 2:
            amount = int(input("Enter the amount of withdrawal: "))
            if amount > b:
                print("SORRY! INSUFFICIENT BALANCE")
                print("Your account balance is", b)
            else:
                b = b - amount
                print("Please collect the amount", name)
                print("Your account balance is", b)
        elif help == 3:
            print("Your account balance is", b)
        else:
            print("invalid option !")
    else:
        print("Invalid pin! Enter the right one!")

else:
    print("SORRY ! INVALID INFORMATION ")
    print("You do not have an account in the F.R.I.E.N.D.S bank")

