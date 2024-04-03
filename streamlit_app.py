import streamlit as st
# from streamlit.state.session_state import SessionState
import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def main():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    st.markdown('<div style="display: flex; justify-content: center; max-width=300px"></div>', unsafe_allow_html=True)
    st.image("chatbot.png",use_column_width=True)
    st.title("Chatbot")
    user_input = st.text_input("You:")
    
    if st.button("Send"):
        if user_input:
            output = query({
                "parameters": {
                    "max_new_tokens": 2048,
                    "temperature" : 0.8,
                    "top_p":0.7
                },
                "inputs": user_input,
            })
            bot_response = output[0]["generated_text"]
            st.session_state.chat_history.append(f"You: {user_input}")
            st.session_state.chat_history.append(f"Bot: {bot_response}")
            
            st.write("Bot:", bot_response)

    st.write("\n".join(st.session_state.chat_history))

if __name__ == "__main__":
    main()
