---
description: 用考試雲出一份模擬練習，逐題作答後交卷並講解錯題（結果寫回考試雲錯題本）
argument-hint: <科目或關鍵字，例如：民法概要 114>
---

使用 examscloud MCP 工具帶使用者練習「$ARGUMENTS」：

1. 用 `search_questions` 找出符合的題目，從結果的 `get_question` 取得 `paper_public_slug`；若有多份試卷，列出年度與科目讓使用者選一份。
2. 用 `start_practice` 建立練習，逐題出給使用者（不要先給答案），一次 5 題，收集使用者的選項。
3. 全部作答完（或使用者說要交卷）後，用 `submit_practice` 交卷，報告得分。還有題目沒作答時先提醒使用者：未作答的題目會算答錯並進錯題本。
4. 針對答錯的題目，用 `get_draft` 讀 AI 擬答，用自己的話簡短講解為何正解是對的；提醒擬答為 AI 生成、可能有誤。
5. 每題附上 examscloud 題目網址。不要用迴圈大量擷取題目。
