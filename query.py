from llama_index.core import VectorStoreIndex, QueryBundle, Response, Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from index import es_vector_store

# Local LLM to send user query to
local_llm = Ollama(model="mistral")
Settings.embed_model = OllamaEmbedding("mistral")

index = VectorStoreIndex.from_vector_store(es_vector_store)
query_engine = index.as_query_engine(local_llm, similarity_top_k=10)

def answer_query(query):
    bundle = QueryBundle(query, embedding=Settings.embed_model.get_query_embedding(query))
    result = query_engine.query(bundle)
    print(result)
    
#answer_query("Quelle est la capitale de la Belgique")
#answer_query("Give me summary of water related issue")
answer_query("Que dit Emily Rodriguez? (merci de répondre en français)")
#answer_query("Quelles sont les personnes qui interviennent dans les conversations ?")


