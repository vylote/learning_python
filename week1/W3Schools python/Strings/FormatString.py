#As we learned in Variables, we cannot combine strings and numbers like this
# age = 36
# #This will produce an error:
# txt = "My name is John, I am " + age
# print(txt)

#but we can combine their by using f-strings or the format() method.
#F-String
#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders 
#for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers
#placeholders can contain variables, operations, functions, and modifiers to format the value
txt = f"My name is John, I am {age + 5} years old."
print(txt)

price = 59.324123123
txt = f"The price is {price:.2f} dollars."
print(txt)
