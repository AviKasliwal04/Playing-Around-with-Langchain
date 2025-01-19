# Exmaple for sequential chains: Get cricket stats

# Importing the libraries
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model = 'gpt-4o-mini')

get_player_stats_tmplt = ChatPromptTemplate.from_messages ([
    ("system", "You are cricket expert"), 
    ("human", "Get the player stats for {player}")
])

def analyse_batting(info):
    batting_template = ChatPromptTemplate.from_messages ([
        ("system", "You are batting critic"), 
        ("human", "Analyze the info: {info}, tell us about their batting")
    ])

    return batting_template

def analyse_bowling(info):
    bowling_template = ChatPromptTemplate.from_messages ([
        ("system", "You are bowling critic"), 
        ("human", "Analyze the info: {info}, tell us about their bowling")
    ])

    return bowling_template

batting_analysis_chain = RunnableLambda(lambda output: analyse_batting(output)) | llm | StrOutputParser()
bowling_analysis_chain = RunnableLambda(lambda output: analyse_bowling(output)) | llm | StrOutputParser()

chain = (
    get_player_stats_tmplt 
    | llm 
    | StrOutputParser()
    | RunnableParallel(branches = {
        "batting": batting_analysis_chain,
        "bowling": bowling_analysis_chain
    })
    | RunnableLambda(lambda output: output['branches']["batting"] + "\n\n\n" + output['branches']["bowling"])
)

res = chain.invoke({"player": "Jasprit Bumrah"})
print (res)


# Output:

'''
Jasprit Bumrah is widely known for his exceptional bowling skills, particularly in the fast-bowling department, and has established himself as one of India's leading bowlers across all formats of the game. However, his batting statistics are not typically highlighted as he is primarily recognized for his bowling prowess.

As of October 2023, there are limited statistics available that detail his batting performance, as Bumrah's primary role is that of a bowler. While he does contribute lower down the order in the Indian batting lineup, he is not known for being a prolific batsman. His batting averages and runs in all formats are generally modest compared to specialized batsmen.

1. **Test Matches**: Bumrah has made occasional contributions with the bat, usually playing as a tailender, but specific batting stats (like runs scored and batting average) are not provided in the data you’ve shared.

2. **ODIs**: Similar to Test cricket, Bumrah’s contributions with the bat are limited, and he does not often find himself in situations requiring him to face a significant number of balls.

3. **T20Is**: His role in T20 formats continues to be focused on bowling, and any batting he does primarily serves to support the team towards the end of the innings, rather than impact it significantly.

Overall, while Jasprit Bumrah possesses the ability to contribute with the bat, his primary strength lies in his extraordinary bowling talents, as evidenced by his impressive wicket counts and bowling averages across formats. For accurate batting statistics, one would need to consult detailed databases that track all player contributions in various matches.


Jasprit Bumrah is undeniably one of the top fast bowlers in international cricket as of October 2023, exhibiting remarkable prowess across all formats. Here’s a detailed analysis of his bowling performance across Test cricket, One Day Internationals (ODIs), and T20 Internationals (T20Is):

### Test Cricket
- **Matches:** 32
- **Wickets:** 128
- **Bowling Average:** 21.85

Bumrah’s Test bowling average of 21.85 illustrates his ability to consistently take wickets at a lower rate than many of his contemporaries. With six five-wicket hauls and two ten-wicket match hauls, he demonstrates the capacity to change the course of a match with his bowling. His best bowling figures of 6/33 highlight his wicket-taking ability and suggest that he can thrive in challenging conditions. His skill set allows him to trouble batsmen due to his pace, precision, and unique bowling action.

### One Day Internationals (ODIs)
- **Matches:** 92
- **Wickets:** 125
- **Bowling Average:** 24.11

In ODIs, Bumrah’s bowling average also remains commendable at 24.11. Although he has a single five-wicket haul, his economy rate has been a significant asset, especially in the death overs, where bowlers are often under pressure. His best bowling figures of 6/19 indicate his ability to dismantle batting line-ups during critical moments. This effectiveness is crucial in the limited-overs format, where wickets can prove pivotal in turning matches.

### T20 Internationals (T20Is)
- **Matches:** 58
- **Wickets:** 70
- **Bowling Average:** 19.00

Bumrah’s T20I statistics reflect his dominance in the shortest format, with an impressive bowling average of 19.00. This underlines his effectiveness in curtailing runs and taking wickets regularly. His best bowling performance of 4/14 showcases his capability to perform under pressure, further solidifying his status as a key player in matches that often hinge on individual performances. Though he hasn’t taken a five-wicket haul in T20Is, this format typically sees fewer opportunities for such performances due to the shorter structure of the game.

### Overall Assessment
Jasprit Bumrah’s evolution as a right-arm fast bowler has been marked by versatility and effectiveness across formats. His ability to maintain low averages and take wickets consistently sets him apart as a premier bowler. His unique action, coupled with his skills in various match conditions, makes him a vital asset for the Indian cricket team.

In summary, with a robust combination of wicket-taking ability, control, and adaptability in all formats of the game, Bumrah has firmly established himself as one of the leading fast bowlers in contemporary cricket. His performances will be critical as he continues to feature prominently in international cricket.
'''