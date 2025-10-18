import pandas as pd
import altair as alt


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
print("-----")
#Sort dataframes by specific column values.
df.sort_values(by="pop", ascending= True, inplace=True )
print(df)
print("-----")
# Note we have changed the index... this means we will not index by
# the newly sorted order, fix by resetting the index
df.reset_index(drop=True, inplace=True)
print(df)
print("-----")
# Lexical ordering of strings
df.sort_values( by="country", ascending = True, inplace=True )
print(df)
print("-----")



#Load excel data as pandas DataFrame
imd_df = pd.read_excel('NorthEast_Domains_of_deprivation.xlsx')
print(imd_df.head(10))
print("-----")
print(imd_df.dtypes)
print("-----")

# if a column has been interpreted as the wrong data type, you can convert the type using the
# astype() method, with syntax: df[“VariableName”]=df[‘variableName’].astype(‘int’)
# Note that you have to assign it back to the DataFrame, since astype() returns a copy.

#Rename variables
imd_df.rename(columns = {'Index of Multiple Deprivation (IMD) Rank (where 1 is most deprived)': 'IMD Rank',
'Income Rank (where 1 is most deprived)':'Income Rank',
'Employment Rank (where 1 is most deprived)':'Employment Rank',
'Education, Skills and Training Rank (where 1 is most deprived)':'Education Rank',
'Health Deprivation and Disability Rank (where 1 is most deprived)':'Health Rank',
'Crime Rank (where 1 is most deprived)':'Crime Rank',
'Barriers to Housing and Services Rank (where 1 is most deprived)':'Housing Rank',
'Living Environment Rank (where 1 is most deprived)':'Living Environment Rank',
'Local Authority District name (2013)':'District Name'}, inplace = True)
print(imd_df.dtypes)

#Set up a scatter plot displaying the IMD Rank of the different districts
chart = alt.Chart(imd_df).mark_point().encode(
x='IMD Rank:Q',
y='District Name:N'
)


#Set up a scatter plot displaying the IMD Rank average across different districts
chart_two = alt.Chart(imd_df).mark_point().encode(
x= 'average(IMD Rank):Q',
y='District Name:N'
)

#chart.save('imd_rank_chart.html')

#chart_two.save('imd_average_rank_chart.html')

#Set up a bar chart instead of a scatter plot
chart_three = alt.Chart(imd_df).mark_bar().encode(
x='average(IMD Rank)',
y='District Name'
)

#chart_three.save('imd_bar_chart.html')

#Set up a bar chart instead of a scatter plot
chart_four = alt.Chart(imd_df).mark_bar().encode(
x='District Name',
y='average(IMD Rank)'
)

#chart_four.save('imd_bar_chart_flipped.html')

#setup a scatterplot displaying IMD Rank vs Income Rank
chart_five = alt.Chart(imd_df).mark_point().encode(
x='Income Rank',
y='IMD Rank'
)

#chart_five.save('Scattered_chart.html')


#set up a scatter plot with colour distinctions
chart_six = alt.Chart(imd_df).mark_point().encode(
x='Income Rank',
y='IMD Rank',
color='District Name'
)

chart_six.save('scatter_colour_chart.html')