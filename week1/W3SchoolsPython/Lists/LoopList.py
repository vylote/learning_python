#You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

print()

#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

print()

#Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print()
#looping using list comprehension
#List Comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
#List comprehension là cách viết gọn để tạo một list mới bằng một dòng, thay cho vòng lặp for nhiều dòng.
[print(x) for x in thislist]

#List Comprehension offers the shortest syntax for looping through lists:

