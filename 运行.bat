@echo off
chcp 65001

title startRun

echo 如果使用该脚本出现异常情况，请先确保已安装好python环境

SET ModlueDIR=Main.py

if not exist %ModlueDIR% (
  echo 请将Main.py与此脚本放置在同一目录下
) else ( 
  python Main.py
)

pause