product = input("Enter Product Name: ")
quantity = int(input("Enter Production Quantity: "))

material = float(input("Enter Material Cost per Unit: "))
labour = float(input("Enter Labour Cost per Unit: "))
wastage_rate = float(input("Enter Wastage Percentage: "))
machine = float(input("Enter Total Machine Cost: "))
selling_price = float(input("Enter Selling Price per Unit: "))
target = float(input("Enter Target Profit Percentage: "))


material_cost = material * quantity


wastage_cost = material_cost * wastage_rate / 100


labour_cost = labour * quantity


total_cost = material_cost + wastage_cost + labour_cost + machine
cost_per_unit = total_cost / quantity


revenue = selling_price * quantity


profit = revenue - total_cost


profit_percentage = (profit / total_cost) * 100


print("\n======================================")
print("  MANUFACTURING COST REPORT")
print("======================================")
print("Product Name        :", product)
print("Production Quantity :", quantity)
print("--------------------------------------")
print("Material Cost       : Rs.", round(material_cost, 2))
print("Wastage Cost        : Rs.", round(wastage_cost, 2))
print("Labour Cost         : Rs.", round(labour_cost, 2))
print("Machine Cost        : Rs.", round(machine, 2))
print("--------------------------------------")
print("Total Production Cost:", round(total_cost, 2))
print("Cost Per Unit       : Rs.", round(cost_per_unit, 2))
print("Total Revenue       : Rs.", round(revenue, 2))
print("Profit / Loss       : Rs.", round(profit, 2))
print("Profit Percentage   :", round(profit_percentage, 2), "%")
print("Target Profit       :", target, "%")
print("--------------------------------------")


if profit_percentage >= target:
    print("RESULT: PROFIT TARGET ACHIEVED")
else:
    print("RESULT: PROFIT TARGET NOT ACHIEVED")

print("======================================")
print("  ANALYSIS COMPLETED")


