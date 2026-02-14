from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

try:
    # Charger texte juridique
    text = open("data/loi_location.txt", encoding="utf-8").read()

    # Découpage
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    docs = splitter.create_documents([text])

    # Embeddings avec Ollama
    embeddings = OllamaEmbeddings(model="mistral")

    # Base vectorielle FAISS
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("db")

    print("✅ Base juridique créée avec succès")
    
except Exception as e:
    print(f"❌ Erreur : {e}")
    print("\n🔧 Solutions :")
    print("1. Vérifiez qu'Ollama est lancé : ollama serve")
    print("2. Vérifiez que le modèle mistral est installé : ollama pull mistral")
    print("3. Si erreur CUDA, relancez Ollama")