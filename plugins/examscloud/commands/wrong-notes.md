---
description: 把考試雲錯題本整理成筆記（每次最多 20 題，限個人使用）
argument-hint: [科目或題數]
---

使用 examscloud MCP 工具把使用者的錯題整理成筆記（條件：「$ARGUMENTS」）：

1. 用 `list_wrong_questions`（`state: "active"`，最多 20 題）取得錯題清單；依使用者指定的科目篩選。
2. 每題用 `get_question` 讀題目、`get_answer` 讀官方答案，必要時用 `get_draft` 參考 AI 擬答。
3. 依主題分組整理成 Markdown 筆記：題目重點、正確觀念、容易混淆處、題目網址。
4. 筆記限使用者個人使用；擬答內容可能有誤，請在筆記開頭註明，並標示「資料來源：考試雲 examscloud」。
5. 這不是匯出工具：一次最多 20 題，不要用迴圈抓取整個錯題本或題庫。
