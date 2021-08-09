import pandas as pd
import math
import matplotlib.pyplot as plt

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

# suppose motor b is at the left

for index, row in df.iterrows():
    if index == 0:
        point = (0, 0)
    else:
        # TODO: right better with dataframe action
        # suppose motor a is at the right
        if df.iloc[index]['motor_a'] == 'move':
            vr = df.iloc[index]['dist_a'] - df.iloc[index-1]['dist_a'] 
        elif df.iloc[index]['motor_a'] == 'reverse':
            vr = df.iloc[index-1]['dist_a'] - df.iloc[index]['dist_a']
        else: # suppose it moves forward
            vr = df.iloc[index]['dist_a'] - df.iloc[index-1]['dist_a'] 
        # suppose motor b is at the left
        if df.iloc[index]['motor_b'] == 'move': 
            vl = df.iloc[index]['dist_b'] - df.iloc[index-1]['dist_b']  
        elif df.iloc[index]['motor_a'] == 'reverse':
            vl = df.iloc[index-1]['dist_b'] - df.iloc[index]['dist_b']  
        else: 
            vl = df.iloc[index]['dist_b'] - df.iloc[index-1]['dist_b']

        dphi = (R/L) * (vr - vl)
        dx = (R/2) * (vr + vl) * math.cos(dphi)
        dy = (R/2) * (vr + vl) * math.sin(dphi)

        x, y = point[0], point[1]
        point = (x + dx, y + dy)

    coords.append(point)

print(coords)
plt.scatter([x for x,_ in coords] , [y for _,y in coords])
plt.show()

