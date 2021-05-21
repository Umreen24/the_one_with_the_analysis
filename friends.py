#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:12:07 2021

@author: umreenimam
"""

"""""""""""""""
IMPORTING PACKAGES
"""""""""""""""
import os
import matplotlib as plt
import pandas as pd
import numpy as np


"""""""""""""""
Set OS 
"""""""""""""""
os.chdir('/Users/umreenimam/Documents/Coding/data_analysis/friends_data')


"""""""""""""""
FUNCTIONS
"""""""""""""""
# Function to read and load data
def load_read_data(data):
    loaded_data = pd.read_excel(data, engine = 'openpyxl')
    
    return loaded_data

