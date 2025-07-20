# pattern_drawing.py

# Prompt the user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Validate that the input is positive
while size <= 0:
    size = int(input("Please enter a positive integer: "))

# Initialize row counter
row = 0

# Outer while loop to handle rows
while row < size:
    # Inner for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")  # Print asterisk without moving to a new line
    print()  # Move to the next line after a row is complete
    row += 1
