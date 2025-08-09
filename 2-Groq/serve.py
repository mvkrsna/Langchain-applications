from fastapi import FastAPI
# Importing the ChatGroq for using Groq api for inferencing
from langchain_groq import ChatGroq

# Importing the Chat Prompt Template
from langchain_core.prompts import ChatPromptTemplate

# Importing the Str Output Parser
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
# adding the routes from langserve
from langserve import add_routes

load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")
model=ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)
system_template="Translate the following to {language}:"
prompt=ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])
parser=StrOutputParser()
chain=prompt|model|parser

# App Definition
app=FastAPI(title="Langchain Server", 
            version="1.0",
            description="description about the project")

##adding chain routes
add_routes(app, chain, path="/chain")

# res=chain.invoke({"language":"French", "text":"hi how are you"})
# print(res)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

