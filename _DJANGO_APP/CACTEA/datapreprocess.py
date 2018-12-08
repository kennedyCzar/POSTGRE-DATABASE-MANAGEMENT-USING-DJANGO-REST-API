# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:42:00 2018

@author: kennedy
"""
from os import chdir
import pandas as pd
path = chdir('D:\\FREELANCER\\DjangoProjectGamma\\DIRECTORY\\CACTEA\\data')

dataset = pd.read_csv('storage.csv', sep = ';', header = 'infer')

dataset = dataset.drop(['ANLAGEN_ID,,,,,,,,,'], axis = 1)

dataset.to_csv('new_storage.csv', sep=',', encoding = 'utf-8')


##create new database
data = pd.DataFrame([])
data.columns = dataset.columns
for ii in range(len(dataset.columns)):
    data.columns[ii] = dataset.columns
    
