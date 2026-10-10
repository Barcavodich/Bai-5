# /***************************/
# Mã sinh viên: 202418900
# Họ tên: Nguyễn Đăng Hiếu
# /***************************/

from datetime import datetime
from device import DeviceStatus

class LabRoom:
    def __init__(self, room_id, name, capacity):
        self.room_id = room_id
        self.name = name
        self.capacity = capacity
        self.devices = []

    def add_device(self, device):
        # Kiem tra trung ma thu cong
        for d in self.devices:
            if d.id == device.id:
                print(f"Loi: Thiet bi ma {device.id} da ton tai!")
                return
        self.devices.append(device)

    def get_total_maintenance_cost(self):
        total = 0
        for d in self.devices:
            total += d.calculate_maintenance_cost()
        return total

    def get_devices_to_maintain(self):
        current_year = datetime.now().year
        need_maintain = []
        for d in self.devices:
            if d.status == DeviceStatus.UNDER_MAINTENANCE or (current_year - d.year_in_use) > 5:
                need_maintain.append(d)
        return need_maintain

    def print_all_devices(self):
        print(f"\n--- Phong: {self.name} ---")
        for d in self.devices:
            print(d.show_info())