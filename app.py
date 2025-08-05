import streamlit as st
import json
import os

ARQUIVO_DE_PERGUNTAS = "questions.json"

def carregar_perguntas():
    if os.path.exists(ARQUIVO_DE_PERGUNTAS):
        with open(ARQUIVO_DE_PERGUNTAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_perguntas(questoes):
    with open(ARQUIVO_DE_PERGUNTAS, "w", encoding="utf-8") as f:
        json.dump(questoes, f, ensure_ascii=False, indent=4)

def estilo_alternativa(alternativa, selecionada, correta):
    if selecionada == alternativa and selecionada == correta:
        return f":green[{alternativa}]"
    elif selecionada == alternativa and selecionada != correta:
        return f":red[{alternativa}]"
    elif alternativa == correta:
        return f":green[{alternativa}]"
    else:
        return alternativa

st.set_page_config(page_title="Anki Quiz – Web para iPhone 📱")

st.title("Anki Quiz – Web para iPhone 📱")

menu = st.sidebar.radio("Menu", ["Inserir Questões", "Responder Quiz"])
perguntas = carregar_perguntas()

if menu == "Inserir Questões":
    st.header("Adicionar nova questão")
    nova_pergunta = st.text_input("Pergunta:")
    nova_alternativa_a = st.text_input("Alternativa A:")
    nova_alternativa_b = st.text_input("Alternativa B:")
    nova_alternativa_c = st.text_input("Alternativa C:")
    nova_alternativa_d = st.text_input("Alternativa D:")
    nova_correta = st.selectbox("Letra da alternativa correta:", ["A", "B", "C", "D"])

    if st.button("Salvar"):
        nova_questao = {
            "id": len(perguntas) + 1,
            "pergunta": nova_pergunta,
            "alternativas": [
                f"A) {nova_alternativa_a}",
                f"B) {nova_alternativa_b}",
                f"C) {nova_alternativa_c}",
                f"D) {nova_alternativa_d}",
            ],
            "resposta_correta": f"{nova_correta})"
        }
        perguntas.append(nova_questao)
        salvar_perguntas(perguntas)
        st.success("Questão adicionada com sucesso!")

elif menu == "Responder Quiz":
    st.header("Responder Quiz")
    for pergunta in perguntas:
        st.markdown(f"**{pergunta['pergunta']}**")
        resposta = st.radio("Escolha uma alternativa:", pergunta["alternativas"], key=pergunta["id"])
        if resposta:
            st.markdown("### Resultado:")
            for alt in pergunta["alternativas"]:
                st.markdown(estilo_alternativa(alt, resposta, pergunta["resposta_correta"]))
            st.markdown("---")
