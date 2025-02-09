from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
import openai
import os
from tenacity import retry, stop_after_attempt, wait_fixed

# 設定 OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# 初始化 FastAPI
app = FastAPI()

# 定義請求格式
class ProductDescriptionRequest(BaseModel):
    product_name: str
    raw_description: str

# 定義回應格式
class ProductDescriptionResponse(BaseModel):
    summarized_description: str
    status: str
    error: str | None

# 讀取 prompt.txt 並格式化
def load_prompt_template(product_name: str, raw_description: str) -> str:
    try:
        with open("prompt.txt", "r", encoding="utf-8") as file:
            prompt_template = file.read()
        return prompt_template.format(product_name=product_name, raw_description=raw_description)
    except FileNotFoundError:
        raise RuntimeError("找不到 prompt.txt，請確認檔案存在。")

# 重試機制 (最多 3 次，間隔 2 秒)
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def call_openai_api(prompt: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "你是一個幫助優化電商描述的 AI。"},
                      {"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200  # 控制輸出長度，節省 token
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"OpenAI API 呼叫失敗: {str(e)}")

# 定義 API 端點
@app.post("/summarized-description", response_model=ProductDescriptionResponse)
async def summarize_product_description(request: ProductDescriptionRequest):
    try:
        if not request.product_name or not request.raw_description:
            raise HTTPException(status_code=400, detail="商品名稱與描述不可為空")

        prompt = load_prompt_template(request.product_name, request.raw_description)
        summarized_description = call_openai_api(prompt)

        return {
            "summarized_description": summarized_description,
            "status": "success",
            "error": None
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        return {
            "summarized_description": "",
            "status": "error",
            "error": str(e)
        }
