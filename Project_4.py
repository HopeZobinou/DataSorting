import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Write your def lines and functions below
#The def lines you create must match the specifications exactly
#You cannot change the names of the functions, the variables, or the default arguments
#Expect a large grade penalty if your def lines are not correct
#This file should not contain any function calls or any code that is not part of
#A function definition
#This means any code unindented besides a def line or the import lines at the top

def make_subset(df, region = None, vaccine = None, year = None): #Makes subsets out of a data frame, returns a data frame
    New_df = df.copy() #Makes a copy of the users data frame.
    if region != None and vaccine != None and year != None: #If region, vaccine, and year are all filled in, the subset will include those 3
        New_df = New_df.loc[New_df["Region"].isin(region) & New_df["Vaccine"].isin(vaccine) & New_df["Year"].isin(year)]
    elif region != None and vaccine != None: #If region and vaccine are filled in, it will subset those 2
        New_df = New_df.loc[New_df["Region"].isin(region) & New_df["Vaccine"].isin(vaccine)]
    elif region != None and year != None: #If region and year are filled in, it will subset those 2
        New_df = New_df.loc[New_df["Region"].isin(region) & New_df["Year"].isin(year)]
    elif vaccine != None and year != None: #If vaccine and year are filled in, it will subset those 2
        New_df = New_df.loc[New_df["Vaccine"].isin(vaccine) & New_df["Year"].isin(year)]
    elif region != None: #If region is filled in, it will subset only region
        New_df = New_df.loc[New_df["Region"].isin(region)]
    elif vaccine != None: #If vaccine is filled in, it will subset vaccine only
        New_df = New_df.loc[New_df["Vaccine"].isin(vaccine)]
    elif year != None: #If year is filled in, it will subset year only
        New_df = New_df.loc[New_df["Year"].isin(year)]
    return New_df #Returns the new Dataframe that is subsetted

def make_plot(series_object, title ='', bar = True): #Takes in a series and returns a bar or line graph  
    if bar == True: #Makes a bar graph
        sns.barplot(y = series_object.index, x = series_object.values, orient = 'h') #Makes the y axis the index of the series, makes the x axis the values of the series, and orient makes it horizontal
        plt.title(title) #Titles the graph
    elif bar == False: #Makes a line graph
        sns.lineplot(x = series_object.index, y = series_object.values) #Makes the x axis the index of the series and makes the y axis the values of the series
        plt.title(title) #Makes the title
        plt.xticks(rotation = 90) #Rotates the names on the x axis by 90 degrees 