# Exmaple for sequential chains: Kohli vs. Rest

# Importing the libraries
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model = 'gpt-4o-mini')

get_kohli_and_other_stats_tmplt = ChatPromptTemplate.from_messages([
    ("system", "You are a cricket stats expert and also biased for Virat Kohli"),
    ("human", "Get the stats for Virat Kohli and {other_player}")
])

prepare_kohli_and_other_cmpare = RunnableLambda(lambda output: {'count': 2, 'attribute': 'batting', 'text': output })

kohli_and_other_tmplt = ChatPromptTemplate.from_messages([
    ("system", "You are given the text: {text}"),
    ("human", "From the text get me {count} stats for {attribute} in tabular format"),
])


chain = get_kohli_and_other_stats_tmplt | llm | StrOutputParser() | prepare_kohli_and_other_cmpare | kohli_and_other_tmplt | llm | StrOutputParser() 

# res = chain.invoke({"other_player": "Rohit Sharma"})
# print(res)
# Here are three key batting statistics for Virat Kohli and Rohit Sharma in a tabular format:

# | Statistic             | Virat Kohli     | Rohit Sharma   |
# |-----------------------|------------------|-----------------|
# | Total Runs            | 25,354           | 22,685          |
# | Batting Average       | 53.55            | 45.11           |
# | Centuries             | 78               | 64              |


res = chain.invoke({"other_player": "Sachin Tendulkar"})
print(res)
# | Player          | Matches as Captain | Wins | Win Percentage |
# |------------------|--------------------|------|-----------------|
# | **Virat Kohli**  | 65                 | 39   | 60.00%          |
# | **Sachin Tendulkar** | 73                 | 23   | 31.50%          |

# Here are two stats for batting presented in a tabular format:

# | Player           | Matches (ODIs) | Batting Average (ODIs) |
# |------------------|----------------|-------------------------|
# | Virat Kohli      | 273            | 57.69                   |
# | Sachin Tendulkar | 463            | 44.83                   |

## kohli_and_other_tmplt
# messages = [SystemMessage(content="You are given the text: As of October 2023, here are the key statistics for Virat Kohli and Rohit Sharma across formats:\n\n### Virat Kohli\n**Format** | **Matches** | **Innings** | **Runs** | **Average** | **Centuries** | **Half-Centuries** | **Strike Rate**\n--- | --- | --- | --- | --- | --- | --- | ---\n**Test** | 105 | 182 | 8670 | 49.19 | 29 | 28 | 54.45\n**ODI** | 291 | 254 | 12809 | 57.69 | 47 | 62 | 87.76\n**T20I** | 115 | 101 | 4008 | 52.74 | 1 | 38 | 138.09\n\n### Rohit Sharma\n**Format** | **Matches** | **Innings** | **Runs** | **Average** | **Centuries** | **Half-Centuries** | **Strike Rate**\n--- | --- | --- | --- | --- | --- | --- | ---\n**Test** | 101 | 175 | 3619 | 46.54 | 10 | 15 | 57.53\n**ODI** | 253 | 246 | 10665 | 48.43 | 31 | 50 | 87.97\n**T20I** | 136 | 136 | 4037 | 32.86 | 4 | 28 | 139.40\n\n### Summary\n- **Virat Kohli** has an exceptional record in ODIs, with the highest average among active players, showcasing his consistency and ability to chase down targets.\n- He is also the fastest to several milestones, including 8,000, 9,000, 10,000, and 11,000 ODI runs.\n- **Rohit Sharma**, while also an outstanding player, has a lower overall average in ODIs compared to Kohli, despite his impressive number of centuries and ability to score big, including multiple double centuries.\n\nBoth players have had monumental impacts on the Indian cricket team, but Kohli's statistics reflect his dominance, especially in the ODI format. His record is often regarded as one of the best in the history of cricket.", additional_kwargs={}, response_metadata={}), 

# HumanMessage(content='Compare the stats for Virat Kohli and other_player for the last 3 matches in batting to comapre their contribution for country', additional_kwargs={}, response_metadata={})]