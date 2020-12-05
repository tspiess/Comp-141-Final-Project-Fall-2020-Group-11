import pandas as pd

import matplotlib.pyplot as plt



df = pd.read_csv("CTARidership.csv")

df.drop_duplicates()

df.service_date = pd.to_datetime(df.service_date)

mask = (df['service_date'] >= '2009-01-01') & (df['service_date'] <= '2019-12-31')

filtered_df = df.loc[mask]



df09 = filtered_df[filtered_df['service_date'].dt.year == 2009]

df10 = filtered_df[filtered_df['service_date'].dt.year == 2010]

df11 = filtered_df[filtered_df['service_date'].dt.year == 2011]

df12 = filtered_df[filtered_df['service_date'].dt.year == 2012]

df13 = filtered_df[filtered_df['service_date'].dt.year == 2013]

df14 = filtered_df[filtered_df['service_date'].dt.year == 2014]

df15 = filtered_df[filtered_df['service_date'].dt.year == 2015]

df16 = filtered_df[filtered_df['service_date'].dt.year == 2016]

df17 = filtered_df[filtered_df['service_date'].dt.year == 2017]

df18 = filtered_df[filtered_df['service_date'].dt.year == 2018]

df19 = filtered_df[filtered_df['service_date'].dt.year == 2019]



df09b = (df09["bus"].mean())

df09r = (df09["rail_boardings"].mean())

df10b = (df10["bus"].mean())

df10r = (df10["rail_boardings"].mean())

df11b = (df11["bus"].mean())

df11r = (df11["rail_boardings"].mean())

df12b = (df12["bus"].mean())

df12r = (df12["rail_boardings"].mean())

df13b = (df13["bus"].mean())

df13r = (df13["rail_boardings"].mean())

df14b = (df14["bus"].mean())

df14r = (df14["rail_boardings"].mean())

df15b = (df15["bus"].mean())

df15r = (df15["rail_boardings"].mean())

df16b = (df16["bus"].mean())

df16r = (df16["rail_boardings"].mean())

df17b = (df17["bus"].mean())

df17r = (df17["rail_boardings"].mean())

df18b = (df18["bus"].mean())

df18r = (df18["rail_boardings"].mean())

df19b = (df19["bus"].mean())

df19r = (df19["rail_boardings"].mean())



data = [["2009", df09b, df09r], ["2010", df10b, df10r], ["2011", df11b, df11r],

        ["2012", df12b, df12r], ["2013", df13b, df13r], ["2014", df14b, df14r],

        ["2015", df15b, df15r], ["2016", df16b, df16r], ["2017", df17b, df17r],

        ["2018", df18b, df18r], ["2019", df19b, df19r]]



df = pd.DataFrame(data, columns=["Year", "Average Daily Bus Riders", "Average Daily Train Riders"])



print(df)



ax = plt.gca()



df.plot(kind='line', x='Year', y='Average Daily Bus Riders', ax=ax)

df.plot(kind='line', x='Year', y='Average Daily Train Riders', color='red', ax=ax)



plt.show()
