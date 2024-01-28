Un llm pour étre efficace a besoin de données et d accès à des ressources externes 
- en interne dans ses paramètres
- dans son contexte
- en rag
- via un web query (première ressource externe)
- via des api et un traitement python

  Coder une ia en langchain est très performant mais difficile. ce n est plus le cas si on lui dit comment : l idée est de lui faire digérer une video youtube avec un exemple donné sur le site.
  A partir de là il crée un mode d emploi:
  comment créer des skills
  comment créer des modèles
  comment créer des agents
  comment créer des workflows

  plus besoin d ihm comme autogen studio.

  il reste à bâtir le workflow mais des pistes existent pour l optimiser
  
Nous allons réaliser un tuto pour que le llm puisse programmer de lui même le code Langchain associé à des tâches complexes.

## Installation des packages et initialisation des variables (sous windows)
'''
pip install langchain langgraph langchain_openai langchainhub langsmith duckduckgo-search beautifulsoup4 gradio
$env OPENAI_API_KEY=xxxxxxxxxx
$env LANGCHAIN_API_KEY=xxxxxxxxxx
'''
## Programme principal : app.py
### import des packages requis ( à adapter au besoin spécifique)
```
import functools, operator, requests, os, json
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.messages import BaseMessage, HumanMessage
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import StateGraph, END
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from typing import Annotated, Any, Dict, List, Optional, Sequence, TypedDict
import gradio as gr
```

###  Set environment variables
```
os.environ["LANGCHAIN_TRACING_V2"] = "true" # to tell LangChain to log traces
os.environ["LANGCHAIN_PROJECT"] = "LangGraph Research Agents"
```
###  Initialize model (openAI)
```
llm = ChatOpenAI(model="gpt-4-turbo-preview")
```
### Initialize model (local)
```
from langchain.chat_models.openai import ChatOpenAI
openai = ChatOpenAI(
    model_name="your-model-name",
    openai_api_key="not needed ",
    openai_api_base="http://localhost:1234/v1"
)
```
### Define custom tools (à adapter au besoin)
```
@tool("internet_search", return_direct=False)
def internet_search(query: str) -> str:
    """Searches the internet using DuckDuckGo."""
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=5)]
        return results if results else "No results found."

@tool("process_content", return_direct=False)
def process_content(url: str) -> str:
    """Processes content from a webpage."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()

tools = [internet_search, process_content]
``` 
### LangChain Agent Creation Tutorial

#### Helper Function for Creating Agents
To create an agent, define a function `create_agent` that takes the language model, tools, and a system prompt as arguments:

```python
def create_agent(llm: ChatOpenAI, tools: list, system_prompt: str):
    # Define the prompt template for the agent
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    # Create the agent
    agent = create_openai_tools_agent(llm, tools, prompt)
    # Create an executor to manage the agent's actions
    executor = AgentExecutor(agent=agent, tools=tools)
    return executor
```
- **Define Agent Nodes**
- Agent nodes are defined to handle the state and action of each agent:

```python
def agent_node(state, agent, name):
    result = agent.invoke(state)
    return {"messages": [HumanMessage(content=result["output"], name=name)]}
```
- **Supervisor Agent Creation**
- A supervisor agent oversees the dialogue and interactions between different agents:

```python
members = ["Web_Searcher", "Insight_Researcher"]
system_prompt = ("As a supervisor, your role is to oversee a dialogue between these"
    " workers: {members}. Based on the user's request,"
    " determine which worker should take the next action. Each worker is responsible for"
    " executing a specific task and reporting back their findings and progress. Once all tasks are complete,"
    " indicate with 'FINISH'.")

options = ["FINISH"] + members
function_def = {
    "name": "route",
    "description": "Select the next role.",
    "parameters": {
        "title": "routeSchema",
        "type": "object",
        "properties": {"next": {"title": "Next", "anyOf": [{"enum": options}] }},
        "required": ["next"],
    },
}

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="messages"),
    ("system", "Given the conversation above, who should act next? Or should we FINISH? Select one of: {options}"),
]).partial(options=str(options), members=", ".join(members))


supervisor_chain = (prompt | llm.bind_functions(functions=[function_def], function_call="route") | JsonOutputFunctionsParser())
```
- **Creating Specific Agents and node**
- Example of creating a Web Searcher and Insight Researcher agent:

```python
search_agent = create_agent(llm, tools, "You are a web searcher. Search the internet for information."))
search_node = functools.partial(agent_node, agent=search_agent, name="Web_Searcher")

insights_research_agent = create_agent(llm, tools, """You are a Insight Researcher. Do step by step. 
        Based on the provided content first identify the list of topics,
        then search internet for each topic one by one
        and finally find insights for each topic one by one.
        Include the insights and sources in the final response
        """)
insights_research_node = functools.partial(agent_node, agent=insights_research_agent, name="Insight_Researcher")
```

#### Define the Agent State
```
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    next: str

workflow = StateGraph(AgentState)
workflow.add_node("Web_Searcher", search_node)
workflow.add_node("Insight_Researcher", insights_research_node)
workflow.add_node("supervisor", supervisor_chain)    #le node du superviseur est la chaîne Langchain
```
#### Define edges
- **Code example**
```
for member in members:
    workflow.add_edge(member, "supervisor")

conditional_map = {k: k for k in members}
conditional_map["FINISH"] = END
workflow.add_conditional_edges("supervisor", lambda x: x["next"], conditional_map)
workflow.set_entry_point("supervisor")
graph = workflow.compile()
```
- Explication:
Let's consider an example where the supervisor requests the insights_research_agent to act, and then asks for the workflow to terminate:

Workflow Execution Begins: The workflow starts at the supervisor node because we set it as the entry point.

Supervisor Requests insights_research_agent: The supervisor, based on the user's request or internal logic, decides that the insights_research_agent should act next. The condition evaluated for the next action (say, based on the user input or some internal decision logic) returns the string "Insight_Researcher" (the name of the insights_research_agent).

Conditional Map Lookup: The workflow looks up "Insight_Researcher" in the conditional_map. Since we defined conditional_map as {k: k for k in members}, it finds that "Insight_Researcher" maps to itself.

insights_research_agent Acts: The workflow transitions to the insights_research_agent, allowing it to perform its designated task.

Request for Termination: Once the insights_research_agent completes its task, let's assume the supervisor decides to terminate the workflow. This decision is represented by the condition returning "FINISH".

Conditional Map for Termination: The workflow checks the conditional_map for "FINISH". It finds that "FINISH" maps to END.

Workflow Ends: Since "FINISH" maps to END, the workflow understands that no further actions are required and thus terminates.

This example demonstrates how the conditional_map guides the workflow's path based on conditions evaluated at the supervisor node

#### Run the graph
```
for s in graph.stream({
    "messages": [HumanMessage(content="""Search for the latest AI technology trends in 2024,
            summarize the content. After summarise pass it on to insight researcher
            to provide insights for each topic""")]
}):
    if "__end__" not in s:
        print(s)
        print("----")

# final_response = graph.invoke({
#     "messages": [HumanMessage(
#         content="""Search for the latest AI technology trends in 2024,
#                 summarize the content
#                 and provide insights for each topic.""")]
# })

# print(final_response['messages'][1].content)
```


