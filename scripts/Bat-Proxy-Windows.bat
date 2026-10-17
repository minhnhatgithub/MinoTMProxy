@echo off
chcp 65001 >nul
title Bat Proxy He Thong Windows - MinoTMProxy

echo ========================================================
echo   BAT PROXY CHO WINDOWS PC (MinoTMProxy)
echo   Proxy Server: 127.0.0.1:8080
echo ========================================================
echo.

reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f >nul
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d "127.0.0.1:8080" /f >nul

echo [✓] DA BAT PROXY WINDOWS (127.0.0.1:8080)!
echo Trinh duyet va cac app tren may tinh se chay qua MinoTMProxy.
echo.
pause
