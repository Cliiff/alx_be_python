# daily_reminder.py

# Prompt the user for the task
task = input("Task: ")

# Prompt for the priority using the exact required wording
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time sensitivity using the exact required wording
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = f"Reminder: Your task is '{task}'."

# Use match-case to customize the message based on priority
match priority:
    case "high":
        reminder += " This is a high priority task."
    case "medium":
        reminder += " This is a medium priority task."
    case "low":
        reminder += " This is a low priority task."
    case _:
        reminder += " Priority not recognized. Defaulting to general importance."

# Add time-sensitive note if applicable
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Display the reminder
print("\n" + reminder)
# End of daily reminder script