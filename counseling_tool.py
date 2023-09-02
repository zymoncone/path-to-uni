from taipy.gui import Gui, notify, navigate
import sys
sys.path.insert(1,'C:/GIT/Hack_The_Classroom/path-to-uni/data')
import pandas as pd
from student_data import student_data_df, student_table_dict

student_A_grades = pd.DataFrame({'classes':student_data_df.loc['Student A'][0:5].index,'grades [%]':student_data_df.loc['Student A'][0:5].values})

property_chart_grades = {"type":"bar",
                         "x": "classes",
                         "y": "grades [%]",
                         "title":"Current Grades"}

student_A_SAT = pd.DataFrame({'categories':student_data_df.loc['Student A'][5:7].index,'score':student_data_df.loc['Student A'][5:7].values})

property_chart_SAT = {"type":"bar",
                      "x":"categories",
                      "y":"score",
                      "title":"Predicted Scores"}

# Definition of the page
student_name = student_data_df.index[0]
student_table = student_table_dict['Student A']

page_1 = """
<|{student_name}|id=student_title|>

<|layout|columns=1 1|id=search|

<|{student_name}|input|>

<|Go To|button|on_action=on_button_action|>

|>

<|layout|columns=1 1|

<|{student_A_grades}|chart|properties={property_chart_grades}|width=100%|>

<|{student_A_SAT}|chart|properties={property_chart_SAT}|width=100%|>

|>

<|Favorited Universities|id=table_title|>
<|{student_table}|table|id=my_table|>
"""

page_2 = """
    TO BE FILLED IN
"""

def on_button_action(state):
    navigate(state, to=state.student_name.lower().replace(" ","_"))
    notify(state, 'info', f'Data updated for: {state.student_name}')

def on_change(state, var_name, var_value):
    notify(state, 'info', f'{state.student_name} needs support')
    
def on_user_init(state):
    notify(state, 'info', f'Data updated for: {state.student_name}')
    return
    
pages = {"/":"<|toggle|theme|>\n<center>\n<|navbar|>\n</center>",
        "student_a":page_1,
        "student_b":page_2,
        "student_c":page_2,
        "student_d":page_2}

Gui(pages=pages,css_file="counseling_tool.css").run(use_reloader=True) # use_reloader=True for dev mode / reloads on save