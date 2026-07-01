from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain.messages import SystemMessage , HumanMessage , AIMessage

MODEL = 'gemini-2.5-flash-lite'
model = ChatGoogleGenerativeAI(model = MODEL)

chat_history = []
while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(user_input))
    if user_input == 'exit':
        break
    else:
      result =  model.invoke(chat_history)
      chat_history.append(AIMessage(result.content))
      print("AI: ",result.content)

print(chat_history)