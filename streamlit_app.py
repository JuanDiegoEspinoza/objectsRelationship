import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

test = st.file_uploader('the notice you want to tell')
df1=pd.read_csv(test)
st.write(df1)
