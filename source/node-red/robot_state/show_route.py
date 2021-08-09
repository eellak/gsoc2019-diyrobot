import pandas as pd
import math

CSV_PATH = './state.csv'

# add the headers of the csv file manually
df = pd.read_csv(CSV_PATH, header=None, names=['dist_a', 'dist_b', 'dist_u', 'motor_a', 'motor_b', 'rev_a', 'rev_b'])
# print(df.head())

# add two columns
df['x'] = 0
df['y'] = 0

coords = []

# define sampling time
T = 1 # sec
R = 3 # radius of wheel in cm
L = 15 # width of robot in cm

