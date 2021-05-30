import numpy as np
import pdb
import  pandas as pd
import requests

def process_pid (x):
    print( x)
    return
df = pd.read_csv('property data.csv')

print(df)

df['PID'].apply (lambda  x: process_pid(x))
pdb.set_trace()
