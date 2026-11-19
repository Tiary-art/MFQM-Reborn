# Windows构建问题

本轮只在Linux实跑，Windows NOT_RUN。旧Phase9脚本文本默认编码和直接调用gradlew.bat的cp932/WinError2风险不能用Linux成功关闭。R0所有CSV/JSON/MD显式UTF-8；run_baseline.py Windows分支用cmd.exe /d /c gradlew.bat并设cwd，日志以二进制捕获，避免终端解码丢失。中文/空格/方括号路径的Windows实机仍需验收。

未为R0强行修改旧Phase9脚本（其修复应单独测试），不假称已修复用户电脑缺图或构建问题。建议Java17、Python3.9+，执行README命令并保留完整原始stderr。反馈应带实际安装JAR hash、出错ID、资源包优先级和latest.log。
