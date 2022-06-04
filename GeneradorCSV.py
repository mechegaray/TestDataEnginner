# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 02:27:49 2022

@author: 54112
"""

import pandas as pd 
import codecs
import shutil


with codecs.open("datos_data_engineer.tsv", encoding="UTF-16-LE") as input_file:
    with codecs.open(
        "outputfile.tsv", "w", encoding="utf-8") as output_file:
        shutil.copyfileobj(input_file, output_file)

tsv_file='outputfile.tsv'    
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('datos_data_engineercsv.csv',sep='|',index=False)