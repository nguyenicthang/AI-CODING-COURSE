# Nhập thư viện datetime để lấy năm hiện tại
from datetime import date

# In lời chào với thông tin cá nhân và ngày hôm nay
print("Xin chào, tôi là Nguyễn Ích Thắng. Hôm nay là 26/5/2026")

# Khai báo năm sinh
birth_year = 2007

# Lấy năm hiện tại từ hệ thống
current_year = date.today().year

# Tính tuổi bằng cách lấy năm hiện tại trừ năm sinh
age = current_year - birth_year

# In kết quả tuổi ra màn hình
print(f"Tuổi của tôi là: {age}")