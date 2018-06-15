import numpy as np
import pandas as pd

def read_test_data ():
    return pd.read_csv('test.csv', sep=',',header=0)

def reshape_row (row):
    return row.reshape(28,28)