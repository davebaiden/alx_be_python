# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"High-priority reminder: {task}"
    case "medium":
        message = f"Medium-priority task: {task}"
    case "low":
        message = f"Low-priority task: {task}"
    case _:
        message = f"Unrecognized priority level for: {task}"

if time_bound == "yes":
    message += " — that requires immediate attention today!"

print("\n" + message)