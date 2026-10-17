#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinoTMProxy — Bật Proxy Hệ thống Windows (PC)
"""

import sys
import ctypes

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def enable_windows_proxy(server="127.0.0.1:8080"):
    import winreg
    reg_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, server)
            winreg.SetValueEx(key, "ProxyOverride", 0, winreg.REG_SZ, "<local>")

        # Lam moi he thong de trinh duyet nhan ngay lap tuc
        try:
            wininet = ctypes.windll.Wininet
            wininet.InternetSetOptionW(0, 39, 0, 0) # INTERNET_OPTION_SETTINGS_CHANGED
            wininet.InternetSetOptionW(0, 37, 0, 0) # INTERNET_OPTION_REFRESH
        except Exception:
            pass

        print("========================================================")
        print(" [✓] ĐÃ BẬT PROXY WINDOWS THÀNH CÔNG (127.0.0.1:8080)!")
        print(" Trình duyệt (Chrome, Edge...) trên máy tính bây giờ sẽ")
        print(" đi qua MinoTMProxy để bắt request.")
        print("========================================================")
        return True
    except Exception as e:
        print(f"[X] Lỗi khi bật Proxy Windows: {e}")
        return False

if __name__ == "__main__":
    enable_windows_proxy()
    input("\nNhấn Enter để thoát...")
