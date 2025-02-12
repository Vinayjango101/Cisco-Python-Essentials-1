od = 0
en = 0

number = int(input("Enter a number or type 0 to stop: "))

while number != 0:

    if number % 2 == 1:
        od += 1
    else:
        en += 1

    number = int(input("Enter a number or type 0 to stop: "))

print("Odd numbers count: ", od)
print ("Even numbers count: ", en)