from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# 設置 OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# 定義請求結構
class ChatRequest(BaseModel):
    chat_history: list  # 使用者與 AI 的對話歷史紀錄
    faq_list: list      # FAQ 列表
    product_list: list  # 產品列表

# 設計 prompt
def generate_prompt(chat_history, faq_list, product_list):
    prompt = f"""
    你是一個專業的 AI 客服助手，幫助用戶在與品牌互動時獲得最佳的聊天體驗。
    請根據聊天記錄、FAQ 列表以及產品列表，生成 2-3 個建議回應，以促使用戶繼續對話。
    
    **聊天歷史:**
    {chat_history}

    **常見問題 (FAQ):**
    {faq_list}

    **產品列表:**
    {product_list}

    **請輸出建議回應 (quick replies)，確保符合用戶需求並促使互動。**
    """
    return prompt

# API 端點: 生成 Quick Replies
@app.post("/generate_quick_replies/")
async def generate_quick_replies(request: ChatRequest):
    try:
        prompt = generate_prompt(request.chat_history, request.faq_list, request.product_list)

        # 調用 OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}]
        )

        quick_replies = response["choices"][0]["message"]["content"]
        return {"quick_replies": quick_replies}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))