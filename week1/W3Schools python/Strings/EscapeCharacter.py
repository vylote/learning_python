#To insert characters that are illegal in a string, use an escape character
#An escape character is a backslash '\' followed by the character u want to insert
#An example of an illegal character is a double quote inside a string that is surrounded by double quote

# #You will get an error if you use double quotes inside a string that is surrounded by double quotes:
# txt = "We are the so-called "Vikings" from the north."

#To fix this problem, use the escape character \"
txt = "We are the so-called \"Vikings\" from the north."

#some example
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
