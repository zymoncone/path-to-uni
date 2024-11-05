import pandas as pd
import os

current_dir = os.getcwd()
filepath = os.path.join(current_dir, 'data', 'College_Admissions.csv')

cols = ['Name', 'Applicants total', 'Admissions total', 'Enrolled total',
       'SAT_Reading_25th_p', 'SAT_Reading_75th_p',
       'SAT_Math_25th_p', 'SAT_Math_75th_p']

college_admis_df = pd.read_csv(filepath, header=0, usecols=[0,1,2,3,6,7,8,9], names=cols, index_col=0).dropna().drop_duplicates()
university_list = list(college_admis_df.index)