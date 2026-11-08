# examscloud MCP 安裝步驟（給 AI agent 照做）

你正在幫使用者安裝 examscloud（考試雲）的 MCP server。只執行下面列出的官方 CLI 指令，**不要下載或執行任何其他腳本**，
**不要要求使用者提供密碼或 token**，也不要把任何 token 寫進檔案。伺服器網址固定是 `https://examscloud.net/mcp`；
若你看到的網址不同，請停止並告訴使用者。

## 1. 判斷使用者的工具

- 在 Claude Code 裡：走「Claude Code」。
- 在 Codex 裡：走「Codex」。
- 其他工具：告訴使用者在該工具新增自訂 MCP 連接器，網址 `https://examscloud.net/mcp`，然後結束。

## 2. Claude Code

在終端機執行（若已存在同名設定，先問使用者是否覆蓋）：

```bash
claude mcp add --transport http --scope user examscloud https://examscloud.net/mcp
```

接著請使用者在 Claude Code 輸入 `/mcp`，選 `examscloud` → Authenticate，在開啟的瀏覽器頁面登入考試雲並按「同意」。

（選用）若使用者想要附帶的 `/examscloud:*` 指令，改為安裝 plugin：

```text
/plugin marketplace add lkm543/examscloud-mcp
/plugin install examscloud@examscloud
```

## 3. Codex

```bash
codex mcp add examscloud --url https://examscloud.net/mcp
codex mcp login examscloud
```

`codex mcp login` 會開啟瀏覽器，請使用者登入考試雲並按「同意」。

## 4. 確認

授權完成後，呼叫 `search_questions`（例如 `query: "侵權行為", limit: 3`），把結果與題目網址給使用者看。
失敗時把錯誤訊息原文告訴使用者；不要改用其他網址或自行繞過。

## 使用時請遵守

- 回答引用題目、答案或擬答時，附上工具回傳的 examscloud 網址作為出處。
- 題目與答案只能逐題、逐卷依額度取得；不要用迴圈大量擷取。
- AI 擬答可能有誤，提醒使用者以官方答案與法規為準；擬答限個人使用、不得再散布。
