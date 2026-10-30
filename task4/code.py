balance = float(input("Enter Initial Balance: Rs. "))
limit = float(input("Enter Withdrawal Limit: Rs. "))


deposits = 0
withdrawals = 0
rejected = 0

n = int(input("Enter Number of Transactions: "))

print("\n--- ATM TRANSACTION PROCESSING ---")

for i in range(n):

    print("\nTransaction", i + 1)

    choice = input("Enter D for Deposit or W for Withdrawal: ").upper()
    amount = float(input("Enter Amount: Rs. "))

    if amount <= 0:
        print("Transaction Rejected: Invalid Amount")
        rejected += 1

    elif choice == "D":
        balance = balance + amount
        deposits += amount
        print("Deposit Successful!")

    elif choice == "W":

        if amount > limit:
            print("Transaction Rejected: Limit Exceeded")
            rejected += 1

        elif amount > balance:
            print("Transaction Rejected: Insufficient Balance")
            rejected += 1

        else:
            balance = balance - amount
            withdrawals += amount
            print("Withdrawal Successful!")

    else:
        print("Invalid Transaction Type")
        rejected += 1

    print("Current Balance: Rs.", round(balance, 2))
print("\n====================================")
print("       ATM TRANSACTION SUMMARY")
print("====================================")
print("Total Deposits      : Rs.", round(deposits, 2))
print("Total Withdrawals   : Rs.", round(withdrawals, 2))
print("Rejected Transactions:", rejected)
print("Final Balance       : Rs.", round(balance, 2))
print("====================================")
print("      TRANSACTION COMPLETED")

