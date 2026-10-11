# /***************************/
# Mã sinh viên: 202418900
# Họ tên: Nguyễn Đăng Hiếu
# /***************************/

from decimal import Decimal

from device import Device
from networkable import INetworkable, NetworkConnection


class Computer(Device, INetworkable):
    """Máy tính: kế thừa Device và luôn có khả năng kết nối mạng."""

    def __init__(self, device_id, name, year_in_use, purchase_price, status,
                 ram, processor, has_gpu):
        """Khởi tạo máy tính.

        Raises:
            ValueError: nếu dung lượng RAM <= 0.
        """
        super().__init__(device_id, name, year_in_use, purchase_price, status)
        if ram <= 0:
            raise ValueError("Dung lượng RAM phải lớn hơn 0.")
        self.ram = ram
        self.processor = processor
        self.has_gpu = has_gpu
        self._connection = NetworkConnection()

    def calculate_maintenance_cost(self):
        """5% giá mua; +2% nếu có GPU rời; +1% nếu dùng trên 5 năm."""
        cost = self.purchase_price * Decimal("0.05")
        if self.has_gpu:
            cost += self.purchase_price * Decimal("0.02")
        if self.age > self.MAINTENANCE_AGE_LIMIT:
            cost += self.purchase_price * Decimal("0.01")
        return cost

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
        gpu = "có GPU" if self.has_gpu else "không GPU"
        return (super().__str__() +
                f" - PC [RAM: {self.ram}GB, CPU: {self.processor}, {gpu}, IP: {ip}]")
