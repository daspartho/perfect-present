import streamlit as st
from main import suggest

st.title('Perfect Present 🎁')

interest = st.text_input("Write Interest", value="")
gender = st.radio("Select Gender",('male', 'female', 'non-binary'))
age = st.slider('Select Age', 0, 100, 10) 

if st.button(label="Suggest", help="Click! Click!"):
    results = suggest(age, gender, interest)
    st.markdown('### Gift Suggestions')
    for suggestion in results:
        st.markdown(f"-{suggestion}")