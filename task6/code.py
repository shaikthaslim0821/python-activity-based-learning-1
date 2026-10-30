n = int(input("Enter Number of Transactions: "))

transactions = []

for i in range(n):
    print("\nTransaction", i + 1)

    tid = input("Enter Transaction ID: ")
    amount = float(input("Enter Transaction Amount: Rs. "))

    transactions.append({
        "id": tid,
        "amount": amount
    })

threshold = float(input("\nEnter Transaction Threshold: Rs. "))

transaction_ids = [t["id"] for t in transactions]

duplicates = []

for tid in transaction_ids:
    if transaction_ids.count(tid) > 1 and tid not in duplicates:
        duplicates.append(tid)

suspicious = []
high_value = []

for t in transactions:

    reasons = []

    if t["id"] in duplicates:
        reasons.append("Duplicate Transaction ID")

    if t["amount"] > threshold:
        reasons.append("Amount Exceeds Threshold")
        high_value.append(t)

    if reasons:
        suspicious.append({
            "id": t["id"],
            "amount": t["amount"],
            "reason": reasons
        })

print("\n======================================")
print("       TRANSACTION ANALYSIS REPORT")
print("======================================")

print("\nAll Transactions:")

for t in transactions:
    print("ID:", t["id"], "| Amount: Rs.", t["amount"])

print("\nDuplicate Transaction IDs:")

if duplicates:
    for tid in duplicates:
        print(tid)
else:
    print("No Duplicate Transactions")

print("\nHigh Value Transactions:")

if high_value:
    for t in high_value:
        print(t["id"], "- Rs.", t["amount"])
else:
    print("No Threshold Violations")

print("\nSuspicious Transactions:")

if suspicious:
    for t in suspicious:
        print("ID:", t["id"])
        print("Amount: Rs.", t["amount"])
        print("Reason:", ", ".join(t["reason"]))
        print("----------------------------------")
else:
    print("No Suspicious Transactions")

print("======================================")
print("       ANALYSIS COMPLETED")

