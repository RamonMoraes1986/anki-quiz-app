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

def estilo_alternativa(alternativa, resposta_usuario, resposta_correta):
    if alternativa == resposta_usuario and alternativa == resposta_correta:
        return f"<span style='color: green;'>{alternativa}</span>"
    elif alternativa == resposta_usuario and alternativa != resposta_correta:
        return f"<span style='color: red;'>{alternativa}</span>"
    elif alternativa == resposta_correta:
        return f"<span style='color: green;'>{alternativa}</span>"
    else:
        return alternativa

st.set_page_config(page_title="Anki Quiz – Web para iPhone 📱")

st.title("Anki Quiz – Web para iPhone 📱")

menu = st.sidebar.radio("Menu", ["Inserir Questões", "Responder Quiz"])

perguntas = carregar_perguntas()

if menu == "Inserir Questões":
    st.header("Adicionar nova questão")

    pergunta = st.text_input("Digite a pergunta:")
    alternativa_a = st.text_input("Alternativa A")
    alternativa_b = st.text_input("Alternativa B")
    alternativa_c = st.text_input("Alternativa C")
    alternativa_d = st.text_input("Alternativa D")
    resposta_correta = st.selectbox("Qual é a alternativa correta?", ["A", "B", "C", "D"])

    if st.button("Salvar questão"):
        nova_questao = {
            "id": len(perguntas) + 1,
            "pergunta": pergunta,
            "alternativas": [
                f"A) {alternativa_a}",
                f"B) {alternativa_b}",
                f"C) {alternativa_c}",
                f"D) {alternativa_d}"
            ],
            "resposta_correta": f"{resposta_correta}) {locals()['alternativa_' + resposta_correta.lower()]}"
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
                st.markdown(estilo_alternativa(alt, resposta, pergunta["resposta_correta"]), unsafe_allow_html=True)
            st.markdown("---")
