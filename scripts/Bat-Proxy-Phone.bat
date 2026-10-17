@echo off
chcp 65001 >nul
title Bat Proxy Cho Phone - MinoTMProxy
cd /d "%~dp0"

set "PY_CMD=python"
if exist "%~dp0..\.venv\Scripts\python.exe" set "PY_CMD=%~dp0..\.venv\Scripts\python.exe"

set "LAN_IP="
if exist "%~dp0get_ip.py" (
    "%PY_CMD%" "%~dp0get_ip.py" > "%TEMP%\mino_ip.txt" 2>nul
    if exist "%TEMP%\mino_ip.txt" (
        set /p LAN_IP=<"%TEMP%\mino_ip.txt"
        del "%TEMP%\mino_ip.txt" 2>nul
    )
)
if "%LAN_IP%"=="" set LAN_IP=127.0.0.1

echo ========================================================
echo   BAT PROXY CHO DIEN THOAI (MinoTMProxy)
echo   Dia chi Proxy: %LAN_IP%:8080
echo ========================================================
echo.

where adb >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Khong tim thay lenh 'adb' trong he thong.
    echo Huong dan cai bang tay tren dien thoai:
    echo   1. Vao Cai dat -^> Wi-Fi -^> Chon Wi-Fi dang ket noi
    echo   2. Chon Nang cao / Proxy -^> Thu cong [Manual]
    echo   3. Host: %LAN_IP%
    echo   4. Port: 8080
    echo.
    pause
    exit /b 0
)

echo [*] Dang gui lenh bat proxy qua ADB...
adb shell settings put global http_proxy %LAN_IP%:8080

echo.
echo [✓] DA BAT PROXY THANH CONG!
echo Toan bo request tren dien thoai bay gio se di qua MinoTMProxy (%LAN_IP%:8080).
echo.
pause
