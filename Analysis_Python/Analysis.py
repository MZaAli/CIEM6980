# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 22:36:44 2022

@author: Ali.Muhammad
"""

import Functions
import pandas as pd

Set = ['07051','07052','07053','07054']
File_Subject = ["Dynamic displacement", "Dynamic force ATI", "Reference wind speed SPS"]
#Optins: "Dynamic displacement", "Dynamic force ATI", "Reference wind speed SPS"
Wind_Speed = ["00", "10", "15", "20", "25", "30", "35", "40", "45", "48"]
#Options: "0000", "0010", "0015", "0020", "0025", "0030", "0035", "0040", "0045", "0048"
Columns_to_import_Results = [0, 3, 9, 10]
Columns_to_import_Wind_raw = [8,9]
Headers_Results = ["Fx (N)", "Myy (Nm)", "d2 (m)", "d3 (m)"]
Headers_Wind_raw = ["P1 (Pa)","P2 (Pa)"]
#Fx: Wind force for along wind, Myy: Moment for along wind, d2: displacement along wind, d3: displacement across wind



#Get results at at wind interval
for j in range (4):
    i = 0
    #Results = pd.DataFrame(columns = ["Fx (N)", "Myy (Nm)", "d2 (m)", "d3 (m)", "Wind Speed (m/s)"])
    Results = None
    Results = pd.DataFrame(columns = Headers_Results)
    for interval in Wind_Speed:
        Temp = Functions.Get_data_column(Set[j],File_Subject[0], Wind_Speed[i], Columns_to_import_Results, Headers_Results)
        Results = pd.concat([Results, Temp], ignore_index=True)
        i += 1
    Results.plot(x="Wind Speed (m/s)", y= Headers_Results)

'''
#Get wind speed
i = 0 
Wind_raw = pd.DataFrame(columns = Headers_Wind_raw)
for interval in Wind_Speed:
    Temp = Functions.Get_data_column(Set[0],File_Subject[2], Wind_Speed[i], Columns_to_import_Wind_raw, Headers_Wind_raw)
    Wind_raw = pd.concat([Wind_raw,Temp], ignore_index=True)
    i += 1
'''

#Results.plot(x="Wind Speed (m/s)", y=["Fx (kN)", "Myy (kNm)", "d2 (mm)", "d3 (mm)"])

#Results_10 = Results.loc[Results['Wind Speed (m/s)'] == 10]

#Results_10.plot(x="Wind Speed (m/s)", y=["Fx (kN)"])