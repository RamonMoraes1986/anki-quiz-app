import streamlit as st
import json
import random

# Carrega o banco de perguntas diretamente
with open("perguntas.json", "r", encoding="utf-8") as f:
    perguntas = json.load(f)

# Escolhe uma pergunta aleatória
if "pergunta_atual" not in st.session_state:
    st.session_state.pergunta_atual = random.choice(perguntas)
    st.session_state.resposta_usuario = None
    st.session_state.enviou_resposta = False

pergunta = st.session_state.pergunta_atual

st.title("📚 Quiz de Simulado - CFP Módulo 4")
st.markdown(f"**{pergunta['pergunta']}**")

# Exibe as alternativas
resposta_escolhida = st.radio("Escolha uma alternativa:", pergunta["alternativas"], index=None)

# Botão para confirmar a resposta
if st.button("✅ Confirmar resposta") and resposta_escolhida:
    st.session_state.resposta_usuario = resposta_escolhida
    st.session_state.enviou_resposta = True

# Exibe o resultado
if st.session_state.enviou_resposta:
    resposta_correta = pergunta["resposta_correta"]

    # Destaca a resposta correta em verde
    for alternativa in pergunta["alternativas"]:
        if alternativa.startswith(resposta_correta):
            st.success(f"✅ {alternativa}")
        elif alternativa == st.session_state.resposta_usuario:
            st.error(f"❌ {alternativa}")
        else:
            st.write(alternativa)

    # Botão para próxima pergunta
    if st.button("➡️ Próxima pergunta"):
        st.session_state.pergunta_atual = random.choice(perguntas)
        st.session_state.resposta_usuario = None
        st.session_state.enviou_resposta = False
        st.rerun()
