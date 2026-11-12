#python has the following data types built in by default, in these categories:
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType

#complex
z = 1 + 2j
print(z)
print(type(z))

#range
x = range(6)
print(x)
print(list(x))

#dict
x = {"name" : "John", "age" : 36, "country" : "Norway"}
print(x)    
print(type(x))

#dict access, add, remove, update
x["name"] = "Jane" #update
x["city"] = "New York" #add
del x["age"] #remove
print(x.pop("country")) #remove and return value
print(x)

# ---------- set ----------
# set: unordered, unindexed, no duplicate values
# Stored in a hash table: position = hash(item) % table_size
# hash of a str depends on a random seed chosen when Python starts
#   -> different seed = different hash = different position = different print order
# set is mutable -> hash could change -> NOT hashable
#   -> cannot be a dict key or an element of another set

x = {"apple", "banana", "cherry"}
print(x)
print(type(x))

# ---------- frozenset ----------
# Same as set: unordered, no duplicates, affected by hash seed
# Different: immutable -> hash never changes while the program runs -> hashable
#   - Add/remove items : set -> yes (add, remove, ...) | frozenset -> no (AttributeError)
#   - Hashable         : set -> no                     | frozenset -> yes
#   - Dict key         : set -> no                     | frozenset -> yes
#   - Element of a set : set -> no                     | frozenset -> yes
# Rule to remember: mutable -> not hashable | immutable -> hashable

x = frozenset(["apple", "banana", "cherry"])
print(x)
print(type(x))

#bytes
b = b"apple"
print(b)           # b'apple'
print(type(b))     # <class 'bytes'>
print(b[0])        # 97  (mã ASCII của 'a', ra số nguyên chứ không phải ký tự)
print(list(b))     # [97, 112, 112, 108, 101]


#bytearray
# bytearray là bản mutable của bytes: cũng là chuỗi các số nguyên 0-255, có thứ tự, có chỉ số, nhưng sửa được tại chỗ. 
# Quan hệ của chúng giống frozenset với set (một bên bất biến, một bên sửa được).
ba = bytearray(b"apple")
print(ba)            # bytearray(b'apple')
print(type(ba))      # <class 'bytearray'>
print(ba[0])         # 97

ba[0] = 65               # đổi byte đầu thành 'A'
print(ba)                # bytearray(b'Apple')

ba.append(33)            # thêm byte '!'
ba.extend(b"??")         # thêm nhiều byte
ba += b"xyz"             # nối thêm
ba.pop()                 # xóa byte cuối
ba[1:3] = b"XY"          # gán theo lát cắt
print(ba)


#memoryview
# memoryview là một “cửa sổ nhìn vào bộ nhớ” của đối tượng khác (bytes, bytearray, array...) mà không sao chép dữ liệu. 
# Nó cho bạn đọc (và có thể ghi) trực tiếp vào vùng nhớ gốc.

#The problem it resolve
# slice bytes or bytearray will create a copy of data
data = bytearray(b"hello world")
phan = data[0:5]       # tạo bản sao mới
phan[0] = ord("J")
print(data)            # bytearray(b'hello world'), không đổi


#with memory view, slice just a new view in the same buffer
mv = memoryview(data)
phan = mv[0:5]         # tạo view mới, không sao chép dữ
phan[0] = ord("J")
print(data)

# Chỉ đọc hay ghi được? TÙy thuộc vào đối tượng gốc
mv1 = memoryview(b"hello")      # bytes -> chỉ đọc
mv1[0] = 1  # TypeError: cannot modify read-only memory

mv2 = memoryview(bytearray(b"hello"))  # bytearray -> đọc và ghi
mv2[0] = 65
print(mv2.readonly)  # False