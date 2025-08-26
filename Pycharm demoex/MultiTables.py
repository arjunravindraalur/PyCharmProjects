# Multiplication Table Program

# Ask user for a number
num = int(input("Enter a number to print its multiplication table: "))

# Print multiplication table up to 10
print(f"\nMultiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
