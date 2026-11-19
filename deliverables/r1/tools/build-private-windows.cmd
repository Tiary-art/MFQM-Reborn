@echo off
py -3 -X utf8 "%~dp0build_private.py" %*
exit /b %errorlevel%
