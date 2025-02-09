from main import generate_quick_replies
import statistics

# 測試資料
chat_history = [{"role": "user", "content": [{"type": "text", "text": "推薦 3C 產品"}]}]

# 單次測試
replies, response_time = generate_quick_replies(chat_history)
print("Quick Replies:", replies)

# 檢查是否為 None，避免格式化錯誤
if response_time is not None:
    print(f"Response Time: {response_time:.2f} seconds")
else:
    print("Response Time: N/A")

# 多次測試（穩定性測試）
test_results = []
for _ in range(5):
    replies, time_taken = generate_quick_replies(chat_history)
    if time_taken:
        test_results.append(time_taken)

# 統計結果
if test_results:
    average_time = statistics.mean(test_results)
    std_dev_time = statistics.stdev(test_results)
    print(f"Average Response Time: {average_time:.2f} sec")
    print(f"Standard Deviation: {std_dev_time:.2f} sec")
else:
    print("No valid responses received for statistical analysis.")
