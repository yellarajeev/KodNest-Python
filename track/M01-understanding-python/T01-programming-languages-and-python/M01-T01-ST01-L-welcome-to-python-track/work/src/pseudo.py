"""
Python Lesson: Basic Logic and Conditionals
File: pseudo.py

Contents:
1. Print Hello World
2. Check whether a number is even or odd
3. Check whether a number is positive, negative, or zero
4. Find the largest among three numbers (a, b, c)
"""

# ==============================================================================
# Task 1: Print Hello World
# ==============================================================================
# Pseudocode / Logic:
#   START
#       DISPLAY "Hello World"
#   END
# ------------------------------------------------------------------------------
print("--- Task 1: Print Hello World ---")
print("Hello World")
print()


# ==============================================================================
# Task 2: Check whether a number is even or odd
# ==============================================================================
# Pseudocode / Logic:
#   START
#       READ n
#       IF n % 2 == 0 THEN
#           DISPLAY n, "is even"
#       ELSE
#           DISPLAY n, "is odd"
#       END IF
#   END
# ------------------------------------------------------------------------------
print("--- Task 2: Even or Odd Checker ---")
n = int(input("Enter an integer: "))
if n % 2 == 0:
    print(f"{n} is even.")
else:
    print(f"{n} is odd.")
print()


# ==============================================================================
# Task 3: Check whether a number is positive, negative, or zero
# ==============================================================================
# Pseudocode / Logic:
#   START
#       READ num
#       IF num > 0 THEN
#           DISPLAY num, "is positive"
#       ELSE IF num < 0 THEN
#           DISPLAY num, "is negative"
#       ELSE
#           DISPLAY "The number is zero"
#       END IF
#   END
# ------------------------------------------------------------------------------
print("--- Task 3: Positive, Negative, or Zero Checker ---")
num = float(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print("The number is zero.")
print()


# ==============================================================================
# Task 4: Find the largest among three numbers a, b, and c
# ==============================================================================
# Pseudocode / Logic:
#   START
#       READ a, b, c
#       IF a >= b AND a >= c THEN
#           largest = a
#       ELSE IF b >= c THEN
#           largest = b
#       ELSE
#           largest = c
#       END IF
#       DISPLAY "The largest number is", largest
#   END
# ------------------------------------------------------------------------------
print("--- Task 4: Find the Largest Among Three Numbers ---")
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
c = float(input("Enter third number (c): "))

if a >= b and a >= c:
    largest = a
elif b >= c:
    largest = b
else:
    largest = c

print(f"The largest number among {a}, {b}, and {c} is {largest}.")
print()
