import os
from crewai import Agent, Task, Crew, Process

from crewai_tools import CSVSearchTool
from dotenv import load_dotenv
load = load_dotenv()

os.environ["OPENAI_API_KEY"]
os.environ["SERPER_API_KEY"] 


tool_resersh = CSVSearchTool(csv='/home/gemac/Documents/langchain-agent/rag-agent/agents/csv/data/Catálogo de serviços CIASC - Página1.csv')






writer = Agent(
  role='Analista de dados senior',
  goal=' analisar os dados internos da planilha.',
  backstory="""analista de dados""",
  verbose=True,
  allow_delegation=True,
  tool = tool_resersh
  )



task1 = Task(
  description="""analista de planilha eletronica""",
  expected_output="listagem de todos os emails",
  agent=writer
)




# Instantiate your crew with a sequential process
crew = Crew(
  agents=[writer],
  tasks=[task1],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)