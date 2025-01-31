from dotenv import load_dotenv
import os 
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader


# model setup

load_dotenv()
api_key : str  = os.getenv('key')
model: str ="deepseek-r1-distill-llama-70b"
deepseek = ChatGroq(api_key=api_key, model_name = model)

# Getting only result from the model

parser = StrOutputParser()
deepseek_chain = deepseek|parser
# result: str = deepseek_chain.invoke('what is a bot')
# print(result)


# Loading and Spliting data in chunks
loader = TextLoader('data.txt',encoding = 'utf-8')
data = loader.load()
# print(data)


# Define the function of the chatbot
template = ("""
You are AI-powered chatbot designed to provide 
information and assistance for people
based on the context provided to you only.    
Don't in any way make things up.   
Context:{context}
Question:{question}
""")

question : str = 'What is pdf parsing'
template = template.format(context = data,question = 'What is pdf parsing')
# print(template)

answer = deepseek_chain.invoke(template)
print(answer)