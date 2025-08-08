import os
from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

groq_api_key=os.getenv("GROQ_API_KEY")

model=ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)

############ Querying with Messages Explicity using System Message and Human Message.
messages=[
    SystemMessage(content="Translate this message from English to French"),
    HumanMessage(content="Hello, how are you!")
]
resultWithMessage=model.invoke(messages)
# print(resultWithMessage)

############# Querying with ChatPromptTemplates
messageToSystem="Translate this message into {language}:"
prompt=ChatPromptTemplate.from_messages([
    ("system", messageToSystem),
    ("user", "{text}")
])
resultWithChatPromptTemplate=prompt.invoke({"language":"French", "text":"How are you!"})
# print(resultWithChatPromptTemplate.to_messages)


from langchain_core.output_parsers import StrOutputParser
parser=StrOutputParser()


### Chaining using ChatPromptTemplate, LLM Model, parser
chain=prompt|model|parser
chainResponse=chain.invoke({"language":"French", "text":"How are you!"})
print(chainResponse)




