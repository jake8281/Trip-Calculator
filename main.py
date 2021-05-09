import mileage_calculator as MC


def main():
    input_destination = str(input("What is your destination?  📍 "))
    input_mileage = float(input("What is your mileage? 🚗 "))
    input_gas_price = float(input("What is the gas price?  💵 "))
    input_tank_size = float(input("What is your tank size? 🛢 "))
    output = MC.Trip(input_destination, input_mileage, input_gas_price, input_tank_size).summary()
    return output


if __name__ == "__main__":
    print(main())