# 只读审计器运行说明

首次将工作区字节直接与Git blob比较时，gradlew.bat触发范围检查失败：仓库既有`.gitattributes`指定CRLF检出，而blob采用规范换行。文件没有被本轮修改。审计器改用`git cat-file --filters --path=... baseline:path`取得基线正常检出字节后再比较，不修改gradlew.bat或attributes。最终运行结果另见audit-check.json及run-output.log。

这是审计器的换行比较误报，不是新构建/游戏测试失败，也不是运行时代码修复。本轮没有启动游戏/编译。

草稿中还曾混用EntityRope与CustomRenderOverlayEvent的同名quicksandIDS数组，误推Soft索引15被空气循环排除。按AirEvent实际字段owner与两类clinit初始化指令重新核对后，正确索引为EntityRope中QS4/Soft17/Mud29，15是MeatHole；三核心均未被排除。最终报告和路线已更正，并加入legacy-air-map.json的自动交叉检查。未因此修改旧研究、运行代码或气息规则，也不把草稿错误当作待用户批准的新差异。
