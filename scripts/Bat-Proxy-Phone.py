#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinoTMProxy — Bật Proxy & Reverse Port cho Điện thoại Android qua ADB
"""

import sys
import subprocess
import shutil

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def enable_phone_proxy():
    if not shutil.which("adb"):
        print("[!] Không tìm thấy lệnh 'adb' trong hệ thống.")
        print("Vui lòng cài ADB hoặc kết nối qua Wi-Fi thủ công.")
        return False

    res = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    lines = [l.strip() for l in res.stdout.splitlines() if l.strip() and not l.startswith("List")]
    if not lines:
        print("[!] Không tìm thấy thiết bị Android nào đang kết nối qua cáp USB.")
        print("Vui lòng cắm cáp USB và bật chế độ 'Gỡ lỗi USB' (USB Debugging).")
        return False

    dev = lines[0].split()[0]
    print(f"[*] Đang thiết lập Reverse Port qua cáp USB cho thiết bị ({dev})...")
    subprocess.run(["adb", "reverse", "tcp:8080", "tcp:8080"], capture_output=True)

    print("[*] Đang bật Global HTTP Proxy trên điện thoại (127.0.0.1:8080)...")
    subprocess.run(["adb", "shell", "settings", "put", "global", "http_proxy", "127.0.0.1:8080"], capture_output=True)

    print("\n========================================================")
    print(f" [✓] ĐÃ BẬT PROXY THÀNH CÔNG CHO ĐIỆN THOẠI ({dev})!")
    print(" Toàn bộ request (App, Game, Web) bây giờ sẽ đi qua MinoTMProxy.")
    print(" (*) Để tắt: Chạy file scripts/Tat-Proxy-Phone.py")
    print("========================================================")
    return True

if __name__ == "__main__":
    enable_phone_proxy()
    input("\nNhấn Enter để thoát...")
