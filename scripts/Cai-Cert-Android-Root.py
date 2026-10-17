#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinoTMProxy — Cài đặt Chứng chỉ CA vào Android Root System (/system/etc/security/cacerts)
Yêu cầu: Điện thoại Android đã ROOT (Magisk / KernelSU / APatch).
"""

import sys
import os

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

if __name__ == "__main__":
    from sync_certs import sync_certs, push_to_android
    hash_fn = sync_certs()
    if hash_fn:
        push_to_android(hash_fn)
    else:
        print("[X] Không thể lấy chứng chỉ mitmproxy.")
    input("\nNhấn Enter để thoát...")
