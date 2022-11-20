import streamlit as st
from main import suggest

st.markdown('# Perfect Present 🎁')
st.markdown("### Enter a person'details and the app will suggest gifts for them.")

st.markdown("### Write Interest")
interest = st.text_input("Write Interest", value="",label_visibility="collapsed")

st.markdown("### Select Gender")
gender = st.radio("Select Gender",('male', 'female', 'non-binary'), label_visibility="collapsed")

st.markdown("### Select Age")
age = st.slider('Select Age', 0, 100, 18, label_visibility="collapsed") 

if st.button(label="Suggest!", help="Click! Click!"):
    suggestions = suggest(age, gender, interest)
    st.markdown('### Gift Suggestions')
    for suggestion in suggestions:
        st.markdown(f"- {suggestion}")