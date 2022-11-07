import pandas as pd

df = pd.read_csv("a.csv", encoding="UTF-8")
# print(type(df.index))
# print(df)
print(df.loc[["shinkiso"]])


# print(type(df))

# print(df.filter(name=["name1"]))


# print(df["id"])
