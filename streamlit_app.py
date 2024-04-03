import streamlit as st
import requests
import pyperclip

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
    
    if st.button("Send"):
        if user_input:
            # st.session_state.chat_history.append(f"You: {user_input}")
            output = query({
                "parameters": {
                    "max_new_tokens": 2048,
                    "temperature" : 0.8,
                    "top_p":0.8,
                    "top_k":45
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

   copy_icon = "<svg aria-hidden='true' focusable='false' data-prefix='far' data-icon='copy' class='svg-inline--fa fa-copy fa-w-14' role='img' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 448 512'><path fill='currentColor' d='M368 80h-88c-26.5 0-48 21.5-48 48v272c0 26.5 21.5 48 48 48h88c26.5 0 48-21.5 48-48V128c0-26.5-21.5-48-48-48zm-16 304c0 8.8-7.2 16-16 16h-88c-8.8 0-16-7.2-16-16V128c0-8.8 7.2-16 16-16h88c8.8 0 16 7.2 16 16v256zm-96-272h-48c-13.3 0-24 10.7-24 24s10.7 24 24 24h48c13.3 0 24-10.7 24-24s-10.7-24-24-24zm0 96h-48c-13.3 0-24 10.7-24 24s10.7 24 24 24h48c13.3 0 24-10.7 24-24s-10.7-24-24-24zm0 96h-48c-13.3 0-24 10.7-24 24s10.7 24 24 24h48c13.3 0 24-10.7 24-24s-10.7-24-24-24z'></path></svg>"
    regenerate_icon = "<svg aria-hidden='true' focusable='false' data-prefix='far' data-icon='redo' class='svg-inline--fa fa-redo fa-w-16' role='img' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'><path fill='currentColor' d='M16.1 262.9c4.7 7.5 15.7 8.5 21.9 1.9l47-45.8C96.4 216.1 136.8 192 192 192c106 0 192 86 192 192 0 50.9-20.4 98.7-56.6 134.7l-21.3-21.3c-10.1-10.1-23.6-15.7-37.7-15.7-29.5 0-53.5 24-53.5 53.5s24 53.5 53.5 53.5 53.5-24 53.5-53.5V362.7c0-13.1-5.1-25.5-14.3-34.7l-57-57c-7.5-7.5-19.8-7.5-27.3 0s-7.5 19.8 0 27.3l57 57c9.4 9.4 14.6 21.8 14.6 34.7v106.8c0 53-43 96-96 96s-96-43-96-96c0-40.6 25-75.6 60.2-90.2l-68.7-68.7c-6.2-6.2-5.2-17.2 1.9-21.9z'></path></svg>"
    clear_icon = "<svg aria-hidden='true' focusable='false' data-prefix='far' data-icon='trash-alt' class='svg-inline--fa fa-trash-alt fa-w-14' role='img' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 448 512'><path fill='currentColor' d='M16 80v40c0 13.3 10.7 24 24 24h360c13.3 0 24-10.7 24-24V80c0-13.3-10.7-24-24-24H40C26.7 56 16 66.7 16 80zm328 312c0 6.6-5.4 12-12 12H116c-6.6 0-12-5.4-12-12V192h240v200zm-64-200H196v-88h84c6.6 0 12-5.4 12-12s-5.4-12-12-12h-84c-26.5 0-48 21.5-48 48v88c0 26.5 21.5 48 48 48h148c6.6 0 12-5.4 12-12s-5.4-12-12-12zm96-304H88c-13.3 0-24 10.7-24 24v40h352v-40c0-13.3-10.7-24-24-24z'></path></svg>"

    if st.button(f"{copy_icon} Copy Bot Response"):
        last_bot_response = st.session_state.chat_history[-1][1]
        pyperclip.copy(last_bot_response)
        st.write("Bot response copied to clipboard!")

    if st.button(f"{regenerate_icon} Regenerate Bot Response"):
        last_user_input = st.session_state.chat_history[-1][0]
        output = query({
            "parameters": {
                "max_new_tokens": 2048,
                "temperature" : 0.8,
                "top_p":0.7
            },
            "inputs": last_user_input,
        })
        new_bot_response = output[0]["generated_text"]
        new_bot_response = new_bot_response.replace(last_user_input, "").strip()
        st.session_state.chat_history[-1] = (last_user_input, new_bot_response)
        st.write("Bot response regenerated!")

    if st.button(f"{clear_icon} Clear Chat History"):
        st.session_state.chat_history.clear()
        st.write("Chat history cleared!")

if __name__ == "__main__":
    main()
