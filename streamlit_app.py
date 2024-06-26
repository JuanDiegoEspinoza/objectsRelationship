import numpy as np
import pandas as pd
import streamlit as st


uploadedFile = st.file_uploader("Choose")

x = pd.read_csv(uploadedFile)

if st.button('Read'):
    i = 0
    while i < len(x):
        row[i]
        st.write(row[i])
        st.write(row[i]['ob1'])
        i+=1