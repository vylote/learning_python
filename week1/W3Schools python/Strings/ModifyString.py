a = "Hello, World!"

#upper case
print(a.upper())

#lower case
print(a.lower())

#remove whitespace from the beginning or the end
b = "   Hello, World!   "
print(b.strip()) # returns "Hello, World!"

#replce a string with another string    
print(a.replace("H", "J")) # returns "Jello, World!"

#Split the string into a list
print(a.split(",")) # returns ['Hello', ' World!']

#String methods can be chained together
print(a.replace("H", "J").upper().split(",")) # returns ['JELLO', ' WORLD!']