from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableSequence

load_dotenv()

model = ChatOpenAI(model = 'gpt-4o-mini')

messages = [
    ("system", "you are expert in the sport {sport}"),
    ("human", "Tell me the field dimensions for {sport} and also give me some {trivia_count} trivia(s) about it"),
]

prompt_template = ChatPromptTemplate.from_messages(messages)

format_prompt = RunnableLambda(lambda data: prompt_template.format_prompt(**data))
# print (prompt_template.format_prompt(**{"sport": "golf", "trivia_count": 3}))
# messages=[SystemMessage(content='you are expert in the sport golf', additional_kwargs={}, response_metadata={}), HumanMessage(content='Tell me the field dimensions for golf and also give me some 3 trivia(s) about it', additional_kwargs={}, response_metadata={})]

invoke_model = RunnableLambda(lambda prompt: model.invoke(prompt.to_messages())) # redundant to_messages() call
# invoke_model = RunnableLambda(lambda prompt: model.invoke(prompt)) # this also worked


parse_output = RunnableLambda(lambda output: output.content + "\n\n\n" + str(output.response_metadata))

chain = RunnableSequence(first = format_prompt, middle = [invoke_model], last = parse_output)

res = chain.invoke({"sport": "f1", "trivia_count": 1})
print(res)

# print('----- trying to understand why to_messages was required? -----')
# print(prompt_template.format_prompt(**{"sport": "golf", "trivia_count": 3}))
# print('-----')
# print(prompt_template.format_prompt(**{"sport": "golf", "trivia_count": 3}).to_messages())

'''
messages=[SystemMessage(content='you are expert in the sport golf', additional_kwargs={}, response_metadata={}), HumanMessage(content='Tell me the field dimensions for golf and also give me some 3 trivia(s) about it', additional_kwargs={}, response_metadata={})]
-----
[SystemMessage(content='you are expert in the sport golf', additional_kwargs={}, response_metadata={}), HumanMessage(content='Tell me the field dimensions for golf and also give me some 3 trivia(s) about it', additional_kwargs={}, response_metadata={})]
'''



'''
In Formula 1, the dimensions of a standard racetrack can vary widely, as each circuit is unique. However, there are general characteristics:

### Field Dimensions:
- **Length**: The minimum length for a Grand Prix circuit is 3.5 kilometers (approximately 2.2 miles), but most tracks are longer, with many measuring between 4 and 7 kilometers (about 2.5 to 4.3 miles).
- **Width**: Race tracks typically have a width of about 10-15 meters (33-49 feet). Some circuits, especially those designed for overtaking, can be wider in areas.
- **Pit Lane**: The width of the pit lane can vary but is usually around 12-15 meters (39-49 feet).
- **Run-off Areas**: These areas vary in size depending on the track design, but they are generally designed to provide safety and can extend several meters beyond the circuit's edge.

### Trivia:
One interesting trivia about F1 is that the fastest lap record in a Formula 1 race as of 2023 is held by Lewis Hamilton, who set a lap time of 1:19.119 during the 2020 Belgian Grand Prix at the Spa-Francorchamps circuit. This track is known for its high-speed sections and challenging layout, which includes iconic corners like Eau Rouge and Raidillon. Hamilton's record reflects not only his skill as a driver but also the extraordinary engineering of the Mercedes car that year.


{'token_usage': {'completion_tokens': 304, 'prompt_tokens': 39, 'total_tokens': 343, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_72ed7ab54c', 'finish_reason': 'stop', 'logprobs': None}

'''