# 範例：用你自己的資料做分析

| 檔案 | 說明 |
|---|---|
| [`wrong_questions_by_subject.py`](wrong_questions_by_subject.py) | 用 `export_my_data` 分頁匯出你的錯題紀錄，統計各科錯題分布 |

共通做法：

1. 到 examscloud.net 會員中心「AI 工具連線」按「產生我的一段話」，複製那段話裡 `Bearer` 後面那串個人 token（只顯示一次，已含讀取作答紀錄與錯題本的權限）。
2. `export EXAMSCLOUD_MCP_TOKEN=...`（token 只放環境變數，不要寫進檔案或提交到 Git）。
3. 以 JSON-RPC `tools/call` 呼叫 `https://examscloud.net/mcp`（範例程式已示範）。

想讓 AI 幫你寫新的分析：把這個資料夾的範例給 Claude Code 或 Codex，請它照同樣方式呼叫
`export_my_data`、`list_attempts` 或 `get_study_report`。範例只示範分析**你本人**的紀錄；
考古題與答案只能逐題、逐卷依額度取得，請勿寫程式大量擷取。
