# Write a python program that accept numbers from user until user says no .
# And print the all entered numbers  and sum and average of all numbers.
ch = 'y'
ave = 0
b = 0
arr = []
while ch == 'y' or ch == 'Y':
    try:
        arr.append(int(input("Enter a number:")))
    except Exception as e:
        print(e)
    ch = input("Want to enter more data?(Y/N):")
for i in arr:
    b = b + i
ave = b / len(arr)
print("Total sum number:", b)
print("Average number:", ave)
print(arr)
