counter = 10
while counter != 0:
    print("inside the loop", counter)
    counter -= 1
    print("Outside the loop", counter)

#The code can be written more compactly 

COUNTER = 10
while COUNTER:
    print("Inside the loop", COUNTER)
    COUNTER -= 1
print("Outside The Loop", COUNTER)