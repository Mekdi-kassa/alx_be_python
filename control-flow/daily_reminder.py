task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a HIGH priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a HIGH priority task. Consider completing it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a MEDIUM priority task that should be done today.")
        else:
            print(f"'{task}' is a MEDIUM priority task. Do it when you have time.")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a LOW priority task, but it's time-bound for today.")
        else:
            print(f"'{task}' is a LOW priority task. Do it whenever you can.")
    case _:
        print("Invalid priority entered.")