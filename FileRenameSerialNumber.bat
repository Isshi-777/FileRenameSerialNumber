@echo off
cd /d %~dp0

rem ����
set DIR_PATH = 1
set FILE_NAME = 2
set SORT_TYPE = 3

echo "�t�@�C���A�ԃ��l�[��(�p�����[�^�[�w��ver)"

rem ���͗v��
set /P DIR_PATH="�Ώۂ̃f�B���N�g���̐�΃p�X�F"
set /P FILE_NAME="���l�[���̘A�Ԕԍ��O�̃t�@�C����(�uxxxx�A��.�g���q�v��xxxx����)�F"
set /P SORT_TYPE="�\�[�g�̃^�C�v�i�uctime�v�F�t�@�C���쐬���A�uname�v�F���l�[���O�̖��O���j�F"

rem python�X�N���v�g���s
python FileRenameSerialNumber.py %DIR_PATH% %FILE_NAME% %SORT_TYPE%

pause