import streamlit as st
import requests

st.markdown(
   """
    <style>
    body {
        background-color: #000000;
        color: #FFFFFF;
    }
    .you{
       font-size: 16px;
       font-style: bold;
    }
    .bot{
       font-size: 16px;
       font-style: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def chunk_iterator(chat_history, chunk_size):
    for i in range(0, len(chat_history), chunk_size):
        yield chat_history[i:i + chunk_size]

def main():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    st.markdown('<div style="display: flex; justify-content: center; max-width=300px"></div>', unsafe_allow_html=True)
    st.image("chatbot.png",use_column_width=True)
    st.title("Chatbot")
    user_input = st.text_input("You:")

    st.markdown("""
       <script>
           document.addEventListener('DOMContentLoaded', function() {
               const user_input = document.getElementById('user_input');
               user_input.addEventListener('keyup', function(event) {
                   if (event.key === 'Enter') {
                       document.getElementById('send_button').click();
                   }
               });
           });
       </script>
    """, unsafe_allow_html=True)
    
    if st.button("Send"):
        if user_input:
            # st.session_state.chat_history.append(f"You: {user_input}")
            output = query({
                "parameters": {
                    "max_new_tokens": 2048,
                    "temperature" : 0.8,
                    "top_p":0.7
                },
                "inputs": user_input,
            })
            bot_response = output[0]["generated_text"]
            bot_response = bot_response.replace(user_input, "").strip()
            # st.session_state.chat_history.append(f"\nBot: {bot_response}")
            st.session_state.chat_history.append((user_input,bot_response))

            st.subheader("Response")
            st.write("Bot:", bot_response)
    st.subheader("Chat History")
    
    for i,(user_input, bot_response) in enumerate(st.session_state.chat_history[:-1]):
            st.write(f"<p class='you'>You: {user_input}</p>", unsafe_allow_html=True)
            st.write(f"<p class='bot'>Bot: {bot_response}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
