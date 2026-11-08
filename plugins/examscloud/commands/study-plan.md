---
description: 依考試雲的學習統計與錯題分布，排一份讀書計畫
argument-hint: [距離考試的天數或目標考試]
---

使用 examscloud MCP 工具為使用者排讀書計畫（條件：「$ARGUMENTS」）：

1. 呼叫 `get_study_report` 讀取作答量、正確率與各科錯題分布；必要時用 `list_attempts` 看最近的練習。
2. 找出弱點科目（錯題多、正確率低），並說明判斷依據的數字。
3. 依使用者給的天數或考試，排出每週（或每日）計畫：每天要複習的科目、建議用 `/examscloud:review` 複習錯題、用 `/examscloud:practice` 練哪些科目。
4. 計畫只根據使用者本人的資料；不要編造統計數字。
