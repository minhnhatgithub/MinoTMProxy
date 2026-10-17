#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinoTMProxy — Terminal Live Request Logger
In log request/response ro rang, truc quan va dep mat ngay tren console CMD.
"""

import sys
from datetime import datetime

class TerminalLogger:
    def response(self, flow):
        try:
            time_str = datetime.now().strftime("%H:%M:%S")
            method = flow.request.method.ljust(6)
            status = str(flow.response.status_code if flow.response else "---")
            
            content_len = len(flow.response.content) if (flow.response and flow.response.content) else 0
            if content_len > 1024 * 1024:
                size_str = f"{content_len / (1024*1024):.1f}MB"
            elif content_len > 1024:
                size_str = f"{content_len / 1024:.1f}KB"
            else:
                size_str = f"{content_len}B"
            size_str = size_str.rjust(7)

            url = flow.request.pretty_url
            if len(url) > 95:
                url = url[:92] + "..."

            flag = "[OK]  " if (flow.response and flow.response.status_code < 400) else "[WARN]"
            line = f"[{time_str}] {flag} {method} {status.ljust(3)} ({size_str}) -> {url}\n"
            sys.__stdout__.write(line)
            sys.__stdout__.flush()
        except Exception:
            pass

    def error(self, flow):
        try:
            time_str = datetime.now().strftime("%H:%M:%S")
            method = flow.request.method.ljust(6)
            err = flow.error.msg if flow.error else "Loi ket noi"
            url = flow.request.pretty_url
            if len(url) > 85:
                url = url[:82] + "..."
            line = f"[{time_str}] [ERR]  {method} FAIL         -> {url} | {err}\n"
            sys.__stdout__.write(line)
            sys.__stdout__.flush()
        except Exception:
            pass

addons = [TerminalLogger()]
