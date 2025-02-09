# Junior AI Engineer Coding Test

## Quick Replies

### 功能簡介
使用 OpenAI GPT-4o-mini 生成 Quick Replies，以提高用戶互動。

### 安裝與使用
```bash
pip install -r requirements.txt
cd quick_replies
```

## Return Process

### 功能簡介
此模組用於電商客服 Chatbot 的退貨流程，能夠依序向用戶蒐集必要的退貨資訊，並在資訊齊全後通知用戶已交由真人客服處理。

### 功能說明
1. **Prompt 設計**：使用 `prompt.txt` 定義資訊收集邏輯。
2. **動態回覆生成**：根據對話紀錄動態生成下一步的問題或確認訊息。
3. **測試與驗證**：透過 `test.py` 進行測試，確保輸出品質與邏輯穩定。

### 安裝與使用
```bash
cd return_process
```

