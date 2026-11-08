# examscloud MCP

在你自己的 AI 工具（Claude Code、Codex、claude.ai…）裡使用 [考試雲 examscloud](https://examscloud.net) 的考古題、官方答案、AI 擬答與你的學習紀錄。

這個 repo 只放**安裝設定、Claude Code plugin 與範例**；伺服器由 examscloud.net 提供，這裡沒有任何題庫資料或密鑰。

## 一段話安裝（推薦）

把下面這段話貼進你的 Claude Code 或 Codex：

```text
請幫我安裝 examscloud 的 MCP：讀 https://github.com/lkm543/examscloud-mcp/blob/main/INSTALL.md ，
依我目前使用的工具（Claude Code 或 Codex）照裡面的指令安裝，裝完後幫我呼叫一次 search_questions 確認可用。
```

第一次使用時，工具會開啟瀏覽器請你登入考試雲並按「同意」，**不需要複製密碼或 token**。

## 手動安裝

| 工具 | 做法 |
|---|---|
| Claude Code | `claude mcp add --transport http examscloud https://examscloud.net/mcp`，或安裝 plugin：`/plugin marketplace add lkm543/examscloud-mcp` → `/plugin install examscloud@examscloud`，然後 `/mcp` 登入 |
| Codex | `codex mcp add examscloud --url https://examscloud.net/mcp`，然後 `codex mcp login examscloud` |
| claude.ai／其他支援自訂連接器的工具 | 新增自訂連接器，網址 `https://examscloud.net/mcp` |
| 不登入先試用 | 連 `https://examscloud.net/mcp/public`（只有考古題與官方答案，額度較低） |

指令語法以各工具官方文件為準。設定範例見 [`codex/config.toml.example`](codex/config.toml.example)。

## 可以做什麼

| 工具 | 說明 | 需要 |
|---|---|---|
| `search_questions`、`get_question`、`get_answer`、`get_paper` | 搜尋考古題、讀單題（預設不給答案）、官方答案、分頁讀整卷 | 免登入可用 |
| `get_draft`、`get_concept_card`、`get_corrections` | 完整 AI 擬答、概念圖卡、修正紀錄 | 登入（扣帳號擬答額度） |
| `start_practice`、`get_practice_questions`、`submit_practice` | 在 AI 裡練習整卷並交卷計分；結果寫回網站的作答紀錄與錯題本 | 登入 |
| `get_review_queue`、`list_wrong_questions`、`update_wrong_question` | 今日複習、錯題本、標記已掌握 | 登入 |
| `list_attempts`、`get_study_report`、`export_my_data` | 作答紀錄、學習統計、分頁匯出本人資料做分析 | 登入 |

Claude Code plugin 另附四個指令：`/examscloud:practice`、`/examscloud:review`、`/examscloud:study-plan`、`/examscloud:wrong-notes`。

## 用你的資料做分析或二度開發

[`examples/`](examples/) 有只用 Python 標準函式庫的範例，例如統計你的錯題科目分布。程式以個人 token（會員中心「AI 工具連線」建立）呼叫 `https://examscloud.net/mcp`；請把 token 放在環境變數 `EXAMSCLOUD_MCP_TOKEN`，**不要寫進會提交到 Git 的檔案**。

## 使用規範

- **你的作答與錯題紀錄**：不限用途。
- **考古題與官方答案**：個人學習與分析；引用時請標示「資料來源：考試雲 examscloud」並附題目網址。**只能逐題、逐卷依額度取得，不提供整科、整年度或全庫下載，請勿以程式大量擷取。**
- **AI 擬答與概念圖卡**：AI 生成、可能有誤；限個人使用，不得再散布。
- 正式條款以 examscloud.net 公告為準；違反規範的 token 或授權可能被撤銷。

可隨時在 examscloud.net 會員中心「AI 工具連線」查看與撤銷已授權的工具和 token。

## 授權

本 repo 的設定檔、plugin 與範例程式採 [MIT](LICENSE)。這個授權不涵蓋透過服務取得的題目、答案或擬答。
