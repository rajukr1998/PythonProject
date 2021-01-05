# Python code to print 10 uniquew random number between 1 to 100
import random
murn = {random.randint(1,100)}
while len(murn) != 10:
    try:
        murn.add(random.randint(1,100))
    except Exception as e:
        print(e)
print(list(murn))