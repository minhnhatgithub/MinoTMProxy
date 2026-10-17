#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
 MinoTMProxy — Modern Cyber Traffic Inspector & Proxy Server
 Khởi động trực tiếp bằng Python, tự động cấu hình môi trường, thiết bị & giao diện.
=============================================================================
"""

import os
import sys
import time
import socket
import subprocess
import shutil
import webbrowser
import atexit
import signal

# 1. Dam bao ma hoa UTF-8 cho console Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Bat ho tro ANSI Escape Sequences tren Windows CMD
if os.name == "nt":
    os.system("")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_DIR = os.path.join(BASE_DIR, ".venv")
VENV_PYTHON = os.path.join(VENV_DIR, "Scripts", "python.exe") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python")

# 2. Tu dong chuyen vao moi truong ao (.venv) neu dang chay bang Python he thong
def ensure_venv():
    if os.path.exists(VENV_PYTHON):
        current_py = os.path.abspath(sys.executable).lower()
        target_py = os.path.abspath(VENV_PYTHON).lower()
        if current_py != target_py:
            try:
                ret = subprocess.call([VENV_PYTHON] + sys.argv)
                sys.exit(ret)
            except Exception as e:
                print(f"[!] Loi re-spawn venv: {e}")

ensure_venv()

# 3. Giai phong cong 8080 va 8081 neu co tien trinh cu treo
def free_ports(ports=(8080, 8081)):
    if os.name != "nt":
        return
    try:
        ps_cmd = (
            f"try {{ Get-NetTCPConnection -LocalPort {','.join(str(p) for p in ports)} -State Listen -ErrorAction SilentlyContinue "
            f"| ForEach-Object {{ Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }} }} catch {{}}; exit 0"
        )
        subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_cmd],
                       capture_output=True, timeout=5)
    except Exception:
        pass

# 4. Lay IP LAN
def get_lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

# 5. Quan ly ADB cho dien thoai Android
adb_connected_device = None

def check_and_setup_adb():
    global adb_connected_device
    if not shutil.which("adb"):
        return None
    try:
        res = subprocess.run(["adb", "devices"], capture_output=True, text=True, timeout=3)
        lines = [l.strip() for l in res.stdout.splitlines() if l.strip() and not l.startswith("List")]
        if lines:
            parts = lines[0].split()
            if len(parts) >= 2 and parts[1] == "device":
                dev = parts[0]
                adb_connected_device = dev
                # Reverse port qua cap USB va bat proxy
                subprocess.run(["adb", "reverse", "tcp:8080", "tcp:8080"], capture_output=True, timeout=3)
                subprocess.run(["adb", "shell", "settings", "put", "global", "http_proxy", "127.0.0.1:8080"], capture_output=True, timeout=3)
                return dev
    except Exception:
        pass
    return None

def cleanup_adb():
    global adb_connected_device
    if adb_connected_device and shutil.which("adb"):
        try:
            subprocess.run(["adb", "shell", "settings", "put", "global", "http_proxy", ":0"], capture_output=True, timeout=3)
            subprocess.run(["adb", "reverse", "--remove", "tcp:8080"], capture_output=True, timeout=3)
            print("\n[*] Đã tự động tắt proxy và khôi phục mạng bình thường cho điện thoại.")
        except Exception:
            pass

atexit.register(cleanup_adb)

def sig_handler(sig, frame):
    cleanup_adb()
    print("\n[✓] Đã dừng MinoTMProxy an toàn. Tạm biệt!")
    sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)
if hasattr(signal, "SIGTERM"):
    signal.signal(signal.SIGTERM, sig_handler)

# 6. Chay dong bo chung chi va ap dung theme
def setup_certs_and_theme():
    # sync certs
    sync_py = os.path.join(BASE_DIR, "scripts", "sync_certs.py")
    if os.path.exists(sync_py):
        subprocess.run([sys.executable, sync_py], capture_output=True)

    # apply theme
    theme_py = os.path.join(BASE_DIR, "custom_web", "apply_theme.py")
    if os.path.exists(theme_py):
        subprocess.run([sys.executable, theme_py], capture_output=True)

# 7. Ham Main khoi dong
def main():
    free_ports((8080, 8081))
    setup_certs_and_theme()

    lan_ip = get_lan_ip()
    adb_dev = check_and_setup_adb()

    # In banner cuc dep va ro rang
    cyan = "\033[96m"
    green = "\033[92m"
    yellow = "\033[93m"
    bold = "\033[1m"
    reset = "\033[0m"

    print(f"{cyan}{bold}======================================================================{reset}")
    print(f"{cyan}{bold}          MinoTMProxy — Modern Cyber Traffic Inspector (v12.2)        {reset}")
    print(f"          Bản Mod Cyber Dark & Light Theme Pro Siêu Đẹp               ")
    print(f"{cyan}{bold}======================================================================{reset}")
    print(f"  {green}[✓] GIAO DIỆN WEB UI :{reset} {bold}http://127.0.0.1:8081/?token=123{reset}")
    print(f"  {green}[✓] MẬT KHẨU WEB     :{reset} 123")
    print(f"  {green}[✓] PROXY LISTENER   :{reset} 0.0.0.0:8080 (IP LAN: {bold}{lan_ip}{reset})")
    print(f"{cyan}======================================================================{reset}")

    if adb_dev:
        print(f"  {green}{bold}[⚡] PHÁT HIỆN ĐIỆN THOẠI ANDROID QUA CÁP USB (ADB: {adb_dev})!{reset}")
        print(f"      -> {green}Đã TỰ ĐỘNG bật Reverse Port & Proxy (127.0.0.1:8080)!{reset}")
        print(f"      -> Mở App / Game / Web trên điện thoại là request sẽ hiện ngay!")
        print(f"      -> Khi tắt tool (Ctrl+C), mạng điện thoại sẽ tự phục hồi lại.")
    else:
        print(f"  {yellow}(*) Để bắt request từ ĐIỆN THOẠI (Android / iOS):{reset}")
        print(f"      - Cách 1: Vào Wi-Fi -> Sửa mạng -> Proxy Thủ công: {bold}{lan_ip}:8080{reset}")
        print(f"      - Cách 2: Cắm cáp USB bật 'Gỡ lỗi USB' rồi chạy {bold}python scripts/Bat-Proxy-Phone.py{reset}")

    print(f"\n  {yellow}(*) Để bắt request trên TRÌNH DUYỆT MÁY TÍNH (PC Chrome / Edge):{reset}")
    print(f"      -> Chạy lệnh: {bold}python scripts/Bat-Proxy-Windows.py{reset} (Để tắt: {bold}python scripts/Tat-Proxy-Windows.py{reset})")
    print(f"{cyan}{bold}======================================================================{reset}")
    print(f"  {bold}[LIVE REQUEST LOG]{reset} Nhật ký request thời gian thực (Bấm {bold}Ctrl+C{reset} để dừng):\n")

    # Tu dong mo Web UI
    try:
        webbrowser.open("http://127.0.0.1:8081/?token=123")
    except Exception:
        pass

    # Chạy mitmweb trực tiếp trong tiến trình chính
    logger_script = os.path.join(BASE_DIR, "scripts", "terminal_logger.py")
    mitm_args = [
        "--web-host", "127.0.0.1",
        "--web-port", "8081",
        "--listen-host", "0.0.0.0",
        "--listen-port", "8080",
        "--set", "block_global=false",
        "--set", "web_password=123",
        "--set", "termlog_verbosity=error",
    ]
    if os.path.exists(logger_script):
        mitm_args.extend(["-s", logger_script])

    try:
        from mitmproxy.tools.main import mitmweb
        mitmweb(mitm_args)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        cleanup_adb()

if __name__ == "__main__":
    main()
