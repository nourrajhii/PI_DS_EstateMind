import streamlit as st
from rag import ask
import os

# Configuration de la page
st.set_page_config(
    page_title="Assistant Juridique Immobilier Tunisien",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour un meilleur design
st.markdown("""
<style>
    /* Fond et couleurs principales */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Titre principal */
    .title-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .title-text {
        color: white;
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
        text-align: center;
    }
    
    .subtitle-text {
        color: #e0e7ff;
        font-size: 1.1rem;
        margin-top: 0.5rem;
        text-align: center;
    }
    
    /* Zone de chat */
    .stChatMessage {
        background-color: white;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Boutons d'exemple */
    .example-button {
        background-color: white;
        border: 2px solid #667eea;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .example-button:hover {
        background-color: #667eea;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(102,126,234,0.3);
    }
    
    /* Zone d'information */
    .info-box {
        background-color: #e0e7ff;
        border-left: 4px solid #667eea;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    /* Disclaimer */
    .disclaimer {
        background-color: #fef3c7;
        border-left: 4px solid #f59e0b;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# En-tête personnalisé
st.markdown("""
<div class="title-container">
    <h1 class="title-text">⚖️ Assistant Juridique Immobilier</h1>
    <p class="subtitle-text">Expert en droit immobilier tunisien - Réponses basées sur les textes de loi</p>
</div>
""", unsafe_allow_html=True)

# Vérifier si la base existe
if not os.path.exists("db"):
    st.error("❌ **Base de données non trouvée**")
    st.info("👉 Exécutez d'abord la commande : `python build_db.py`")
    st.stop()

# Sidebar avec informations
with st.sidebar:
    st.markdown("### 📚 Domaines couverts")
    st.markdown("""
    - 📋 **Baux d'habitation**
    - 🏢 **Vente immobilière**
    - 💰 **Fiscalité immobilière**
    - 📝 **Procédures notariales**
    - ⚖️ **Droits réels**
    - 🏗️ **Copropriété**
    """)
    
    st.markdown("---")
    
    st.markdown("### ℹ️ Comment ça marche ?")
    st.markdown("""
    1. **Posez** votre question
    2. L'IA **recherche** dans les textes de loi
    3. Vous recevez une **réponse précise** avec les articles pertinents
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Avertissement Important")
    st.warning("""
    Cet outil fournit des **informations juridiques générales**, 
    pas des conseils juridiques personnalisés.
    
    Pour votre situation spécifique, consultez un **avocat** ou un **notaire**.
    """)
    
    st.markdown("---")
    
    if st.button("🔄 Nouvelle conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.caption("💡 Propulsé par Mistral AI & Ollama")

# Initialiser l'historique
if "messages" not in st.session_state:
    st.session_state.messages = []

# Afficher l'historique des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🧑" if message["role"] == "user" else "⚖️"):
        st.markdown(message["content"])

# Zone de saisie
if question := st.chat_input("💬 Posez votre question juridique ici..."):
    # Ajouter et afficher la question
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(question)
    
    # Générer et afficher la réponse
    with st.chat_message("assistant", avatar="⚖️"):
        with st.spinner("🔍 Recherche dans les textes juridiques..."):
            try:
                response = ask(question)
                
                # Afficher la réponse
                st.markdown(response)
                
                # Ajouter le disclaimer
                st.markdown("""
                <div class="disclaimer">
                    <strong>⚠️ Disclaimer :</strong> Cette réponse est basée sur les textes de loi disponibles 
                    dans la base de données. Elle constitue une information juridique générale et ne remplace 
                    pas un conseil juridique personnalisé d'un avocat ou notaire.
                </div>
                """, unsafe_allow_html=True)
                
                # Sauvegarder dans l'historique
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                st.error(f"❌ **Erreur :** {str(e)}")
                st.info("💡 **Solutions possibles :**\n- Vérifiez qu'Ollama est lancé\n- Vérifiez que le modèle Mistral est installé")

# Exemples de questions (affiché uniquement si pas de conversation)
if not st.session_state.messages:
    st.markdown("### 💡 Questions fréquentes")
    st.markdown("*Cliquez sur une question pour commencer*")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📝 Comment enregistrer un bail immobilier ?", use_container_width=True):
            st.session_state.messages.append({
                "role": "user", 
                "content": "Comment enregistrer un bail immobilier en Tunisie ?"
            })
            st.rerun()
        
        if st.button("⏱️ Quelle est la durée minimale d'un bail ?", use_container_width=True):
            st.session_state.messages.append({
                "role": "user",
                "content": "Quelle est la durée minimale d'un bail à usage d'habitation ?"
            })
            st.rerun()
        
        if st.button("💰 Quels sont les droits d'enregistrement ?", use_container_width=True):
            st.session_state.messages.append({
                "role": "user",
                "content": "Quels sont les droits d'enregistrement pour l'achat d'un bien immobilier ?"
            })
            st.rerun()
    
    with col2:
        if st.button("🚪 Comment résilier un bail ?", use_container_width=True):
            st.session_state.messages.append({
                "role": "user",
                "content": "Quelles sont les conditions pour résilier un bail ?"
            })
            st.rerun()
        
        if st.button("📄 Quelles sont les obligations du bailleur ?", use_container_width=True):
            st.session_state.messages.append({
                "role": "user",
                "content": "Quelles sont les obligations légales du bailleur ?"
            })
            st.rerun()
        
        if st.button("🏢 Comment acheter un bien immobilier ?", use_container_width=True):
            st.session_state.messages.append({
                "role": "user",
                "content": "Quelle est la procédure d'achat d'un bien immobilier en Tunisie ?"
            })
            st.rerun()
    
    # Section d'information
    st.markdown("---")
    st.markdown("""
    <div class="info-box">
        <h4>📖 À propos de cet assistant</h4>
        <p>
            Cet assistant juridique utilise l'intelligence artificielle pour vous fournir 
            des informations précises basées sur les textes de loi tunisiens en vigueur 
            concernant l'immobilier. Les réponses sont générées à partir d'une base de 
            connaissances juridiques certifiée.
        </p>
    </div>
    """, unsafe_allow_html=True)