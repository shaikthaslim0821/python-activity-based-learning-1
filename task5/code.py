weight = float(input("Enter Parcel Weight (kg): "))
length = float(input("Enter Length (cm): "))
width = float(input("Enter Width (cm): "))
height = float(input("Enter Height (cm): "))

zone = input("Enter Distance Zone (Local/National/International): ").lower()
urgency = input("Enter Urgency (Normal/Express): ").lower()
restricted = input("Does parcel contain restricted items? (yes/no): ").lower()

if weight <= 0 or length <= 0 or width <= 0 or height <= 0:
    print("Invalid Parcel Weight or Dimensions")

elif zone not in ["local", "national", "international"]:
    print("Invalid Distance Zone")

elif urgency not in ["normal", "express"]:
    print("Invalid Urgency")

elif restricted not in ["yes", "no"]:
    print("Invalid Restriction Details")

else:
   
    volumetric_weight = (length * width * height) / 5000

    chargeable_weight = max(weight, volumetric_weight)

    zone_rates = {
        "local": 30,
        "national": 60,
        "international": 150
    }

    rate = zone_rates[zone]

    basic_charge = chargeable_weight * rate

    services = {
        "Standard": {
            "factor": 1.0,
            "max_weight": 20,
            "restricted_allowed": False
        },
        "Express": {
            "factor": 1.5,
            "max_weight": 10,
            "restricted_allowed": False
        },
        "Special Handling": {
            "factor": 2.0,
            "max_weight": 30,
            "restricted_allowed": True
        }
    }

    eligible_services = {}

    print("\n======================================")
    print("       COURIER SERVICE REPORT")
    print("======================================")

    print("Actual Weight       :", weight, "kg")
    print("Volumetric Weight   :", round(volumetric_weight, 2), "kg")
    print("Chargeable Weight   :", round(chargeable_weight, 2), "kg")
    print("Distance Zone       :", zone.title())
    print("Delivery Urgency    :", urgency.title())

    print("--------------------------------------")
    print("SERVICE COMPARISON")
    print("--------------------------------------")

    for service, details in services.items():

        if chargeable_weight > details["max_weight"]:
            print(service, ": Not Eligible (Weight Limit)")
            continue

        if restricted == "yes" and not details["restricted_allowed"]:
            print(service, ": Not Eligible (Restricted Parcel)")
            continue

        if urgency == "express" and service == "Standard":
            print(service, ": Not Eligible (Urgency)")
            continue

        charge = basic_charge * details["factor"]

        eligible_services[service] = charge

        print(service, ": Rs.", round(charge, 2))

    print("--------------------------------------")

    if eligible_services:
        best_service = min(eligible_services, key=eligible_services.get)
        best_charge = eligible_services[best_service]

        print("Recommended Service :", best_service)
        print("Minimum Courier Fee : Rs.", round(best_charge, 2))
    else:
        print("No Eligible Courier Service Found")

    print("======================================")
    print("       ANALYSIS COMPLETED")

