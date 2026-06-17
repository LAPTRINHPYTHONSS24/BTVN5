import re

class MenuItem:
    service_charge = 0.0  # Class Attribute

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name
        self.__base_price = base_price
        self.__is_available = True

    @property
    def base_price(self): return self.__base_price

    @base_price.setter
    def base_price(self, value):
        if value > 0:
            self.__base_price = value
        else:
            print("Giá đồ uống phải lớn hơn 0!")

    @property
    def is_available(self): return self.__is_available

    def calculate_selling_price(self):
        return self.__base_price + (self.__base_price * MenuItem.service_charge)

    def toggle_availability(self):
        self.__is_available = not self.__is_available

    @staticmethod
    def is_valid_item_id(item_code):
        # Kiểm tra: 2 chữ in hoa + 2 chữ số
        return bool(re.match(r"^[A-Z]{2}\d{2}$", item_code))

    @classmethod
    def update_service_charge(cls, new_rate):
        cls.service_charge = new_rate

# --- CHƯƠNG TRÌNH CHÍNH ---
menu_db = [
    MenuItem("CF01", "Cà Phê Đen", 30000),
    MenuItem("CF02", "Bạc Xỉu", 45000),
    MenuItem("TE01", "Trà Đào Cam Sả", 50000)
]

def main():
    while True:
        print("\n--- HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ---")
        print("1. Xem thực đơn | 2. Thêm món | 3. Cập nhật trạng thái | 4. Sửa giá | 5. Cập nhật phí | 6. Thoát")
        choice = input("Chọn: ")

        if choice == '1':
            for i, item in enumerate(menu_db, 1):
                status = "Đang bán" if item.is_available else "HẾT HÀNG"
                print(f"{i}. Mã: {item.item_id} | Tên: {item.item_name:<12} | Trạng thái: {status:<8} | Giá niêm yết: {item.calculate_selling_price():,.0f} VNĐ")
        
        elif choice == '2':
            cid = input("Nhập mã món: ")
            if MenuItem.is_valid_item_id(cid):
                if any(m.item_id == cid for m in menu_db): print("Mã đã tồn tại!")
                else:
                    name = input("Tên món: ")
                    price = int(input("Giá gốc: "))
                    menu_db.append(MenuItem(cid, name, price))
                    print("Thêm thành công!")
            else: print("Mã không hợp lệ! (VD: CF01)")

        elif choice == '3':
            cid = input("Nhập mã món cần cập nhật: ")
            item = next((m for m in menu_db if m.item_id == cid), None)
            if item:
                item.toggle_availability()
                status = "ĐANG BÁN" if item.is_available else "HẾT HÀNG"
                print(f">> Đã cập nhật {item.item_name} thành {status}!")
            else: print("Không tìm thấy món.")

        elif choice == '4':
            cid = input("Nhập mã món cần đổi giá: ")
            item = next((m for m in menu_db if m.item_id == cid), None)
            if item:
                new_price = int(input("Nhập giá mới: "))
                item.base_price = new_price
                print("Cập nhật giá gốc thành công!")
            else: print("Không tìm thấy món.")

        elif choice == '5':
            rate = float(input("Nhập phụ phí mới (ví dụ 0.1 cho 10%): "))
            MenuItem.update_service_charge(rate)
            print("Cập nhật phụ phí thành công!")
            
        elif choice == '6': break

if __name__ == "__main__":
    main()