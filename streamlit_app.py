import numpy as np
import pandas as pd
import streamlit as st

test = st.file_uploader('the notice you want to tell')

pd.read_excel(test)

if st.button('Read'):
    st.write(x)