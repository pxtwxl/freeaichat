# import streamlit as st
# import requests

# st.set_page_config(page_title="FreeChatAI", page_icon="cbico.ico")

# st.markdown(
#    """
#     <style>
#     body {
#         background-color: #000000;
#         color: #FFFFFF;
#     }
#     .you{
#        font-size: 16px;
#        font-style: bold;
#     }
#     .bot{
#        font-size: 16px;
#        font-style: bold;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()

# def main():
#     st.sidebar.image("chatbotsb.png", use_column_width=True)
#     st.sidebar.title("Navigation")
#     menu_selection = st.sidebar.radio("Go to", ["Chat", "About"])

#     if menu_selection == "Chat":
#         if "chat_history" not in st.session_state:
#             st.session_state.chat_history = []

#         st.markdown('<div style="display: flex; justify-content: center; max-width=300px"></div>', unsafe_allow_html=True)
#         st.image("chatbottxt.png",use_column_width=True)
#         st.title("Chatbot")
#         user_input = st.text_input("You:")

#         if st.button("Send"):
#             if user_input:
#                 output = query({
#                     "parameters": {
#                         "max_new_tokens": 2048,
#                         "temperature" : 0.8,
#                         "top_p":0.8,
#                         "top_k":45
#                     },
#                     "inputs": user_input,
#                 })
#                 bot_response = output[0]["generated_text"]
#                 bot_response = bot_response.replace(user_input, "").strip()
#                 st.session_state.chat_history.append({"You": user_input, "Bot": bot_response})

#                 st.subheader("Response")
#                 st.write("Bot:", bot_response)

#         st.sidebar.subheader("Chat History")
#         for i, chat_pair in enumerate(st.session_state.chat_history):
#             if st.sidebar.button(chat_pair['You']):
#                 st.write(f"Bot: {chat_pair['Bot']}")

#     elif menu_selection == "About":
#         st.title("About")
#         st.write("This is an AI chatbot application using Streamlit.")
#         # Add more about information here

# if __name__ == "__main__":
#     main()

import streamlit as st
import requests

st.set_page_config(page_title="FreeChatAI", page_icon="cbico.ico")

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
       overflow-wrap: break-word; /* Wrap long words */
       word-wrap: break-word; /* Wrap long words */
       word-break: break-all; /* Break long words */
       white-space: nowrap; /* Prevent wrapping */
       max-width: 300px; /* Limit width */
       display: inline-block; /* Ensure inline display */
    }
    .bot{
       font-size: 16px;
       font-style: bold;
       overflow-wrap: break-word; /* Wrap long words */
       word-wrap: break-word; /* Wrap long words */
       word-break: break-all; /* Break long words */
       white-space: normal; /* Handle overflow */
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

def main():
    st.sidebar.image("chatbotsb.png", use_column_width=True)
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("Go to", ["Chat", "About"])

    if menu_selection == "Chat":
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        st.markdown('<div style="display: flex; justify-content: center; max-width: 300px;"></div>', unsafe_allow_html=True)
        st.image("chatbottxt.png", use_column_width=True)
        st.title("Chatbot")
        user_input = st.text_input("You:")

        if st.button("Send"):
            if user_input:
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
                st.session_state.chat_history.append({"You": user_input, "Bot": bot_response})

                st.subheader("Response")
                st.write("Bot:", bot_response)

        st.sidebar.subheader("Chat History")
        for i, chat_pair in enumerate(st.session_state.chat_history):
            if st.sidebar.button(chat_pair['You']):
                st.sidebar.write(f"Bot: {chat_pair['Bot']}")

    elif menu_selection == "About":
        st.title("About")
        st.write("This is an AI chatbot application using Streamlit.")
        # Add more about information here

if __name__ == "__main__":
    main()

