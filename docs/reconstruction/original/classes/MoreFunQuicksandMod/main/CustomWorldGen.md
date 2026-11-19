# MoreFunQuicksandMod/main/CustomWorldGen

ID `class:ad8267fe0dea0edbc2628031`；class SHA `1c7f6d275b1fa97198289b0561a788b6c692873066dd98fa8ca7dba5e1896375`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / FIRST_BATCH_PARTIAL**（除重点模块报告给出的分支外）。super `java/lang/Object`；interfaces `cpw/mods/fml/common/IWorldGenerator`；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/CustomWorldGen`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__CustomWorldGen.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:9cda6787cb9e7380feae4ec6` `T_BoP:Z` access 0

## 方法目录

- `method:2ffb280794809c5c6a4d395d` `<init>()V` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:f1fc611c640a839f5a7e2719` `generate(Ljava/util/Random;IILnet/minecraft/world/World;Lnet/minecraft/world/chunk/IChunkProvider;Lnet/minecraft/world/chunk/IChunkProvider;)V` access 1，1668 code bytes；语义 NOT_ANALYZED
- `method:5209b85a62c31e474d1e3946` `generateEnd(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，1 code bytes；语义 NOT_ANALYZED
- `method:48b0eb24f8adb9b78d1cd4d5` `soilBlock(IILnet/minecraft/world/World;)Lnet/minecraft/block/Block;` access 2，26 code bytes；语义 NOT_ANALYZED
- `method:d60148310d8f228aa8c15c7b` `fillerBlock(IILnet/minecraft/world/World;)Lnet/minecraft/block/Block;` access 2，26 code bytes；语义 NOT_ANALYZED
- `method:0b1c3e911bfccbd271c30dd7` `validGroundMaterial(IIILnet/minecraft/world/World;)Z` access 2，55 code bytes；语义 NOT_ANALYZED
- `method:2a11dddfe5b3a0b351c88356` `validGroundOrLMireMaterial(IIILnet/minecraft/world/World;)Z` access 2，83 code bytes；语义 NOT_ANALYZED
- `method:8e4cc04acf6de4bf8dcb7f7b` `validCaveMaterial(IIILnet/minecraft/world/World;)Z` access 2，72 code bytes；语义 NOT_ANALYZED
- `method:d414bf5054c60106e52c530d` `validSnowMaterial(IIILnet/minecraft/world/World;)Z` access 2，38 code bytes；语义 NOT_ANALYZED
- `method:1c0f49bc1ef83263f446e56f` `validFallingMaterial(IIILnet/minecraft/world/World;)Z` access 2，38 code bytes；语义 NOT_ANALYZED
- `method:8c745e97b6858e1974258901` `validSandMaterial(ZIIILnet/minecraft/world/World;)Z` access 2，84 code bytes；语义 NOT_ANALYZED
- `method:ac024d979e69895c72fcde5b` `validClayMaterial(IIILnet/minecraft/world/World;)Z` access 2，21 code bytes；语义 NOT_ANALYZED
- `method:e398e2b433de66ce8eb48551` `validWaterMaterial(IIILnet/minecraft/world/World;)Z` access 2，21 code bytes；语义 NOT_ANALYZED
- `method:5759d3291c7cf1911076e29f` `validLavaMaterial(IIILnet/minecraft/world/World;)Z` access 2，21 code bytes；语义 NOT_ANALYZED
- `method:7f840d8afa55ebb4eb3a6ece` `validLiqMaterial(IIILnet/minecraft/world/World;)Z` access 2，15 code bytes；语义 NOT_ANALYZED
- `method:02d48108c1cdbf11ecbdcd67` `validCSMaterial(IIILnet/minecraft/world/World;)Z` access 2，35 code bytes；语义 NOT_ANALYZED
- `method:023387848adc5d6050545130` `validBloodMaterial(IIILnet/minecraft/world/World;)Z` access 2，18 code bytes；语义 NOT_ANALYZED
- `method:024bd9a0e05ccd351064d3f3` `validVoreMaterial(IIILnet/minecraft/world/World;)Z` access 2，43 code bytes；语义 NOT_ANALYZED
- `method:2d2bc1989bd16f091670e993` `validTarMaterial(IIILnet/minecraft/world/World;)Z` access 2，35 code bytes；语义 NOT_ANALYZED
- `method:9395a1b2a7d83d62cb663dd4` `validLarvMaterial(IIILnet/minecraft/world/World;)Z` access 2，30 code bytes；语义 NOT_ANALYZED
- `method:a6be9159ce48d6922ac3f72f` `validSolidMaterial(IIILnet/minecraft/world/World;)Z` access 2，21 code bytes；语义 NOT_ANALYZED
- `method:9b892c134a24f3de608a8507` `validMorassMaterial(IIILnet/minecraft/world/World;)Z` access 2，35 code bytes；语义 NOT_ANALYZED
- `method:66c2433e12ec160172dbd148` `validSlimeMaterial(IIILnet/minecraft/world/World;)Z` access 2，35 code bytes；语义 NOT_ANALYZED
- `method:d410fbbe4f6a7672a9fc5b34` `validHoneycombMaterial(IIILnet/minecraft/world/World;)Z` access 2，18 code bytes；语义 NOT_ANALYZED
- `method:5966d873463c6362608bdad0` `validWebbingMaterial(IIILnet/minecraft/world/World;)Z` access 2，35 code bytes；语义 NOT_ANALYZED
- `method:93ecf7f3c17befe4d4d64ba7` `validSlurryMaterial(IIILnet/minecraft/world/World;)Z` access 2，35 code bytes；语义 NOT_ANALYZED
- `method:6613d21525a00584cc7b6780` `validWebMaterial(IIILnet/minecraft/world/World;)Z` access 2，49 code bytes；语义 NOT_ANALYZED
- `method:042cf756f0f581da40404ca1` `validGroundClayMaterial(IIILnet/minecraft/world/World;)Z` access 2，69 code bytes；语义 NOT_ANALYZED
- `method:8a3fe4c13c8bdc2a47abf30b` `validSoftQuicksandMaterial(IIILnet/minecraft/world/World;)Z` access 2，51 code bytes；语义 NOT_ANALYZED
- `method:31d3b324116fcbdcba0b671d` `validPlantMaterial(IIILnet/minecraft/world/World;)Z` access 2，94 code bytes；语义 NOT_ANALYZED
- `method:3caa3a223713073105eb85f2` `genIsFlatGroundSlime(IIIILnet/minecraft/world/World;)Z` access 2，306 code bytes；语义 NOT_ANALYZED
- `method:7329e720b200b2ef1dcd12f1` `genIsFlatSoftQuicksand(IIIILnet/minecraft/world/World;)Z` access 2，158 code bytes；语义 NOT_ANALYZED
- `method:d4856579c5fba3537b931773` `genIsFlat(IIIILnet/minecraft/world/World;)Z` access 2，158 code bytes；语义 NOT_ANALYZED
- `method:8ec5646b3ceb1e170308c9ae` `genIsFlatHoneycomb(IIIILnet/minecraft/world/World;)Z` access 2，158 code bytes；语义 NOT_ANALYZED
- `method:0d0ad0b89c5a9e248365e866` `genIsHoneycombNear(IIIILnet/minecraft/world/World;)Z` access 2，172 code bytes；语义 NOT_ANALYZED
- `method:ea12bf740a32a4c20679445b` `genIsFlatOrLMire(IIIILnet/minecraft/world/World;)Z` access 2，158 code bytes；语义 NOT_ANALYZED
- `method:cdd1f43716a82128c2e0c040` `genIsFlatClay(IIIILnet/minecraft/world/World;)Z` access 2，158 code bytes；语义 NOT_ANALYZED
- `method:b31559178903cd57c7644879` `genIsFlatVore(IIIILnet/minecraft/world/World;)Z` access 2，158 code bytes；语义 NOT_ANALYZED
- `method:dc648f5a8bd5c14e2bc0e2a9` `genIsFlatSnow(IIIILnet/minecraft/world/World;)Z` access 2，306 code bytes；语义 NOT_ANALYZED
- `method:0bf0089ced421772e4ab512c` `genIsFlatSand(ZIIIILnet/minecraft/world/World;)Z` access 2，174 code bytes；语义 NOT_ANALYZED
- `method:10f8f3ad3f59fe501e37aa40` `genIsFlatBog(IIIILnet/minecraft/world/World;)Z` access 2，322 code bytes；语义 NOT_ANALYZED
- `method:e536e7377097e00dc51c510e` `genIsFlatTar(IIIILnet/minecraft/world/World;)Z` access 2，158 code bytes；语义 NOT_ANALYZED
- `method:5774cc0f47228207a6c1951e` `genIsFlatSlime(IIIILnet/minecraft/world/World;)Z` access 2，158 code bytes；语义 NOT_ANALYZED
- `method:6f0ec7387867236bc7b648c9` `genIsFlatWebbing(IIIILnet/minecraft/world/World;)Z` access 2，158 code bytes；语义 NOT_ANALYZED
- `method:bb8b0b74641d11ec58309021` `genIsFlatLarv(IIIILnet/minecraft/world/World;)Z` access 2，158 code bytes；语义 NOT_ANALYZED
- `method:fd62a417b29578a229263cc3` `genIsFlatLarv2(IIIILnet/minecraft/world/World;)Z` access 2，454 code bytes；语义 NOT_ANALYZED
- `method:53f2f9fd4e6073996f6b65f0` `genIsFlatSolid(IIIILnet/minecraft/world/World;)Z` access 2，158 code bytes；语义 NOT_ANALYZED
- `method:5466e9646c94d7c0884d349b` `genIsFlatSlurry(IIIILnet/minecraft/world/World;)Z` access 2，158 code bytes；语义 NOT_ANALYZED
- `method:65a5579ac1fbcf2570a058f0` `genIsFlatMorass(IIIILnet/minecraft/world/World;)Z` access 2，158 code bytes；语义 NOT_ANALYZED
- `method:f0b4e8dbb3e0b527b1325c55` `genIsBrickNear(IIIILnet/minecraft/world/World;)Z` access 2，172 code bytes；语义 NOT_ANALYZED
- `method:1a3b6bd7d40f7ef91c07cd70` `genIsTarNear(IIIILnet/minecraft/world/World;)Z` access 2，172 code bytes；语义 NOT_ANALYZED
- `method:b861356ce3d817cb83b3c3cf` `genIsUnderWaterFlat(IIIILnet/minecraft/world/World;)Z` access 2，298 code bytes；语义 NOT_ANALYZED
- `method:2a1bb8c775af70ba1c29737b` `isAboveFreeSpace(IIILnet/minecraft/world/World;)Z` access 9，54 code bytes；语义 NOT_ANALYZED
- `method:91b8c817639ae9dbc5853e35` `isAboveSky(IIILnet/minecraft/world/World;)Z` access 9，46 code bytes；语义 NOT_ANALYZED
- `method:3bd79b12da332734a6e72a90` `isAboveEmpty(IIILnet/minecraft/world/World;)Z` access 2，50 code bytes；语义 NOT_ANALYZED
- `method:6e126d5163179e9c9f851689` `isAbovePlant(IIILnet/minecraft/world/World;)Z` access 2，56 code bytes；语义 NOT_ANALYZED
- `method:c6561d0c6ec58def7eaf59f4` `isAboveSolid(IIILnet/minecraft/world/World;)Z` access 2，52 code bytes；语义 NOT_ANALYZED
- `method:0ef364178689a449daa69069` `isNearAboveCeil(IIILnet/minecraft/world/World;I)Z` access 2，144 code bytes；语义 NOT_ANALYZED
- `method:b37045ad43e6e065fe3d0d93` `isNearAbovePlant(IIILnet/minecraft/world/World;I)Z` access 2，144 code bytes；语义 NOT_ANALYZED
- `method:58bfa48e8fe25904d018e189` `isInCave(IIILnet/minecraft/world/World;I)Z` access 2，144 code bytes；语义 NOT_ANALYZED
- `method:cb44fa19340ebc0a3265eb59` `isWaterNear(IIIILnet/minecraft/world/World;)Z` access 2，168 code bytes；语义 NOT_ANALYZED
- `method:dbea39b2ed7ea55cf8b006d1` `isGroundNear(IIIILnet/minecraft/world/World;)Z` access 2，127 code bytes；语义 NOT_ANALYZED
- `method:76d8edce3e5e55f028421f33` `isGroundQS(IIIILnet/minecraft/world/World;Lnet/minecraft/block/Block;)Z` access 2，142 code bytes；语义 NOT_ANALYZED
- `method:10706cfb51c443dc74273c58` `isGroundMossNear(IIIILnet/minecraft/world/World;)Z` access 2，161 code bytes；语义 NOT_ANALYZED
- `method:eccbd69077a577c7f5197773` `isItLake(IIIILnet/minecraft/world/World;)Z` access 2，123 code bytes；语义 NOT_ANALYZED
- `method:ce4a8898bf6adcab96e538ab` `isItLake2(IIIILnet/minecraft/world/World;Z)Z` access 2，142 code bytes；语义 NOT_ANALYZED
- `method:e7b38a38887b7277e52207f4` `isGroundBogNear(IIIILnet/minecraft/world/World;)Z` access 2，143 code bytes；语义 NOT_ANALYZED
- `method:84d4f0c5b2e51950bf6f6a94` `isWoodNear(IIILnet/minecraft/world/World;)Z` access 2，329 code bytes；语义 NOT_ANALYZED
- `method:34c9ba6bf95d1f48ebd9eec5` `validVoreDown(IIILnet/minecraft/world/World;I)Z` access 2，35 code bytes；语义 NOT_ANALYZED
- `method:b83ae36c5749c8f65353f807` `isVorePlace(IIILnet/minecraft/world/World;)Z` access 2，157 code bytes；语义 NOT_ANALYZED
- `method:b5c23dd24b88871f3fda4e5d` `IsDifficultSwamp(I)Z` access 2，24 code bytes；语义 NOT_ANALYZED
- `method:69d85d174b2bc8d68cd413dd` `IsNormalSwamp(I)Z` access 2，41 code bytes；语义 NOT_ANALYZED
- `method:5a4663ff68c9ffec6766a377` `IsEasySwamp(I)Z` access 2，14 code bytes；语义 NOT_ANALYZED
- `method:53e8956d043a548430ad9c9d` `getSwampDifficult(I)I` access 2，41 code bytes；语义 NOT_ANALYZED
- `method:7f5374ba6997c1c85f99ea35` `generateClearWater(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，226 code bytes；语义 NOT_ANALYZED
- `method:1d4685454840b9c3d48cc4a8` `generateBrownClay(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，691 code bytes；语义 NOT_ANALYZED
- `method:716aaa53e608c358874bec9d` `generateMineralClay(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，682 code bytes；语义 NOT_ANALYZED
- `method:ed8a5aac8b22df23b881aaef` `generateMire(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/material/Material;Lnet/minecraft/block/Block;)V` access 2，609 code bytes；语义 NOT_ANALYZED
- `method:02a731c68f0eb89fe7b11056` `generateMireM(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/material/Material;Lnet/minecraft/block/Block;I)V` access 2，643 code bytes；语义 NOT_ANALYZED
- `method:c4441dfae859b985c4553ce7` `generateMireO(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/material/Material;Lnet/minecraft/block/Block;)V` access 2，735 code bytes；语义 NOT_ANALYZED
- `method:e26194fddad216c0aea6e6bb` `generateMud(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，605 code bytes；语义 NOT_ANALYZED
- `method:ea70fc96857407d88dad62b1` `generateForcedMud(IIIILnet/minecraft/world/World;Ljava/util/Random;I)V` access 2，685 code bytes；语义 NOT_ANALYZED
- `method:a465639e8cb463990db3571b` `generateFlatMud(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，590 code bytes；语义 NOT_ANALYZED
- `method:e5cad41adb85d182351e9b8d` `generateMud2(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，456 code bytes；语义 NOT_ANALYZED
- `method:49a26967cf8f2323a30d44a1` `generateMire2(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/material/Material;Lnet/minecraft/block/Block;)V` access 2，649 code bytes；语义 NOT_ANALYZED
- `method:e259aefdd36dd4a6678fcbba` `generateMossQS(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/Block;)V` access 2，698 code bytes；语义 NOT_ANALYZED
- `method:91ba7b5eb6531fa14d3c284e` `generateMireOD(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/material/Material;Lnet/minecraft/block/Block;I)V` access 2，1125 code bytes；语义 NOT_ANALYZED
- `method:93b92b2d66b65309d891a044` `generateMireD(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/material/Material;Lnet/minecraft/block/Block;Z)V` access 2，1094 code bytes；语义 NOT_ANALYZED
- `method:fc2d36b2dfed60d25ffb9614` `generateLeavesAround(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，417 code bytes；语义 NOT_ANALYZED
- `method:d6843e427cefdb2322ea9f87` `generateHoneyNest(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，1420 code bytes；语义 NOT_ANALYZED
- `method:2faaab86ad71592a6b2b3ea5` `generateHoneyChest(Lnet/minecraft/world/World;IIIILjava/util/Random;)V` access 1，458 code bytes；语义 NOT_ANALYZED
- `method:319a3a8aca96dc0bbddc45ed` `generateHoneycomb(IIIILnet/minecraft/world/World;Ljava/util/Random;I)V` access 2，694 code bytes；语义 NOT_ANALYZED
- `method:d005fa198f346ffc960137e9` `generateSolidHoney(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，398 code bytes；语义 NOT_ANALYZED
- `method:046e0aaf989f672595b2aeee` `generateBlood(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/material/Material;)V` access 2，266 code bytes；语义 NOT_ANALYZED
- `method:8b9aace00228e577bbb63d3a` `generateBlood2(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，305 code bytes；语义 NOT_ANALYZED
- `method:f35ded7bed955dee04d8fa01` `generateBlood3(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，231 code bytes；语义 NOT_ANALYZED
- `method:7cb88615fabec636a0ae9c23` `generateVore(IIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，1357 code bytes；语义 NOT_ANALYZED
- `method:074210f419a0b0a7aaddea9e` `genColumnBlockMeta(IIILnet/minecraft/world/World;ILnet/minecraft/block/Block;I)V` access 2，34 code bytes；语义 NOT_ANALYZED
- `method:05f802fc44531fae9913c31d` `preventLiquid(IIILnet/minecraft/world/World;Lnet/minecraft/block/Block;I)V` access 2，141 code bytes；语义 NOT_ANALYZED
- `method:724d2b47e00591e986874fe8` `generateSlurry(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，1100 code bytes；语义 NOT_ANALYZED
- `method:7d6cfc09b984cf4dbfb7e384` `ClearArea3(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，143 code bytes；语义 NOT_ANALYZED
- `method:67a5b008797854d6e9a78f47` `generateAss(IIIILnet/minecraft/world/World;Ljava/util/Random;)Z` access 2，692 code bytes；语义 NOT_ANALYZED
- `method:fca9bea30846bff0c8dd8567` `generateSlime(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，1015 code bytes；语义 NOT_ANALYZED
- `method:610e2a5416cc627002f220bc` `generateCaveWebbing(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，751 code bytes；语义 NOT_ANALYZED
- `method:a710bf7cc80a5cb3b2896be7` `generateLiquidMire(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/material/Material;I)V` access 2，574 code bytes；语义 NOT_ANALYZED
- `method:ef0e35cd3e7f8f3648c061b3` `spawnMorass(Lnet/minecraft/world/World;IIII)V` access 2，433 code bytes；语义 NOT_ANALYZED
- `method:4ce8588d6e7a12c9443bd608` `generateMorass(IIIILnet/minecraft/world/World;Ljava/util/Random;FI)V` access 2，1660 code bytes；语义 NOT_ANALYZED
- `method:2fc94244b7737fe0e764d93e` `generateWater(IIIILnet/minecraft/world/World;Ljava/util/Random;I)V` access 2，1169 code bytes；语义 NOT_ANALYZED
- `method:6ff2c4fff6540d71c41882e8` `generateTar(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，446 code bytes；语义 NOT_ANALYZED
- `method:314624ea2607d071212cec86` `generateLarvae(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，990 code bytes；语义 NOT_ANALYZED
- `method:7db0cd99e8bc85240c46ad39` `generateDenseWeb(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，1319 code bytes；语义 NOT_ANALYZED
- `method:0725613138139c8cf3ba5d3c` `generateBog(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/material/Material;)V` access 2，457 code bytes；语义 NOT_ANALYZED
- `method:2c67d7ffb475dd1b13aad862` `generateSnow(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，388 code bytes；语义 NOT_ANALYZED
- `method:f10664f6a9e2bae1343366dc` `generateGravel(IIIILnet/minecraft/world/World;Ljava/util/Random;Z)V` access 2，199 code bytes；语义 NOT_ANALYZED
- `method:e383f290b5a0a8473a3347d0` `generateEmptyColumn(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，82 code bytes；语义 NOT_ANALYZED
- `method:fb490341c81d27a23fb465a0` `generateGravelColumn(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，41 code bytes；语义 NOT_ANALYZED
- `method:997a3690732912d039e5bee8` `generateGravelPit(IIIILnet/minecraft/world/World;Ljava/util/Random;I)V` access 2，1305 code bytes；语义 NOT_ANALYZED
- `method:ed36ce27008fdde5dd02eccf` `generateSoftSand(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，622 code bytes；语义 NOT_ANALYZED
- `method:a8779916c1c7068e39fc446c` `generateMoorGrass(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/Block;)V` access 2，265 code bytes；语义 NOT_ANALYZED
- `method:5f7659d0f91f9058d2178edc` `generateTendrils(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，275 code bytes；语义 NOT_ANALYZED
- `method:cf1ebc85d78fe91d08293659` `generateWeb(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，266 code bytes；语义 NOT_ANALYZED
- `method:ff2e5528535ccdcc04b2a300` `generateCaveWeb(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，351 code bytes；语义 NOT_ANALYZED
- `method:7a42c7d22446710b66e8006d` `generateClay(IIIIILnet/minecraft/world/World;Ljava/util/Random;I)V` access 2，2061 code bytes；语义 NOT_ANALYZED
- `method:7a9054ec965516027701abd0` `generateOnlyClay(ZIIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，1579 code bytes；语义 NOT_ANALYZED
- `method:c41020fb97f8d6327e0c1302` `ClearArea(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，219 code bytes；语义 NOT_ANALYZED
- `method:e8ca2f30aaf390e885d4daec` `ClearArea2(IIIILnet/minecraft/world/World;Ljava/util/Random;)I` access 2，433 code bytes；语义 NOT_ANALYZED
- `method:fe42f6c8123e5c7731f346bf` `spawnGreenStone(IIILnet/minecraft/world/World;Ljava/util/Random;I)V` access 2，169 code bytes；语义 NOT_ANALYZED
- `method:acddfa959b96359f56554cfd` `spawnSoftQuicksand(IIILnet/minecraft/world/World;Ljava/util/Random;I)V` access 2，67 code bytes；语义 NOT_ANALYZED
- `method:ff01adc2f12e85ac2021c004` `generateSoftQuicksandForest(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/material/Material;Lnet/minecraft/block/Block;)V` access 2，489 code bytes；语义 NOT_ANALYZED
- `method:231e366374ce54f89fee15aa` `generateSoftQuicksand(IIIILnet/minecraft/world/World;Ljava/util/Random;I)V` access 2，1413 code bytes；语义 NOT_ANALYZED
- `method:b4740b94f22706a6f527ef3a` `generateFlatTar(IIIILnet/minecraft/world/World;Ljava/util/Random;ILnet/minecraft/block/Block;I)V` access 2，1735 code bytes；语义 NOT_ANALYZED
- `method:864e8ac18282242745185fe7` `generateCliffsTar(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/Block;I)V` access 2，318 code bytes；语义 NOT_ANALYZED
- `method:242fdbb644a202989cc87e3a` `generateRockTar(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/Block;I)V` access 2，312 code bytes；语义 NOT_ANALYZED
- `method:7c14c105aaea689df52eef0a` `generateCliffs(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，299 code bytes；语义 NOT_ANALYZED
- `method:6bf5b04daeedbdf070a3c48e` `generateRock(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，247 code bytes；语义 NOT_ANALYZED
- `method:36a366c4bf8603195a2f1e24` `generateMoss(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，976 code bytes；语义 NOT_ANALYZED
- `method:84af0c765163ee68345bb83b` `generateWaxTree(IIIILnet/minecraft/world/World;Ljava/util/Random;)Z` access 2，1264 code bytes；语义 NOT_ANALYZED
- `method:5a0d3c4becab1bf09615028d` `generateWax(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，474 code bytes；语义 NOT_ANALYZED
- `method:06a23f2a7e70019ea9f6f9df` `generateHill(IIIILnet/minecraft/world/World;Ljava/util/Random;)V` access 2，913 code bytes；语义 NOT_ANALYZED
- `method:90470173e91a7544a0a44941` `getSwampType(I)I` access 2，72 code bytes；语义 NOT_ANALYZED
- `method:8dbee2d7d52207f2b557b405` `isSwampIsNear(IIILnet/minecraft/world/World;)Z` access 2，101 code bytes；语义 NOT_ANALYZED
- `method:556871495bb9fc40a68aedd1` `isJungleIsNear(IIILnet/minecraft/world/World;)Z` access 2，101 code bytes；语义 NOT_ANALYZED
- `method:2ef137c94ad877ae35fa5fb3` `isTarBiomeIsNear(IIILnet/minecraft/world/World;)I` access 2，108 code bytes；语义 NOT_ANALYZED
- `method:4461a21f2b978514efc97453` `isRiverIsNear(IIILnet/minecraft/world/World;)Z` access 2，108 code bytes；语义 NOT_ANALYZED
- `method:6841af17cdae2bf234ce01d1` `getTarCount(I)I` access 2，53 code bytes；语义 NOT_ANALYZED
- `method:605212308c4809523b895c62` `getJungleType(I)I` access 2，42 code bytes；语义 NOT_ANALYZED
- `method:cae44940c35f7df5ca96efc6` `getDesertType(I)I` access 2，65 code bytes；语义 NOT_ANALYZED
- `method:c95b30d50460d6df372ecd68` `getHillsType(I)I` access 2，76 code bytes；语义 NOT_ANALYZED
- `method:9d29f9d7d30d9dc0d6d707c0` `getSnowType(I)I` access 2，31 code bytes；语义 NOT_ANALYZED
- `method:565df14f3643433acfe15d8b` `getLarvType(I)I` access 2，42 code bytes；语义 NOT_ANALYZED
- `method:b9fbb04fb4b74d33a9bc6676` `getCSandsType(I)I` access 2，20 code bytes；语义 NOT_ANALYZED
- `method:27e0e46ff0bf4ebc1ae4fd8f` `getBloodType(I)I` access 2，20 code bytes；语义 NOT_ANALYZED
- `method:099174518f82c77aa236daaf` `getSlurryType(I)I` access 2，20 code bytes；语义 NOT_ANALYZED
- `method:76ad52c8ddcbff2189e20fd2` `getXcor(Lnet/minecraft/world/World;IIII)Lnet/minecraft/util/Vec3;` access 2，119 code bytes；语义 NOT_ANALYZED
- `method:953535816a75b61371328245` `getZcor(Lnet/minecraft/world/World;IIII)Lnet/minecraft/util/Vec3;` access 2，119 code bytes；语义 NOT_ANALYZED
- `method:804a5f7adf67c7a048e6ed4b` `getPeatBogType(I)I` access 2，61 code bytes；语义 NOT_ANALYZED
- `method:b62983d933dcea8c8a93e672` `getPeatBogGenBirch(I)Z` access 2，41 code bytes；语义 NOT_ANALYZED
- `method:3c9ed20fe8cabd0523a3e00d` `getForestTypeBOP(I)I` access 2，105 code bytes；语义 NOT_ANALYZED
- `method:09130d079d8e2c8d24e1c40f` `getForestTypeVan(I)I` access 2，41 code bytes；语义 NOT_ANALYZED
- `method:85c13aa81891c938175abdbb` `generateAOADimDustopia(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，1 code bytes；语义 NOT_ANALYZED
- `method:e738f0aca6046f678cf98761` `generateAOADimShyrelands(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，1 code bytes；语义 NOT_ANALYZED
- `method:e4098225d04a6928bdfa55ad` `generateAOADimCandyland(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，1 code bytes；语义 NOT_ANALYZED
- `method:ebb8031dface496a1a4732d0` `generateAOADimVoxPonds(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，560 code bytes；语义 NOT_ANALYZED
- `method:ee11fcbe5747ecd3c35e1801` `generateAOADimBarathos(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，510 code bytes；语义 NOT_ANALYZED
- `method:c71fffcd390e7bec2919b2bf` `generateAOADimCrystevia(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，580 code bytes；语义 NOT_ANALYZED
- `method:85152eb3db866d5e79966e91` `generateAOADimGreckon(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，1173 code bytes；语义 NOT_ANALYZED
- `method:f1864188bb1f5c82b9d27d63` `generateAOADimGardencia(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，1323 code bytes；语义 NOT_ANALYZED
- `method:a641f76b2648018e7251ded6` `generateAOADimPrecasia(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，1921 code bytes；语义 NOT_ANALYZED
- `method:a8dd6eac93df5b9a73533374` `generateAOADimIromine(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，1097 code bytes；语义 NOT_ANALYZED
- `method:02d38d490c975fd67f83ca16` `generateAOADimLandsLelyetia(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，224 code bytes；语义 NOT_ANALYZED
- `method:d52d18d5ebdc81c24273647c` `generateAOADimCeleve(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，400 code bytes；语义 NOT_ANALYZED
- `method:2b325f4c1db5048936ad15a8` `generateAOADimLunalus(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，104 code bytes；语义 NOT_ANALYZED
- `method:b34f566f97e61fe06eb8e063` `generateAOADimMysterium(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，128 code bytes；语义 NOT_ANALYZED
- `method:633f9ffeee2c858386afd74e` `generateAOADimCreeponia(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，864 code bytes；语义 NOT_ANALYZED
- `method:790c7c261766ff932e85c459` `generateAOADimLBorean(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，602 code bytes；语义 NOT_ANALYZED
- `method:e370ca63d8a64a8f110a0809` `generateAOADimAbyss(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，1130 code bytes；语义 NOT_ANALYZED
- `method:40ef7c601e18d92bca811f29` `generateAOADimDeeplands(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，907 code bytes；语义 NOT_ANALYZED
- `method:2a5c14aeeb4e05ae84fd479e` `generateAOADimHeaven(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，368 code bytes；语义 NOT_ANALYZED
- `method:b6e55000aae9ece75b2b25f1` `generateTBL(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，1523 code bytes；语义 NOT_ANALYZED
- `method:c65c3676674a0a091afe65e1` `generateEUDimDeepDark(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，1144 code bytes；语义 NOT_ANALYZED
- `method:d01522b5fadf6b3094a9aa64` `generateWLD(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，6553 code bytes；语义 NOT_ANALYZED
- `method:c9cad61d38d683b98741f98c` `generateABC4(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，159 code bytes；语义 NOT_ANALYZED
- `method:e563b43890a7ae99163bcaaa` `generateABC3(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，334 code bytes；语义 NOT_ANALYZED
- `method:cb076e8690b917a1db9b8e48` `generateABC2(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，1918 code bytes；语义 NOT_ANALYZED
- `method:89e15a844c36d20ec8f7f873` `generateABC1(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，826 code bytes；语义 NOT_ANALYZED
- `method:7e1d9679bb202a776724bc96` `generateCustom(Lnet/minecraft/world/World;Ljava/util/Random;III)V` access 2，6674 code bytes；语义 NOT_ANALYZED
- `method:f0f64c2114295ed03b1bce36` `generateNether(Lnet/minecraft/world/World;Ljava/util/Random;II)V` access 2，2021 code bytes；语义 NOT_ANALYZED
- `method:800c6edccf26bb23ee9cf0b7` `generateSurface(Lnet/minecraft/world/World;Ljava/util/Random;III)V` access 2，14262 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## 首批深度档案入口

generateSurface先SSand再QS共享blockGen；original-phase5/02_SURFACE_BRANCH_CLOSURE.md；重点报告§6。

[深度证据、规范与对照](../../../../../../reconstruction/reports/DEEP_FIRST_BATCH.md)

1. 身份/字节哈希/工具：本页顶部，原始来源非原作者源码。
2. 原文证据与解释：按上述位置与重点报告分栏读取。
3. 职责和触发：重点报告对应模块列出输入、调用次序、提前返回。
4. 功能与资源：对应 ORIGINAL_REGISTRY、RESOURCE_USAGE 和本类调用边，不将名字映射当语义。
5. 行为规范：重点报告的分支和边界；未列分支 UNKNOWN。
6. 现代差异：重点报告逐模块对照现代真实路径及存档风险。
7. 测试设计：原版对照本轮 NOT_RUN，现有现代回归见 R0_TEST_RESULTS.json。
8. 结论：PARTIAL，仅已列静态链；下一步按 NEXT_WORK_PACKAGES.md 闭合。
