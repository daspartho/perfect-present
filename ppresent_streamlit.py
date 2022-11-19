import streamlit as st
import pandas as pd
import numpy as np
from main import suggest

def run_suggest(*args):
    age = args[0]
    gender_m = args[1]
    gender_f = args[2]
    interests = args[3]
    if gender_m and not gender_f:
        gender = "male"
    elif gender_f and not gender_m:
        gender = "female"
    else:
        gender = "nonbinary"

    results = suggest(age, gender, interests)
    print(results)

st.title('Perfect Present')
interests = st.text_input("Interests", value="")
gender_m = st.checkbox("Male", value=False)
gender_f = st.checkbox("Female", value=False)
age = st.slider('age', 0, 100, 10) 

st.button(label="Predict", key=None, help=None, on_click=run_suggest, args=(age, gender_m, gender_f, interests,))
