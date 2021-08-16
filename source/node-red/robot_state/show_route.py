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
# T = 0.2 # sec
# R = 3 # radius of wheel in cm
# L = 15 # width of robot in cm
PI = 3.14159 
AXLE_LENGTH = 15 # width of robot in cm


# useful links for dead reckoning: 
# * http://www.seattlerobotics.org/encoder/200010/dead_reckoning_article.html
# * http://rossum.sourceforge.net/papers/DiffSteer/DiffSteer.html


for index, row in df.iterrows():
    if index == 0:
        # x, y, theta (angle counted from x axis)
        cur_x, cur_y, cur_theta = 0.0, 0.0, 0.0
        point = (cur_x, cur_y, cur_theta)
    else:
        # calculate distance travelled by right motor
        if df.iloc[index]['motor_a'] == 'move':
            dist_right = (df.iloc[index]['dist_a'] - df.iloc[index-1]['dist_a']) 
        elif df.iloc[index]['motor_a'] == 'reverse':
            dist_right = (df.iloc[index-1]['dist_a'] - df.iloc[index]['dist_a']) 
        else: # suppose it moves forward
            dist_right = (df.iloc[index]['dist_a'] - df.iloc[index-1]['dist_a'])

        # calculate distance travelled by left motor
        if df.iloc[index]['motor_b'] == 'move': 
            dist_left = (df.iloc[index]['dist_b'] - df.iloc[index-1]['dist_b'])
        elif df.iloc[index]['motor_b'] == 'reverse':
            dist_left = (df.iloc[index-1]['dist_b'] - df.iloc[index]['dist_b'])
        else: 
            dist_left = (df.iloc[index]['dist_b'] - df.iloc[index-1]['dist_b'])

        cos_current = math.cos(cur_theta)
        sin_current = math.sin(cur_theta)

        if (dist_left == dist_right):
        # moving in straight line, that means that distances are equal (or almost equal)
            cur_x = prv_x + dist_left * cos_current
            cur_y = prv_y + dist_left * sin_current
        else:
        # moving in an arc
            expr1 = (AXLE_LENGTH * (dist_right + dist_left)) / (2 * (dist_right - dist_left))
            right_minus_left = dist_right - dist_left

            cur_x = prv_x + expr1 * (math.sin(right_minus_left / AXLE_LENGTH + cur_theta) - sin_current)
            cur_y = prv_y - expr1 * (math.cos(right_minus_left / AXLE_LENGTH + cur_theta) - cos_current)

            # Calculate new orientation
            cur_theta = prv_theta + right_minus_left / AXLE_LENGTH

            # Keep in the range -PI to +PI
            while (cur_theta > PI): 
                cur_theta -= (2.0 * PI)
            while (cur_theta < -PI):
                cur_theta += (2.0 * PI)

    point = (cur_x, cur_y, cur_theta)
    coords.append(point)
    prv_x, prv_y, prv_theta = cur_x, cur_y, cur_theta


plt.title("Route of robot (starting at (0, 0))")
plt.xlabel("x")
plt.ylabel("y")
plt.scatter([x for x,_,_ in coords] , [y for _,y,_ in coords])
plt.savefig("route.png")
