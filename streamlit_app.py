import numpy as np
import pandas as pd
import streamlit as st


uploadedFile = st.file_uploader("Choose")

x = pd.read_csv(uploadedFile)

if st.button('Read'):
    i = 0
    while i < len(x):
        st.write(x.iloc[i])
        st.write(x.iloc[i]['ob1'])
        i+=1