# 24个单人场景的实测轨迹

阶段2：已加入玩家位移预算，尚未修复换维度Capability句柄；物理求解器与最终版本相同。每个文件200行、约9.95秒。不是旧版一致性验收。Y为服务端接受位置，速度是求解后值。

| 场景 | Y始→末 | vy范围 | 最大水平速度 | 眼覆盖行 | 最低air | 最低health | CSV |
| --- | --- | --- | --- | --- | --- | --- | --- |
| quicksand_still | 65.010→63.496 | -0.0162..-0.0049 | 0.0000 | 0 | 300 | 20 | [raw](traces/phase2/quicksand_still_8656_14.csv) |
| quicksand_walk | 65.010→63.560 | -0.0154..-0.0049 | 0.0000 | 0 | 300 | 20 | [raw](traces/phase2/quicksand_walk_9282_14.csv) |
| quicksand_jump | 65.010→62.000 | -0.1415..-0.0049 | 0.0000 | 166 | 134 | 20 | [raw](traces/phase2/quicksand_jump_9858_14.csv) |
| quicksand_hold_jump | 65.010→62.000 | -0.2280..-0.0049 | 0.0000 | 171 | 129 | 20 | [raw](traces/phase2/quicksand_hold_jump_10158_14.csv) |
| quicksand_edge | 65.010→63.383 | -0.0176..-0.0049 | 0.0000 | 0 | 300 | 20 | [raw](traces/phase2/quicksand_edge_11478_14.csv) |
| quicksand_single_layer | 65.010→64.000 | -0.0103..-0.0049 | 0.0000 | 0 | 300 | 20 | [raw](traces/phase2/quicksand_single_layer_11788_14.csv) |
| quicksand_multi_layer | 64.932→62.839 | -0.1123..-0.0049 | 0.0000 | 23 | 277 | 20 | [raw](traces/phase2/quicksand_multi_layer_12080_14.csv) |
| quicksand_fast_fall | 68.000→62.000 | -1.1156..-0.0357 | 0.0000 | 184 | 116 | 20 | [raw](traces/phase2/quicksand_fast_fall_13024_14.csv) |
| mud_still | 65.010→63.700 | -0.0137..-0.0049 | 0.0000 | 0 | 300 | 20 | [raw](traces/phase2/mud_still_13340_14.csv) |
| mud_walk | 65.010→63.700 | -0.0137..-0.0049 | 0.0000 | 0 | 300 | 20 | [raw](traces/phase2/mud_walk_13760_14.csv) |
| mud_jump | 65.010→63.700 | -0.0566..-0.0049 | 0.0000 | 0 | 300 | 20 | [raw](traces/phase2/mud_jump_14002_14.csv) |
| mud_hold_jump | 65.010→63.700 | -0.0968..-0.0049 | 0.0000 | 0 | 300 | 20 | [raw](traces/phase2/mud_hold_jump_14317_14.csv) |
| mud_fast_fall | 68.000→63.700 | -1.0584..-0.0055 | 0.0000 | 0 | 300 | 20 | [raw](traces/phase2/mud_fast_fall_14603_14.csv) |
| mud_edge | 65.010→64.700 | -0.0054..-0.0049 | 0.0000 | 0 | 300 | 20 | [raw](traces/phase2/mud_edge_14904_14.csv) |
| mud_single_layer | 65.010→64.000 | -0.0103..-0.0049 | 0.0000 | 0 | 300 | 20 | [raw](traces/phase2/mud_single_layer_15188_14.csv) |
| mud_multi_layer | 65.010→63.700 | -0.0137..-0.0049 | 0.0000 | 0 | 300 | 20 | [raw](traces/phase2/mud_multi_layer_15504_14.csv) |
| soft_quicksand_still | 64.860→62.093 | -0.1394..-0.0064 | 0.0000 | 32 | 268 | 20 | [raw](traces/phase2/soft_quicksand_still_15721_14.csv) |
| soft_quicksand_walk | 64.860→62.000 | -0.1409..-0.0064 | 0.0027 | 31 | 269 | 20 | [raw](traces/phase2/soft_quicksand_walk_16085_14.csv) |
| soft_quicksand_jump | 64.782→62.000 | -0.1392..-0.0064 | 0.0000 | 174 | 126 | 20 | [raw](traces/phase2/soft_quicksand_jump_16344_14.csv) |
| soft_quicksand_hold_jump | 64.860→62.000 | -0.2286..-0.0064 | 0.0000 | 175 | 125 | 20 | [raw](traces/phase2/soft_quicksand_hold_jump_16679_14.csv) |
| soft_quicksand_fast_fall | 66.850→62.000 | -1.0584..-0.0347 | 0.0000 | 186 | 114 | 20 | [raw](traces/phase2/soft_quicksand_fast_fall_16958_14.csv) |
| soft_quicksand_edge | 64.860→62.000 | -0.1415..-0.0064 | 0.0056 | 34 | 266 | 20 | [raw](traces/phase2/soft_quicksand_edge_17290_14.csv) |
| soft_quicksand_single_layer | 64.860→64.000 | -0.0103..-0.0064 | 0.0000 | 0 | 300 | 20 | [raw](traces/phase2/soft_quicksand_single_layer_17698_14.csv) |
| soft_quicksand_multi_layer | 64.860→62.000 | -0.1413..-0.0064 | 0.0000 | 29 | 271 | 20 | [raw](traces/phase2/soft_quicksand_multi_layer_18060_14.csv) |

所有24项：有限数、tick不重复、settlements差等于tick差。jump记录到2–3行held，hold_jump约59–60行；walk是实际按W2.5秒。未观察到的自主脱离时间=未知；另见deep_oxygen文件中的指令辅助退出。池中心是每种材料still场景，edge为X4.75。
