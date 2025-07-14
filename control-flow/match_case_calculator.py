first = input("Enter the first number:")
second = input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "+":
        print(f"The result is{int(first) + int(second)}.")
        
    case "-":
        print(f"The result is{int(first) - int(second)}.")
    case "*":
        print(f"The result is{int(first) * int(second)}.")
    case "/":
        if int(second) == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is{int(first) / int(second)}.")
    case _:
        print("Invalid operation.")

