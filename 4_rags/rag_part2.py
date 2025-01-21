import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_chroma import Chroma

current_dir = os.path.dirname(os.path.abspath(__file__))
chrom_db = os.path.join(current_dir, 'db')

embeddings = OpenAIEmbeddings(model='text-embedding-3-small')

db = Chroma(
    persist_directory = chrom_db,
    embedding_function = embeddings
)

query = '''
    What all tables are required to create the customer behavior table?
'''

retriever = db.as_retriever(
    search_type = 'similarity_score_threshold',
    search_kwargs={"k": 1, "score_threshold": 0.2},
)

relevant_doc = retriever.invoke(query)

# print(relevant_doc[0].page_content)

combined_input = f'''
    I will supply you the relevant docs to answer my query:
    {query}

    Doc:
    {relevant_doc[0].page_content}

    The first line in doc contains the file name.

    You need to answer only using the relevant docs, if not possible then pls respond with "No Answer Found"
'''

llm = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage('You are a Data Warehouse expert'),
    HumanMessage(combined_input)
]

result = llm.invoke(messages)

print(result.content)

'''
To create the customer behavior table, the following tables are required:

1. **lake.sales** - This table is needed to get transaction details such as `transaction_id`, `quantity`, and `total_amount`.
2. **dim.customers** - This table is needed to link customer information with their respective behavior data, using the `customer_id` and `customer_key`. 

Thus, the two tables required are:
- lake.sales
- dim.customers
'''