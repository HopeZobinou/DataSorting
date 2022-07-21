import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Project_4 import *

#Read in the data
vaccine = pd.read_csv("vaccine_data.csv")
#Assign column names
vaccine.columns = ["Region", "Vaccine", "Year", "Percentage"] 
#print(vaccine.head())
#Update region names to replace & with and and remove spaces
vaccine['Region'] = vaccine["Region"].str.replace('&','and').str.replace(" ","_")
#print(vaccine)
#Change type of Year column to a string
vaccine["Year"] = vaccine["Year"].apply(str)
#print(vaccine)
#print(vaccine.dtypes)
#Create description column
#The dictionary line is correct, you must use the dictionary
mappings = {'BCG':'tuberculosis', 'DTP1':'diphteria_pertussis_tetanus','DTP3': 'diptheria_pertussis_tetanus',\
'MCV1':'meningococcal_disease','MCV2':'meningococcal_disease','HEPBB':'hepatitis B', 'HEPB3':'hepatitis B',\
'HIB1':'Haeomphilus influenza', 'HIB3':'Haemophilus influenza','IPV1': 'polio','IPV3': 'polio', 'POL3': 'polio','PCV3':'pneumococcal disease', 'RCV1':'rubella',\
'ROTAC':'rotavirus','YFV':'Yellow Fever Virus'}
vaccine['Description'] = vaccine["Vaccine"].apply(lambda x: mappings[x])
#Check the data frame before continuing
print(vaccine)
def make_subset(df, region = None, vaccine = None, year = None): #Makes subsets out of a data frame, returns a data frame
    New_df = df.copy() #Makes a copy of the users data frame.
    if region != None and vaccine != None and year != None:
        New_df = New_df.loc[New_df["Region"].isin(region) & New_df["Vaccine"].isin(vaccine) & New_df["Year"].isin(year)]
    elif region != None and vaccine != None:
        New_df = New_df.loc[New_df["Region"].isin(region) & New_df["Vaccine"].isin(vaccine)]
    elif region != None and year != None:
        New_df = New_df.loc[New_df["Region"].isin(region) & New_df["Year"].isin(year)]
    elif vaccine != None and year != None:
        New_df = New_df.loc[New_df["Vaccine"].isin(vaccine) & New_df["Year"].isin(year)]
    elif region != None:
        New_df = New_df.loc[New_df["Region"].isin(region)]
    elif vaccine != None:
        New_df = New_df.loc[New_df["Vaccine"].isin(vaccine)]
    elif year != None:
        New_df = New_df.loc[New_df["Year"].isin(year)]
    return New_df
#print(make_subset(vaccine, region = ['Global','Western_Europe'], vaccine = ['POL3', 'DTP1'], year = ["1980", "2017"]))
#print()
#print(make_subset(vaccine, region = ["Global"], vaccine = ["BCG", "IPV1"]))
#print()
#print(make_subset(vaccine, region = ["North_America"], year = ["1991"]))
#print()
#print(make_subset(vaccine, vaccine = ["ROTAC", "YFV"], year = ["1998"]))
#print()
#print(make_subset(vaccine, region = ["Global"]))
#print()
print(make_subset(vaccine, vaccine = ["HEPB3"]))
#print()
#print(make_subset(vaccine, year = ["2006"]))
#print()
#print(make_subset(vaccine, region = ["a"], vaccine = ['v'], year = ['2000']))
DPT1_Years = make_subset(vaccine, region = ["East_Asia_and_Pacific"], vaccine = ["DPT1"])
#print(DPT1_Years)
vac_series = vaccine.groupby("Region")["Percentage"].mean()
#print(vac_series)
def make_plot(series_object, title ='', bar = True): #Takes in a series and returns a bar or line graph  
    if bar == True: #Makes a bar graph
        sns.barplot(y = series_object.index, x = series_object.values, orient = 'h') #Makes the y axis the index of the series, makes the x axis the values of the series, and orient makes it horizontal
        plt.title(title) #Titles the graph
    elif bar == False: #Makes a line graph
        sns.lineplot(x = series_object.index, y = series_object.values) #Makes the x axis the index of the series and makes the y axis the values of the series
        plt.title(title) #Makes the title
        plt.xticks(rotation = 90) #Rotates the names on the x axis by 90 degrees 
#graph = make_plot(vac_series, "Test")
#plt.show()
#graph2 = make_plot(vac_series, "Test", False)
#plt.show()
