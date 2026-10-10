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

class Computer(Device, INetworkable):
    def __init__(self, id, name, year_in_use, purchase_price, status, ram, processor, has_gpu):
        super().__init__(id, name, year_in_use, purchase_price, status)
        self.ram = ram
        self.processor = processor
        self.has_gpu = has_gpu
        self.ip_address = ""
        self.is_connected = False

    def calculate_maintenance_cost(self):
        cost = self.purchase_price * 0.05
        if self.has_gpu:
            cost += self.purchase_price * 0.02
        if datetime.now().year - self.year_in_use > 5:
            cost += self.purchase_price * 0.01
        return cost

    def connect(self, ip_address):
        self.ip_address = ip_address
        self.is_connected = True

    def disconnect(self):
        self.ip_address = ""
        self.is_connected = False

    def show_info(self):
        ip = self.ip_address if self.is_connected else "Chua ket noi"
        return super().show_info() + f" - PC [RAM: {self.ram}GB, IP: {ip}]"

class Printer(Device):
    def __init__(self, id, name, year_in_use, purchase_price, status, type_printer, pages, is_color):
        super().__init__(id, name, year_in_use, purchase_price, status)
        self.type_printer = type_printer
        self.pages = pages
        self.is_color = is_color

    def calculate_maintenance_cost(self):
        cost = self.purchase_price * 0.04
        if self.pages > 100000:
            cost += 500000
        if self.is_color:
            cost += 300000
        return cost

    def show_info(self):
        return super().show_info() + f" - May in [{self.type_printer}, So trang: {self.pages}]"

class NetworkPrinter(Printer, INetworkable):
    def __init__(self, id, name, year_in_use, purchase_price, status, type_printer, pages, is_color):
        super().__init__(id, name, year_in_use, purchase_price, status, type_printer, pages, is_color)
        self.ip_address = ""
        self.is_connected = False

    def connect(self, ip_address):
        self.ip_address = ip_address
        self.is_connected = True

    def disconnect(self):
        self.ip_address = ""
        self.is_connected = False
        
    def show_info(self):
        ip = self.ip_address if self.is_connected else "Chua ket noi"
        return super().show_info() + f" - [Co mang - IP: {ip}]"

class Projector(Device):
    def __init__(self, id, name, year_in_use, purchase_price, status, brightness, bulb_hours):
        super().__init__(id, name, year_in_use, purchase_price, status)
        self.brightness = brightness
        self.bulb_hours = bulb_hours

    def calculate_maintenance_cost(self):
        cost = self.purchase_price * 0.03
        if self.bulb_hours > 3000:
            cost += 1500000
        return cost

    def show_info(self):
        return super().show_info() + f" - May chieu [Sang: {self.brightness}, Bong: {self.bulb_hours}h]"