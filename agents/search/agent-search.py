import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI
from crewai_tools import YoutubeVideoSearchTool


os.environ["OPENAI_API_KEY"]
os.environ["SERPER_API_KEY"]  


search_tool = SerperDevTool()
tool = YoutubeVideoSearchTool()


researcher = Agent(
  role='Engenheiro de dados senior',
  goal='Objetivo de pesquisar no canal do youtube e fazer resumos de videos ',
  backstory=""". Experiência: Pesquisador experiente no CIASC, expert em encontrar vídeos relevantes no Youtube.
    Missão: Guardião da informação no Youtube para o CIASC, buscando vídeos valiosos e impactantes.
    Impacto: Contribui para o avanço do CIASC, conectando-o ao conhecimento e garantindo que esteja à frente da curva.""",
  verbose=True,
  allow_delegation=False,
  tools=[tool],
  memory= True,
  llm=ChatOpenAI(model_name="gpt-4", temperature=0.2)
)
writer = Agent(
  role='escritor de blogs tecnicos de tecnologia',
  goal='objetivo de documentar de fomra detalhada os processos tecnicos de tecnologia de acordo com a base de conhecimento fornecida',
  backstory="""Você é um renomado estrategista de conteúdo, conhecido por seus artigos perspicazes e envolventes.
  Você transforma conceitos complexos em narrativas convincentes.""",
  verbose=True,
  allow_delegation=False,
  tools=[tool],
  memory= True,
  llm=ChatOpenAI(model_name="gpt-4", temperature=0.2)
)

task1 = Task(
  description="""conduza uma analise no canal do youtube do ciasc sobre como configurar a vpn detranet.""",
  expected_output="mostrar o passo a passo em detalhes de como configurar a vpn do detranet",
  agent=researcher
)

task2 = Task(
  description=""" usando os insigths fornecidos desenvolva um blog técnico de como se dá o processo de
  download e configuração da vpn de forma detalhada. Vale ressatar que o conteudo 
  deverá ser em linguagem simples para que os mais leigos entendam.""",
  expected_output="postagem completa de como funciona o passo a passo",
  agent=researcher
)

# Instantiate your crew with a sequential process
# crew = Crew(
#   agents=[researcher, writer],
#   tasks=[task1, task2],
#   verbose=2, # You can set it to 1 or 2 to different logging levels
# )

crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)