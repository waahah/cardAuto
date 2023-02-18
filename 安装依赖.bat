@echo off

color 0a
title pip-Install
echo 启动中，请稍等

echo 如果使用该脚本出现异常情况，请先确保已安装好python环境

pip install requests -i https://pypi.douban.com/simple/
pip install pytz -i https://pypi.douban.com/simple/
pip install pycryptodome -i https://pypi.douban.com/simple/

pause