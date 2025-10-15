import pandas as pd

popList = [56286961, 5463300, 3152879, 1893667]
print(popList)
print("-----")
cNames= pd.Series(["England", "Scotland", "Wales", "Northern Ireland"])
print (cNames)
print("-----")
df = pd.DataFrame()
df["country"] = cNames
pop = pd.Series([56286961, 5463300, 3152879, 1893667])
df["pop"] = pop
print(df)
print("-----")
print(df.iloc[0:1])
print("-----")
#Select all rows for columns starting at 0 and up to, but not including, column 1
print(df.iloc[:,0:1])
print("-----")
#Select all rows and all columns
print(df.iloc[:,:])
print("-----")
# Access a single element as an indexed DataFrame or as a single value.
print(df.iloc[0:1,1:2])
print("-----")
print(df.iloc[0,1])
# Conditional access to a set of rows based on column values.
print("-----")
print(df[df["pop"] < 50000000])