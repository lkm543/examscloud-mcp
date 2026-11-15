# examscloud MCP

在你自己的 AI 工具（Claude Code、Codex、claude.ai…）裡使用 [考試雲 examscloud](https://examscloud.net) 的考古題、官方答案、AI 擬答與你的學習紀錄。

這個 repo 只放**安裝設定、Claude Code plugin 與範例**；伺服器由 examscloud.net 提供，這裡沒有任何題庫資料或密鑰。

## 安裝：一段話

1. 登入 [examscloud.net](https://examscloud.net)，到會員中心「AI 工具連線」按「產生我的一段話」。
2. 複製那段話，貼進 Claude Code 或 Codex 的對話框。不用分辨自己用的是哪一個，AI 會自己判斷並完成設定。
3. 設定完成後新開一個對話，就能使用下面的工具。

那段話含你的個人 token（90 天到期、只顯示一次），只貼進你自己的 AI 工具，不要分享或截圖；外流或不用時，可在同一頁撤銷。

## 可以做什麼

| 工具 | 說明 | 需要 |
|---|---|---|
| `search_questions`、`get_question`、`get_answer`、`get_paper` | 搜尋考古題、讀單題（預設不給答案）、官方答案、分頁讀整卷；聽力題另附官方音檔網址（`listening_audio`，免登入可直接播放） | 免登入可用 |
| `get_draft`、`get_concept_card`、`get_corrections` | 完整 AI 擬答、概念圖卡、修正紀錄 | 登入（扣帳號擬答額度） |
| `start_practice`、`get_practice_questions`、`submit_practice` | 在 AI 裡練習整卷並交卷計分；結果寫回網站的作答紀錄與錯題本 | 登入 |
| `get_review_queue`、`list_wrong_questions`、`update_wrong_question` | 今日複習、錯題本、標記已掌握 | 登入 |
| `report_question` | 回報題目錯字、缺圖、選項或答案錯誤（每人每天 20 題） | 登入 |
| `send_feedback` | 把問題或缺漏回報給考試雲（題目有誤、缺試卷／題目／答案／音檔、網站或工具故障、建議）；AI 會先請你確認內容再送出，想收到回覆可留 email | 免登入可用（有次數上限） |
| `list_attempts`、`get_study_report`、`export_my_data` | 作答紀錄、學習統計、分頁匯出本人資料做分析 | 登入 |

另有四個 MCP prompts：`practice`（練習）、`review`（今日複習）、`study-plan`（讀書計畫）、`wrong-notes`（錯題筆記）。

交卷時沒作答的題目會跟網頁模擬考一樣算答錯並進錯題本。

## 用你的資料做分析或二度開發

[`examples/`](examples/) 有只用 Python 標準函式庫的範例，例如統計你的錯題科目分布。程式以你的個人 token 呼叫 `https://examscloud.net/mcp`：在會員中心「AI 工具連線」按「產生我的一段話」，那段話裡 `Bearer` 後面那串就是（只顯示一次）；請把 token 放在環境變數 `EXAMSCLOUD_MCP_TOKEN`，**不要寫進會提交到 Git 的檔案**。

## 使用規範

- **你的作答與錯題紀錄**：不限用途。
- **考古題與官方答案**：個人學習與分析；引用時請標示「資料來源：考試雲 examscloud」並附題目網址。**只能逐題、逐卷依額度取得，不提供整科、整年度或全庫下載，請勿以程式大量擷取。**
- **AI 擬答與概念圖卡**：AI 生成、可能有誤；限個人使用，不得再散布。
- 正式條款以 examscloud.net 公告為準；違反規範的 token 可能被撤銷。

可隨時在 examscloud.net 會員中心「AI 工具連線」查看與撤銷已產生的一段話（token）。

## 授權

本 repo 的設定檔、plugin 與範例程式採 [MIT](LICENSE)。這個授權不涵蓋透過服務取得的題目、答案或擬答。
