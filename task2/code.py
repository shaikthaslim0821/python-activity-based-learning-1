def calculate_bill(units, fixed_charge, surcharge_rate, rebate):
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    elif units <= 300:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5
    else:
        energy = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300) * 7

    subtotal = energy + fixed_charge
    surcharge = subtotal * surcharge_rate / 100
    total = max(0, subtotal + surcharge - rebate)

    return energy, surcharge, total


months = int(input("Enter number of months: "))
fixed = float(input("Enter fixed charge: "))
rate = float(input("Enter surcharge rate (%): "))
rebate = float(input("Enter rebate: "))

previous_bill = None

for i in range(months):
    month = input("\nEnter month name: ")
    units = float(input("Enter units consumed: "))

    if units < 0:
        print("Invalid units!")
        continue

    energy, surcharge, bill = calculate_bill(
        units, fixed, rate, rebate
    )

    print("\nMonth:", month)
    print("Energy charges: Rs.", round(energy, 2))
    print("Fixed charges: Rs.", round(fixed, 2))
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total bill: Rs.", round(bill, 2))

    if previous_bill is not None:
        if previous_bill > 0:
            increase = (bill - previous_bill) / previous_bill * 100
            print("Bill change:", round(increase, 2), "%")

            if increase > 15:
                print("ALERT: Unusual bill increase!")
            else:
                print("No unusual increase detected.")
        elif bill > 0:
            print("ALERT: Bill increased from zero.")

    previous_bill = bill

print("\nBilling analysis completed.")

