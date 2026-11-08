---
description: 今日複習：從考試雲錯題本出題，作答後對答案並標記已掌握的題目
argument-hint: [題數，預設 10]
---

使用 examscloud MCP 工具帶使用者做今日複習（題數：「$ARGUMENTS」，未指定時 10 題）：

1. 呼叫 `get_review_queue` 取得待複習題目（不含答案），一題一題出給使用者作答。
2. 每題作答後用 `get_answer` 對答案；答錯時可用 `get_draft` 簡短講解（提醒 AI 擬答可能有誤）。
3. 使用者連續答對、或表示已掌握的題目，用 `update_wrong_question`（`mastered: true`）移出待複習清單；做之前先問使用者。
4. 最後總結今天答對幾題、哪些題目還需要再複習，並附上題目網址。
