class MemberCard:
    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        self.__points = points  # Sử dụng Name Mangling

    # Getter để đọc điểm
    @property
    def points(self):
        return self.__points

    # Setter để kiểm duyệt dữ liệu khi gán
    @points.setter
    def points(self, value):
        if isinstance(value, int) and value >= 0:
            self.__points = value
        else:
            print(">> [Lỗi]: Dữ liệu điểm không hợp lệ!")

    def add_points(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__points += amount
        else:
            print(">> [Lỗi]: Số điểm cộng thêm phải là số nguyên dương!")

    # Static method cho hàm tiện ích
    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000

# --- KỊCH BẢN TEST ---

# Tạo thẻ mới
card1 = MemberCard("Le Van C", 100)

# 1. Thử gán giá trị sai (Hệ thống sẽ từ chối)
card1.points = -50  
card1.points = "một trăm"

# 2. Gọi hàm check voucher trực tiếp từ Class (Không cần tạo object)
check = MemberCard.is_eligible_for_voucher(250000)

print(f"\nKhách hàng: {card1.customer_name} | Điểm hiện tại: {card1.points}")
print(f"Hóa đơn 250k có được tặng Voucher không? {'Có' if check else 'Không'}")