#Lesson 08: Control Modules & Functions
def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))

# Importing a module
import math

# Using a function from the math module
print("Square root of 16 is:", math.sqrt(16))

#Lesson 09: Exception Handling
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This runs no matter what.")

#Lesson 10: File Handling
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, file handling in Python!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:", content)

#Lesson 11: The Math, DateTime & Calendar
import math
import datetime
import calendar

# Math module
print("Cosine of 0:", math.cos(0))

# DateTime module
now = datetime.datetime.now()
print("Current date and time:", now)

# Calendar module
print("Calendar for May 2025:")
print(calendar.month(2025, 5))
