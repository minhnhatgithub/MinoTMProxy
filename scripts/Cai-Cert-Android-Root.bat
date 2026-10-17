@echo off
chcp 65001 >nul
title Cai Dat Chung Chi Vao He Thong Android (Root) - MinoTMProxy
cd /d "%~dp0\.."

echo ========================================================
echo   CAI DAT CHUNG CHI CA VAO HE THONG ANDROID (/system)
echo   Yeu cau: Dien thoai da ROOT (Magisk / KernelSU / APatch)
echo ========================================================
echo.

where adb >nul 2>nul
if %errorlevel% neq 0 (
    echo [X] Khong tim thay ADB trong may tinh!
    pause
    exit /b 1
)

set CERT_FILE=certificates\c8750f0d.0
if not exist "%CERT_FILE%" (
    echo [X] Khong tim thay tep chung chi %CERT_FILE%!
    pause
    exit /b 1
)

echo [*] Dang day chung chi vao /data/local/tmp/ ...
adb push "%CERT_FILE%" /data/local/tmp/c8750f0d.0

echo [*] Dang remount va copy vao /system/etc/security/cacerts/ ...
adb shell "su -c 'mount -o remount,rw / || mount -o remount,rw /system 2>/dev/null; cp /data/local/tmp/c8750f0d.0 /system/etc/security/cacerts/; chmod 644 /system/etc/security/cacerts/c8750f0d.0; chown root:root /system/etc/security/cacerts/c8750f0d.0'"

echo.
echo [✓] HOAN TAT!
echo Chung chi MinoTMProxy da duoc cai truc tiep vao Root CA cua Android.
echo (Ban co the bat tat ca app HTTPS tren Android 7+ ma khong bi loi chung chi).
echo.
pause
