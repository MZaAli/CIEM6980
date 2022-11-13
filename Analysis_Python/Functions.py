# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 22:36:18 2022

@author: Ali.Muhammad
"""

import os
import pandas as pd
import numpy as np

myPath = os.getcwd()

def Get_data_column(Subject, Wind_speed, Columns, Headers):
    f_path = myPath[:-16] + "\\Wind_Tunnel_Test_Resuls\\" + Subject + "\\00" + Wind_speed + ".csv"
    print (f_path)
    #df = pd.read_csv(f_path, usecols= Column)
    df = pd.read_csv(f_path, usecols= Columns, names=Headers)
    df = df.iloc[1: , :]
    df["Wind Speed (m/s)"] = Wind_speed
    df=df.astype(float)
    return df