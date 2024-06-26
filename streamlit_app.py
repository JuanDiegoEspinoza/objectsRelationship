import numpy as np
import pandas as pd
import streamlit as st


uploadedFile = st.file_uploader("Choose")

x = pd.read_csv(uploadedFile)

if st.button('Read'):
    for row in x:
        st.write(row.ob1, row.ob2)