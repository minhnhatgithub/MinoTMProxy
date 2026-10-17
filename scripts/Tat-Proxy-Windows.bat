@echo off
chcp 65001 >nul
title Tat Proxy He Thong Windows - MinoTMProxy

echo ========================================================
echo   TAT PROXY CHO WINDOWS PC (MinoTMProxy)
echo ========================================================
echo.

reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f >nul

echo [✓] DA TAT PROXY WINDOWS!
echo May tinh da quay lai ket noi mang truc tiep.
echo.
pause
