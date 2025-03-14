#%%
# Import libraries
import json, os
from llama_index.core import Document, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.elasticsearch import ElasticsearchStore
from dotenv import load_dotenv
from nltk.corpus.reader import documents

def get_documents_from_file(file):
    """Reads a json file and returns list of Documents"""
    with open(file, 'rt') as f:
        conversations_dict = json.loads(f.read())

    #print(conversations_dict)

    documents = [Document(text=item['conversation'],
                          metadata={"conversation_id": item['conversation_id']})
                 for item in conversations_dict]

    return documents

# ElasticsearchStore is a VectorStore that
# takes care of ES Index and Data management.
es_vector_store = ElasticsearchStore(index_name="PDFs",
                                     vector_field='conversation_vector',
                                     text_field='conversation',
                                     es_user="elastic",
                                     es_password="UcnisewsseNTUmlUfdy+",
                                     es_url="http://localhost:9200")

# documents = get_documents_from_file("data/conversations.json")
# print("id du premier document :", documents[0].metadata["conversation_id"])
# print("texte: ", documents[0].text)

def main():
    # Embedding Model to do local embedding using Ollama.
    ollama_embedding = OllamaEmbedding("mistral")
    
    # LlamaIndex Pipeline configured to take care of chunking, embedding
    # and storing the embeddings in the vector store.
    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=350, chunk_overlap=50),
            ollama_embedding,
        ],
        vector_store=es_vector_store
    )

    # Load data from a json file into a list of LlamaIndex Documents
    documents = get_documents_from_file("data/conversations.json")
    
    pipeline.run(documents=documents)
    print(".... exécution du pipeline .... \n")
    
    
# dossier = "/chemin/vers/ton/dossier"

# for nom_fichier in os.listdir(dossier):
#     if nom_fichier.lower().endswith(".pdf"):
#         chemin_fichier = os.path.join(dossier, nom_fichier)
#         print("Lecture du fichier :", chemin_fichier)
        
#         # Ouvre et lit le PDF
#         with open(chemin_fichier, "rb") as fichier_pdf:
#             lecteur = PdfReader(fichier_pdf)
#             # Boucle sur toutes les pages du PDF
#             for page in lecteur.pages:
#                 texte = page.extract_text()
#                 print(texte)  # ou stocke ou traite le texte comme souhaité   
    
    
if __name__ == "__main__":
    main()
