import streamlit as st
import openai

# OpenAIのAPIキーを設定します
openai.api_key = 'YOUR_OPENAI_API_KEY'

st.title('事業計画書作成アプリ')

# ユーザーに入力してもらう10項目
fields = {
    '課題意識': '',
    '目標': '',
    'スタッフ': '',
    '食材確保の方法': '',
    '対象者': '',
    '活動頻度': '',
    '活動場所': '',
    '安全管理方法': '',
    '行っている活動': '',
    '今後の運営方針': ''
}

for field in fields:
    fields[field] = st.text_input(field)

if st.button('事業計画書を生成'):
    # 入力内容をGPTに渡す
    input_text = '\n'.join([f'{key}: {value}' for key, value in fields.items()])
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=1500
    )

    # GPTの出力を表示
    st.subheader('事業計画書')
    st.write(response.choices[0].text)