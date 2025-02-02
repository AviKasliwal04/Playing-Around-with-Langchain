import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
# from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

current_path = os.path.dirname(__file__)
code_directory = os.path.join(current_path, 'sql_codes')
vector_db_directory = os.path.join(current_path, 'db')

FORCE_RUN = False

if not os.path.exists(vector_db_directory) or FORCE_RUN == True:
    
    sql_files = [f for f in os.listdir(code_directory) if f.endswith('.sql')]

    sql_codes = []

    for sql_file in sql_files:
        sql_path = os.path.join(code_directory, sql_file)

        loader = TextLoader(sql_path)
        sqls = loader.load()

        for sql in sqls:
            sql.metadata = {'source': sql_file}
            sql_codes.append(sql)

    
    text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 50)
    sql_codes_chunked = text_splitter.split_documents(sql_codes)

    print('Sql Codes Chunked into {x} parts'.format(x = len(sql_codes_chunked)))
    print(f'Sample chunk: {sql_codes_chunked[0]}\n\n\n')

    embeddings = OllamaEmbeddings(model='mxbai-embed-large')
    print ('Embeding created')


    db = Chroma.from_documents(
        documents = sql_codes_chunked,
        embedding = embeddings,
        persist_directory = vector_db_directory
    )
    print('Vector DB created')
else:
    print('Vector DB already exists')