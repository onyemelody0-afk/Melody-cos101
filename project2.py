def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * (velocity ** 2)

def calculate_force(mass, acceleration):
    return mass * acceleration

def calculate_potential_energy(mass, height, gravity=9.8):
    return mass * gravity * height

def calculate_ohms_law_voltage(current, resistance):
    return current * resistance

def calculate_speed(distance, time):
    if time == 0:
        return "Time cannot be zero"
    return distance / time

while True:
    print("\n--- Physics Calculator ---")
    print("1. Kinetic Energy")
    print("2. Force")
    print("3. Potential Energy")
    print("4. Ohm's Law Voltage")
    print("5. Speed")

    choice = input("Enter operation 1-5: ")

    if choice == "1":
        mass = float(input("Enter mass: "))
        velocity = float(input("Enter velocity: "))
        print("Kinetic Energy =", calculate_kinetic_energy(mass, velocity))

    elif choice == "2":
        mass = float(input("Enter mass: "))
        acceleration = float(input("Enter acceleration: "))
        print("Force =", calculate_force(mass, acceleration))

    elif choice == "3":
        mass = float(input("Enter mass: "))
        height = float(input("Enter height: "))
        print("Potential Energy =", calculate_potential_energy(mass, height))

    elif choice == "4":
        current = float(input("Enter current: "))
        resistance = float(input("Enter resistance: "))
        print("Voltage =", calculate_ohms_law_voltage(current, resistance))

    elif choice == "5":
        distance = float(input("Enter distance: "))
        time = float(input("Enter time: "))
        print("Speed =", calculate_speed(distance, time))

    else:
        print("Not a valid option. Please enter 1-5.")

    again = input("\nDo you want to run another operation? (yes/no): ").lower()

    if again != "yes":
        print("Goodbye!")
        break