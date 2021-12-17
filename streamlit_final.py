#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:19:21 2021

@author: AlvinDevasia
"""

import pandas as pd
import plotly.express as px
import pandas as pd
import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly


##How does Stony Brook compare to the rest of NY?
##Stony Brook - Most expensive inpatient DRGs
##Stony Brook - Most expensive outpatient DRGs

@st.cache
def load_hospitals():
   hospitaldf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')
   return hospitaldf
@st.cache
def load_inatpatient():
    inpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')
    return inpatientdf
@st.cache
def load_outpatient():
    outpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
    return outpatientdf

st.title('HHA 507 - Final Assignment')
st.write('-Alvin Devasia :sunglasses:') 
st.write('This app is providing answers to the following questions:')
st.write('1. How does Stony Brook compare to the rest of NY?')
st.write('2. Stony Brook - Most expensive inpatient DRGs')
st.write('3. Stony Brook - Most expensive outpatient DRGs')
st.write('4. What hospital type is the most common in New York?')
st.write('5. Which states have the lowest number of inpatient and outpatient facilities?')
st.write('6. ')

# Load the data:     
hospitaldf = load_hospitals()
inpatientdf = load_inatpatient()
outpatientdf = load_outpatient()  

# Preview the dataframes 
st.header('Hospital Data Preview')
st.dataframe(hospitaldf)

st.header('Outpatient Data Preview')
st.dataframe(outpatientdf)

st.header('Inpatient Data Preview')
st.dataframe(inpatientdf)

#Bar Chart 1
st.subheader('Hospital Type in New York')
bar1 = hospitaldf['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)
st.caption('Acute care hospitals is the most common hospital type in New York ')

#2
st.title('Inpatient and outpatient dataframes')

st.subheader('Inpatient Facility')
bar7 = inpatientdf['provider_state'].value_counts().reset_index()
st.dataframe(bar7)

st.subheader('Inpatient Facilities by state')
fig7 = px.bar(bar7, x='index', y='provider_state')
st.plotly_chart(fig7)


st.markdown('The dataframe displayed below is for the outpatient facility')

st.subheader('Outpatient Facility')
bar7 = outpatientdf['provider_state'].value_counts().reset_index()
st.dataframe(bar7)

st.subheader('Outpatient Facilities by state')
fig7 = px.bar(bar7, x='index', y='provider_state')
st.plotly_chart(fig7)

st.markdown('2.  Which states have the lowest number of inpatient and outpatient facilities?')
st.markdown('- Alaska has the lowest number of inpatient and outpatient facilities. ') 

st.subheader('Question 1')
st.write('Question1: How does the data for Stony Brook compare to other outpatient facilities for the most expensive APCs?')
st.markdown('Based on the two pivot tables here, we can see that the most expensive outpatient APC at Stonybrook is 0074 - Level IV Endoscopy Upper Airway. The most expensive outpatient APC in non Stonybrook facilities is also 0074 - Level IV Endoscopy Upper Airway, however the average total payment for this APC at Stonybrook is $2307.21 whereas outside of Stonybrook the average total payment is $2783.802785')

##djweifjiwwifw
table2 = outpatientdf['average_estimated_submitted_charges'].value_counts().reset_index()
st.header('outpatient drgs')
st.dataframe(table2)
#3

#4
table4 = outpatientdf['average_total_payments'].value_counts().reset_index()
st.header('outpatient services')
st.dataframe(table4)





