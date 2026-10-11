# /***************************/
# Mã sinh viên: 202418900
# Họ tên: Nguyễn Đăng Hiếu
# /***************************/

from abc import ABC, abstractmethod


class INetworkable(ABC):
    """Interface biểu diễn năng lực kết nối mạng.

    Năng lực này độc lập với cây kế thừa Device: Computer và NetworkPrinter
    thuộc hai nhánh khác nhau nhưng cùng thực thi interface này.
    """

    @property
    @abstractmethod
    def ip_address(self):
        """Địa chỉ IP hiện tại ("" nếu chưa kết nối)."""

    @property
    @abstractmethod
    def is_connected(self):
        """True nếu thiết bị đang kết nối mạng."""

    @abstractmethod
    def connect(self, ip_address):
        """Kết nối mạng với địa chỉ IP cho trước."""

    @abstractmethod
    def disconnect(self):
        """Ngắt kết nối mạng."""


class NetworkConnection:
    """Thành phần kết nối mạng dùng chung (kết tập vào thiết bị).

    Gom logic kiểm tra kết nối vào một nơi để Computer và NetworkPrinter
    không phải viết lặp lại.
    """

    def __init__(self):
        self._ip_address = ""
        self._is_connected = False

    @property
    def ip_address(self):
        return self._ip_address

    @property
    def is_connected(self):
        return self._is_connected

    def connect(self, ip_address):
        """Kết nối mạng.

        Raises:
            ValueError: nếu IP rỗng.
            RuntimeError: nếu đang kết nối (không cho kết nối lại).
        """
        if ip_address is None or not str(ip_address).strip():
            raise ValueError("Địa chỉ IP không được rỗng.")
        if self._is_connected:
            raise RuntimeError(
                f"Thiết bị đang kết nối với IP {self._ip_address}, không thể kết nối lại.")
        self._ip_address = str(ip_address).strip()
        self._is_connected = True

    def disconnect(self):
        """Ngắt kết nối và xóa địa chỉ IP đang hoạt động."""
        self._ip_address = ""
        self._is_connected = False
