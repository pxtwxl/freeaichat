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

# def chunk_iterator(chat_history, chunk_size):
#     for i in range(0, len(chat_history), chunk_size):
#         yield chat_history[i:i + chunk_size]

# def main():
#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = []
    
#     st.markdown('<div style="display: flex; justify-content: center; max-width=300px"></div>', unsafe_allow_html=True)
#     st.image("chatbottxt.png",use_column_width=True)
#     st.title("Chatbot")
#     user_input = st.text_input("You:")
    
#     if st.button("Send"):
#         if user_input:
#             # st.session_state.chat_history.append(f"You: {user_input}")
#             output = query({
#                 "parameters": {
#                     "max_new_tokens": 2048,
#                     "temperature" : 0.8,
#                     "top_p":0.8,
#                     "top_k":45
#                 },
#                 "inputs": user_input,
#             })
#             bot_response = output[0]["generated_text"]
#             bot_response = bot_response.replace(user_input, "").strip()
#             # st.session_state.chat_history.append(f"\nBot: {bot_response}")
#             st.session_state.chat_history.append((user_input,bot_response))

#             st.subheader("Response")
#             st.write("Bot:", bot_response)
#     st.subheader("Chat History")
    
#     for i,(user_input, bot_response) in enumerate(st.session_state.chat_history[:-1]):
#             st.write(f"<p class='you'>You : \n{user_input}</p>", unsafe_allow_html=True)
#             st.write(f"<p class='bot'>Bot : \n{bot_response}</p>", unsafe_allow_html=True)


# if __name__ == "__main__":
#     main()

import streamlit as st
import requests

st.set_page_config(page_title="FreeChatAI", page_icon="cbico.ico")

# Top bar HTML code with sidebar button
sidebar_js = """
<script>
function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
}
</script>
"""

# Sidebar HTML code
sidebar = """
<div id="mySidebar" class="sidebar" style="position: fixed; top: 0; left: 0; height: 100%; width: 0; z-index: 1; background-color: #333; padding-top: 60px; transition: 0.5s;">
    <a href="javascript:void(0)" class="closebtn" onclick="closeNav()" style="position: absolute; top: 10px; right: 10px; font-size: 36px; color: white;">&times;</a>
    <div style="padding: 10px;">
        <h2 style="color: white;">Navigation</h2>
        <a href="#" style="color: white; text-decoration: none;">Home</a>
        <a href="#" style="color: white; text-decoration: none;">About</a>
        <!-- Add more sidebar links as needed -->
    </div>
</div>
"""

# Inject the sidebar JavaScript and HTML into the Streamlit app
st.markdown(sidebar_js, unsafe_allow_html=True)
# st.markdown(top_bar, unsafe_allow_html=True)
st.markdown(sidebar, unsafe_allow_html=True)

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

def main():
    st.sidebar.image("chatbotsb.png", use_column_width=True)
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("Go to", ["Chat", "About"])

    if menu_selection == "Chat":
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        st.markdown('<div style="display: flex; justify-content: center; max-width=300px"></div>', unsafe_allow_html=True)
        st.image("chatbottxt.png",use_column_width=True)
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
                st.write(f"Bot: {chat_pair['Bot']}")

    elif menu_selection == "About":
        st.title("About")
        st.write("This is an AI chatbot application using Streamlit.")
        # Add more about information here

if __name__ == "__main__":
    main()


