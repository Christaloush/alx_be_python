# pattern_drawing.py

# Prompt the user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to control rows
while row < size:
    # Use for loop to control columns
    for col in range(size):
        print("*", end="")
    # Move to next line after each row
    print()
    row += 1
