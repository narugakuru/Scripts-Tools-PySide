@echo off
python -m nuitka ^
--onefile ^
--output-dir=app ^
--mingw64 ^
--lto=yes ^
--enable-plugin=pyside6 ^
--show-progress ^
--show-memory ^
--follow-imports ^
--assume-yes-for-downloads ^
--include-qt-plugins=sensible,qml,styles,sqldrivers ^
--windows-icon-from-ico=.\resource\logo.ico ^
--company-name="小岚岚有限公司" ^
--product-name="IT Tools" ^
--file-version=2.3.0.0 ^
--product-version=2.3.0.0 ^
--file-description="IT Tools by 小岚岚 hikari021004@gmail.com" ^
--copyright="© 2024 Hikari" ^
--trademarks="Hikari Trademark" ^
--nofollow-import-to=numpy ^
app.py
