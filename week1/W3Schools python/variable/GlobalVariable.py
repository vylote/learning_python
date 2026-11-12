# global variable: variable that is defined outside of a function and can 
# be accessed by everyone both inside and outside of functions

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#if u create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
def myfunc2():
    x = "fantastic"
    print("Python is " + x)

myfunc2()

print("Python is " + x)

#If you use the global keyword, the variable belongs to the global scope:
def myfunc3():
    global x
    x = "wonderful"
    print("Python is " + x)

myfunc3()
print("Python is " + x)
