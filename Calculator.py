def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice : "))

    n1 = float(input("Enter First number: "))
    n2 = float(input("Enter Second number: "))

    if choice == 1:
        result = n1 + n2
        print(f"{n1} + {n2} = {result}")
    elif choice == 2:
        result = n1 - n2
        print(f"{n1} - {n2} = {result}")
    elif choice == 3:
        result = n1 * n2
        print(f"{n1} * {n2} = {result}")
    elif choice == 4:
        if n2 != 0:
            result = n1 / n2
            print(f"{n1} / {n2} = {result}")
        else:
            print("Error! Division by zero is Invalid.")
    else:
        print("Choice is invalid. Please choose a valid operation.")

if __name__ == "__main__":
    calculator()