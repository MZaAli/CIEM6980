# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:01:42 2022

@author: 10036
"""

##txt to csv
###############transfer the txt to csv
from tqdm  import tqdm 
import pandas as pd
def parse_data(file,out_file):
    data = []
    with open(file,"r",encoding="gbk")as f:
        for index,line in tqdm(enumerate(f)):
            if index<11:continue
            data.append(line.strip().split("\t"))
    
    data = pd.DataFrame(data)
    data.to_csv(out_file,index=False,header=None)
    return "ok"
    
for file in ["0000 (Ve).ap","0010 (Ve).ap","0015 (Ve).ap","0020 (Ve).ap","0025 (Ve).ap","0030 (Ve).ap","0035 (Ve).ap","0040 (Ve).ap","0045 (Ve).ap","0048 (Ve).ap"]:
    parse_data(file,file.split(".")[0]+".csv")


#parse_data(file,"parsed_"+file.split(".")[0]+".csv")
