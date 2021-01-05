# Write a python program that accept a number and print the squre of entered number in reverse order
# 9 = 81 =18(Print)
vd = True
while vd:
    try:
        n = int(input("Enter any number:"))
        vd = False
    except ValueError:
        print("You have entered data that can't be converted to int")
    else: # Executes when no exception throw
        print("Horrhay! you have entered a valid number I am giving result")
    finally:
        print("1 round Completed")

b = n * n
# convert n into string
b = str(b)
b = b[::-1]
print(b)