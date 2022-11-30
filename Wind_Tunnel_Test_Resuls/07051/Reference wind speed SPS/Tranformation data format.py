# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:01:42 2022

@author: 10036
"""

##txt to csv

from tqdm  import tqdm 
import pandas as pd
def parse_data(file,out_file):
    data = []
    with open(file,"r",encoding="gbk")as f:
        for index,line in tqdm(enumerate(f)):
            if index<7:continue
            data.append(line.strip().split("\t"))
    
    data = pd.DataFrame(data)
    data.to_csv(out_file,index=False,header=None)
    return "ok"
    
for file in ["0000.txt",'0010.txt',"0015.txt",'0020.txt',"0025.txt",'0030.txt',"0035.txt",'0040.txt',"0045.txt",'0048.txt']:
    parse_data(file,file.split(".")[0]+".csv")


#parse_data(file,"parsed_"+file.split(".")[0]+".csv")