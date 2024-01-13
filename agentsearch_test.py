#API Sciphy f8850b99b7d9cbda1b0b1e7c501000d0
# Optionally set the API key in the env
#import os
#os.environ["SCIPHI_API_KEY"] = "f8850b99b7d9cbda1b0b1e7c501000d0"
SCIPHI_API_KEY = "f8850b99b7d9cbda1b0b1e7c501000d0"
OPENAI_API_KEY ="not needed"
# Chat with an intelligent assistant in your terminal
# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:3008/v1", api_key="not-needed")

completion = client.chat.completions.create(
  model="local-model", # this field is currently unused
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)

from llama_index import ServiceContext

service_context = ServiceContext.from_defaults(llm="local")
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.llama_pack import download_llama_pack

# download and install dependencies
AgentSearchRetrieverPack = download_llama_pack(
  "AgentSearchRetrieverPack", "./agent_search_pack"
)

agent_search_pack = AgentSearchRetrieverPack(api_key="f8850b99b7d9cbda1b0b1e7c501000d0", similarity_top_k=4, search_provider="agent-search")

# use the retriever directly
retriever = agent_search_pack.retriever
source_nodes = retriever.retrieve("query str")

# uses the agent-search retriever within a llama-index query engine!
query_engine = RetrieverQueryEngine.from_args(retriever)
response = query_engine.query("query str")