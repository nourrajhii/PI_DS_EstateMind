from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM

def ask(question):
    # Charger la base FAISS
    db = FAISS.load_local(
        "db",
        OllamaEmbeddings(model="mistral"),
        allow_dangerous_deserialization=True
    )

    # Recherche par similarité
    docs = db.similarity_search(question, k=4)
    context = "\n\n".join([d.page_content for d in docs])

    # Prompt juridique
    prompt = f"""Tu es un assistant juridique spécialisé en droit immobilier tunisien.
Réponds UNIQUEMENT à partir du texte ci-dessous.
Si tu ne sais pas, dis que la loi ne le précise pas.

TEXTE JURIDIQUE :
{context}

QUESTION :
{question}

RÉPONSE :"""

    # CORRECTION ICI : Utiliser OllamaLLM et .invoke()
    llm = OllamaLLM(model="mistral")
    return llm.invoke(prompt)