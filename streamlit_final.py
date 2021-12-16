#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:19:21 2021

@author: AlvinDevasia
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time
import matplotlib.pyplot as plt


@st.cache
def load_hospitals():
    hospital_info = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return hospital_info

@st.cache
def load_outpatient():
    outpatient2015 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient_2.csv')
    return outpatient2015

@st.cache
def load_inpatient():
    inpatient2015 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient_2.csv')
    return inpatient2015




st.title('Medicare — Expenses - National')

##How does Stony Brook compare to the rest of NY?
##sTONY Brook - Most expensive inpatient DRGs
##Stony Brook - Most expensive outpatient DRGs