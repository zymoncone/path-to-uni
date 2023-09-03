import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import random

########## - CLEAN DATA - ##########
# clean up data and do random split for math / reading-writing since data not available
# with more time we could get data from each high school from past few years and make a 
# collective dataset to use here or other predictive model
filepath = 'C:/GIT/Hack_The_Classroom/path-to-uni/data/SAT_GPA.csv'
df = pd.read_csv(filepath)
df = df[(df!=0).all(1)]

# scale for 1600 point scale
df['SAT'] = df['SAT'] * 1600 / 2400

# do random split
split_factor = random.uniform(0.475,0.525)
df['SAT_Math'] = df['SAT'] * split_factor
df['SAT_RW'] = df['SAT'] * (1 - split_factor)

x=df['GPA'].values
y_math=df['SAT_Math'].values
y_rw = df['SAT_RW'].values

x_reshaped = x.reshape([-1,1])
y_math_reshaped = y_math.reshape([-1,1])
y_rw_reshaped = y_rw.reshape([-1,1])

reg_math=LinearRegression()
reg_math.fit(x_reshaped,y_math_reshaped)

reg_rw=LinearRegression()
reg_rw.fit(x_reshaped,y_rw_reshaped)


########## - DEFINE FUNCTIONS - ##########
def predict_SAT_math(GPA):
    result = reg_math.coef_[0] * GPA + reg_math.intercept_
    return np.round(result[0],0)

def predict_SAT_rw(GPA):
    result = reg_rw.coef_[0] * GPA + reg_rw.intercept_
    return np.round(result[0],0)