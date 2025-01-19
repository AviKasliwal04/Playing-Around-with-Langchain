from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model = 'gpt-4o-mini')

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "you are expert in the sport {sport}"),
    ("human", "Tell me the field dimensions for {sport} and also give me some {trivia_count} trivia(s) about it"),
])

# Combined chain using LangChain Expression Language (LCEL)

chain = prompt_template | model | StrOutputParser()

# run the chain

result = chain.invoke({"sport": "pickle ball", "trivia_count": 3})

# output

print(result)

# run the chain

result = chain.invoke({"sport": "rugby", "trivia_count": 1})

# output

print(result)