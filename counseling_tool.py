from taipy.gui import Gui, notify, navigate, Markdown
import sys
sys.path.insert(1,'C:/GIT/Hack_The_Classroom/path-to-uni/data')
import pandas as pd
from student_data import student_data_df, student_table_dict_SAT_math, student_table_dict_SAT_rw, student_table_dict_main, student_sig_underperforming, student_mildly_underperforming

############### - TAIPY Functions & Properties - ###############
# Chart Properties
property_chart_grades = {"type":"bar",
                         "x": "classes",
                         "y": "grades [%]",
                         "title":"Current Grades"}

property_chart_SAT = {"type":"bar",
                      "x":"categories",
                      "y":"score",
                      "title":"Predicted Scores"}

# Taipy GUI functions
def on_button_action(state):
    navigate(state, to=state.student_name.lower().replace(" ","_"))
    notify(state, 'info', f'Data updated for: {state.student_name}')

def on_change(state, var_name, var_value):
    if var_value == False:
        notify(state, 'info', 'Panel closed, re-open with button')
    
def on_user_init(state):
    notify(state, 'info', f'Data updated for: {state.student_name}')
    return

def table_style(_1, _2, value):
    # breakpoint()
    if value[0] > -1:
        return "green-cell"
    elif value[0] > -30:
        return "yellow-cell"
    else:
        return "red-cell"

# Data creation
student_names = []
student_grades =[]
student_SAT = []
student_tables_SAT_math = []
student_tables_SAT_rw = []
student_tables_main = []

for student_name in student_data_df.index:

    student_names.append(student_name)

    student_grades.append(pd.DataFrame({'classes':student_data_df.loc[student_name][0:5].index,'grades [%]':student_data_df.loc[student_name][0:5].values}))

    student_SAT.append(pd.DataFrame({'categories':student_data_df.loc[student_name][5:7].index,'score':student_data_df.loc[student_name][5:7].values}))

    student_tables_SAT_math.append(student_table_dict_SAT_math[student_name])

    student_tables_SAT_rw.append(student_table_dict_SAT_rw[student_name])

    student_tables_main.append(student_table_dict_main[student_name])

########################################## - PAGES - ##########################################
# ISSUES WITH TRYING TO CREATE FOR LOOP FOR EACH PAGE, SO WROTE OUT INDIVIDUALLY FOR NOW
show_pane = True
student_name = student_names[0]
page_1 = """
<|{student_names[0]}|id=student_title|>

<|layout|columns=1 1|id=search|

<|{student_name}|input|>

<|Go To|button|on_action=on_button_action|>

|>

<|layout|columns=1 1|

<|{student_grades[0]}|chart|properties={property_chart_grades}|width=100%|>

<|{student_SAT[0]}|chart|properties={property_chart_SAT}|width=100%|>

|>

<|Favorited Universities (+/- compared to {student_names[0]})|id=table_title|>

<|layout|columns=2 1 1|

<|{student_tables_main[0]}|table|show_all|id=my_table|>

<|{student_tables_SAT_math[0]}|table|style=table_style|show_all|id=my_table|>

<|{student_tables_SAT_rw[0]}|table|style=table_style|show_all|id=my_table|>

|>

<|d-flex|
<|{show_pane}|pane|persistent|width=400px|
##### Student Status
<|{student_sig_underperforming}|table|show_all|>

<|{student_mildly_underperforming}|table|show_all|>
|>
<|Open Panel|button|on_action={lambda s: s.assign("show_pane", True)}|>
|>
"""

student_name = student_names[1]
page_2 = """
<|{student_names[1]}|id=student_title|>

<|layout|columns=1 1|id=search|

<|{student_name}|input|>

<|Go To|button|on_action=on_button_action|>

|>

<|layout|columns=1 1|

<|{student_grades[1]}|chart|properties={property_chart_grades}|width=100%|>

<|{student_SAT[1]}|chart|properties={property_chart_SAT}|width=100%|>

|>

<|Favorited Universities (+/- compared to {student_names[1]})|id=table_title|>

<|layout|columns=1 1 1|

<|{student_tables_main[1]}|table|show_all|id=my_table|>

<|{student_tables_SAT_math[1]}|table|style=table_style|show_all|id=my_table|>

<|{student_tables_SAT_rw[1]}|table|style=table_style|show_all|id=my_table|>

|>

<|d-flex|
<|{show_pane}|pane|persistent|width=400px|
##### Student Status
<|{student_sig_underperforming}|table|show_all|>

<|{student_mildly_underperforming}|table|show_all|>
|>
<|Open Panel|button|on_action={lambda s: s.assign("show_pane", True)}|>
|>
"""

student_name = student_names[2]
page_3 = """
<|{student_names[2]}|id=student_title|>

<|layout|columns=1 1|id=search|

<|{student_name}|input|>

<|Go To|button|on_action=on_button_action|>

|>

<|layout|columns=1 1|

<|{student_grades[2]}|chart|properties={property_chart_grades}|width=100%|>

<|{student_SAT[2]}|chart|properties={property_chart_SAT}|width=100%|>

|>

<|Favorited Universities (+/- compared to {student_names[2]})|id=table_title|>

<|layout|columns=1 1 1|

<|{student_tables_main[2]}|table|show_all|id=my_table|>

<|{student_tables_SAT_math[2]}|table|style=table_style|show_all|id=my_table|>

<|{student_tables_SAT_rw[2]}|table|style=table_style|show_all|id=my_table|>

|>

<|d-flex|
<|{show_pane}|pane|persistent|width=400px|
##### Student Status
<|{student_sig_underperforming}|table|show_all|>

<|{student_mildly_underperforming}|table|show_all|>
|>
<|Open Panel|button|on_action={lambda s: s.assign("show_pane", True)}|>
|>
"""

student_name = student_names[3]
page_4 = """
<|{student_names[3]}|id=student_title|>

<|layout|columns=1 1|id=search|

<|{student_name}|input|>

<|Go To|button|on_action=on_button_action|>

|>

<|layout|columns=1 1|

<|{student_grades[3]}|chart|properties={property_chart_grades}|width=100%|>

<|{student_SAT[3]}|chart|properties={property_chart_SAT}|width=100%|>

|>

<|Favorited Universities (+/- compared to {student_names[3]})|id=table_title|>

<|layout|columns=1 1 1|

<|{student_tables_main[3]}|table|show_all|id=my_table|>

<|{student_tables_SAT_math[3]}|table|style=table_style|show_all|id=my_table|>

<|{student_tables_SAT_rw[3]}|table|style=table_style|show_all|id=my_table|>

|>

<|d-flex|
<|{show_pane}|pane|persistent|width=400px|
##### Student Status
<|{student_sig_underperforming}|table|show_all|>

<|{student_mildly_underperforming}|table|show_all|>
|>
<|Open Panel|button|on_action={lambda s: s.assign("show_pane", True)}|>
|>
"""

# root page
root_md = """
<|UNI PATH|id=title|>

<|toggle|theme|>\n<center>\n<|navbar|>\n</center>
"""

######################### - RUN APP - #########################
# create pages
pages = {"/":root_md,
         "student_a":page_1,
         "student_b":page_2,
         "student_c":page_3,
         "student_d":page_4}

# run GUI
app = Gui(pages=pages,css_file="counseling_tool.css")
app.run(use_reloader=True) # use_reloader=True for dev mode / reloads on save