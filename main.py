# /***************************/
# Mã sinh viên: 202418900
# Họ tên: Nguyễn Đăng Hiếu
# /***************************/

from computer import Computer
from device import DeviceStatus, format_vnd
from lab_room import LabRoom
from networkable import INetworkable
from printer import NetworkPrinter, Printer, PrinterType
from projector import Projector


def section(title):
    """In tiêu đề cho từng bước test."""
    print(f"\n===== {title} =====")


def main():
    room1 = LabRoom("LAB01", "Phòng thực hành máy tính 1", 30)
    room2 = LabRoom("LAB02", "Phòng in ấn", 10)

    # Dữ liệu test: 2 máy tính (1 có GPU), 2 máy in (1 máy > 100.000 trang), 1 máy chiếu > 3.000h
    pc1 = Computer("PC01", "Dell XPS", 2017, 15000000, DeviceStatus.ACTIVE, 16, "i5", False)
    pc2 = Computer("PC02", "Asus ROG", 2024, 30000000, DeviceStatus.ACTIVE, 32, "i7", True)
    pr1 = Printer("PR01", "Canon LBP", 2020, 4000000, DeviceStatus.UNDER_MAINTENANCE,
                  PrinterType.LASER, 120000, False)
    pr2 = NetworkPrinter("PR02", "HP Color", 2022, 6000000, DeviceStatus.ACTIVE,
                         PrinterType.INKJET, 5000, True)
    pj1 = Projector("PJ01", "Sony", 2019, 10000000, DeviceStatus.ACTIVE, 3000, 3500)

    section("1. Thêm thiết bị vào phòng")
    for room, devices in ((room1, [pc1, pc2, pj1]), (room2, [pr1, pr2])):
        for d in devices:
            room.add_device(d)
            print(f"Đã thêm {d.device_id} vào {room.room_id}")

    section("2. Thử thêm thiết bị trùng mã")
    try:
        room1.add_device(pc1)
    except ValueError as e:
        print(f"Lỗi: {e}")

    section("2b. Thử thêm null và tạo thiết bị sai dữ liệu")
    for action, call in (
        ("Thêm None", lambda: room1.add_device(None)),
        ("Mã rỗng", lambda: Computer("", "X", 2020, 1000, DeviceStatus.ACTIVE, 8, "i3", False)),
        ("Giá <= 0", lambda: Projector("PJ99", "X", 2020, 0, DeviceStatus.ACTIVE, 1000, 10)),
        ("Năm ở tương lai", lambda: Projector("PJ98", "X", 2999, 1000, DeviceStatus.ACTIVE, 1000, 10)),
    ):
        try:
            call()
        except ValueError as e:
            print(f"{action}: Lỗi: {e}")

    section("3. Danh sách thiết bị từng phòng")
    room1.print_all_devices()
    room2.print_all_devices()

    section("4. Tổng chi phí bảo trì dự kiến")
    for room in (room1, room2):
        print(f"{room.name}: {format_vnd(room.calculate_annual_maintenance_cost())}")

    section("5. Thiết bị cần bảo trì")
    for room in (room1, room2):
        for d in room.get_devices_requiring_maintenance():
            print(f"[{room.room_id}] {d}")

    section("6 + 7. Kết nối mạng qua kiểu INetworkable")
    all_devices = room1.devices + room2.devices
    network_devices = [d for d in all_devices if isinstance(d, INetworkable)]
    for i, d in enumerate(network_devices, start=1):
        d.connect(f"192.168.1.{10 + i}")
        print(f"Đã kết nối {d.name} - IP: {d.ip_address} - is_connected: {d.is_connected}")

    section("Điều kiện kết nối")
    device = network_devices[0]
    for action, call in (
        ("IP rỗng", lambda: device.connect("")),
        ("Kết nối lại khi đang kết nối", lambda: device.connect("10.0.0.1")),
    ):
        try:
            call()
        except (ValueError, RuntimeError) as e:
            print(f"{action}: Lỗi: {e}")
    device.disconnect()
    print(f"Sau khi ngắt: is_connected = {device.is_connected}, ip = '{device.ip_address}'")

    section("Tìm và xóa thiết bị")
    print(f"find_device('PC01') -> {room1.find_device('PC01').name}")
    print(f"remove_device('PC01') -> {room1.remove_device('PC01')}")
    print(f"remove_device('PC01') lần 2 -> {room1.remove_device('PC01')}")
    print(f"pc1 vẫn tồn tại sau khi rời phòng: {pc1.name}")


if __name__ == "__main__":
    main()
