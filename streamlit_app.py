import numpy as np
import pandas as pd
import streamlit as st


uploadedFile = st.file_uploader("Choose")

x = pd.read_csv(uploadedFile)

if st.button('Read'):
    for row in df.rows:
        print(row['REFERENCING_OBJECT_NAME'], row['REFERENCED_OBJECT_NAME'])