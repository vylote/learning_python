# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#ithout list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList1 = [x for x in fruits if "o" in x]
print(newList1)

#The Syntax
#newlist = [expression for item in iterable if condition == True]

#The condition is optional and can be omitted:


#Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.
#You can use the range() function to create an iterable:

#Iterable (đối tượng có thể lặp) là bất cứ thứ gì mà vòng for có thể lấy ra từng phần tử một. Nó là phần đứng sau chữ in:

newlist = [x for x in range(10)] 

print(newlist)

#Expression
#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate 
# before it ends up like a list item in the new list:

#Câu đó nói về phần biểu thức (expression) ở đầu list comprehension, tức phần đứng trước chữ for:

# [ x  for x in fruits ]
# #  ^
# #  biểu thức (expression)
#Ý 1: Biểu thức chính là phần tử hiện tại của vòng lặp
#Ở mỗi vòng, x nhận một phần tử trong list. Biểu thức có thể chỉ là x, nghĩa là lấy nguyên phần tử đó.

# fruits = ["apple", "banana", "cherry"]
# newlist = [x for x in fruits]
# print(newlist)    # ['apple', 'banana', 'cherry']

#Ý 2: Nhưng nó cũng là kết quả, và bạn có thể chỉnh sửa nó trước khi đưa vào list mới
# Thứ bạn viết ở phần biểu thức chính là cái được bỏ vào list mới. Nên bạn không cần để nguyên x, mà có thể biến đổi x rồi mới bỏ vào.

# # Biến thành chữ hoa
# print([x.upper() for x in fruits])    # ['APPLE', 'BANANA', 'CHERRY']

# # Thay mọi phần tử bằng một giá trị cố định
# print(["hello" for x in fruits])      # ['hello', 'hello', 'hello']

# # Lấy độ dài của mỗi phần tử
# print([len(x) for x in fruits])       # [5, 6, 6]