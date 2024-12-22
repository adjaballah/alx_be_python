
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


if time_bound == "yes":
    reminder_message = f"'{task}' is a {priority} priority task that requires immediate attention today!"
else:
    reminder_message = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."


print(f"Reminder: {reminder_message}")
