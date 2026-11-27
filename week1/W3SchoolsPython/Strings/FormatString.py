# As we learned in Variables, we cannot combine strings and numbers like this
# age = 36
# # This will produce an error:
# txt = "My name is John, I am " + age   # TypeError: chỉ nối được str với str
# print(txt)

# But we can combine them by using f-strings or the format() method.

# ==========================================
# 1. F-STRING CƠ BẢN
# ==========================================
# Thêm chữ 'f' (hoặc 'F') trước dấu ngoặc kép, đặt biến vào trong cặp ngoặc nhọn {}
age = 36
txt = f"My name is John, I am {age}"
print(txt)  # My name is John, I am 36

# ==========================================
# 2. PLACEHOLDERS (Biểu thức & Hàm bên trong {})
# ==========================================
# Trong {} có thể tính toán hoặc gọi hàm trực tiếp
txt = f"My name is John, I am {age + 5} years old."
print(txt)  # My name is John, I am 41 years old.

name = "john"
print(f"Hello {name.upper()}!")  # Hello JOHN!

# ==========================================
# 3. MODIFIERS (Định dạng hiển thị sau dấu hai chấm :)
# ==========================================
price = 59.324123123
print(f"The price is {price:.2f} dollars.")  # 59.32     -> Lấy 2 chữ số thập phân (tự làm tròn)

money = 1000000
print(f"Salary: {money:,} VND")             # 1,000,000 -> Thêm dấu phẩy ngăn cách hàng nghìn

rate = 0.256
print(f"Discount: {rate:.2%}")              # 25.60%     -> Đổi sang phần trăm (lấy 2 số sau dấu)

num = 42
print(f"ID: {num:05d}")                     # 00042     -> Thêm số 0 ở đầu cho đủ 5 chữ số

# ==========================================
# 4. MẸO DEBUG NHANH (Dấu = bên trong {})
# ==========================================
# Rất tiện khi kiểm tra giá trị biến lúc chạy thử code:
x = 10
y = 20
print(f"{x = }, {y = }, {x + y = }")        # x = 10, y = 20, x + y = 30