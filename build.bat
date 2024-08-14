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
--windows-icon-from-ico=./resource/logo.png ^
--nofollow-import-to=numpy ^
app.py
