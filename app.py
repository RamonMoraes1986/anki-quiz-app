import streamlit as st
import json
import random

# Carrega o banco de perguntas
with open("perguntas.json", "r", encoding="utf-8") as f:
    perguntas = json.load(f)

# Escolhe uma pergunta aleatória
pergunta = random.choice(perguntas)

st.title("Responder Quiz")

# Exibe a pergunta
st.write(f"**{pergunta['pergunta']}**")

# Inicializa sessão
if "resposta_usuario" not in st.session_state:
    st.session_state.resposta_usuario = None

# Exibe as alternativas como botões de rádio
alternativa_escolhida = st.radio("Escolha uma alternativa:", pergunta["alternativas"], index=None)

# Botão para enviar resposta
if st.button("Confirmar resposta"):
    st.session_state.resposta_usuario = alternativa_escolhida

# Exibe o resultado após a escolha
if st.session_state.resposta_usuario:
    st.markdown("## Resultado:")

    for alt in pergunta["alternativas"]:
        letra = alt[0]  # A letra da alternativa (A, B, C ou D)

        if alt == st.session_state.resposta_usuario:
            if letra == pergunta["resposta_correta"]:
                st.success(alt)  # Alternativa correta escolhida → verde
            else:
                st.error(alt)  # Alternativa incorreta escolhida → vermelha
        elif letra == pergunta["resposta_correta"]:
            st.success(alt)  # Exibe a correta mesmo se o usuário errou
        else:
            st.write(alt)  # Outras alternativas normais
