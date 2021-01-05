# Example of exception Handling
try:
    a = int(input("Enter a First Number:"))
    b = int(input("Enter a Second Number:"))

    c = a / b
except ZeroDivisionError as a:
    print("Error is", a)
except ValueError as s:
    print("Error is", s)
except Exception as e:
    print("Any Type Error Handle", e)
finally:
    print("Hi! You are Lucky")

print(c)
