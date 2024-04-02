import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def main():
    st.markdown('<div style="display: flex; justify-content: center;"><img src="chatbot.png" style="width: 500px;"></div>', unsafe_allow_html=True)
    # st.image("chatbot.png",use_column_width=True)
    st.title("Chatbot")
    user_input = st.text_input("You:")
    if st.button("Send"):
        if user_input:
            output = query({
                "parameters": {
                    "max_new_tokens": 2048,
                },
                "inputs": user_input,
            })
            bot_response = output[0]["generated_text"]
            st.write("Bot:", bot_response)

if __name__ == "__main__":
    main()
