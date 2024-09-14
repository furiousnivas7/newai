import streamlit as st
from agents.manifesto_agent import compare_manifestos
from agents.query_agent import get_answer

st.title("Election Misinformation App")

# Manifesto Comparison Section
st.header("Manifesto Comparator")
candidate1 = st.text_input("Enter Candidate 1 Manifesto URL:")
candidate2 = st.text_input("Enter Candidate 2 Manifesto URL:")
if st.button("Compare Manifestos"):
    comparison = compare_manifestos(candidate1, candidate2)
    st.write(comparison)

# AI Chatbot Section
st.header("Election Query Bot")
query = st.text_input("Ask a question about the election:")
if st.button("Get Answer"):
    answer = get_answer(query)
    st.write(answer)

