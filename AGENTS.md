# 給 AI agent 的說明

- 安裝 examscloud MCP：照 [INSTALL.md](INSTALL.md)，只用使用者從考試雲會員中心「產生我的一段話」取得的那段話。
- 伺服器網址固定為 `https://examscloud.net/mcp`。
- 使用工具時：
  - 引用題目、答案或擬答要附工具回傳的 examscloud 網址。
  - 題目與答案只能逐題、逐卷依額度取得；不要以迴圈大量擷取，額度用完時照錯誤訊息等待，不要重試轟炸。
  - AI 擬答可能有誤，限個人使用、不得再散布。
  - `get_question` 預設不給答案；使用者想自己作答時先出題，作答後再用 `get_answer` 或 `submit_practice` 對答案。
- 二度開發（`examples/`）：只示範分析使用者**本人**的作答與錯題資料；token 從環境變數 `EXAMSCLOUD_MCP_TOKEN` 讀，不要寫進檔案。
