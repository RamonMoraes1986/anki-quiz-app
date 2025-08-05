import streamlit as st
import json
import random
import os

# Caminho seguro para o arquivo JSON
caminho = os.path.join(os.path.dirname(__file__), "perguntas.json")

# Carrega perguntas
with open(caminho, "r", encoding="utf-8") as f:
    perguntas = json.load(f)

# Seleciona uma pergunta aleatória
if "pergunta_atual" not in st.session_state:
    st.session_state.pergunta_atual = random.choice(perguntas)
    st.session_state.resposta_usuario = None
    st.session_state.confirmado = False

pergunta = st.session_state.pergunta_atual

# Exibe pergunta
st.title("Quiz CFP - Simulado Interativo")
st.markdown(f"**{pergunta['pergunta']}**")

# Exibe alternativas
alternativa_escolhida = st.radio("Escolha uma alternativa:", pergunta["alternativas"], index=None)

# Botão de confirmação
if st.button("Confirmar resposta") and alternativa_escolhida:
    st.session_state.resposta_usuario = alternativa_escolhida
    st.session_state.confirmado = True

# Exibe resultado apenas após confirmação
if st.session_state.confirmado:
    resposta_correta = next((alt for alt in pergunta["alternativas"] if alt.startswith(pergunta["resposta_correta"] + ")")), None)

    if st.session_state.resposta_usuario == resposta_correta:
        st.success(f"✅ Resposta correta: {resposta_correta}")
    else:
        st.error(f"❌ Resposta incorreta: {st.session_state.resposta_usuario}")
        st.success(f"✅ Resposta correta: {resposta_correta}")

    if st.button("Próxima pergunta"):
        st.session_state.pergunta_atual = random.choice(perguntas)
        st.session_state.resposta_usuario = None
        st.session_state.confirmado = False
        st.experimental_rerun()
