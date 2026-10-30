capacity = int(input("Enter Maximum Bus Capacity: "))
passengers = int(input("Enter Initial Number of Passengers: "))
stops = int(input("Enter Number of Bus Stops: "))


if capacity <= 0 or passengers < 0 or stops <= 0:
    print("Invalid Bus Details")

elif passengers > capacity:
    print("Initial Passengers Exceed Bus Capacity")

else:
    occupancy = []
    violations = []

    maximum_occupancy = passengers
    valid = True

   
    for i in range(stops):

        print("\nBus Stop", i + 1)

        alighting = int(input("Enter Alighting Passengers: "))
        boarding = int(input("Enter Boarding Passengers: "))

      
        if alighting < 0 or boarding < 0:
            print("Invalid Passenger Count")
            valid = False
            break

        elif alighting > passengers:
            print("Error: More passengers alighting than onboard")
            valid = False
            break

        else:
            Update passenger count
            passengers = passengers - alighting
            passengers = passengers + boarding

            occupancy.append(passengers)

            maximum_occupancy = max(
                maximum_occupancy, passengers
            )

            Check capacity violation
            if passengers > capacity:
                violations.append((i + 1, passengers))

    Display report
    if valid:

        print("\n======================================")
        print("       BUS OCCUPANCY REPORT")
        print("======================================")

        for i in range(stops):

            print("Stop", i + 1,
                  "- Passengers:", occupancy[i])

            if occupancy[i] > capacity:
                print("WARNING: CAPACITY EXCEEDED")
            else:
                print("Status: Within Capacity")

        print("--------------------------------------")
        print("Maximum Occupancy:", maximum_occupancy)
        print("Bus Capacity:", capacity)

        print("\nCAPACITY VIOLATIONS:")

        if violations:
            for stop, count in violations:
                print("Stop", stop, "- Passengers:", count)
        else:
            print("No Capacity Violations")

        print("======================================")
        print("       SIMULATION COMPLETED")
        print("======================================")

    else:
        print("Simulation stopped due to invalid input.")

