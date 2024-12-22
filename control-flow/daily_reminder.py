task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


reminder_message = f"Reminder: '{task}' is a {priority} priority task."

match priority:
    case "high":
        reminder_message += " It requires immediate attention today!"
    case "medium":
        reminder_message += " It should be completed soon."
    case "low":
        reminder_message += " Consider completing it when you have free time."
    case _:
        reminder_message = "Invalid priority entered."


if time_bound == "yes":
    reminder_message = f"'{task}' is a time-sensitive task that requires immediate action today!"
elif time_bound == "no":
    reminder_message += " It is not time-sensitive."


print(reminder_message)
