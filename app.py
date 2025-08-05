
import streamlit as st
import json
import os

QUESTIONS_FILE = "questions.json"

def load_questions():
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_questions(questions):
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

st.title("Anki Quiz - Web para iPhone 📱")

menu = st.sidebar.radio("Menu", ["Inserir Questões", "Quiz"])

if menu == "Inserir Questões":
    st.header("Adicionar nova questão")
    question = st.text_area("Pergunta")
    a = st.text_input("Alternativa A")
    b = st.text_input("Alternativa B")
    c = st.text_input("Alternativa C")
    d = st.text_input("Alternativa D")
    correct = st.selectbox("Alternativa correta", ["A", "B", "C", "D"])

    if st.button("Salvar"):
        if question and a and b and c and d and correct:
            questions = load_questions()
            questions.append({
                "question": question,
                "options": [a, b, c, d],
                "correct": correct
            })
            save_questions(questions)
            st.success("Questão salva com sucesso!")
        else:
            st.error("Preencha todos os campos.")

elif menu == "Quiz":
    st.header("Responder Quiz")
    questions = load_questions()
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
        st.session_state.answered = False
        st.session_state.selected = None

    if st.session_state.q_index >= len(questions):
        st.success("Fim do quiz!")
    else:
        q = questions[st.session_state.q_index]
        st.markdown(f"**{q['question']}**")
        options = q["options"]
        selected = st.radio("Escolha a alternativa:", ["A", "B", "C", "D"], index=0)

        if st.button("Responder"):
            st.session_state.answered = True
            st.session_state.selected = selected

        if st.session_state.answered:
            correct = q["correct"]
            if st.session_state.selected == correct:
                st.markdown(f":blue[✅ Resposta correta: {correct}]")
            else:
                st.markdown(f":red[❌ Errado: Você marcou {st.session_state.selected}]")
                st.markdown(f":blue[✅ Correta: {correct}]")
            if st.button("Próxima"):
                st.session_state.q_index += 1
                st.session_state.answered = False
                st.session_state.selected = None
