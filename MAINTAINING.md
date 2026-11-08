# 維護說明

## 修改流程

`main` 受保護：所有變更（含維護者）都要開 PR。伺服器網址固定為 `https://examscloud.net/mcp`，任何改網址的 PR 都要特別確認。

伺服器的工具清單（`tools/list`）改變時，同一個 PR 一起：

1. 更新 README 的工具表與 plugin 指令。
2. 遞增 `plugins/examscloud/.claude-plugin/plugin.json` 的 `version`。
3. 需要時遞增 `server.json` 的 `version` 並重新發布到 MCP Registry。
4. 跑 `claude plugin validate --strict .` 與 `claude plugin validate --strict plugins/examscloud`。

## 發布到官方 MCP Registry

`server.json` 使用 `io.github.lkm543/examscloud` 命名空間，由 GitHub 帳號 lkm543 驗證：

```bash
mcp-publisher login github
mcp-publisher publish
```

`login github` 會顯示裝置碼，請在瀏覽器以 lkm543 登入 GitHub 授權。發布後可用下面的網址確認：

```text
https://registry.modelcontextprotocol.io/v0/servers?search=io.github.lkm543/examscloud
```
