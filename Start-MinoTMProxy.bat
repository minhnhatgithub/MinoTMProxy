@echo off
chcp 65001 >nul
title MinoTMProxy — Modern Traffic Inspector
cd /d "%~dp0"

echo ======================================================================
echo           MinoTMProxy — Modern Dark Pro Traffic Inspector
echo             Bản Mod Dark Theme Pro Siêu Đẹp ^& Bắt Request
echo ======================================================================
echo.

:: 1. Xác định môi trường Python và mitmproxy
if exist "%~dp0.venv\Scripts\python.exe" (
    if exist "%~dp0.venv\Scripts\mitmweb.exe" (
        set "PY_CMD=%~dp0.venv\Scripts\python.exe"
        set "MITM_CMD=%~dp0.venv\Scripts\mitmweb.exe"
        goto :INIT_CERTS
    )
)

where python >nul 2>nul
if errorlevel 1 goto :AUTO_SETUP_ENV

set "PY_CMD=python"
set "MITM_CMD=mitmweb"

:CHECK_MITM
"%PY_CMD%" -c "import mitmproxy" >nul 2>nul
if errorlevel 1 goto :INSTALL_DEPS
goto :INIT_CERTS

:INSTALL_DEPS
echo [*] Dang cai dat mitmproxy vao he thong...
"%PY_CMD%" -m pip install -r "%~dp0requirements.txt"
if errorlevel 1 (
    echo [!] He thong Python hien tai thieu thu vien build hoac khong tuong thich.
    goto :AUTO_SETUP_ENV
)
"%PY_CMD%" -c "import mitmproxy" >nul 2>nul
if errorlevel 1 goto :AUTO_SETUP_ENV
goto :INIT_CERTS

:AUTO_SETUP_ENV
echo [*] Dang tu dong khoi tao moi truong Python 3.12 doc lap sieu toc (.venv)...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ErrorActionPreference = 'Stop'; if (-not (Get-Command uv -ErrorAction SilentlyContinue)) { try { Invoke-RestMethod https://astral.sh/uv/install.ps1 | Invoke-Expression } catch {} }; $uv = if (Test-Path \"$env:USERPROFILE\.local\bin\uv.exe\") { \"$env:USERPROFILE\.local\bin\uv.exe\" } elseif (Get-Command uv -ErrorAction SilentlyContinue) { 'uv' } else { $null }; if ($uv) { & $uv venv --python 3.12 .venv; & $uv pip install -r requirements.txt --python .venv } else { if (Get-Command python -ErrorAction SilentlyContinue) { & python -m venv .venv; & \".\.venv\Scripts\pip.exe\" install -r requirements.txt } }"
if exist "%~dp0.venv\Scripts\python.exe" (
    if exist "%~dp0.venv\Scripts\mitmweb.exe" (
        set "PY_CMD=%~dp0.venv\Scripts\python.exe"
        set "MITM_CMD=%~dp0.venv\Scripts\mitmweb.exe"
        goto :INIT_CERTS
    )
)

echo [X] LOI: Khong the khoi tao moi truong chay cho mitmproxy.
echo Vui long kiem tra ket noi Internet hoac cai dat Python 3.11/3.12 tu python.org.
pause
exit /b 1

:INIT_CERTS
:: 2. Tự động đồng bộ và khởi tạo chứng chỉ SSL CA cho máy hiện tại
if exist "%~dp0scripts\sync_certs.py" (
    "%PY_CMD%" "%~dp0scripts\sync_certs.py"
)

:APPLY_THEME
:: 3. Tự động áp dụng giao diện Dark Pro Mod
echo [*] Dang kiem tra va ap dung giao dien Dark Pro...
"%PY_CMD%" "%~dp0custom_web\apply_theme.py"

:: 4. Lấy địa chỉ IP LAN của máy tính
set "LAN_IP="
if exist "%~dp0scripts\get_ip.py" (
    "%PY_CMD%" "%~dp0scripts\get_ip.py" > "%TEMP%\mino_ip.txt" 2>nul
    if exist "%TEMP%\mino_ip.txt" (
        set /p LAN_IP=<"%TEMP%\mino_ip.txt"
        del "%TEMP%\mino_ip.txt" 2>nul
    )
)
if "%LAN_IP%"=="" set LAN_IP=127.0.0.1

echo.
echo ======================================================================
echo  [✓] GIAO DIEN WEB UI : http://127.0.0.1:8081/?token=123
echo  [✓] MAT KHAU WEB     : 123
echo  [✓] PROXY CHO PHONE  : %LAN_IP%:8080
echo.
echo  (*) De bat proxy tren dien thoai:
echo      - Vao Cai dat Wifi -^> Chinh sua mang -^> Proxy Thu cong:
echo        + Ten may chu proxy: %LAN_IP%
echo        + Cong             : 8080
echo      - Hoac chay file: scripts\Bat-Proxy-Phone.bat [neu co cap ADB]
echo ======================================================================
echo.

:: 5. Mở Web UI trên trình duyệt
start http://127.0.0.1:8081/?token=123

:: 6. Khởi động mitmweb (Tự động giải phóng cổng 8080/8081 nếu còn tiến trình cũ)
powershell -NoProfile -ExecutionPolicy Bypass -Command "try { Get-NetTCPConnection -LocalPort 8080,8081 -State Listen -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue } } catch {}; exit 0" >nul 2>&1
"%MITM_CMD%" --web-host 127.0.0.1 --web-port 8081 --listen-host 0.0.0.0 --listen-port 8080 --set block_global=false --set web_password=123

pause
