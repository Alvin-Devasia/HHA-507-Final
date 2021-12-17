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
st.write('1. What hospital type is the most common?')
st.write('2. Which states have the lowest number of inpatient and outpatient facilities?')
st.write('3. Stony Brook - Most expensive inpatient DRGs')
st.write('4. Stony Brook - Most expensive outpatient APC')
st.write('5. Which state has the most hospitals?')
st.write('6. What caused the most discharges DRGs for Stony Brook Hospital?')

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
st.header('Question 1: What hospital type is the most common?')
st.subheader('Hospital Type in New York')
bar1 = hospitaldf['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)
st.markdown('Answer: Acute care hospitals is the most common hospital type')

#2
st.header('Question 2: Which states have the lowest number of inpatient and outpatient facilities?')
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

st.markdown('Answer: Alaska has the lowest number of inpatient and outpatient facilities. ') 


##3
# Create a unique dataframe for Stony Brook Inpatient info
st.header('Question 3: Stony Brook - Most expensive inpatient DRGs')
sb_inpatient = inpatientdf[inpatientdf['provider_id']==330393]
st.header('Inpatient Data for Stony Brook')
st.markdown('This dataset filters out inpatient data for Stony Brook University Hospital from the main inpatient dataframe')
st.dataframe(sb_inpatient)

##Answering Highest average payments per DRG for Stony Brook
sb_discharges = sb_inpatient.pivot_table(index =['drg_definition'],values =['average_total_payments'],aggfunc='mean')
st.header('Average Total Payments for DRG Codes at Stony Brook')
st.markdown('This pivot table shows the average total payments per drg code for Stony Brook University Hospital.')
st.dataframe(sb_discharges)
st.markdown('Answer: The highest average total payment came from drg code 003 - ECMO OR TRACH W MV >96 HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R.')

##4
# Create a unique dataframe for Stony Brook Outpatient info
st.header('Question 4: Stony Brook - Most expensive outpatient APC')
sb_outpatient = outpatientdf[outpatientdf['provider_id']==330393]
st.header('Outpatient Data for Stony Brook')
st.markdown('This dataset filters out outpatient data for Stony Brook University Hospital from the main outpatient dataframe')
st.dataframe(sb_outpatient) 


sb_services = sb_outpatient.pivot_table(index =['apc'],values=['average_total_payments'],aggfunc='mean')
st.header('Total Outpatient Services for APC Codes at Stony Brook')
st.markdown('This pivot table shows the average total payments per apc code for Stony Brook University Hospital')
st.dataframe(sb_services)
st.markdown('Answer: The apc code with the highest average total payment is 0074 - Level IV Endoscopy Upper Airway.')

##5

##Question 5. Bar chart for number of hospitals by state
st.header('Question 5: Which state has the most hospitals?')
st.subheader('Number of Hospitals for each State')
bar2 = hospitaldf['state'].value_counts().reset_index()
#st.bar_chart(data=bar2, width=0, height=0, use_container_width=True)
st.dataframe(bar2)

st.subheader('Number of Hospitals per state')
fig10 = px.bar(bar2, x='index', y='state')
st.plotly_chart(fig10)
st.markdown('Answer: Texas is the state with the most hospitals')

#6
st.header('Question 6: What caused the most discharges DRGs for Stony Brook Hospital?')
sbinpatient = inpatientdf[inpatientdf['provider_id']==330393]
st.header('Inpatient Data from Stony Brook Hospital')
st.dataframe(sbinpatient)
sbdischarges = sbinpatient.pivot_table(index =['drg_definition'],values =['total_discharges'],aggfunc='mean')
st.header(' Discharges for DRG Codes at Stony Brook')
st.dataframe(sbdischarges)
st.markdown('Answer: The highest amount of discharges came from "SEPTICEMIA OR SEVERE SEPSIS W/O MV 96+ HOURS W MCC" 628 discharges.')





