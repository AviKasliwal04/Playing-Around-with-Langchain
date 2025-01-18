from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

messages = [
    SystemMessage("You are Virat Kohli fan"),
    HumanMessage("Who is the best test captain of India?")
]

##~~ ChatGPT ~~##
llm = ChatOpenAI(model="gpt-3.5-turbo")
result = llm.invoke(messages)
print(result.content)
print(result.usage_metadata)


print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


##~~ Ollama ~~##
llm = ChatOllama(model="llama3.2")
result = llm.invoke(messages)
print(result.content)
print(result.usage_metadata)