import csv
import pandas as pd
import plotly.express as px

with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
totalMarks=0
totalEntries=len(file_data)

for marks in file_data:
    totalMarks=totalMarks+float(marks[1])

mean=totalMarks/totalEntries
print("Mean = "+str(mean))

df = pd.read_csv("data.csv")
fig=px.scatter(df, x="Index", y="Weight")
fig.update_layout(shapes=[
    dict(type='line', y0=mean, y1=mean, x0=0, x1=totalEntries)
])

fig.show()
def get_median(totalEntries,sorted_data):
    if totalEntries%==0:
        