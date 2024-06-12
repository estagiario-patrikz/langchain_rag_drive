from dotenv import load_dotenv
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI

from langchain_experimental.agents import create_csv_agent 
from langchain.llms import OpenAI 


df = pd.read_csv("/home/gemac/Documents/langchain-agent/rag-agent/agents/csv/data/Catálogo de serviços CIASC - Página1.csv")
llm = ChatOpenAI(temperature = 0.4, OPENAI_API_KEY="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")


agent_execute = create_csv_agent(llm,df)
print(agent_execute.invoke("Quais são os numeros de telefone presente nos canais de atendimento?"))