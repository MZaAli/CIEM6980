# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 22:36:44 2022

@author: Ali.Muhammad
"""

import Functions
import pandas as pd

File_Subject = ["Dynamic displacement", "Dynamic force ATI", "Reference wind speed SPS"]
#Optins: "Dynamic displacement", "Dynamic force ATI", "Reference wind speed SPS"
Wind_Speed = ["00", "10", "15", "20", "25", "30", "35", "40", "45", "48"]
#Options: "0000", "0010", "0015", "0020", "0025", "0030", "0035", "0040", "0045", "0048"
Columns_to_import = [0, 3, 9, 10]
Headers = ["Fx (kN)", "Myy (kNm)", "d2 (mm)", "d3 (mm)"]    
#Fx: Wind force for along wind, Myy: Moment for along wind, d2: displacement along wind, d3: displacement across wind



#Get results at at wind interval
i = 0
Results = pd.DataFrame(columns = ["Fx (kN)", "Myy (kNm)", "d2 (mm)", "d3 (mm)", "Wind Speed (m/s)"])
for interval in Wind_Speed:
    Temp = Functions.Get_data_column(File_Subject[0], Wind_Speed[i], Columns_to_import, Headers)
    Results = pd.concat([Results, Temp], ignore_index=True)
    i += 1


Results.plot(x="Wind Speed (m/s)", y=["Fx (kN)", "Myy (kNm)", "d2 (mm)", "d3 (mm)"])

Results_10 = Results.loc[Results['Wind Speed (m/s)'] == 10]

Results_10.plot(x="Wind Speed (m/s)", y=["Fx (kN)"])