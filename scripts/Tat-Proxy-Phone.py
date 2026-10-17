#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinoTMProxy — Tắt Proxy cho Điện thoại Android qua ADB
"""

import sys
import subprocess
import shutil

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def disable_phone_proxy():
    if not shutil.which("adb"):
        print("[!] Không tìm thấy lệnh 'adb'.")
        return False

    print("[*] Đang gửi lệnh tắt Proxy trên điện thoại...")
    subprocess.run(["adb", "shell", "settings", "put", "global", "http_proxy", ":0"], capture_output=True)
    subprocess.run(["adb", "reverse", "--remove", "tcp:8080"], capture_output=True)

    print("\n========================================================")
    print(" [✓] ĐÃ TẮT PROXY TRÊN ĐIỆN THOẠI THÀNH CÔNG!")
    print(" Điện thoại bây giờ kết nối mạng bình thường trực tiếp.")
    print("========================================================")
    return True

if __name__ == "__main__":
    disable_phone_proxy()
    input("\nNhấn Enter để thoát...")
