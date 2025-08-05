import streamlit as st
import json
import random
import os

# Caminho absoluto para o arquivo perguntas.json
caminho = os.path.join(os.path.dirname(__file__), "perguntas.json")

# Verifica se o arquivo existe antes de tentar abrir
if not os.path.exists(caminho):
    st.error("❌ Arquivo perguntas.json NÃO ENCONTRADO.")
    st.stop()

# Carrega o banco de perguntas
with open(caminho, "r", encoding="utf-8") as f:
    perguntas = json.load(f)

# Escolhe uma pergunta aleatória
pergunta = random.choice(perguntas)

# Título do app
st.title("📚 Questionário de Respostas – Estilo Anki")

# Exibe a pergunta
st.write(f"**{pergunta['pergunta']}**")

# Inicializa a sessão se necessário
if "resposta_usuario" not in st.session_state:
    st.session_state.resposta_usuario = None

# Exibe alternativas como botões de rádio
alternativa_escolhida = st.radio("Escolha uma alternativa:", pergunta["alternativas"])

# Botão de confirmação de resposta
if st.button("Confirmar resposta"):
    st.session_state.resposta_usuario = alternativa_escolhida

# Exibe o feedback visual após confirmação
if st.session_state.resposta_usuario:
    resposta_correta = pergunta["resposta_correta"]

    # Identifica o índice da alternativa correta
    alternativa_correta = [alt for alt in pergunta["alternativas"] if alt.startswith(resposta_correta + ")")][0]

    if st.session_state.resposta_usuario == alternativa_correta:
        st.success("✅ Resposta correta!")
    else:
        st.error("❌ Resposta incorreta!")
        st.info(f"A alternativa correta era: **{alternativa_correta}**")
