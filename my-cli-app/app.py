import socket

def menu():
    print("\n=== Unit Converter (running on container: %s) ===" % socket.gethostname())
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    print("3. Kilometres -> Miles")
    print("q. Quit")
    return input("Choose an option: ").strip().lower()

def read_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid number, please try again.")
        return None

def main():
    while True:
        choice = menu()
        if choice == "q":
            print("Goodbye!")
            break
        if choice not in ("1", "2", "3"):
            print("Unknown option.")
            continue
        value = read_number("Enter value: ")
        if value is None:
            continue
        if choice == "1":
            print(f"{value} C = {value * 9 / 5 + 32:.2f} F")
        elif choice == "2":
            print(f"{value} F = {(value - 32) * 5 / 9:.2f} C")
        else:
            print(f"{value} km = {value * 0.621371:.2f} miles")

if __name__ == "__main__":
    main()