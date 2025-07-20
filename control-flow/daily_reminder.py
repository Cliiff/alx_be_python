# daily_reminder.py

# Prompt the user to input task details
task = input("Enter your task for today: ")
time_bound = input("Is this task time-bound? (yes or no): ").lower()
priority = input("Set the task priority (high, medium, low): ").lower()

# Initialize reminder message
reminder = f"Reminder: Your task is '{task}'."

# Use match-case for priority-based response
match priority:
    case "high":
        reminder += " This is a high priority task."
    case "medium":
        reminder += " This is a medium priority task."
    case "low":
        reminder += " This is a low priority task."
    case _:
        reminder += " Priority not recognized. Defaulting to general importance."

# Add extra note if the task is time-sensitive
if time_bound == "yes":
    reminder += " This task **requires immediate attention today!**"

# Print the final reminder
print("\n" + reminder)
# End of daily reminder script