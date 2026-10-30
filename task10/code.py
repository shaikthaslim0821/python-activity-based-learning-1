n = int(input("Enter Number of Areas: "))
days = int(input("Enter Number of Days: "))

if n <= 0 or days <= 0:
    print("Invalid Number of Areas or Days")

else:
    areas = []
    demand = []
    supply = []
    valid = True

  
    for i in range(n):
        name = input("Enter Area Name: ")
        areas.append(name)

   
    for i in range(n):
        demand_row = []
        supply_row = []

        print("\nArea:", areas[i])

        for j in range(days):
            print("Day", j + 1)

            d = float(input("Enter Water Demand (litres): "))
            s = float(input("Enter Water Supply (litres): "))

            if d < 0 or s < 0:
                print("Invalid Water Quantity")
                valid = False
                break

            demand_row.append(d)
            supply_row.append(s)

        if not valid:
            break

        demand.append(demand_row)
        supply.append(supply_row)

    if valid:

       
        area_demand = []
        area_supply = []
        shortages = []
        shortage_percentages = []

        for i in range(n):
            total_demand = sum(demand[i])
            total_supply = sum(supply[i])

            shortage = max(0, total_demand - total_supply)

            if total_demand > 0:
                percentage = (shortage / total_demand) * 100
            else:
                percentage = 0

            area_demand.append(total_demand)
            area_supply.append(total_supply)
            shortages.append(shortage)
            shortage_percentages.append(percentage)

      
        print("\n======================================")
        print(" WATER DISTRIBUTION FAIRNESS REPORT")
        print("======================================")

        print("\nAREA-WISE ANALYSIS")

        for i in range(n):
            print("\nArea:", areas[i])
            print("Total Demand:", area_demand[i], "litres")
            print("Total Supply:", area_supply[i], "litres")
            print("Water Shortage:", shortages[i], "litres")
            print("Shortage Percentage:",
                  round(shortage_percentages[i], 2), "%")

       
        print("\nDAILY WATER DISTRIBUTION")

        for j in range(days):
            daily_demand = 0
            daily_supply = 0

            for i in range(n):
                daily_demand += demand[i][j]
                daily_supply += supply[i][j]

            daily_shortage = max(0, daily_demand - daily_supply)

            print("\nDay", j + 1)
            print("Total Demand:", daily_demand, "litres")
            print("Total Supply:", daily_supply, "litres")
            print("Total Shortage:", daily_shortage, "litres")

       
        maximum_shortage = max(shortage_percentages)

        print("\nMOST UNDERSERVED AREA(S):")

        for i in range(n):
            if shortage_percentages[i] == maximum_shortage:
                print(areas[i],
                      "- Shortage:",
                      round(shortage_percentages[i], 2), "%")

        print("\n======================================")
        print(" ANALYSIS COMPLETED")
        print("======================================")

    else:
        print("Program stopped due to invalid input.")

