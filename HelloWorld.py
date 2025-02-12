#-----2.1.1 Our very first program, 2.1.2 The Print() Function

print("Hello World!") #Here "print" is a function which displays the text given in ("SOME TEXT GIVEN HERE")

# Where does the "print" fucntion comes from ? 
# 1.FROM PYTHON ITSELF ! (INBUILT)
# 2.FROM EXTERNAL MODULES               
# 3.FROM OUR CODE (we can also write our own function!)

# * A FUNCTION MAY ALSO HAVE A EFFECT OR A RESULT!

#----2.1.3 Function Args/ Arguments

# FUNCTION INVOCATION 
#The function name (print in this case) along with the parentheses and argument(s), forms the function invocation.

# EXAMPLE- function_name(argument)



#What happens when Python encounters an invocation like this one below?

#function_name(argument)

#Let's see:

#First, Python checks if the name specified is legal (it browses its internal data in order to find an existing function of the name; if this search fails, Python aborts the code)
#second, Python checks if the function's requirements for the number of arguments allows you to invoke the function in this way (e.g., if a specific function demands exactly two arguments, any invocation delivering only one argument will be considered erroneous, and will abort the code's execution)
#third, Python leaves your code for a moment and jumps into the function you want to invoke; of course, it takes your argument(s) too and passes it/them to the function;
#fourth, the function executes its code, causes the desired effect (if any), evaluates the desired result(s) (if any) and finishes its task;
#finally, Python returns to your code (to the place just after the invocation) and resumes its execution.




