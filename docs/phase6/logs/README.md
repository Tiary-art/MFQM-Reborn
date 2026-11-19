完整 Gradle 原始输出同时保存在同名 .log.gz（未修改字节）。可读 .log 仅去掉每行尾空格以通过 Git whitespace 检查，未裁剪内容。最终验收日志为 gradle-clean-test-build.log 与 TEST-*.xml；其他 Gradle 日志包含此前失败或尚未加入新测试时的尝试。JSON/stdout/stderr 为实际工具结果。
