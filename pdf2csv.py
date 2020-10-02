#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Kur0s4ki
"""

from tabula import read_pdf
import pandas as pd

FILE_NAME="" #Ppdf file as input
dest="" #destination csv file name

df= read_pdf(FILE_NAME)
x=df.values
data=pd.DataFrame(data=x[1:,1:],columns=x[0,1:])

data.to_csv(dest,sep=',',encoding="utf-8")