# /***************************/
# Mã sinh viên: 202418900
# Họ tên: Nguyễn Đăng Hiếu
# /***************************/

from enum import Enum
from abc import ABC, abstractmethod
from datetime import datetime

class DeviceStatus(Enum):
    ACTIVE = "Active"
    UNDER_MAINTENANCE = "UnderMaintenance"
    RETIRED = "Retired"

class INetworkable(ABC):
    @abstractmethod
    def connect(self, ip_address):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass

class Device(ABC):
    def __init__(self, id, name, year_in_use, purchase_price, status):
        self.id = id
        self.name = name
        self.year_in_use = year_in_use
        self.purchase_price = purchase_price
        self.status = status

    @abstractmethod
    def calculate_maintenance_cost(self):
        pass

    def show_info(self):
        return f"[{self.id}] {self.name} - Năm: {self.year_in_use} - Trạng thái: {self.status.value}"