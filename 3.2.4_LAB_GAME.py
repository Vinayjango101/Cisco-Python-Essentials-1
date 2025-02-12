SECRET_NUMBER = 777

x = 0
while x == 0:
    User_input = int(input("Enter the SECRET NUMBER~: "))
    if User_input != SECRET_NUMBER:
        print("ha ha! you are stuck in my loop!")
    else:
        print("Well done, muggle! You are free now.")
        exit()