# /***************************/
# Mã sinh viên: 202418900
# Họ tên: Nguyễn Đăng Hiếu
# /***************************/

from decimal import Decimal
from enum import Enum

from device import Device
from networkable import INetworkable, NetworkConnection


class PrinterType(Enum):
    """Loại máy in theo đề: laser hoặc phun."""
    LASER = "Laser"
    INKJET = "Phun"


class Printer(Device):
    """Máy in thường (không có khả năng kết nối mạng).

    Thuộc tính is_color là thuộc tính bổ sung ngoài đề, vì chi phí bảo trì
    có cộng thêm 300.000 đồng cho máy in màu nên cần biết máy có in màu không.
    """

    def __init__(self, device_id, name, year_in_use, purchase_price, status,
                 printer_type, pages, is_color):
        """Khởi tạo máy in.

        Raises:
            ValueError: nếu loại máy in sai kiểu hoặc số trang < 0.
        """
        super().__init__(device_id, name, year_in_use, purchase_price, status)
        if not isinstance(printer_type, PrinterType):
            raise ValueError("Loại máy in phải là giá trị của PrinterType.")
        if pages < 0:
            raise ValueError("Số trang đã in không được âm.")
        self.printer_type = printer_type
        self.pages = pages
        self.is_color = is_color

    def calculate_maintenance_cost(self):
        """4% giá mua; +500.000 nếu in trên 100.000 trang; +300.000 nếu máy in màu."""
        cost = self.purchase_price * Decimal("0.04")
        if self.pages > 100000:
            cost += Decimal(500000)
        if self.is_color:
            cost += Decimal(300000)
        return cost

    def __str__(self):
        color = "màu" if self.is_color else "đen trắng"
        return (super().__str__() +
                f" - Máy in [{self.printer_type.value}, {color}, Số trang: {self.pages}]")


class NetworkPrinter(Printer, INetworkable):
    """Máy in có hỗ trợ mạng: kế thừa Printer và thực thi INetworkable.

    Dùng cho mô hình "chỉ một số máy in có khả năng mạng".
    """

    def __init__(self, device_id, name, year_in_use, purchase_price, status,
                 printer_type, pages, is_color):
        super().__init__(device_id, name, year_in_use, purchase_price, status,
                         printer_type, pages, is_color)
        self._connection = NetworkConnection()

    @property
    def ip_address(self):
        return self._connection.ip_address

    @property
    def is_connected(self):
        return self._connection.is_connected

    def connect(self, ip_address):
        self._connection.connect(ip_address)

    def disconnect(self):
        self._connection.disconnect()

    def __str__(self):
        ip = self.ip_address if self.is_connected else "Chưa kết nối"
        return super().__str__() + f" - [Có mạng - IP: {ip}]"
