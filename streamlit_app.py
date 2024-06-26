import numpy as np
import pandas as pd
import streamlit as st


uploadedFile = st.file_uploader()

x = pd.read_excel(uploadedFile)

if st.button('Read'):
    st.write(x)