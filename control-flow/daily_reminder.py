
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task that requires immediate attention today!"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task. It should be completed soon."
    case "low":
        reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder_message = "Invalid priority entered."


if time_bound == "yes":
    reminder_message = f"'{task}' is a time-sensitive task that requires immediate action today!"
elif time_bound == "no":
    reminder_message += " It is not time-sensitive."


print(f"Reminder: {reminder_message}")
