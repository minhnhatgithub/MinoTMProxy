@echo off
chcp 65001 >nul
title MinoTMProxy — Modern Traffic Inspector
cd /d "%~dp0"

echo ======================================================================
echo           MinoTMProxy — Modern Dark Pro Traffic Inspector
echo             Bản Mod Dark Theme Pro Siêu Đẹp & Bắt Request
echo ======================================================================
echo.

:: 1. Kiểm tra Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [X] LOI: May tinh chua cai dat Python!
    echo Vui long cai dat Python tu: https://www.python.org/downloads/
    echo Nho tich chon: "Add Python to PATH" khi cai dat.
    pause
    exit /b 1
)

:: 2. Kiểm tra mitmproxy
python -c "import mitmproxy" >nul 2>nul
if %errorlevel% neq 0 (
    echo [*] Dang cai dat mitmproxy (lan dau tien chay)...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [X] Cai dat mitmproxy that bai. Vui long kiem tra ket noi mang.
        pause
        exit /b 1
    )
)

:: 3. Tự động áp dụng giao diện Dark Pro Mod
echo [*] Dang kiem tra va ap dung giao dien Dark Pro...
python custom_web\apply_theme.py

:: 4. Lấy địa chỉ IP LAN của máy tính
for /f "usebackq tokens=*" %%i in (`python -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(('8.8.8.8', 80)); print(s.getsockname()[0]); s.close()" 2^>nul`) do set LAN_IP=%%i
if "%LAN_IP%"=="" set LAN_IP=127.0.0.1

echo.
echo ======================================================================
echo  [✓] GIAO DIEN WEB UI : http://127.0.0.1:8081/?token=123
echo  [✓] MAT KHAU WEB     : 123
echo  [✓] PROXY CHO PHONE  : %LAN_IP%:8080
echo.
echo  (*) De bat proxy tren dien thoai:
echo      - Vao Cai dat Wifi -> Chinh sua mang -> Proxy Thu cong:
echo        + Ten may chu proxy: %LAN_IP%
echo        + Cong             : 8080
echo      - Hoac chay file: scripts\Bat-Proxy-Phone.bat (neu co cap ADB)
echo ======================================================================
echo.

:: 5. Mở Web UI trên trình duyệt
start http://127.0.0.1:8081/?token=123

:: 6. Khởi động mitmweb
mitmweb --web-host 127.0.0.1 --web-port 8081 --listen-host 0.0.0.0 --listen-port 8080 --set block_global=false --set web_password=123

pause
