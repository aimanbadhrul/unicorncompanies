import streamlit as st 
import numpy as np 
import pandas as pd

#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report




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

unicorn_master = pd.read_csv('Unicorn_Companies.csv')
st.write (unicorn_master.head(3))
