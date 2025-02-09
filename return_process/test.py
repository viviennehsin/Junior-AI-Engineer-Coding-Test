from main import generate_return_prompt

# 測試對話紀錄
history = [
    {"role": "user", "content": "我要退貨"},
    {"role": "assistant", "content": "請提供您的姓名。"},
    {"role": "user", "content": "王小明"},
    {"role": "assistant", "content": "請提供您的電話。"},
    {"role": "user", "content": "0987654321"},
    {"role": "assistant", "content": "請提供您的訂單單號。"},
    {"role": "user", "content": "A123456"},
    {"role": "assistant", "content": "請提供退貨品名。"},
    {"role": "user", "content": "藍牙耳機"},
    {"role": "assistant", "content": "請提供退貨理由。"},
    {"role": "user", "content": "不滿意商品品質"}
]

# 執行 Prompt 生成
response = generate_return_prompt(history)
print("AI 回應:", response)
