# /***************************/
# Mã sinh viên: 202418900
# Họ tên: Nguyễn Đăng Hiếu
# /***************************/

from decimal import Decimal

from device import Device


class Projector(Device):
    """Máy chiếu (phiên bản hiện tại không có khả năng kết nối mạng)."""

    def __init__(self, device_id, name, year_in_use, purchase_price, status,
                 brightness, bulb_hours):
        """Khởi tạo máy chiếu.

        Raises:
            ValueError: nếu độ sáng <= 0 hoặc số giờ bóng đèn < 0.
        """
        super().__init__(device_id, name, year_in_use, purchase_price, status)
        if brightness <= 0:
            raise ValueError("Độ sáng (lumen) phải lớn hơn 0.")
        if bulb_hours < 0:
            raise ValueError("Số giờ sử dụng bóng đèn không được âm.")
        self.brightness = brightness
        self.bulb_hours = bulb_hours

    def calculate_maintenance_cost(self):
        """3% giá mua; +1.500.000 nếu bóng đèn đã dùng trên 3.000 giờ."""
        cost = self.purchase_price * Decimal("0.03")
        if self.bulb_hours > 3000:
            cost += Decimal(1500000)
        return cost

    def __str__(self):
        return (super().__str__() +
                f" - Máy chiếu [Sáng: {self.brightness} lumen, Bóng đèn: {self.bulb_hours}h]")
