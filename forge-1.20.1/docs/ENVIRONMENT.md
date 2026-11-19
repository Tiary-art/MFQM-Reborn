# 环境与可复现命令

## 锁定版本

- Minecraft 1.20.1 / official mappings 1.20.1
- Forge 47.2.0（MDK来源 https://maven.minecraftforge.net/net/minecraftforge/forge/1.20.1-47.2.0/forge-1.20.1-47.2.0-mdk.zip）
- ForgeGradle 6.0.24（精确plugin版本，不使用区间）
- Gradle Wrapper 8.1.1（distributionSha256Sum在wrapper properties中）
- Java语言/字节码17；本次运行 Eclipse Temurin 17.0.21+9，Linux amd64
- Python 3（仅资源审计/私有资源包工具；没有额外Python依赖）

JDK下载来源 https://api.adoptium.net/v3/binary/latest/17/ga/linux/x64/jdk/hotspot/normal/eclipse 。该URL随时间变化，实际本次版本及下载文件SHA-256见 toolchain_provenance.json。安装任意兼容JDK17可以构建，但要严格复现实验应使用记录的相同发行版。Gradle/FG/Forge版本和运行产物哈希单独记录，未宣称跨所有操作系统逐字节相同。

## 本次云环境专用设置

首次Java直连Gradle发行站点被拒绝，日志保留。curl能下载，但Java不自动读取http_proxy环境变量。代理/信任库设置仅写在工作目录内的私有GRADLE_USER_HOME，不加入工程配置；未关闭TLS验证。

本次执行前设置（路径为此云环境专用，用户本机不要照抄）：

```sh
export JAVA_HOME=/workspace/work/task002-tools/jdk-17.0.21+9
export GRADLE_USER_HOME=/workspace/work/task002-tools/gradle-home
export JAVA_TOOL_OPTIONS='-Dhttps.proxyHost=proxy -Dhttps.proxyPort=8080 -Djavax.net.ssl.trustStore=/etc/ssl/certs/java/cacerts'
```

私有Gradle用户配置设http/https proxyHost=proxy、proxyPort=8080，nonProxyHosts为localhost/127.*；使用系统Java trustStore。一般家庭网络不需要这些设置；企业环境按管理员提供的可信代理和CA配置，不将凭据写入工程。

实际构建/运行命令：

```sh
./gradlew --no-daemon --console=plain build
./gradlew --no-daemon --console=plain runGameTestServer
./gradlew --no-daemon --console=plain runClient
./gradlew --no-daemon --console=plain runServer
python3 tools/verify_project.py build/libs/mfqm-reborn-0.0.2-dev.jar
```

游戏需下载Minecraft自有资产，下载缓存不随完整工程或模组JAR分发。MDK许可证及credits保存在工程根目录，旧Mod授权状况仍以任务001报告06为准。模组metadata暂标All Rights Reserved，不代表获得原作素材许可。
