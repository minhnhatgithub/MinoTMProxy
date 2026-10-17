#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MinoTMProxy — Certificate Synchronizer & Android Root Installer
Tu dong dong bo chung chi SSL CA rieng cua may tinh vao thu muc certificates/
va ho tro day truc tiep vao thu vien Root CA cua he thong Android (/system).
"""

import os
import sys
import shutil
import hashlib
import subprocess

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def get_mitm_dir():
    return os.path.expanduser(os.path.join("~", ".mitmproxy"))

def ensure_mitm_certs():
    mitm_dir = get_mitm_dir()
    os.makedirs(mitm_dir, exist_ok=True)
    pem_path = os.path.join(mitm_dir, "mitmproxy-ca-cert.pem")

    if not os.path.exists(pem_path):
        try:
            from mitmproxy.certs import CertStore
            CertStore.from_store(mitm_dir, "mitmproxy", 2048)
            print("[+] Da khoi tao cap chung chi CA moi cho may tinh nay.")
        except Exception as e:
            print(f"[!] Chua the tao truoc chung chi ({e}), se doi mitmproxy tu tao khi khoi dong.")
    return mitm_dir

def compute_android_hash(pem_path):
    try:
        from cryptography import x509
        cert_data = open(pem_path, "rb").read()
        cert = x509.load_pem_x509_certificate(cert_data)
        der_subject = cert.subject.public_bytes()
        md5_digest = hashlib.md5(der_subject).digest()
        hash_val = (
            md5_digest[0]
            | (md5_digest[1] << 8)
            | (md5_digest[2] << 16)
            | (md5_digest[3] << 24)
        )
        return f"{hash_val:08x}"
    except Exception as e:
        return "c8750f0d"

def sync_certs():
    mitm_dir = ensure_mitm_certs()
    pem_src = os.path.join(mitm_dir, "mitmproxy-ca-cert.pem")
    cer_src = os.path.join(mitm_dir, "mitmproxy-ca-cert.cer")

    if not os.path.exists(pem_src):
        return None

    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    cert_dir = os.path.join(root_dir, "certificates")
    os.makedirs(cert_dir, exist_ok=True)

    android_hash = compute_android_hash(pem_src)
    hash_filename = f"{android_hash}.0"
    hash_dst = os.path.join(cert_dir, hash_filename)

    shutil.copy2(pem_src, hash_dst)
    shutil.copy2(pem_src, os.path.join(cert_dir, "mitmproxy-ca-cert.pem"))
    if os.path.exists(cer_src):
        shutil.copy2(cer_src, os.path.join(cert_dir, "mitmproxy-ca-cert.cer"))

    print(f"[✓] Da dong bo chung chi CA cua may vao: certificates/{hash_filename}")
    return hash_filename

def push_to_android(hash_filename):
    print("[*] Dang kiem tra ket noi ADB toi dien thoai...")
    try:
        dev_res = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        lines = [line.strip() for line in dev_res.stdout.splitlines() if line.strip() and not line.startswith("List")]
        if not lines:
            print("[X] LOI: Khong tim thay thiet bi Android nao ket noi qua ADB!")
            print("    Vui long cam cap USB va bat che do 'Go loi USB' (USB Debugging).")
            return False
    except FileNotFoundError:
        print("[X] LOI: May tinh chua cai dat hoac chua them lenh 'adb' vao PATH!")
        return False

    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    cert_path = os.path.join(root_dir, "certificates", hash_filename)
    if not os.path.exists(cert_path):
        print(f"[X] Khong tim thay tep chung chi: {cert_path}")
        return False

    tmp_path = f"/data/local/tmp/{hash_filename}"
    sys_path = f"/system/etc/security/cacerts/{hash_filename}"

    print(f"[*] Dang day chung chi {hash_filename} vao {tmp_path}...")
    push_res = subprocess.run(["adb", "push", cert_path, tmp_path], capture_output=True, text=True)
    if push_res.returncode != 0:
        print(f"[X] Day file that bai: {push_res.stderr}")
        return False

    print("[*] Dang yeu cau quyen Root va cai dat vao /system/etc/security/cacerts/...")
    cmd = (
        f"su -c '"
        f"mount -o remount,rw / 2>/dev/null || mount -o remount,rw /system 2>/dev/null; "
        f"cp {tmp_path} {sys_path}; "
        f"chmod 644 {sys_path}; "
        f"chown root:root {sys_path}"
        f"'"
    )
    res = subprocess.run(["adb", "shell", cmd], capture_output=True, text=True)

    check_res = subprocess.run(
        ["adb", "shell", f"ls -l {sys_path} 2>/dev/null"], capture_output=True, text=True
    )
    if hash_filename in check_res.stdout:
        print("[✓] CAI DAT CHUNG CHI HE THONG (ROOT CA) THANH CONG!")
        print(f"    Chi tiet: {check_res.stdout.strip()}")
        print("    Bay gio anh co the bat toan bo request HTTPS cua app tren dien thoai.")
        return True
    else:
        print("[!] Canh bao: Khong the ghi vao /system. Vui long kiem tra quyen Root (Magisk/KernelSU).")
        return False

if __name__ == "__main__":
    hash_fn = sync_certs()
    if "--push-adb" in sys.argv:
        if hash_fn:
            push_to_android(hash_fn)
        else:
            print("[X] Khong the lay chung chi mitmproxy.")
