import pandas as pd

filepath = 'C:/GIT/Hack_The_Classroom/path-to-uni/data/College_Admissions.csv'

cols = ['Name', 'Applicants total', 'Admissions total', 'Enrolled total',
       'SAT_Reading_25th_p', 'SAT_Reading_75th_p',
       'SAT_Math_25th_p', 'SAT_Math_75th_p']

college_admis_df = pd.read_csv(filepath, header=0, usecols=[0,1,2,3,6,7,8,9], names=cols, index_col=0).dropna()
university_list = list(college_admis_df.index)