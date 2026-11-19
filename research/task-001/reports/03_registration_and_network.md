# 03 — 注册、网络与兼容风险

本报告为 2026-11-17 静态分析。原始 JAR 未执行，未启动 Minecraft，未验证运行时表现。高置信度表示归档/指令直接支持；中置信度表示反编译控制流与旧版 SRG 名称解释，仍需旧版实机复核；设计建议不代表旧版事实。所有方法描述符与十进制字节码偏移见 `evidence/*bytecode.txt`；`*.analysis.txt` 是 CFR 0.152 反编译的带行号分析文本，不是原始源码，也不是新版实现。

## 静态注册表

以下是传入 Forge 注册 API 的**原始字符串**，保留大小写和空格。旧环境通常以活动 modid 附加命名空间（`MFQM:<字符串>`），最终存档序列化键与加载成功情况需要旧实例导出确认；不是纹理名称列表。现代资源路径必须重新规范化为小写，不能直接把这些键作为 1.20.1 ResourceLocation。

| 类型 | 字段 | 注册字符串 | 构造类型 | 条件 | 证据行 |
| --- | --- | --- | --- | --- | --- |
| Block | MudBlock | Mud | BlockMud | preInit 无条件调用 | MFQM.analysis.txt:968 |
| Block | BogBlock | Bog | BlockBog | preInit 无条件调用 | MFQM.analysis.txt:974 |
| Block | SoftSnowBlock | SoftSnow | BlockSoftSnow | preInit 无条件调用 | MFQM.analysis.txt:978 |
| Block | SandBlock | DryQuicksand | BlockSand | preInit 无条件调用 | MFQM.analysis.txt:982 |
| Block | SoftQuicksandBlock | SoftQuicksand | BlockSoftQuicksand | preInit 无条件调用 | MFQM.analysis.txt:986 |
| Block | MorassBlock | Morass | BlockMorass | preInit 无条件调用 | MFQM.analysis.txt:989 |
| Block | WetPeatBlock | WetPeat | BlockWetPeat | preInit 无条件调用 | MFQM.analysis.txt:995 |
| Block | PeatBlock | HPeat | BlockPeat | preInit 无条件调用 | MFQM.analysis.txt:998 |
| Block | BrownClayBlock | BrownClay | BlockBrownClay | preInit 无条件调用 | MFQM.analysis.txt:1003 |
| Block | WaxBlock | Wax | BlockWax | preInit 无条件调用 | MFQM.analysis.txt:1009 |
| Block | QuicksandBlock | Quicksand | BlockQuicksand | preInit 无条件调用 | MFQM.analysis.txt:1012 |
| Block | SandstoneTrapBlock | SandstoneTrapBlock | BlockSandstoneTrap | preInit 无条件调用 | MFQM.analysis.txt:1015 |
| Block | JungleQuicksandBlock | JungleQuicksand | BlockJungleQuicksand | preInit 无条件调用 | MFQM.analysis.txt:1018 |
| Block | LiquidMireBlock | LiquidMire0 | BlockLiquidMire | preInit 无条件调用 | MFQM.analysis.txt:1022 |
| Block | StableLiquidMireBlock | LiquidMire1 | BlockStableLiquidMire | preInit 无条件调用 | MFQM.analysis.txt:1026 |
| Block | SinkyLiquidBlock | SinkyLiquid | BlockSinkyLiquid | preInit 无条件调用 | MFQM.analysis.txt:1030 |
| Block | SlimeBlock | SinkingSlime | BlockSlime | preInit 无条件调用 | MFQM.analysis.txt:1035 |
| Block | MucusBlock | Mucus | BlockMucus | preInit 无条件调用 | MFQM.analysis.txt:1039 |
| Block | MireBlock | Mire | BlockMire | preInit 无条件调用 | MFQM.analysis.txt:1043 |
| Block | MoorBlock | Moor | BlockMoor | preInit 无条件调用 | MFQM.analysis.txt:1046 |
| Block | HClayBlock | HardenedClay | BlockHardenedClay | preInit 无条件调用 | MFQM.analysis.txt:1049 |
| Block | SClayBlock | SinkingClay | BlockSinkingClay | preInit 无条件调用 | MFQM.analysis.txt:1052 |
| Block | MossBlock | TangleRootMoss | BlockMoss | preInit 无条件调用 | MFQM.analysis.txt:1055 |
| Block | DenseWebBlock | DenseWebbing | BlockDenseWeb | preInit 无条件调用 | MFQM.analysis.txt:1058 |
| Block | TarBlock | Tar | BlockTar | preInit 无条件调用 | MFQM.analysis.txt:1062 |
| Block | LarvaeBlock | Larvae | BlockLarvae | preInit 无条件调用 | MFQM.analysis.txt:1066 |
| Block | CSandBlock | CorruptedSand | BlockCorruptedSand | preInit 无条件调用 | MFQM.analysis.txt:1070 |
| Block | SwFleshBlock | SwallowingFlesh | BlockSwallowingFlesh | preInit 无条件调用 | MFQM.analysis.txt:1079 |
| Block | AcidBlock | Acid | BlockAcid | preInit 无条件调用 | MFQM.analysis.txt:1082 |
| Block | SlurryBlock | Slurry | BlockSlurry | preInit 无条件调用 | MFQM.analysis.txt:1086 |
| Block | GasBlock | Gas | BlockGas | preInit 无条件调用 | MFQM.analysis.txt:1090 |
| Block | SoftGravelBlock | SoftGravel | BlockSoftGravel | preInit 无条件调用 | MFQM.analysis.txt:1093 |
| Block | HoneyBlock | Honey | BlockHoney | preInit 无条件调用 | MFQM.analysis.txt:1097 |
| Block | SolidHoneyBlock | SolidHoney | BlockSolidHoney | preInit 无条件调用 | MFQM.analysis.txt:1101 |
| Block | HoneycombBlock | Honeycomb | BlockHoneycomb | preInit 无条件调用 | MFQM.analysis.txt:1104 |
| Block | LiquidChocolateBlock | LiquidChocolate | BlockLiquidChocolate | preInit 无条件调用 | MFQM.analysis.txt:1109 |
| Block | ChocolateBlock | ChocolateBlock | BlockChocolate | preInit 无条件调用 | MFQM.analysis.txt:1113 |
| Block | SinkingWoolBlock | SinkingRug | BlockSinkingWool | preInit 无条件调用 | MFQM.analysis.txt:1116 |
| Block | LureBlock | LureBlock | BlockLure | preInit 无条件调用 | MFQM.analysis.txt:1122 |
| Block | BlossomBlock | BlossomBlock | BlockBlossom | preInit 无条件调用 | MFQM.analysis.txt:1127 |
| Block | BlossomSlabBlock | BlossomBlockSlab | BlockBlossomSlab | preInit 无条件调用 | MFQM.analysis.txt:1134 |
| Block | VoreHoleBlock | TempVore | BlockVoreHole | preInit 无条件调用 | MFQM.analysis.txt:1141 |
| Block | MeatBlock | MeatWall | BlockMeat | preInit 无条件调用 | MFQM.analysis.txt:1146 |
| Block | MeatHoleBlock | TempMeat | BlockMeatHole | preInit 无条件调用 | MFQM.analysis.txt:1152 |
| Block | WaxWoodBlock | WaxWood | BlockWaxWood | preInit 无条件调用 | MFQM.analysis.txt:1155 |
| Block | CustomLilyPadBlock | CustomLilyPad | BlockCustomLilyPad | preInit 无条件调用 | MFQM.analysis.txt:1162 |
| Block | MoorGrassBlock | MoorGrass | BlockMoorGrass | preInit 无条件调用 | MFQM.analysis.txt:1166 |
| Block | TentBlock | Tendrils | BlockTent | preInit 无条件调用 | MFQM.analysis.txt:1172 |
| Block | LeavesBlock | LeavesPile | BlockLeaves | preInit 无条件调用 | MFQM.analysis.txt:1178 |
| Item | BogBucketItem | BucketOfLiquidBog | ItemBogBucket | preInit 无条件调用 | MFQM.analysis.txt:1181 |
| Item | ClayBucketItem | Bucket of Clay | ItemClayBucket | preInit 无条件调用 | MFQM.analysis.txt:1184 |
| Item | QuicksandBucketItem | BucketOfQuicksand | ItemQuicksandBucket | preInit 无条件调用 | MFQM.analysis.txt:1186 |
| Item | SandBucketItem | BucketOfSand | ItemSandBucket | preInit 无条件调用 | MFQM.analysis.txt:1189 |
| Item | MireBucketItem | BucketOfMire | ItemMireBucket | preInit 无条件调用 | MFQM.analysis.txt:1192 |
| Item | SlimeBucketItem | BucketOfSlime | ItemSlimeBucket | preInit 无条件调用 | MFQM.analysis.txt:1195 |
| Item | MucusBucketItem | BucketOfMucus | ItemMucusBucket | preInit 无条件调用 | MFQM.analysis.txt:1198 |
| Item | TarBucketItem | BucketOfTar | ItemTarBucket | preInit 无条件调用 | MFQM.analysis.txt:1201 |
| Item | AcidBucketItem | BucketOfAcid | ItemAcidBucket | preInit 无条件调用 | MFQM.analysis.txt:1204 |
| Item | ChocolateBucketItem | BucketOfChocolate | ItemChocolateBucket | preInit 无条件调用 | MFQM.analysis.txt:1207 |
| Item | ChocolatePowderBucketItem | BucketOfChocolatePowder | ItemChocolatePowderBucket | preInit 无条件调用 | MFQM.analysis.txt:1210 |
| Item | HoneyBucketItem | BucketOfHoney | ItemHoneyBucket | preInit 无条件调用 | MFQM.analysis.txt:1218 |
| Item | SlurryBucketItem | BucketOfSlurry | ItemSlurryBucket | preInit 无条件调用 | MFQM.analysis.txt:1221 |
| Item | FertilizerItem | Fertilizer | ItemFertilizer | preInit 无条件调用 | MFQM.analysis.txt:1224 |
| Item | LongStickItem | LongStick | ItemLongStick | preInit 无条件调用 | MFQM.analysis.txt:1229 |
| Item | RescueItem | Rescuing | ItemRescue | preInit 无条件调用 | MFQM.analysis.txt:1232 |
| Item | RopeItem | Rope | ItemRope | preInit 无条件调用 | MFQM.analysis.txt:1235 |
| Item | CableItem | Cable | ItemCable | preInit 无条件调用 | MFQM.analysis.txt:1238 |
| Item | CoilItem | Coil | Item | preInit 无条件调用 | MFQM.analysis.txt:1241 |
| Item | HookItem | Hook | Item | preInit 无条件调用 | MFQM.analysis.txt:1244 |
| Item | FilterItem | Filter | Item | preInit 无条件调用 | MFQM.analysis.txt:1247 |
| Item | GasMaskItem | GasMask | ItemGasMask | preInit 无条件调用 | MFQM.analysis.txt:1250 |
| Item | GrapplingHookItem | GrapplingHook | ItemGrapplingHook | preInit 无条件调用 | MFQM.analysis.txt:1257 |
| Item | GrapplingHookBRKItem | GrapplingHookBroken | ItemGrapplingHookBRK | preInit 无条件调用 | MFQM.analysis.txt:1260 |
| Item | LiqGunItem | LiqGunItem | ItemLiqGun | preInit 无条件调用 | MFQM.analysis.txt:1270 |
| Item | WaxItem | WaxPiece | ItemWaxPiece | preInit 无条件调用 | MFQM.analysis.txt:1276 |
| Item | LifeJacketItem | LifeJacket | ItemLifeJacket | preInit 无条件调用 | MFQM.analysis.txt:1293 |
| Item | PeatItem | PeatItem | Item | preInit 无条件调用 | MFQM.analysis.txt:1299 |
| Item | LarvaRawItem | LarvaRaw | ItemFood | preInit 无条件调用 | MFQM.analysis.txt:1305 |
| Item | LarvaCookedItem | LarvaCooked | ItemFood | preInit 无条件调用 | MFQM.analysis.txt:1308 |
| Item | CberryItem | Cranberry | ItemCranberry | preInit 无条件调用 | MFQM.analysis.txt:1312 |
| Item | DonutItem0 | Donut0 | ItemFood | preInit 无条件调用 | MFQM.analysis.txt:1315 |
| Item | DonutItem1 | Donut1 | ItemFood | preInit 无条件调用 | MFQM.analysis.txt:1319 |
| Item | DonutItem2 | Donut2 | ItemFood | preInit 无条件调用 | MFQM.analysis.txt:1330 |
| Item | DonutItem3 | Donut3 | ItemFood | preInit 无条件调用 | MFQM.analysis.txt:1336 |
| Item | DonutItem4 | Donut4 | ItemFood | preInit 无条件调用 | MFQM.analysis.txt:1351 |
| Item | MyPotionItem | Potion | ItemMyPotion | preInit 无条件调用 | MFQM.analysis.txt:1358 |
| Item | ThrPotionItem | SPotion | ItemSPotion | preInit 无条件调用 | MFQM.analysis.txt:1360 |
| Item | EmptycombItem | Emptycomb | Item | postInit: !BoP | MFQM.analysis.txt:1848 |
| Item | HoneycombItem | HoneycombItem | ItemFood | postInit: !BoP | MFQM.analysis.txt:1852 |
| Item | WadingBoots | wadingBoots | ItemWadingBoots | postInit: BootsID == 1（未复用扫描到的靴子） | MFQM.analysis.txt:1858 |
| Item | PreWadingBoots0 | preWadingBoots0 | ItemPreWadingBoots0 | postInit 无条件调用 | MFQM.analysis.txt:1863 |
| Item | PreWadingBoots1 | preWadingBoots1 | ItemPreWadingBoots1 | postInit 无条件调用 | MFQM.analysis.txt:1866 |

方块附带的 ItemBlock 不属于上表显式 registerItem 数量；`Mud` 使用 ItemMud、SoftSnow/Morass/BrownClay 等使用 ItemMeta，SinkingRug/MoorGrass 使用 ItemMetaColor，保留 meta→BlockState/颜色映射。`TempVore/TempMeat` 等技术性方块已见注册调用，但不能因此宣称可在生存或创造栏直接取得。

| 实体类 | 注册字符串 | mod 内数字 ID | 追踪范围 | 更新周期 tick | 速度同步 | 条件 | MFQM 行 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EntitySlimeHole | EntitySlimeHole | 102 | 120 | 2 | false | 无条件调用 | 1033 |
| EntityTentacles | EntityTentacles | 109 | 120 | 2 | false | QSTentacles | 1073 |
| EntityMudTentacles | EntityMudTentacles | 98 | 120 | 2 | false | QSMudTentacles | 1076 |
| EntityLongStick | EntityLongStick | 106 | 120 | 2 | true | 无条件调用 | 1227 |
| EntityRope | EntityRope | 100 | 120 | 2 | true | 无条件调用 | 1380 |
| EntityHook | EntityHook | 101 | 120 | 2 | true | 无条件调用 | 1381 |
| EntityRescue | EntityRescue | 108 | 120 | 2 | true | 无条件调用 | 1382 |
| EntityLiqBall | EntityLiqBall | 112 | 120 | 2 | true | 无条件调用 | 1383 |
| EntitySPotion | EntitySPotion | 113 | 120 | 2 | true | 无条件调用 | 1384 |
| EntityVoreSlime | VoreSlime | 103 | 80 | 3 | true | InitMobs；自然刷怪另受 SpawnVS/MB/SB/TS 控制 | 1427 |
| EntityMuddyBlob | MuddyBlob | 104 | 80 | 3 | true | InitMobs；自然刷怪另受 SpawnVS/MB/SB/TS 控制 | 1435 |
| EntitySandBlob | SandBlob | 99 | 80 | 3 | true | InitMobs；自然刷怪另受 SpawnVS/MB/SB/TS 控制 | 1443 |
| EntityTarSlime | TarSlime | 105 | 80 | 3 | true | InitMobs；自然刷怪另受 SpawnVS/MB/SB/TS 控制 | 1451 |
| EntityBee | Bee | 111 | 80 | 3 | true | 无条件调用 | 1459 |
| EntityBubble | EntityBubble | 107 | 120 | 2 | false | 无条件调用 | 1462 |
| EntityTarTreads | EntityTarTreads | 110 | 120 | 2 | false | 无条件调用 | 1463 |

四种史莱姆还调用 `registerGlobalEntityID` 生成旧刷怪蛋；Bee 通过 `registerEntityEgg/getUniqueEntityEggId` 从 300 起寻找数字 ID。数字 ID 不应迁入新版。

| 流体类 | 流体字符串 | 条件 |
| --- | --- | --- |
| BogFluid | Bog | MFQM.preInit registerFluid；返回值未检查 |
| ChocolateFluid | LiquidChocolate | MFQM.preInit registerFluid；返回值未检查 |
| SinkyFluid | SinkyFluid | MFQM.preInit registerFluid；返回值未检查 |
| SlurryFluid | Slurry | MFQM.preInit registerFluid；返回值未检查 |
| MucusFluid | MucusFluid | MFQM.preInit registerFluid；返回值未检查 |
| TarFluid | Tar | MFQM.preInit registerFluid；返回值未检查 |
| QuicksandFluid | JungleQuicksand | MFQM.preInit registerFluid；返回值未检查 |
| SlimeFluid | SlimeFluid | MFQM.preInit registerFluid；返回值未检查 |
| HoneyFluid | Honey | MFQM.preInit registerFluid；返回值未检查 |
| AcidFluid | AcidFluid | MFQM.preInit registerFluid；返回值未检查 |
| SandFluid | SandFluid | MFQM.preInit registerFluid；返回值未检查 |
| MireFluid | LiquidMire | MFQM.<clinit> 参数；preInit 注册 |
| MireFluid | LiquidMireS | MFQM.<clinit> 参数；preInit 注册 |

流体名是 Fluid 构造参数，方块名另行注册。流体密度/黏度参数不是直接的实体下沉速度。流体注册冲突与静态字段是否复用已有流体待实测。TileEntity：`TileEntityLure` → `tileEntityLure`。世界生成：`MFQM.Init(FMLPostInitializationEvent)` 注册 CustomWorldGen，权重 9999999；另注册 CustomGenerationEvent。生成开关不等于方块注册开关，具体 biome/dimension 分支见旧分析文本和指令。

`PotionStuck` 不是继承 Potion 的类，而是 `IExtendedEntityProperties`；未找到自定义 Potion 注册。`Potion`、`SPotion` 是物品字符串；代码还施加原版 PotionEffect（如 10、15、17、19），不能将这些数字误作 MFQM 自有药水 ID。

## CustomRegister：存在的替换机制不等于实际调用

`registerItem/registerBlock` 若 id 不以 `modId + ":"` 开头，调用正常 GameRegistry；否则通过反射获取旧注册表 Map/ObjectIntIdentityMap，用旧数字 ID 放入新对象，将旧对象放到 `removed:<path>` 并隐藏创造栏；尝试修改 Items/Blocks 静态 final 字段，物品还修改 StatCrafting。异常仅打印。

本 JAR 中 MFQM 确实构造 CustomRegister，但对所有 class 指令搜索，未发现对其 registerItem/registerBlock 的调用。因此“具备反射替换分支”是高置信度事实，“本版本启动会替换原版方块/物品”没有证据，不能确认。新版不移植这套反射操作。

## 三类网络消息

频道 `MFQM_REC`，在 MFQM.preInit 注册：

| 判别 ID | 消息 | 方向 | 载荷 | 服务端处理 |
| --- | --- | --- | --- | --- |
| 0 | RopeMessage | C→S / Side.SERVER | 1 个 ByteBuf float，4 字节 Len | handleCurLen |
| 1 | HookMessage | C→S / Side.SERVER | 1 个 float，4 字节 Len | handleCurLenHook |
| 2 | RescueMessage | C→S / Side.SERVER | 1 个 float，4 字节 Len | handleCurLen |

载荷不含玩家名、UUID 或实体 ID；服务端取 `ctx.getServerHandler().field_147369_b` 的玩家名，扫描对应的固定 64 槽全局数组，对非 null 且名字匹配的实体设置 double `curLen = (double)len`。三个 Handler 直接调用，没有显式主线程排队。网络调用线程的实际行为由旧 Forge 实现决定；这里只确认处理器没有调度代码。

证据表（3 类同构，可逐类复核 bytecode）：

| 类/方法 | 字节码证据 | 结论 | 置信度 |
| --- | --- | --- | --- |
| RopeMessage.fromBytes | offset 2 invokevirtual ByteBuf.readFloat；5 putfield Len:F | 未自行检查包长、范围或有限值；底层 ByteBuf 对短包的行为由 Netty 决定 | 高 |
| RopeMessage.toBytes | offset 5 invokevirtual ByteBuf.writeFloat | 4 字节 float；默认 ByteBuf 字节序，代码未调用 order() | 高 |
| RopeMessage.handleCurLen | 8 bipush 64；27 if_acmpne；40 putfield EntityRope.curLen:D | 使用 String 引用比较，不是 equals；直接写长度 | 高 |
| HookMessage/RescueMessage.handle… | 同构 readFloat / if_acmpne / f2d / putfield curLen，见对应指令文本 | 同样的边界与关联问题 | 高 |
| 各 Handler.onMessage | 取 ServerHandler.player → 静态 handle；返回 null | 无应答消息，无显式调度或节流 | 高 |
| MFQM.preInit | newSimpleChannel + registerMessage ×3，Side.SERVER | 消息方向与判别 ID 已确认 | 高 |

风险与移植要求：

- **长度校验缺失**：NaN、±Infinity、负数、极大有限值可到达赋值。不能把其他实体 tick 分支的部分 `Math.min(maxLen, curLen)` 当成消息入口校验；NaN 仍会污染后续运算。是否形成可利用后果需独立服务端测试。
- **关联脆弱**：`if_acmpne` 比较引用，同内容名字可能不匹配；64 槽为全局静态容量。物品/实体生命周期中存在设置与清理操作，不能据此声称从不清理；跨维度、掉线、死亡、容量耗尽仍需全链路压测。
- **授权不足**：入口没有验证目标实体仍活着、同维度、距离、持有工具、拥有者 UUID、最大长度或调整速率；客户端实体 ID 未传入，攻击面应按实际数组映射评估。
- **新版建议**：SimpleChannel 明确协议版本与 PLAY_TO_SERVER，解码长度固定，enqueueWork 到服务端主线程；按发送者 UUID 查找活动救援会话，检查实体有效性/同世界/所有权/距离/工具；仅接收增减意图或严格限幅后的参数，所有 float/double 先做 isFinite，限制每 tick 调整量与消息速率。

## 配方与配置条件

全部原始调用附在 `recipe_calls.txt`，包括 TurnStick/TurnRope/TurnHook/TurnJacket/TurnGasMask/TurnPotion/TurnLiqGun/TurnBoots 的配方开关。多数工具即使关闭配方仍见无条件注册，不应写成“关闭就不存在”。毛毯配方有 ix5 0..15 循环，不能以静态调用点数量代替最终配方数量。

现代化时将 shaped/shapeless/smelting、loot、tags、biome modifiers、worldgen 改为数据驱动。旧注册字符串如 `Bucket of Clay` 含空格，必须记录明确的旧名→新名映射，并分别处理显示名、注册名、纹理路径。

## 未解决问题与下一步

- 实际完整 registry dump、配方展开数量、第三方整合存在/缺失矩阵尚未运行验证。
- 64 槽生命周期与实体物理对恶意长度的最终响应需旧版专服实验；未声称已验证漏洞。
- CustomWorldGen 五个方法反编译控制流不完整；移植生成规则前按字节码与固定种子样本交叉核对。
- 下一步建议先建立旧版基线与数据映射；新版工程需另行授权。
