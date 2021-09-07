@echo off
cd /d %~dp0

rem 引数
set DIR_PATH = 1
set FILE_NAME = 2
set SORT_TYPE = 3

echo "ファイル連番リネーム(パラメーター指定ver)"

rem 入力要求
set /P DIR_PATH="対象のディレクトリの絶対パス："
set /P FILE_NAME="リネームの連番番号前のファイル名(「xxxx連番.拡張子」のxxxx部分)："
set /P SORT_TYPE="ソートのタイプ（「ctime」：ファイル作成順、「name」：リネーム前の名前順）："

rem pythonスクリプト実行
python FileRenameSerialNumber.py %DIR_PATH% %FILE_NAME% %SORT_TYPE%

pause