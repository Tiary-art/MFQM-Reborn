# 三核心主运动分支表

以下39条为人工核对的主要阶段/深度分支，方法内十进制字节码偏移为区域（含端点），不是反编译源码行号。源码行号指附录evidence/source；完整嵌套判断仍应查逐指令文本。全部14169条跳转的结构索引在branches.csv，但不宣称均已语义还原。

|类|偏移区域|条件/阶段|结果|源码行|
|---|---|---|---|---|
|BlockQuicksand|0-184|coordinate setup; player vs other|k=Y-blockY-1 for player; other +.5; km=max(k,0); previous k separately|90–118|
|BlockQuicksand|246-568|living actor; calculate mr and action flags|mr=min(5+floor(max(0,100*(1.5-km))),145); moving includes displacement/rotation|130–160|
|BlockQuicksand|568-615|entry/each collision callback|X/Z=0; Y>-.1 ->0; otherwise /2|161–163|
|BlockQuicksand|615-1097|FX stage precedes later physics RNG|clock/action gates invoke original swim/slime/water/silverfish sounds and bubbles|164–201|
|BlockQuicksand|1098-1395|special EntitySandBlob / compatible unaffected actors|buoyancy .08/.1; onGround/fall reset; early return|202–248|
|BlockQuicksand|1396-1579|topology and jump suction|top+1 & top+2 same -> k=.001 WITHOUT recomputing km; suction conditional decrement|249–260|
|BlockQuicksand|1580-1755|k>=1.2 and !splash|positive Y compensation with motion/depth denominators; web/ground randomness|261–276|
|BlockQuicksand|1756-1875|k<1.2 and rising deltaY>.001, RNG and suction check|additional downward increment; original suction sound|278–281|
|BlockQuicksand|1876-2060|.9<=k<1.2|positive compensation; setStuck(mr); clear fall; random web/ground|282–296|
|BlockQuicksand|2061-2171|k<.9|tick-varying a2; conditional side-specific stuck; fall reset|298–308|
|BlockQuicksand|2172-2325|.5<=k<.9|web branch chooses .0725/.075; moving divides support by div+.075|309–315|
|BlockQuicksand|2326-2418|k<.5; k<.45 and isTrulySink|web; a2=1.05; moving denominator div+.025; force mr145|316–323|
|BlockQuicksand|2419-2514|water tail / blocked topology / common tail|positive Y /4 in water; blocked topology web/stuck; antiHoldJumpScript; nonliving web below1.45|326–337|
|BlockSoftQuicksand|0-219|coordinate setup and living/player entry|k is QS coordinate minus .2; check drowning/muddy|104–139|
|BlockSoftQuicksand|220-542|action/mr calculation|mr=min(5+floor(max(0,pow(12.5*(1.5-km),1.75))),175); div=1+2*distance +rotation|140–170|
|BlockSoftQuicksand|542-603|entry damping|X/Z *=.71; Y>-.1 ->0 else /2|171–173|
|BlockSoftQuicksand|603-1218|FX and actor special cases|FX precedes general physics; EntitySandBlob special early return; later SpawnMudTentacles|174–220|
|BlockSoftQuicksand|1219-1438|topology / jump suction|two blocks above -> k=.001, km not refreshed; conditional jump penalty|221–233|
|BlockSoftQuicksand|1439-1749|1.2<=k<1.3 and !splash; k>=1.3 skips subbranch|add .0735 support first; X/Z *=clamp((k-1.25)*4); subsequent .0725 assignment not used to re-add current support|234–256|
|BlockSoftQuicksand|1750-1906|k<1.2 rising displacement + RNG + suction|additional negative increment|258–262|
|BlockSoftQuicksand|1907-2171|.9<=k<1.2|stuck mr; player tick selects .0735/.0715+web; nonplayer position backstep; support denominator 2*div-1|263–283|
|BlockSoftQuicksand|2172-2388|k<.9; .075<=radius<.5|X/Z zero, center attraction /max(10,km*50); sufficiently strong centering changes entMoving/div|284–301|
|BlockSoftQuicksand|2389-2507|k<.9 continued|a2 tick1.01/1.05; random ground; side-specific stuck; fall reset|302–310|
|BlockSoftQuicksand|2508-2677|.5<=k<.9|web/random support, moving denominator 4*div+.075|311–317|
|BlockSoftQuicksand|2678-2773|k<.5, and <.45 side eligible|web; moving denominator16*div+.025; force Stuck175|318–324|
|BlockSoftQuicksand|2774-2882|water/topology/antiHold tail; nonliving|water positive Y /4; topology web and capped stuck; antiHold; nonliving tentacle handler|327–342|
|BlockMud|0-582|metadata/pool safety/actor filtering/boots|mtd=max(meta,geometricDepth) when meta<3; safe boundary may reset0; WadingBoots; muddy update|199–283|
|BlockMud|582-914|action/mr calculation|mr=min(5+floor(max(0,pow(4*(1.5-km),1.5))),145); div=1+5*distance; rotation term|284–316|
|BlockMud|914-1023|no WadingBoots and onGround; then mtd0 path|X/Z *=.1; mtd0 returns before general /.10Y damping; nonplayer shallow support|317–329|
|BlockMud|1024-1814|special actor / FX branches|early-return actor exceptions; sounds and bubbles; affects RNG before physics|330–413|
|BlockMud|1815-1884|mtd>0 normal path|X/Z *=.71; bootsFloat=false if k<1.3; Y>-.1->0 else /10|414–419|
|BlockMud|1885-2267|dimension effects, tentacles, topology and jump suction|compat toxicity; top+2 same -> k=.001; conditional negative increment|420–443|
|BlockMud|2268-2596|k>=1.3, !splash|a1 .075/.07485 period8; boots .085/.1 else support denominator includes /3 and mtdkof*17.5; web or nonplayer backstep|444–472|
|BlockMud|2597-2718|k<1.3 rising/RNG/suction|additional negative increment|474–477|
|BlockMud|2719-2999|.9<=k<1.3|stuck mr; a1 period4; mtd>2 groundfalse; support when!splash; web/positionback|478–501|
|BlockMud|3000-3117|k<.9|a2=1/.95; setweb; side-specific stuck; no .71 repetition here|503–514|
|BlockMud|3118-3271|.5<=k<.9|random support .0725/.075; moving divisor div+.25|515–521|
|BlockMud|3272-3408|k<.5|a2=1.01 for water/overwater else1.05 ifk<.475; moving divisor div+.025; force145 ifk<.45|522–533|
|BlockMud|3409-3522|inWater / blocked topology / nonliving tail|inWater positiveY=0 then -.01; antiHold only normal topology branch; blocked branch web; nonliving tentacles|536–554|
