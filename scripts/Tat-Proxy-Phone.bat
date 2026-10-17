@echo off
chcp 65001 >nul
title Tat Proxy Phone - MinoTMProxy
cd /d "%~dp0"

echo ========================================================
echo   TAT PROXY CHO DIEN THOAI (MinoTMProxy)
echo ========================================================
echo.

where adb >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Khong tim thay ADB. Vui long vao Cai dat Wi-Fi tren dien thoai va tat Proxy thu cong [Chon None hoac Khong co].
    pause
    exit /b 0
)

echo [*] Dang gui lenh tat proxy qua ADB...
adb shell settings put global http_proxy :0
adb reverse --remove tcp:8080 >nul 2>&1

echo.
echo [✓] DA TAT PROXY CHO DIEN THOAI THANH CONG!
echo Dien thoai bay gio ket noi mang binh thuong truc tiep.
echo.
pause
