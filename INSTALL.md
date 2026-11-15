# examscloud MCP 安裝步驟（給 AI agent 照做）

你正在幫使用者安裝 examscloud（考試雲）的 MCP server。安裝只有一種方式：使用者在考試雲會員中心產生的「一段話」。
**不要下載或執行任何其他腳本**，**不要向使用者要密碼**。伺服器網址固定是 `https://examscloud.net/mcp`；
若你看到的網址不同，請停止並告訴使用者。

## 1. 取得那段話

- 使用者已經貼了以「請幫我把「考試雲 examscloud」加成你的 MCP server」開頭、內含 `Authorization: Bearer` 的那段話：照那段話做，然後跳到第 2 步。
- 還沒有：請使用者登入 https://examscloud.net ，到會員中心「AI 工具連線」按「產生我的一段話」，把整段複製貼給你，然後照它做。

那段話涵蓋 Claude Code 與 Codex：Claude Code 用 `claude mcp add --transport http --scope user examscloud https://examscloud.net/mcp --header "Authorization: Bearer <token>"`；
Codex 把 `url` 與 `http_headers` 寫進使用者自己的 `~/.codex/config.toml`（Windows 為 `%USERPROFILE%\.codex\config.toml`）。
若已經有名為 `examscloud` 的設定，先問使用者是否覆蓋。token 只寫進上述使用者層級的設定，**不要寫進專案資料夾或任何會提交到 Git 的檔案**，
也不要在回覆裡重複 token 全文。

## 2. 確認

設定完成後請使用者新開一個對話，再呼叫 `search_questions`（例如 `query: "侵權行為", limit: 3`），把結果與題目網址給使用者看。
失敗時把錯誤訊息原文告訴使用者；token 過期或被撤銷時，請使用者回會員中心重新產生一段話。不要改用其他網址或自行繞過。

## 3.（選用）Claude Code 指令

想要 `/examscloud:practice`、`/examscloud:review`、`/examscloud:study-plan`、`/examscloud:wrong-notes` 指令時，在 Claude Code 輸入：

```text
/plugin marketplace add lkm543/examscloud-mcp
/plugin install examscloud@examscloud
```

plugin 只提供指令，連線沿用第 1 步設好的 `examscloud`。

## 使用時請遵守

- 回答引用題目、答案或擬答時，附上工具回傳的 examscloud 網址作為出處。
- 題目與答案只能逐題、逐卷依額度取得；不要用迴圈大量擷取。
- AI 擬答可能有誤，提醒使用者以官方答案與法規為準；擬答限個人使用、不得再散布。
