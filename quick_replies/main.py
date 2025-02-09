import openai
import json
import time
import os

# 正確初始化 OpenAI 客戶端
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai.api_key)

def generate_quick_replies(chat_history):
    with open("prompt.txt", "r", encoding="utf-8") as file:
        prompt = file.read()

    formatted_prompt = prompt.format(chat_history=json.dumps(chat_history, ensure_ascii=False))

    try:
        start_time = time.time()

        # 呼叫 API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": formatted_prompt}],
            max_tokens=100,
            temperature=0.7
        )

        end_time = time.time()
        response_time = end_time - start_time

        content = response.choices[0].message.content
        print("DEBUG - Model Response:", content)

        try:
            reply_data = json.loads(content)
            if "quick_replies" not in reply_data:
                raise KeyError("缺少 'quick_replies' 欄位！")
        except json.JSONDecodeError:
            raise ValueError("模型回應的內容不是有效的 JSON 格式。")

        return reply_data, response_time

    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}, None

