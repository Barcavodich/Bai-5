# /***************************/
# Mã sinh viên: 202418900
# Họ tên: Nguyễn Đăng Hiếu
# /***************************/

from abc import ABC, abstractmethod
from datetime import datetime
from decimal import Decimal
from enum import Enum


class DeviceStatus(Enum):
    """Trạng thái hoạt động của thiết bị."""
    ACTIVE = "Active"
    UNDER_MAINTENANCE = "UnderMaintenance"
    RETIRED = "Retired"


def format_vnd(amount):
    """Định dạng số tiền theo kiểu 1,234,567 VND."""
    return f"{amount:,.0f} VND"


class Device(ABC):
    """Lớp trừu tượng chứa thông tin chung của mọi thiết bị.

    Không thể tạo trực tiếp đối tượng Device, vì mỗi loại thiết bị
    có cách tính chi phí bảo trì riêng.
    """

    # Số năm sử dụng tối đa trước khi thiết bị bị coi là cũ
    MAINTENANCE_AGE_LIMIT = 5

    def __init__(self, device_id, name, year_in_use, purchase_price, status):
        """Khởi tạo và kiểm tra tính hợp lệ của dữ liệu chung.

        Raises:
            ValueError: nếu mã rỗng, giá <= 0 hoặc năm lớn hơn năm hiện tại.
        """
        if device_id is None or not str(device_id).strip():
            raise ValueError("Mã thiết bị không được rỗng.")

        price = Decimal(str(purchase_price))
        if price <= 0:
            raise ValueError("Giá mua phải lớn hơn 0.")

        if year_in_use > datetime.now().year:
            raise ValueError("Năm đưa vào sử dụng không được lớn hơn năm hiện tại.")

        if not isinstance(status, DeviceStatus):
            raise ValueError("Trạng thái phải là một giá trị của DeviceStatus.")

        self._device_id = str(device_id).strip()
        self.name = name
        self.year_in_use = year_in_use
        self.purchase_price = price
        self.status = status

    @property
    def device_id(self):
        """Mã thiết bị: chỉ đọc, chỉ được gán khi khởi tạo."""
        return self._device_id

    @property
    def age(self):
        """Số năm đã sử dụng tính đến năm hiện tại."""
        return datetime.now().year - self.year_in_use

    @abstractmethod
    def calculate_maintenance_cost(self):
        """Tính chi phí bảo trì dự kiến trong một năm (trả về Decimal)."""

    def __str__(self):
        """Biểu diễn thông tin chung của thiết bị dưới dạng chuỗi."""
        return (f"[{self.device_id}] {self.name} - Năm: {self.year_in_use} "
                f"- Giá: {format_vnd(self.purchase_price)} "
                f"- Trạng thái: {self.status.value}")
