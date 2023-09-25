# UniPath
Part of Hack_The_Classroom competition hosted by MLH. See demo [here](https://vimeo.com/860586728?share=copy)

Sub prizes includes best use of Taipy, hence a heavy use of this Python library

## Inspiration
We were inspired by the need to help students meet their goals faster and make it easier for student counselors to point out gaps. In the United States, high schools are fairly large and can easily reach 1000 students per graduating class. For those students, there are only a handful of student counselors, and with so many students it is impossible to help everyone. We also felt there was a lack of support for the students that were so close to reaching their university goals but fell short because they did not know where they stood until it was too late. This could mean from going to a community college versus a state school. We don't want to leave the middle class (of students) behind.

We want this tool to help freshman and the counselors of those students to feel inspired, as they progress through high school and see their goals come to fruition.
## What it does
This tool is aimed at student counselors to help get a quick glance at what students need the most help. Each student gets a page, and the user can easily search for any student within the school system. Grades are pulled from the school's database and displayed. Additionally, SAT scores are shown predicted on the right, this way as a student progresses through high school they can see what their expected SAT scores will be. This is particularly important because students are able to select their top university options and see how they will line up and know whether more effort needs to be put in order for them to reach their goals.
## How we built it
We built this tool using Taipy GUI, which allows us to more easily build up an application without getting into detailed html and css work. We also used Taipy Core for predictive modelling with the SATs, but when we could not get the right data we used a linear regression model from sklearn. Data was also manipulated using pandas.
## Challenges we ran into
Our team was fairly new to hackathons, so a key issue was time management. 2 days might feel like plenty of time, but by the time you are coming up with ideas, there are so many that you have to force yourself to re-align your scope with the team. Additionally, once you start coding, most of us have a tendency to focus on fixing that bug and nothing else, but when a half-hour, one-hour pass by it's better to create a work-around and focus on building a minimal viable product first.

This was also our first time working with Taipy, as this was one of the sub-prizes, we wanted to push ourselves to use this library. WE LEARNED A LOT. I think the biggest issue we had was the lack of online resources for this library, so it was mainly reading through documentation to figure anything out. We especially had a difficult time with scaling up the pages, it seemed as though the markdown text did not read in variables properly when looped through.

Another challenge that we ran into was training the predictive model. As the model is time based and the data that we could find was not, we realized we could no longer make use of the predictive model and would instead need to shift to a simple regression model. Unfortunately, the data we would need would not be available within a few days and would need to be collected from school to school. Ideally, we would have school specific SAT and GPA data throughout a range of calendar year (i.e. 2000-2020). Challenges and limitations affecting the model's performance and reliability include the absence of outliers and anomalies, potential model overfitting, and constrained generalization. 

However, we did still want to showcase that TaiPy Core does have the ability to create predictive models if we had the right data. And that can be seen in _mlmodel.py_.
## Accomplishments that we're proud of
- Interfacing with a new python library (TaiPy)
- Learning how to create an ML Pipeline and different scenarios
## What we learned
How to create an interactive GUI within Taipy and more about the four fundamental concepts in Taipy Core.
## What's next for UniPath
We want to find more data to help build up the credibility of the app. But this will take research and most likely visiting school by school to collect information. This data would encompass a large time range and ideally include the breakdown of the GPA to include the student's academic grades, but also the scores of the SAT sections. If we have that, this tool can be really powerful. 

Second, we want this tool to be available for students as well. Therefore, a student version of the app to come soon. The student's version would be a tool that could be used for progress tracking and as a planner to help adjust their studies to tailor best to their top universities.
