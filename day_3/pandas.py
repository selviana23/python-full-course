import pandas as pd
data = {
    'name': ['Alice' , 'bob' , 'Carol'],
    'age': [25, 30, 35]
}
df = pd.DataFrame(data)
print(df)
print(df['age'].mean())