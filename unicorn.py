import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px



st.title('Unicorn Companies Around the World')

st.sidebar.write("""
Unicorn Companies Analysis App
""")


st.sidebar.write("<a href='https://www.linkedin.com/in/aimanbadhrul/'>Aiman Badhrulhisham </a>", unsafe_allow_html=True)


choice = st.sidebar.selectbox(
    "Choose a country",   
    ('Default', 'User-defined '),
    index = 0
    
)

st.write(f"## Unicorn Companies from <font color='Aquamarine'>{choice}</font> ", unsafe_allow_html=True)

unicorn_master = pd.read_csv(r"C:\Users\aiman\Documents\Singularity Aerotech Asia\Training\MIGHT Reskilling Cohort 3\Python\dataset\Unicorn_Companies.csv")
unicorn_master.head(3)
