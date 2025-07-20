# daily_reminder.py

task = input("What is your main task for today? ")
priority = input("What is the priority level? (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        message = f"High-priority reminder: {task}"
    case "medium":
        message = f"Medium-priority task: {task}"
    case "low":
        message = f"Low-priority task: {task}"
    case _:
        message = f"Unrecognized priority for: {task}"

# Add time sensitivity notice
if time_bound == "yes":
    message += " — that requires immediate attention today!"

print("\n" + message)