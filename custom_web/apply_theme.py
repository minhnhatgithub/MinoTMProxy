#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinoTMProxy — Theme & UI Applicator
"""

import os
import shutil
import sys
import re

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def apply_theme():
    try:
        import mitmproxy
    except ImportError:
        print("[!] mitmproxy chua duoc cai dat.")
        return False

    base_dir = os.path.dirname(os.path.abspath(__file__))
    mitm_dir = os.path.dirname(mitmproxy.__file__)
    web_dir = os.path.join(mitm_dir, "tools", "web")
    web_static = os.path.join(web_dir, "static")
    web_html = os.path.join(web_dir, "index.html")
    app_py = os.path.join(web_dir, "app.py")

    if not os.path.exists(web_static):
        print(f"[!] Khong tim thay thu muc mitmweb tai: {web_static}")
        return False

    # Copy modern-pro.css
    css_src = os.path.join(base_dir, "modern-pro.css")
    if os.path.exists(css_src):
        shutil.copy2(css_src, os.path.join(web_static, "modern-pro.css"))

    # Copy theme.js
    js_src = os.path.join(base_dir, "theme.js")
    if os.path.exists(js_src):
        shutil.copy2(js_src, os.path.join(web_static, "theme.js"))

    # Copy index.html
    html_src = os.path.join(base_dir, "index.html")
    if os.path.exists(html_src):
        shutil.copy2(html_src, web_html)

    # Patch CSP in app.py to allow fonts and inline styles
    if os.path.exists(app_py):
        with open(app_py, "r", encoding="utf-8") as f:
            code = f.read()

        old_csp_pattern = re.compile(
            r'self\.add_header\(\s*"Content-Security-Policy",\s*".*?"\s*\)',
            re.DOTALL
        )
        new_csp = (
            'self.add_header(\n'
            '            "Content-Security-Policy",\n'
            '            "default-src \'self\'; "\n'
            '            "script-src \'self\' \'unsafe-inline\' \'unsafe-eval\'; "\n'
            '            "connect-src \'self\' ws:; "\n'
            '            "img-src \'self\' data: https:; "\n'
            '            "style-src   \'self\' \'unsafe-inline\' https:; "\n'
            '            "font-src    \'self\' data: https:;",\n'
            '        )'
        )
        if old_csp_pattern.search(code):
            code = old_csp_pattern.sub(new_csp, code)
            with open(app_py, "w", encoding="utf-8") as f:
                f.write(code)
            print("[OK] Cap nhat Content-Security-Policy trong app.py thanh cong.")

    print(f"[OK] Da ap dung giao dien Cyber & Light Mode thanh cong vao: {mitm_dir}")
    return True

if __name__ == "__main__":
    apply_theme()
