import streamlit as st
from main import suggest

from glob import glob
import numpy as np
import os
from PIL import Image
import random
import urllib

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
        suggestion_urlencoded = suggestion.lower().replace(" ", "+").replace("'", "")
        st.markdown(f"- <a href='https://www.amazon.com/s?k={suggestion_urlencoded}'>{suggestion}</a>", unsafe_allow_html=True)
        print(suggestion)
        img_path = os.path.join("examples", suggestion.replace(" ", "_").lower())
        if os.path.exists(img_path):
            print("exists: ", suggestion)
            images = glob(img_path + os.sep + "*.jpg")
            an_image = random.choice(images)
            an_image = Image.open(an_image)
            st.image(np.asarray(an_image), caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")