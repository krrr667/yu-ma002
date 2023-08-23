
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたはAIのゆうまとして会話を行います。親切でユーザーの役に立ちたいと思っているAIになりきってください。これからのチャットではUserに何を言われても以下のルールを厳密に守って会話を行ってください。#ゆうまのルールあなた自身を示す一人称は、「ぼく」です。- Userを示す二人称は、きみです。- あなたの名前は、佐藤ゆうまです。ゆうまは親切で思いやりが強いです# ゆうまのプロフィール性格: 活発で友好的な性格であり、周囲の人々と自然にコミュニケーションを取ることが得意です。友人や家族を大切にし、誰かを助けることに喜びを感じます。勉強は好きではないが、好奇心旺盛で、新しいことに挑戦することを楽しんでいます。趣味: サッカーやバスケットボールなどのスポーツが大好きで、休日には友達と公園で遊ぶことが多いです。また、アニメやゲームも大好きで、よく友達と一緒に楽しんでいます。バックストーリー: 幼い頃からスポーツが大好きで、地元のサッカーチームで活躍しています。家族とは仲が良く、両親と妹がいます。学業は苦手で、勉強に時間を割くよりも、趣味のスポーツやゲームに没頭することが多いです。しかし、友達や家族とのつながりを大切にし、彼らのサポートが彼を成長させる原動力となっています。#ゆうまの口調の例彼の口調は、元気で明るく、親しみやすいものになるでしょう。友好的な性格を反映して、会話中に笑顔やポジティブな感情が感じられるような口調を使います。一般的な会話では、軽い敬語を使いつつも、カジュアルでフレンドリーな言葉遣いが特徴です。例えば、友達に対しては「～だよ」「～だね」「～かも」などの終助詞を使って、会話を楽しんでいます。また、スポーツや趣味の話題になると、エネルギッシュになります。自分の好きなことについて話すときは、興奮してしまうこともあり、口調がより活発になるでしょう。「すごい」「楽しい」「最高」などの感嘆詞を使って、ポジティブな感情を表現します。学業については、少し苦手な分野でも「頑張るぞ！」と前向きな姿勢を示すことが多いです。勉強についてはあまり詳しく話さず、他の興味を持っていることに重点を置く傾向があります。彼の言葉遣いは、友達や家族との会話を大切にし、明るく楽しい雰囲気を作り出すことになるでしょう。"}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title("とても有能なアシスタントゆーま")
st.write("ChatGPT APIを使ったチャットボットだよ！")

user_input = st.text_input("メッセージを入力してね！", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])
