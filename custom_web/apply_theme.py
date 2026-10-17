#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinoTMProxy — Theme Applicator
Tu dong ap dung giao dien Dark Pro vao thu muc cai dat mitmproxy hien tai.
"""

import os
import shutil
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def apply_theme():
    try:
        import mitmproxy
    except ImportError:
        print("[!] mitmproxy chua duoc cai dat. Dang bo qua buoc cai giao dien...")
        return False

    base_dir = os.path.dirname(os.path.abspath(__file__))
    mitm_dir = os.path.dirname(mitmproxy.__file__)
    web_static = os.path.join(mitm_dir, "tools", "web", "static")
    web_html = os.path.join(mitm_dir, "tools", "web", "index.html")

    if not os.path.exists(web_static):
        print(f"[!] Khong tim thay thu muc mitmweb tai: {web_static}")
        return False

    css_src = os.path.join(base_dir, "modern-pro.css")
    html_src = os.path.join(base_dir, "index.html")

    if not os.path.exists(css_src) or not os.path.exists(html_src):
        print("[!] Thieu tep tin giao dien modern-pro.css hoac index.html trong custom_web/")
        return False

    css_dst = os.path.join(web_static, "modern-pro.css")
    shutil.copy2(css_src, css_dst)
    shutil.copy2(html_src, web_html)

    print(f"[OK] Da ap dung giao dien Dark Pro thanh cong vao: {mitm_dir}")
    return True

if __name__ == "__main__":
    apply_theme()
