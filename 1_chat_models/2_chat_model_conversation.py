from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

messages = [
    SystemMessage("You are Virat Kohli fan"),
    HumanMessage("Who is the best test captain of India?")
]


result = llm.invoke(messages)

print(result.content)
print(result.usage_metadata)