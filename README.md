# path-to-uni
Part of Hack_The_Classroom competition hosted by MLH

Sub prizes includes best use of Taipy, hence a heavy use of this Python library

## Inspiration
We were inspired by the need to help students meet their goals faster, and make it easier for student counselors to point out gaps. In the United States, high schools are fairly large and can easily reach 1000 students per graduating class. For those students, there are only a handful of student counselors, and with so many students it is impossible to help everyone. We also felt there was a lack of support for the students that were so close to reaching their university goals, but fell short because they did not know where they stood until it was too late. This could mean from going to a community college versus a state school. We don't want to leave the middle class (of students) behind.

We want this tool to help freshman and the counselor's of those students to feel inspired, as they progress through high school, see their goals come to fruition.
## What it does
This tool is aimed at student counselors to help get a quick-glance at what students need the most help. Each student gets a page, and the user can easily search for any student within the school system. Grades are pulled from the school's database, and the students are to provide the school with their top school choices. 
## How we built it

## Challenges we ran into
Our team was fairly new to hackathons, so a key issue was time management. 2 days might feel like plenty of time, but by the time you are coming up with ideas, there are so many that you have to force yourself to re-align your scope with the team. Additionally, once you start coding, most of us have a tendency to focus on fixing that bug and nothing else, but when a half-hour, one-hour pass by it's better to create a work-around and focus on building a minimal viable product first.

This was also our first time working with Taipy, as this was one of the sub-prizes, we wanted to push ourselves to use this library. WE LEARNED A LOT. I think the biggest issue we had was the lack of online resources for this library, so it was mainly reading through documentation to figure anything out. We especially had a diffult time with scaling up the pages, it seemed as though the markdown text did not read in variables properly when looped through.

Another challenge that we ran into was training the predictive model. As the model is time based and the data that we could find was not, we realized we could no longer make use of the predictive model and would instead need to shift to a simple interpolation. Ideally we would have school specific SAT and GPA data throughout a range of calendar year(i.e. 2000-2020). Challenges and limitations affecting the model's performance and reliability include the absence of outliers and anomalies, potential model overfitting, and constrained generalization. 
 
## Accomplishments that we're proud of
- Interfacing with a new python library. 
- Learning how to creaet a ML Pipeline and different scenarios

## What we learned
How to create an interactive GUI within Taipy and more about the four fundamental concepts in Taipy Core.

## What's next for Uni Path
We want to find more data to help build up the credibility of the app. But this will take research and most likely going school to school to collect information. This data would encompass a large time range and ideally include the breakdown of the GPA to include the student's academic grades, but also the scores of the SAT sections. If we have that this tool can be really powerful. 

Second, we want this tool to be available for students as well. So a student version of the app to come soon. The student's version would be a tool that could be used for progress tracking and as a study plan to adjust their studies to tailor best to their top universities. 
