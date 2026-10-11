# /***************************/
# Mã sinh viên: 202418900
# Họ tên: Nguyễn Đăng Hiếu
# /***************************/

from decimal import Decimal

from device import Device, DeviceStatus


class LabRoom:
    """Phòng thực hành, chứa nhiều thiết bị (quan hệ kết tập).

    Thiết bị tồn tại độc lập với phòng: bỏ thiết bị khỏi phòng hoặc xóa phòng
    thì đối tượng thiết bị vẫn còn.
    """

    def __init__(self, room_id, name, capacity):
        """Khởi tạo phòng.

        Raises:
            ValueError: nếu mã phòng rỗng hoặc sức chứa <= 0.
        """
        if room_id is None or not str(room_id).strip():
            raise ValueError("Mã phòng không được rỗng.")
        if capacity <= 0:
            raise ValueError("Sức chứa phải lớn hơn 0.")
        self.room_id = room_id
        self.name = name
        self.capacity = capacity
        self._devices = []

    @property
    def devices(self):
        """Bản sao danh sách thiết bị (tránh sửa trực tiếp từ bên ngoài)."""
        return list(self._devices)

    def add_device(self, device):
        """Thêm thiết bị vào phòng.

        Raises:
            ValueError: nếu thiết bị là None, trùng mã hoặc phòng đã đầy.
        """
        if device is None:
            raise ValueError("Không chấp nhận thiết bị null.")
        if not isinstance(device, Device):
            raise ValueError("Đối tượng thêm vào phải là Device.")
        if self.find_device(device.device_id) is not None:
            raise ValueError(f"Thiết bị mã {device.device_id} đã tồn tại trong phòng.")
        if len(self._devices) >= self.capacity:
            raise ValueError(f"Phòng {self.name} đã đầy (sức chứa {self.capacity}).")
        self._devices.append(device)

    def remove_device(self, device_id):
        """Xóa thiết bị theo mã. Trả về True nếu xóa được, False nếu không tìm thấy."""
        device = self.find_device(device_id)
        if device is None:
            return False
        self._devices.remove(device)
        return True

    def find_device(self, device_id):
        """Tìm thiết bị theo mã. Trả về None nếu không có."""
        for d in self._devices:
            if d.device_id == device_id:
                return d
        return None

    def calculate_annual_maintenance_cost(self):
        """Tổng chi phí bảo trì một năm của cả phòng.

        Dùng đa hình: gọi calculate_maintenance_cost() trên từng Device,
        không kiểm tra loại thiết bị bằng if/switch.
        """
        return sum((d.calculate_maintenance_cost() for d in self._devices), Decimal(0))

    def get_devices_requiring_maintenance(self):
        """Thiết bị đang UnderMaintenance hoặc đã dùng trên 5 năm."""
        return [d for d in self._devices
                if d.status == DeviceStatus.UNDER_MAINTENANCE
                or d.age > Device.MAINTENANCE_AGE_LIMIT]

    def print_all_devices(self):
        """In danh sách thiết bị trong phòng."""
        print(f"\n--- Phòng {self.room_id}: {self.name} "
              f"({len(self._devices)}/{self.capacity}) ---")
        for d in self._devices:
            print(d)
