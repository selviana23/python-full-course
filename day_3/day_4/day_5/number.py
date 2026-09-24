import pandas as pd
data={ "name": ["riddhica", "selviana", "prasansha", "karuna", "kriti"],
        "marks": [90,85,87,76,34]}
df=pd.DataFrame(data)
print(df)
print("highest score:")
print(df["marks"].max())
df["passed"]= df["marks"] >=50
print(df)
print("pass count:",df["passed"].sum())