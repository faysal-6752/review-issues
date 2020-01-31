#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import streamlit as st
import plotly.graph_objs as go
df_one = pd.read_csv('one.csv')
df_janets =  pd.read_csv('janets.csv')
df_cg = pd.read_csv('cg.csv')


## Set password
password = st.text_input("Please Enter Your Password to Proceed")
if password =="%#*06942722@37":


  # One education
  trace = go.Pie(labels=df_one.issue, 
                     values=df_one.frequency,
                     #hoverinfo='label+percent', 
                     
                     rotation=90)
      
  layout = go.Layout(
                      title="One Education's Percent Review Issues",
                      font= dict(family='Arial', size=13, color='#909090'),
                      #legend=dict(x=0.9, y=0.5)
                      )
  data = [trace]
  fig = go.Figure(data=data, layout=layout)
  st.plotly_chart(fig)


  # In[6]:


  # cg
  trace = go.Pie(labels=df_cg.issue, 
                     values=df_cg.frequency,
                     #hoverinfo='label+percent', 
                     
                     rotation=90)
      
  layout = go.Layout(
                      title="Course Gate's Percent Review Issues",
                      font= dict(family='Arial', size=13, color='#909090'),
                      #legend=dict(x=0.9, y=0.5)
                      )
  data = [trace]
  fig = go.Figure(data=data, layout=layout)
  st.plotly_chart(fig)


  # In[7]:


  # cg
  trace = go.Pie(labels=df_janets.issue, 
                     values=df_janets.frequency,
                     #hoverinfo='label+percent', 
                     
                     rotation=90)
      
  layout = go.Layout(
                      title="Janets's Percent Review Issues",
                      font= dict(family='Arial', size=13, color='#909090'),
                      #legend=dict(x=0.9, y=0.5)
                      )
  data = [trace]
  fig = go.Figure(data=data, layout=layout)
  st.plotly_chart(fig)

else:
  st.subheader('Incorrect Password')

