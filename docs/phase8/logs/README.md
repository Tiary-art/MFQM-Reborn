完整原始 .log 输出另存同名 .log.gz，未裁剪；可读 .log 仅移除尾部空白。最终主日志 final-verified-clean.log：43项通过、正常退出；另有46项JUnit XML。早期失败、配置诊断及客户端主动终止143退出均保留。JSONL gzip为完整已捕获数据，客户端有3600tick预算，预算外不声称已观察。框架时钟为宿主UTC。
