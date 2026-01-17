from dotenv import load_dotenv
import streamlit as st

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model= "gemini-2.5-flash")

st.title("QNA AI Bot using Gemini-2.5-flash")
st.markdown("Ask any question and get answers powered by Gemini-2.5-flash!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message['role']
    content = message['content']
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask me anything")

if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.session_state.messages.append({"role": "ai", "content": res.content})
    st.chat_message('ai').markdown(res.content)


# que = "who is the president of India?"

# res = llm.invoke(que)
# print(res.content)

# while True:
#     que = input('user:')

#     if que.lower() in ['exit', 'quit','bye']:
#         print("Exiting the QNA bot. Goodbye!")
#         break

#     result = llm.invoke(que)
#     print(result.content)