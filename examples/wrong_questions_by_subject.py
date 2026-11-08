#!/usr/bin/env python3
"""統計你在考試雲的錯題科目分布（只用 Python 標準函式庫）。

用法：
    export EXAMSCLOUD_MCP_TOKEN=exc_mcp_...   # 會員中心「AI 工具連線」建立，需勾選「讀取我的作答紀錄、錯題本」
    python3 wrong_questions_by_subject.py

只讀你本人的錯題紀錄（export_my_data），不抓題目全文或答案。token 只從環境變數讀取，不要寫進檔案。
"""
from __future__ import annotations

import collections
import json
import os
import sys
import urllib.request

URL = "https://examscloud.net/mcp"


def call_tool(token: str, name: str, arguments: dict) -> dict:
    body = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": name, "arguments": arguments}}
    req = urllib.request.Request(
        URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "MCP-Protocol-Version": "2025-11-25",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        result = json.loads(resp.read().decode("utf-8"))["result"]
    if result.get("isError"):
        raise SystemExit(result["content"][0]["text"])
    return result["structuredContent"]


def main() -> int:
    token = os.environ.get("EXAMSCLOUD_MCP_TOKEN", "").strip()
    if not token:
        print("請先設定環境變數 EXAMSCLOUD_MCP_TOKEN", file=sys.stderr)
        return 2
    counts: collections.Counter = collections.Counter()
    cursor = None
    pages = 0
    while True:
        args = {"kind": "wrong_questions", "limit": 200}
        if cursor:
            args["cursor"] = cursor
        page = call_tool(token, "export_my_data", args)
        for item in page.get("items") or []:
            counts[item.get("subject_name") or "（未分類）"] += 1
        pages += 1
        cursor = page.get("next_cursor")
        if not page.get("has_more") or not cursor or pages >= 50:
            break
    total = sum(counts.values())
    print(f"錯題共 {total} 題，依科目：")
    for subject, n in counts.most_common():
        print(f"  {subject}: {n}（{n / total:.0%}）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
