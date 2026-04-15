import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales"],
    "Marks": [85, 78, 92, 70, 88, 76],
    "Age": [21, 22, 20, 23, 21, 22]
}

df = pd.DataFrame(data)
print(df)

top_marks = df[df["Marks"]>80]
Dep = df[(df["Marks"]>80) & (df["Department"] == "Sales")]
print("hi")


