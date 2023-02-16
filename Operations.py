# Sum two numbers recieved from the user
def sum(a, b):
    return a + b;

# divide two numbers recieved from the user
def divide(a, b):
    return a / b;

# Multiply two numbers recieved from the user
def multiply(a, b):
    return a * b;

# Subtract two numbers recieved from the user
def subtract(a, b):
    return a - b;

# Print the sum of two numbers
a = int(input("Enter the first number: "));
b = int(input("Enter the second number: "));
# Print Inserted numbers
print("a is: " + str(a));
print("b is: " + str(b));
# Print the result of the operations
print("The Operations are: ");
print("The sum of a and b is: " + str(sum(a, b)));
print("The division of a and b is: " + str(divide(a, b)));
print("The multiplication of a and b is: " + str(multiply(a, b)));
print("The subtraction of a and b is: " + str(subtract(a, b)));