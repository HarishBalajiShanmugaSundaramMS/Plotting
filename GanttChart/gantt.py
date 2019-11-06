import matplotlib.pyplot as plt
import plotly.figure_factory as ff
df = [
    dict(Task="Task 05", Start='2020-02-02', Finish='2020-02-16'),
    dict(Task="Task 04", Start='2020-03-01', Finish='2020-03-15'),
    dict(Task="Task 03", Start='2020-02-16', Finish='2020-03-15'),
    dict(Task="Task 02", Start='2020-01-20', Finish='2020-03-15'),
    dict(Task="Task 01", Start='2020-01-16', Finish='2020-02-28')
]
fig = ff.create_gantt(df,showgrid_x=True,showgrid_y=True)
fig.show()
