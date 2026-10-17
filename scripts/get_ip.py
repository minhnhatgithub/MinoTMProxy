#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinoTMProxy — LAN IP Resolver
Tu dong xac dinh chinh xac dia chi IP LAN cua may tinh de cau hinh Proxy cho dien thoai.
"""

import socket
import sys

def get_lan_ip():
    # 1. Thu ket noi UDP toi DNS cong cong de tim IP card mang chinh (khong thuc su gui goi tin)
    dns_targets = [('8.8.8.8', 80), ('1.1.1.1', 80), ('114.114.114.114', 80)]
    for host, port in dns_targets:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(0.5)
            s.connect((host, port))
            ip = s.getsockname()[0]
            s.close()
            if ip and not ip.startswith('127.') and not ip.startswith('169.254.'):
                return ip
        except Exception:
            pass

    # 2. Neu mang offline khong co internet, duyet toan bo card mang tren he thong
    try:
        hostname = socket.gethostname()
        candidates = []
        for info in socket.getaddrinfo(hostname, None):
            ip = info[4][0]
            if ':' in ip or ip.startswith('127.') or ip.startswith('169.254.'):
                continue
            candidates.append(ip)

        # Uu tien card mang that: loai bo cac dai IP thuong thay cua may ao (VMware/VirtualBox)
        filtered = [
            ip for ip in candidates
            if not any(ip.startswith(prefix) for prefix in ['192.168.32.', '192.168.61.', '192.168.56.'])
        ]
        if filtered:
            return filtered[0]
        if candidates:
            return candidates[0]
        return socket.gethostbyname(hostname)
    except Exception:
        return '127.0.0.1'

if __name__ == '__main__':
    ip = get_lan_ip()
    if '--port' in sys.argv:
        print(f"{ip}:8080")
    else:
        print(ip)
