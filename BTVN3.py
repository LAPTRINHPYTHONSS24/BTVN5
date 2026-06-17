import re

class MemberCard:
    point_value_vnd = 1000  # Class Attribute

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name
        self.__points = 0       # Private
        self.__tier = "Standard" # Private

    # Getters (Property)
    @property
    def points(self): return self.__points
    @property
    def tier(self): return self.__tier

    @staticmethod
    def is_valid_card_id(card_id):
        # Kiểm tra bắt đầu bằng RC và theo sau là đúng 2 chữ số
        return bool(re.match(r"^RC\d{2}$", card_id))

    @classmethod
    def update_point_value(cls, new_value):
        cls.point_value_vnd = new_value

    def earn_points(self, bill_amount):
        earned = bill_amount // 10000
        self.__points += earned
        if self.__points >= 100:
            self.__tier = "VIP"
        return earned

    def redeem_points(self, points_to_use):
        if 0 < points_to_use <= self.__points:
            self.__points -= points_to_use
            return points_to_use * self.point_value_vnd
        return None

# --- LUỒNG CHÍNH (Main Flow) ---
cards_database = []

# Ví dụ thêm mới:
def register_card():
    cid = input("Nhập mã thẻ: ")
    if MemberCard.is_valid_card_id(cid):
        if any(c.card_id == cid for c in cards_database):
            print("Mã thẻ đã tồn tại!")
        else:
            name = input("Nhập tên: ")
            cards_database.append(MemberCard(cid, name))
            print("Đăng ký thành công!")
    else:
        print("Mã thẻ không hợp lệ (Ví dụ: RC01)!")