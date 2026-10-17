#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinoTMProxy — Tắt Proxy Hệ thống Windows (PC)
"""

import sys
import ctypes

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def disable_windows_proxy():
    import winreg
    reg_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 0)

        try:
            wininet = ctypes.windll.Wininet
            wininet.InternetSetOptionW(0, 39, 0, 0) # INTERNET_OPTION_SETTINGS_CHANGED
            wininet.InternetSetOptionW(0, 37, 0, 0) # INTERNET_OPTION_REFRESH
        except Exception:
            pass

        print("========================================================")
        print(" [✓] ĐÃ TẮT PROXY WINDOWS THÀNH CÔNG!")
        print(" Máy tính bây giờ kết nối mạng trực tiếp bình thường.")
        print("========================================================")
        return True
    except Exception as e:
        print(f"[X] Lỗi khi tắt Proxy Windows: {e}")
        return False

if __name__ == "__main__":
    disable_windows_proxy()
    input("\nNhấn Enter để thoát...")
