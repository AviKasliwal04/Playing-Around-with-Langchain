from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

template = "Write a {tone} poem dedicated to Virat Kohli's {skill}, please keep it max 6 lines. Also give poem a {title_type} title."

# Now the template above is in plain english which is not understood by langchain as is, we need to convert it to a format that langchain can understand

prompt_template = ChatPromptTemplate.from_template(template)
# print(prompt_template)
# input_variables=['skill', 'tone'] input_types={} partial_variables={} messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['skill', 'tone'], input_types={}, partial_variables={}, template="Write a {tone} poem dedicated to Virat Kohli's {skill}"), additional_kwargs={})]

prompt = prompt_template.invoke({
    'skill': "batting and fielding",
    'tone': "firey",
    'title_type': "kickass"
})

# print(prompt) # messages=[HumanMessage(content="Write a funny poem dedicated to Virat Kohli's batting", additional_kwargs={}, response_metadata={})]

response = llm.invoke(prompt)
print(response.content)
print(response.response_metadata)

# Title: "Kohli's Batting Bliss"

# With a wave of his mighty bat,
# Virat Kohli swings like a cat.
# Fielders tremble, bowlers fret,
# As he smashes boundaries without a sweat.

# His shots are pure magic, it's plain to see,
# Virat Kohli, the king of the cricketing spree!
# {'token_usage': {'completion_tokens': 72, 'prompt_tokens': 37, 'total_tokens': 109, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}


# Title: The Fire Within

# Virat Kohli, a blazing inferno at the crease,
# His bat a weapon, his eyes a fierce feast.
# Fielding like a demon, he roams with speed,
# Opponents tremble, knowing defeat is a lockheed.
# In the realm of cricket, he is the king supreme,
# Virat Kohli, a fiery force that cannot be redeemed.
# {'token_usage': {'completion_tokens': 81, 'prompt_tokens': 40, 'total_tokens': 121, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}