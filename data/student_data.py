import sys
sys.path.insert(1,'C:/GIT/Hack_The_Classroom/path-to-uni')
import random
import pandas as pd
import numpy as np
from clean_data import university_list, college_admis_df

################################################# - DEFINE DATA - #################################################
# student data -- TEMP MADE UP FOR NOW
student_data = [{"Name":"Student A", "Math":80,"English":73,"History":76,"Comp Sci":99,"Elective":86,"SAT Math":800,"SAT Reading-Writing":650, "Favorited_Universities":random.choices(university_list,k=5)},
                {"Name":"Student B", "Math":79,"English":70,"History":80,"Comp Sci":90,"Elective":88,"SAT Math":700,"SAT Reading-Writing":650, "Favorited_Universities":random.choices(university_list,k=4)},
                {"Name":"Student C", "Math":90,"English":90,"History":90,"Comp Sci":90,"Elective":90,"SAT Math":500,"SAT Reading-Writing":650, "Favorited_Universities":random.choices(university_list,k=3)},
                {"Name":"Student D", "Math":80,"English":70,"History":80,"Comp Sci":72,"Elective":85,"SAT Math":500,"SAT Reading-Writing":500, "Favorited_Universities":random.choices(university_list,k=6)}]

################################################# - DEFINE FUNCTIONS - #################################################
# process student data
def process_data(data=student_data) -> pd.DataFrame:
    df = pd.DataFrame(data)

    df['Name_For_GUI'] = df.Name.apply(lambda x: x.lower().replace(" ","_"))

    df.set_index("Name",inplace=True)

    return df

# create student tables from data
def create_student_tables(df, compare_75th_percentile=True):

    student_table_dict = {}

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
        GPA = np.mean(df.loc[student_name][0:5]) / 100 * 4.0
        GPA_diff = ["N/A" for i in range(len(SAT_RW_diff))] #[np.round(GPA - college_admis_df.loc[school_name].GPA,2) for school_name in favorites]

        student_table = {"school names":favorites, 
                           "GPA":GPA_diff, 
                           "SAT Math":SAT_Math_diff,
                           "SAT Reading + Writing":SAT_RW_diff}
        
        student_table_dict[student_name] = student_table

    return student_table_dict

################################################# - MAIN - #################################################
student_data_df = process_data()
student_table_dict = create_student_tables(student_data_df)


# breakpoint()