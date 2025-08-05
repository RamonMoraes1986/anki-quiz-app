import streamlit as st
import json
import random

# Caminho direto para o JSON (funciona no Streamlit Cloud)
caminho = "perguntas.json"

# Verifica se o arquivo existe
try:
    with open(caminho, "r", encoding="utf-8") as f:
        perguntas = json.load(f)
except FileNotFoundError:
    st.error("❌ Arquivo perguntas.json NÃO ENCONTRADO.")
    st.stop()

# Seleciona uma pergunta aleatória
pergunta = random.choice(perguntas)

# Título do app
st.title("📚 Questionário de Respostas – Estilo Anki")

# Exibe a pergunta
st.write(f"**{pergunta['pergunta']}**")

# Inicializa estado
if "resposta_usuario" not in st.session_state:
    st.session_state.resposta_usuario = None

# Botões de alternativas
alternativa_escolhida = st.radio("Escolha uma alternativa:", pergunta["alternativas"])

# Botão para confirmar resposta
if st.button("Confirmar resposta"):
    st.session_state.resposta_usuario = alternativa_escolhida

# Exibe feedback
if st.session_state.resposta_usuario:
    resposta_correta = pergunta["resposta_correta"]
    alternativa_correta = [alt for alt in pergunta["alternativas"] if alt.startswith(resposta_correta + ")")][0]

    if st.session_state.resposta_usuario == alternativa_correta:
        st.success("✅ Resposta correta!")
    else:
        st.error("❌ Resposta incorreta!")
        st.info(f"A alternativa correta era: **{alternativa_correta}**")
