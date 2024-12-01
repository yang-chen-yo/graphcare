import os
import openai

# 讀取 openai.key 檔案內容
#with open("../../resources/openai.key", 'r') as f:
#    lines = f.readlines()
#    api_url = lines[0].split("API URL")[1].strip()  # 解析 API URL
#    api_key = lines[1].split("API KEY")[1].strip()  # 解析 API KEY


#print(api_url)
#print(api_key)
# 設定 OpenAI 的 API 基本參數
#openai.api_base = api_url  # 設定自訂 API URL
#openai.api_key = api_key   # 設定 API Key

openai.api_base = "https://free.v36.cm/v1"
openai.api_key = "sk-RFCn5XAIanQqIw5eB0C58d15328246769b87D2355fAf6192"

class ChatGPT:
    def __init__(self):
        self.messages = []

    def chat(self, message):
        self.messages.append({"role": "user", "content": message})
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini  # 替換為正確的模型名稱
                messages=self.messages
            )
            # 取得助理回覆並追加到對話紀錄中
            assistant_message = response["choices"][0]["message"]["content"]
            self.messages.append({"role": "assistant", "content": assistant_message})
            return assistant_message
        except Exception as e:
            return f"Error: {str(e)}"
