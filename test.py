import pandas as pd
import streamlit as st

df = pd.DataFrame()
df['index'] = [0]
df['name'] = ['matthew wang']
df['uni'] = ['mw3071']
df['prof'] = [['jae woo lee', 'helen wang']]
df['classes'] = [['AP']]

user_input = 'matthew wang'

if (df['name']==user_input).any():
    index = df.loc[df['name']==user_input, 'index']
    temp = df.iloc[index]['prof'][0]
    temp.append('matthew')
    df.iloc[index]['prof'][0] = temp
    st.write(df)
