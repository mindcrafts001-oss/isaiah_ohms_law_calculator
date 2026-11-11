# ==========================================
# OHM'S LAW AND POWER CALCULATOR
# Author: Isaiah Sosan
# Department: Mechatronics Engineering
# ==========================================

import math

# Stores previous calculations
history = []


# Function to perform calculations
def calculate(target, values, selected_pair):

    a, b = selected_pair

    # Calculate Voltage
    if target == "voltage":

        if a == "current" and b == "resistance":
            return values["current"] * values["resistance"], "V", "V = I x R"

        elif a == "power" and b == "current":
            return values["power"] / values["current"], "V", "V = P / I"

        elif a == "power" and b == "resistance":
            return math.sqrt(values["power"] * values["resistance"]), "V", "V = sqrt(P x R)"

    # Calculate Current
    elif target == "current":

        if a == "voltage" and b == "resistance":
            return values["voltage"] / values["resistance"], "A", "I = V / R"

        elif a == "voltage" and b == "power":
            return values["power"] / values["voltage"], "A", "I = P / V"

        elif a == "resistance" and b == "power":
            return math.sqrt(values["power"] / values["resistance"]), "A", "I = sqrt(P / R)"

    # Calculate Resistance
    elif target == "resistance":

        if a == "voltage" and b == "current":
            return values["voltage"] / values["current"], "Ohms", "R = V / I"

        elif a == "voltage" and b == "power":
            return (values["voltage"] ** 2) / values["power"], "Ohms", "R = V² / P"

        elif a == "current" and b == "power":
            return values["power"] / (values["current"] ** 2), "Ohms", "R = P / I²"

    # Calculate Power
    elif target == "power":

        if a == "voltage" and b == "current":
            return values["voltage"] * values["current"], "W", "P = V x I"

        elif a == "voltage" and b == "resistance":
            return (values["voltage"] ** 2) / values["resistance"], "W", "P = V² / R"

        elif a == "current" and b == "resistance":
            return (values["current"] ** 2) * values["resistance"], "W", "P = I² x R"


# Main program
while True:

    print("\n================================")
    print("       OHM'S LAW CALCULATOR")
    print("================================")

    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")
    print("4. Calculate Power")
    print("5. View Calculation History")
    print("6. Exit")

    choice = input("\nSelect an option (1-6): ")

    # Exit program
    if choice == "6":
        print("\nThank you for using the calculator!")
        break

    # View calculation history
    elif choice == "5":

        print("\n====== CALCULATION HISTORY ======")

        if len(history) == 0:
            print("No calculations recorded yet.")

        else:
            for record in history:
                print(record)

        continue

    # Select calculation
    elif choice in ["1", "2", "3", "4"]:

        targets = {
            "1": "voltage",
            "2": "current",
            "3": "resistance",
            "4": "power"
        }

        target = targets[choice]

        print("\nYou selected:", target.upper())

        # Available combinations of known values
        options = {
            "voltage": [
                ("current", "resistance"),
                ("power", "current"),
                ("power", "resistance")
            ],

            "current": [
                ("voltage", "resistance"),
                ("voltage", "power"),
                ("resistance", "power")
            ],

            "resistance": [
                ("voltage", "current"),
                ("voltage", "power"),
                ("current", "power")
            ],

            "power": [
                ("voltage", "current"),
                ("voltage", "resistance"),
                ("current", "resistance")
            ]
        }

        print("\nChoose the two values you already know:")

        for index, pair in enumerate(options[target], 1):
            print(index, ".", pair[0].title(), "and", pair[1].title())

        try:

            pair_choice = int(input("\nSelect (1-3): "))

            if pair_choice < 1 or pair_choice > 3:
                print("Invalid selection. Choose 1, 2 or 3.")
                continue

            selected_pair = options[target][pair_choice - 1]

            values = {}

            # Collect known values
            for quantity in selected_pair:

                value = float(
                    input("Enter " + quantity.title() + ": ")
                )

                if value <= 0:
                    raise ValueError("Values must be greater than zero.")

                values[quantity] = value

            # Perform calculation
            result, unit, formula = calculate(
                target, values, selected_pair
            )

            # Display result
            print("\n========== RESULT ==========")
            print("Formula:", formula)
            print("Answer:", round(result, 4), unit)
            print("============================")

            # Save result in calculation history
            record = (
                target.title() + " = "
                + str(round(result, 4)) + " " + unit
            )

            history.append(record)

        except ValueError as error:

            print("\nInvalid input:", error)

        except ZeroDivisionError:

            print("\nError: Division by zero is not allowed.")

    else:

        print("\nInvalid option. Please select between 1 and 6.")