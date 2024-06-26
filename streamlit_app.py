import numpy as np
import pandas as pd
import streamlit as st


uploadedFile = st.file_uploader("Choose")

x = pd.read_csv(uploadedFile)

if st.button('Read'):
    st.write(x)