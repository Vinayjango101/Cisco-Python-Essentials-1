#input function without  an Argument!
print("tell me anything~!")
anything = input()
print("Hmm...", anything, "....Really?")


#input function with an Argument!

something = input("Tell me Something: ")
print("Hmmmmm", something, "Really?")


#This means that you mustn't use it as an argument of any arithmetic operation, e.g., you can't use 
# this data to square it, divide it by anything, or divide anything by it.



#type casting (type Conversions)
# Python offers two simple functions to specify a type of data and solve this problem ‒ here they are: int() and float().

# Their names are self-commenting:

# the int() function takes one argument (e.g., a string: int(string)) and tries to convert it into an integer; if it fails, the whole program will fail too (there is a workaround for this situation, but we'll show you this a little later);
# the float() function takes one argument (e.g., a string: float(string)) and tries to convert it into a float (the rest is the same).
number_inp = float(input("Enter a NUMBER: "))
sqrit = number_inp ** 2.0
print(number_inp, "to the power of 2 is", sqrit)