@echo off
cd /d %~dp0

echo "ファイル連番リネーム(YAMLファイル内のパラメーター使用)"

rem pythonスクリプト実行
python FileRenameSerialNumber.py

pause