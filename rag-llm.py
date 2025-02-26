from langchain_community.llms import Ollama
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain

def connect():
    url = "bolt://localhost:7687"
    username="neo4j"
    password="Password123" # Update with your password
    graph = Neo4jGraph(url, username, password)
    return graph

def init_model():
    llm = Ollama(model="llama3:latest")
    return llm

def run_prompt(prompt, llm, graph):
    chain = GraphCypherQAChain.from_llm(
        llm, graph=graph, verbose=True
    )
    result = chain.invoke({"query": prompt})
    return result['result']

def main():
    graph = connect()
    llm = init_model()
    prompt = "Show me everyone that owns a Project?"
    result = run_prompt(prompt, llm, graph)
    print(result)

if __name__ == "__main__":
    main()