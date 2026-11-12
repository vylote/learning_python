#Change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#change a range of item values 
#To change the value of items within a specific range, define a list with the new values, and refer to the range
#of index numbers where u want to insert the new values:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining 
# items will move accordingly:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 

#insert item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#ADD LIST ITEM


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable
# The extend() method does not have to append lists, you can add any 
# iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)