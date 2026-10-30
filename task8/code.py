

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]


n = int(input("Enter Number of Appliances: "))

if n <= 0:
    print("Invalid Number of Appliances")

else:
    appliances = []
    consumption = []


    for i in range(n):
        name = input("Enter Appliance Name: ")
        appliances.append(name)


    for i in range(n):
        row = []
        print("\nAppliance:", appliances[i])

        for day in days:
            value = float(input(day + ": "))

            if value < 0:
                print("Invalid Electricity Reading")
                row = []
                break

            row.append(value)

        if len(row) != 7:
            break

        consumption.append(row)

    if len(consumption) == n:

      
        appliance_totals = []

        for i in range(n):
            appliance_totals.append(sum(consumption[i]))

      
        daily_totals = []

        for j in range(7):
            total = 0

            for i in range(n):
                total += consumption[i][j]

            daily_totals.append(total)

      
        weekly_total = sum(daily_totals)

       
        daily_limit = float(
            input("\nEnter Daily Consumption Limit (kWh): ")
        )

        appliance_limit = float(
            input("Enter Weekly Appliance Limit (kWh): ")
        )

        if daily_limit < 0 or appliance_limit < 0:
            print("Invalid Consumption Limit")

        else:
            print("\n======================================")
            print(" WEEKLY ELECTRICITY REPORT")
            print("======================================")

          
            print("\nAPPLIANCE-WISE CONSUMPTION")

            for i in range(n):
                print(appliances[i], ":",
                      round(appliance_totals[i], 2), "kWh")

          
            print("\nDAILY CONSUMPTION")

            for j in range(7):
                print(days[j], ":",
                      round(daily_totals[j], 2), "kWh")

            print("\nTOTAL WEEKLY CONSUMPTION:",
                  round(weekly_total, 2), "kWh")

          
            print("\nDAYS EXCEEDING DAILY LIMIT")

            found = False

            for j in range(7):
                if daily_totals[j] > daily_limit:
                    print(days[j], ":", daily_totals[j], "kWh")
                    found = True

            if not found:
                print("No Daily Limit Violations")

           
            print("\nAPPLIANCES EXCEEDING WEEKLY LIMIT")

            found = False

            for i in range(n):
                if appliance_totals[i] > appliance_limit:
                    print(appliances[i], ":",
                          appliance_totals[i], "kWh")
                    found = True

            if not found:
                print("No Appliance Limit Violations")

            print("\n======================================")
            print(" ANALYSIS COMPLETED")
            print("======================================")

    else:
        print("Program stopped due to invalid readings.")

