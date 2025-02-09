import re

def load_prompt_template():
    with open('prompt.txt', 'r', encoding='utf-8') as file:
        return file.read()

def extract_info(content, field):
    """
    根據欄位類型提取資訊
    """
    if field == "姓名":
        match = re.search(r"(姓名[:：]?\s*)(\S+)", content)
        if match:
            return match.group(2)
        elif len(content.strip()) <= 5:  # 假設姓名不超過 5 個字
            return content.strip()
    elif field == "電話":
        match = re.search(r"(\d{8,11})", content)
        if match:
            return match.group(1)
    elif field == "訂單單號":
        match = re.search(r"(A\d{6,})", content)
        if match:
            return match.group(1)
    elif field == "退貨品名":
        # 偵測常見商品名稱或簡單輸入
        match = re.search(r"(品名[:：]?\s*)([\w\u4e00-\u9fff]{2,20})", content)
        if match:
            return match.group(2)
        # 如果沒有品名標籤，則直接偵測輸入是否可能是商品名稱
        if len(content.strip()) >= 2 and len(content.strip()) <= 20:
            return content.strip()
    elif field == "退貨理由":
        # 改進退貨理由的判斷邏輯
        common_reasons = [
            "不滿意", "瑕疵", "損壞", "尺寸不合", "收到錯誤商品",
            "品質不好", "不符合預期", "變形", "功能故障", "寄錯"
        ]
        # 檢查是否包含常見退貨理由
        if any(reason in content for reason in common_reasons):
            return content.strip()
        # 若句子超過 5 個字，視為可能的退貨理由
        if len(content.strip()) > 5:
            return content.strip()

    return None  # 若無法提取資訊則返回 None

def generate_return_prompt(history):
    prompt_template = load_prompt_template()
    required_fields = ["姓名", "電話", "訂單單號", "退貨品名", "退貨理由"]

    # 解析已提供的資訊
    collected_info = {}
    for message in history:
        if message["role"] == "user":
            for field in required_fields:
                if field not in collected_info:  # 尚未收集該欄位
                    extracted = extract_info(message["content"], field)
                    if extracted:
                        collected_info[field] = extracted

    # 找出缺少的資訊
    missing_fields = [field for field in required_fields if field not in collected_info]

    if missing_fields:
        return f"請提供您的{missing_fields[0]}。"

    return "感謝您的資訊，我們已將您的退貨申請提交給真人客服，請稍候處理。"
