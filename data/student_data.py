import sys
sys.path.insert(1,'C:/GIT/Hack_The_Classroom/path-to-uni')
import random
import pandas as pd
import numpy as np
from clean_data import university_list, college_admis_df
import regression_algo

################################################# - DEFINE DATA - #################################################
# student data -- TEMP MADE UP FOR NOW
student_data = [{"Name":"Student A", "Math":80,"English":73,"History":76,"Comp Sci":99,"Elective":86,"SAT Math":0,"SAT Reading-Writing":0, "Favorited_Universities":random.choices(university_list,k=5)},
                {"Name":"Student B", "Math":79,"English":70,"History":80,"Comp Sci":90,"Elective":88,"SAT Math":0,"SAT Reading-Writing":0, "Favorited_Universities":random.choices(university_list,k=4)},
                {"Name":"Student C", "Math":90,"English":90,"History":90,"Comp Sci":90,"Elective":90,"SAT Math":0,"SAT Reading-Writing":0, "Favorited_Universities":random.choices(university_list,k=3)},
                {"Name":"Student D", "Math":80,"English":70,"History":80,"Comp Sci":72,"Elective":85,"SAT Math":0,"SAT Reading-Writing":0, "Favorited_Universities":random.choices(university_list,k=6)}]

################################################# - DEFINE FUNCTIONS - #################################################
# process student data
def process_data(data=student_data) -> pd.DataFrame:
    df = pd.DataFrame(data)

    df['Name_For_GUI'] = df.Name.apply(lambda x: x.lower().replace(" ","_"))

    df.set_index("Name",inplace=True)

    df['GPA'] = df[["Math","English","History","Comp Sci","Elective"]].mean(axis=1) / 100 * 4.0

    df['SAT Math'] = df['GPA'].apply(lambda x: regression_algo.predict_SAT_math(x))

    df['SAT Reading-Writing'] = df['GPA'].apply(lambda x: regression_algo.predict_SAT_rw(x))

    return df

# create student tables from data
def create_student_tables(df, compare_75th_percentile=True):

    student_table_dict_SAT = {}
    student_table_dict_SAT_math = {}
    student_table_dict_SAT_rw = {}
    student_table_dict_main = {}

    if compare_75th_percentile:
        read_col = "SAT_Reading_75th_p" 
        math_col = "SAT_Math_75th_p"
    else:
        read_col = "SAT_Reading_25th_p" 
        math_col = "SAT_Math_25th_p"

    for student_name in list(df.index):

        favorites = df.loc[student_name]["Favorited_Universities"]

        SAT_Math_diff = [df.loc[student_name]['SAT Math'] - college_admis_df.loc[school_name][math_col] for school_name in favorites]
        SAT_RW_diff = [df.loc[student_name]['SAT Reading-Writing'] - college_admis_df.loc[school_name][read_col] for school_name in favorites]
        GPA = np.round(df.loc[student_name]['GPA'], 2)
        # Temporary until GPA data is available
        GPA_diff = [np.round(random.uniform(-0.5,0.5),2) for i in range(len(SAT_RW_diff))]

        student_table_main = {"school names":favorites,
                              f"GPA [{GPA} Overall]":GPA_diff}
        
        student_table_SAT = {"SAT Math":SAT_Math_diff,
                             "SAT Reading + Writing":SAT_RW_diff}
        
        student_table_dict_SAT[student_name] = student_table_SAT
        student_table_dict_SAT_math[student_name] = {"SAT Math":SAT_Math_diff}
        student_table_dict_SAT_rw[student_name] = {"SAT Reading + Writing":SAT_RW_diff}
        student_table_dict_main[student_name] = student_table_main

    return student_table_dict_SAT, student_table_dict_SAT_math, student_table_dict_SAT_rw, student_table_dict_main

# return significantly under performing students
def check_sig_underperforming_students(table,limit=-70):
    student_underperforming = []
    for student_name, student_dict in table.items():
        # breakpoint()
        Math_list = student_dict['SAT Math']
        RW_list = student_dict['SAT Reading + Writing']
        print('Math List: ', Math_list)

        res_Math = True in (ele < limit for ele in Math_list)
        res_RW = True in (ele < limit for ele in RW_list)

        if res_Math and res_RW:
            text = f'> {student_name} needs help in Math & English'
        elif res_Math:
            text = f'> {student_name} needs help in Math'
        elif res_RW:
            text = f'> {student_name} needs help in English'
        else:
            text = None

        if text != None:
            student_underperforming.append(text)
    
    return pd.DataFrame({'Students Of Concern':student_underperforming})
   
# return mildly under performing students
def check_mildly_performing_students(table,l_bound=-50,r_bound=-10):
    student_underperforming = []
    for student_name, student_dict in table.items():
        # breakpoint()
        Math_list = student_dict['SAT Math']
        RW_list = student_dict['SAT Reading + Writing']

        res_Math = True in (l_bound < ele < r_bound for ele in Math_list)
        res_RW = True in (l_bound < ele < r_bound for ele in RW_list)

        if res_Math and res_RW:
            text = f'> {student_name} is so close in reaching their goal with Math & English'
        elif res_Math:
            text = f'> {student_name} is so close in reaching their goal with Math'
        elif res_RW:
            text = f'> {student_name} is so close in reaching their goal with English'
        else:
            text = None

        if text != None:
            student_underperforming.append(text)
    
    return pd.DataFrame({'Students To Watch':student_underperforming})

################################################# - MAIN - #################################################
student_data_df = process_data()
# breakpoint()
student_table_dict_SAT, student_table_dict_SAT_math, student_table_dict_SAT_rw, student_table_dict_main = create_student_tables(student_data_df)
student_sig_underperforming = check_sig_underperforming_students(student_table_dict_SAT)
student_mildly_underperforming = check_mildly_performing_students(student_table_dict_SAT)

