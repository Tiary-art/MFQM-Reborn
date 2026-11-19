原始完整 .log 输出另存同名 .log.gz，未裁剪；可读 .log 仅去掉行末空格以满足 Git whitespace 检查。最终主要结果是 timing-diagnostic-run.log 的36项通过、正常退出，及45项JUnit XML；以前失败/卡住/锁失败/资源审计失败均保留。Gradle单独成功不代表游戏启动或测试成功。框架日志使用宿主UTC时间。
