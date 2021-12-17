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
st.write('1. Compare the mortality rate between NY and CA hospitals')
st.write('2. Stony Brook - Most expensive inpatient DRGs')
st.write('3. Stony Brook - Most expensive outpatient APC')
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


st.subheader('Outpatient Facility')
bar7 = outpatientdf['provider_state'].value_counts().reset_index()
st.dataframe(bar7)

st.subheader('Outpatient Facilities by state')
fig7 = px.bar(bar7, x='index', y='provider_state')
st.plotly_chart(fig7)

st.markdown('2.  Which states have the lowest number of inpatient and outpatient facilities?')
st.markdown('- Alaska has the lowest number of inpatient and outpatient facilities. ') 


##3
# Create a unique dataframe for Stony Brook Inpatient info
sb_inpatient = inpatientdf[inpatientdf['provider_id']==330393]
st.header('Inpatient Data for Stony Brook')
st.markdown('This dataset filters out inpatient data for Stony Brook University Hospital from the main inpatient dataframe')
st.dataframe(sb_inpatient)

##Answering Highest average payments per DRG for Stony Brook
sb_discharges = sb_inpatient.pivot_table(index =['drg_definition'],values =['average_total_payments'],aggfunc='mean')
st.header('Average Total Payments for DRG Codes at Stony Brook')
st.markdown('This pivot table shows the average total payments per drg code for Stony Brook University Hospital.')
st.dataframe(sb_discharges)
st.markdown('Per the table above, you can see that the highest average total payment came from drg code 003 - ECMO OR TRACH W MV >96 HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R.')

##4
# Create a unique dataframe for Stony Brook Outpatient info
sb_outpatient = outpatientdf[outpatientdf['provider_id']==330393]
st.header('Outpatient Data for Stony Brook')
st.markdown('This dataset filters out outpatient data for Stony Brook University Hospital from the main outpatient dataframe')
st.dataframe(sb_outpatient) 


sb_services = sb_outpatient.pivot_table(index =['apc'],values=['average_total_payments'],aggfunc='mean')
st.header('Total Outpatient Services for APC Codes at Stony Brook')
st.markdown('This pivot table shows the average total payments per apc code for Stony Brook University Hospital')
st.dataframe(sb_services)
st.markdown('Per the table above, you can see that the apc code with the highest average total payment is 0074 - Level IV Endoscopy Upper Airway.')

##5
##Question 5. Bar chart for hospital type in the U.S
st.header('Q5. What is the frequency for hospital types across the nation?')
st.subheader('Hospital Types - United States')
bar1 = hospitaldf['hospital_type'].value_counts().reset_index()
st.bar_chart(data=bar1, width=0, height=0, use_container_width=True)
st.markdown('The majority of hospitals in the United States are acute care, followed by critical access')

##Question 6. Bar chart for number of hospitals by state
st.header('6. Which state has the most hospitals?')
st.subheader('Number of Hospitals for each State')
bar2 = hospitaldf['state'].value_counts().reset_index()
st.bar_chart(data=bar2, width=0, height=0, use_container_width=True)
st.markdown('Texas has 449 hospitals, which makes it the state with the most hospitals, followed by California')




