import pandas as pd

d = pd.read_csv("student_performance.csv")
print("Original Data:\n")
print(d)
subjects = ["Math", "English", "Science", "Social"]
mea = d[subjects].mean()
add = d[subjects].sum()
d.loc['Total'] = ['-', add['Math'], add['English'], add['Science'], add['Social']]
d.loc['Average'] = ['-', mea['Math'], mea['English'], mea['Science'], mea['Social']]
d['Total'] = d[subjects].sum(axis=1)
d['Average'] = d[subjects].mean(axis=1)
d.loc[d.index[:-2], 'Grade'] = d.loc[d.index[:-2], 'Average'].apply(lambda x: 'A' if x>=85 else 'B' if x>=70 else 'C' if x>=50 else 'F')
print(d)