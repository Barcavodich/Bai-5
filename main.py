# /***************************/
# Mã sinh viên: 202418900
# Họ tên: Nguyễn Đăng Hiếu
# /***************************/

from device import Computer, Printer, NetworkPrinter, Projector, DeviceStatus, INetworkable
from lab_room import LabRoom

def main():
    room1 = LabRoom("LAB01", "Phong thuc hanh may tinh 1", 30)
    room2 = LabRoom("LAB02", "Phong in an", 10)

    # Tao data test
    pc1 = Computer("PC01", "Dell XPS", 2017, 15000000, DeviceStatus.ACTIVE, 16, "i5", False)
    pc2 = Computer("PC02", "Asus ROG", 2024, 30000000, DeviceStatus.ACTIVE, 32, "i7", True)
    
    pr1 = Printer("PR01", "Canon LBP", 2020, 4000000, DeviceStatus.UNDER_MAINTENANCE, "Laser", 120000, False)
    pr2 = NetworkPrinter("PR02", "HP Color", 2022, 6000000, DeviceStatus.ACTIVE, "Phun", 5000, True)

    pj1 = Projector("PJ01", "Sony", 2019, 10000000, DeviceStatus.ACTIVE, 3000, 3500)

    # Them vao phong
    room1.add_device(pc1)
    room1.add_device(pc2)
    room1.add_device(pj1)
    room2.add_device(pr1)
    room2.add_device(pr2)

    # Thu them trung ma
    room1.add_device(pc1)

    # In ra man hinh
    room1.print_all_devices()
    room2.print_all_devices()

    # Tinh tien
    print(f"\nTong phi bao tri {room1.name}: {room1.get_total_maintenance_cost()} VND")
    print(f"Tong phi bao tri {room2.name}: {room2.get_total_maintenance_cost()} VND")

    # Loc thiet bi hu hong hoac cu
    print("\n--- Danh sach can bao tri ---")
    all_maintain = room1.get_devices_to_maintain() + room2.get_devices_to_maintain()
    for d in all_maintain:
        print(d.show_info())

    # Test ket noi mang
    print("\n--- Test ket noi mang interface ---")
    all_devices = room1.devices + room2.devices
    for d in all_devices:
        if isinstance(d, INetworkable):
            d.connect(f"192.168.1.10{d.id[-1]}")
            print(f"Da ket noi {d.name} qua IP: {d.ip_address}")

if __name__ == "__main__":
    main()