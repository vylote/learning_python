#u can return a range of characters by using the slice syntax
#specify the start index and the end index, separated by a colon, to return a part of the string
b = "HelloWorld"
print(b[2:5]) #get characters from position 2 to position 5

#slice from the start
#By leaving out the start index, the range will start at the first character
print(b[:5])

#slice to the end
#By leaving out the end index, the range will go to the end
print(b[2:])

#negative indexing
#Use negative indexes to start the slice from the end of the string
print(b[-5:-2]) #get characters from position -5 to position -2


s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5    (chỉ số dương)
#   -6 -5 -4 -3 -2 -1    (chỉ số âm)

print(s[-1])   # n
print(s[-2])   # o
print(s[-6])   # P