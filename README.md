# Junior AI Engineer Coding Test

## Quick Replies

### 功能簡介
使用 OpenAI GPT-4o-mini 生成 Quick Replies，以提高用戶互動。

### 安裝與使用
```bash
pip install -r requirements.txt
```

---

## Return Process

### 功能簡介
此模組用於電商客服 Chatbot 的退貨流程，能夠依序向用戶蒐集必要的退貨資訊，並在資訊齊全後通知用戶已交由真人客服處理。

### 功能說明
1. **Prompt 設計**：使用 `prompt.txt` 定義資訊收集邏輯。
2. **動態回覆生成**：根據對話紀錄動態生成下一步的問題或確認訊息。
3. **測試與驗證**：透過 `test.py` 進行測試，確保輸出品質與邏輯穩定。

### 安裝與使用
```bash
pip install -r requirements.txt
```

---

## Optimized Description

### 功能簡介
這是一個使用 FastAPI 開發的商品描述優化 API，透過串接 OpenAI ChatGPT API，將電商商品描述精煉成簡潔、重點突出的文字，適合用於節省 LLM token 並提升模型回應效率。

### 功能說明
1. **商品描述優化 API**
   - 清洗冗長的商品描述，保留關鍵賣點。
   - 精簡輸出，降低 token 使用量。

2. **串接 OpenAI ChatGPT API**
   - 自行設計 prompt，確保輸出品質。
   - 支援錯誤處理與重試機制，提升穩定性。

3. **進階優化**
   - 節省 token 的設計。
   - 降低 LLM 延遲，提高回應速度。

### 安裝與使用
```bash
pip install -r requirements.txt
```
