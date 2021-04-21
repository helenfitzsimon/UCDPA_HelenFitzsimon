# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import csv file into a pandas dataframe
imdb_dataset = pd.read_csv('imdb_top_1000.csv')

# analyse the dataframe
print(imdb_dataset.head())
print(imdb_dataset.tail())
print(imdb_dataset.shape)
print(imdb_dataset.columns)

# check null values
print(imdb_dataset.isnull().sum())

# drop unnecessary columns
imdb_dataset.drop(['Poster_Link', 'Overview', 'Certificate'], axis='columns', inplace=True)

print(imdb_dataset.shape)

#Check for duplicates - (no duplicates present)
drop_duplicates = imdb_dataset.drop_duplicates()
print(imdb_dataset.shape, drop_duplicates.shape)

# Check prime id key
print(len(imdb_dataset.Series_Title.unique()))

print(imdb_dataset['Series_Title'])

print(imdb_dataset.loc[:5, ['Series_Title', 'Gross']])

print(imdb_dataset.loc[0])

# Number of top 1000 movies since 2018
Recent_Top_Movies = imdb_dataset[imdb_dataset['Released_Year'] >= '2018']

print(Recent_Top_Movies)

print(imdb_dataset['Released_Year'].value_counts())

print(type('Released_Year'))

print(imdb_dataset['Gross'].value_counts())

# Change PG to 1995 for Apollo 13
print(imdb_dataset.loc[966,:])

imdb_dataset['Released_Year'].replace('PG', '1995', inplace=True)

print(imdb_dataset.loc[966,:])


print(imdb_dataset.describe())

list1= imdb_dataset.loc[:, ['IMDB_Rating', 'Meta_score']]
print(list1)

# Fill the missing values of Meta score with the mean
imdb_dataset['Meta_score'].fillna((imdb_dataset['Meta_score'].mean()), inplace=True)

print(imdb_dataset.isnull().sum())

# Fill the missing values in the Gross column
  # get the types in the column
print(imdb_dataset['Gross'].apply(type))

# Overall column dtype is object
print(imdb_dataset['Gross'].apply(type).value_counts())

def clean_gross(x):

    ##If the value is a string, then remove delimiters
    if isinstance(x, str):
        return(x.replace(',', ''))
    return(x)

imdb_dataset['Gross'] = imdb_dataset['Gross'].apply(clean_gross).astype('float')

print(imdb_dataset.dtypes)

print(imdb_dataset['Gross'].describe())

imdb_dataset['Gross'].fillna((imdb_dataset['Gross'].median()), inplace=True)

print(imdb_dataset.isnull().sum())





