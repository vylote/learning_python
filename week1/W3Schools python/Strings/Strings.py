#Strings in Python are surrounded by either single quotation marks, or double quotation marks.
print("Hello")
print('Hello')

#Quote inside a quote
print("I'm a programmer")   
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Multiline Strings
#You can assign a multiline string to a variable by using three quotes, or three double quotes
a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(a)

print("\n")

a = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'''
print(a)

#Strings are arrays

#Looping through a string
for x in "banana":
  print(x)

#Check String
#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

#use it in if statement
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#Check if NOT
#To check if a certain phrase or character is NOT present in a string, we can use
print("expensive" not in txt)

#use it in if statement
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")