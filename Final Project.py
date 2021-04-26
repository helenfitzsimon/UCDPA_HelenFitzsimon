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

# Top 10 Highest earning movie
Highest_earning_movies=imdb_dataset.sort_values(by=['Gross'], ascending=False).head()

# Find the best Director
print(imdb_dataset.groupby('Director').IMDB_Rating.mean().sort_values(ascending= False).head(10))


# Compare the top 5 movies
top_5_voted_movies = imdb_dataset.sort_values(['No_of_Votes'], ascending=False).head()
fig,axs=plt.subplots(figsize=(35,5))
a=sns.barplot(x=top_5_voted_movies['Series_Title'][:5], y=top_5_voted_movies['No_of_Votes'][:5], palette = 'hls')
a.set_title("Top 5 Voted Movies", weight = "bold")
plt.xlabel('Movie Title')
plt.ylabel('No. of votes (million)')
plt.show()

# get the IMDB rating of the top 5 movies and plot
fig,axs=plt.subplots(figsize=(15,5))
a=sns.barplot(x=top_5_voted_movies['Series_Title'][:5],y=top_5_voted_movies['IMDB_Rating'][:5], palette = 'husl')
a.set_title("IMDB Rating of top 5 voted movies", weight = "bold")
plt.xlabel('Movie Title')
plt.ylabel('IMDB Rating')
plt.show()

# get the Metascore of the top 5 movies and plot
fig,axs=plt.subplots(figsize=(15,5))
a=sns.barplot(x=top_5_voted_movies['Series_Title'][:5],y=top_5_voted_movies['Meta_score'][:5], palette = 'husl')
a.set_title("Metascore of top 5 voted movies", weight = "bold")
plt.xlabel('Movie Title')
plt.ylabel('Metascore')
plt.show()

# Plot the gross of the top 5 movies
fig,axs=plt.subplots(figsize=(15,5))
a=sns.barplot(x=top_5_voted_movies['Series_Title'][:5],y=top_5_voted_movies['Gross'][:5], palette = 'husl')
a.set_title("Gross of top 5 movies", weight = "bold")
plt.xlabel('Movie Title')
plt.ylabel('Gross (100 millions)')
plt.show()

# Show the highest earning movies
highest_earning = imdb_dataset.sort_values(['Gross'], ascending= False).head()
fig,axs=plt.subplots(figsize=(15,5))
g=sns.barplot(x=highest_earning['Series_Title'][:5],y=highest_earning['Gross'][:5], palette = 'husl')
g.set_title("Highest earning movies", weight = "bold")
plt.xlabel('Movie Title')
plt.ylabel('Gross (100 million)')
plt.xticks(fontsize=10)
plt.show()

# Remove string min from runtime and change to integer, add to new column duration
import re
duration=[]
for x in imdb_dataset["Runtime"]:
    m=re.compile('\d+')
    l=m.findall(x)
    if len(l)==2:
        duration.append(int(l[1])-int(l[0])+1)
    else:
        duration.append(int(l[0])+1)
imdb_dataset['duration']=duration

print(imdb_dataset['duration'])

print(imdb_dataset.duration.mean())
duration_sorted= imdb_dataset.sort_values('duration')
print(duration_sorted.head())
print(duration_sorted.tail())

# See distribution of runtime
plt.figure(figsize=(10,6))
runtime= sns.distplot(imdb_dataset['duration'], color = 'blue')
runtime.axes.set_title('Movie runtime distribution', fontsize=15)
runtime.set_xlabel('Runtime (mins)', fontsize=10)
plt.show()

# Now compare to boxplot
imdb_dataset.duration.plot(kind='box')

# Now compare runtime with the year movie was released
Runtime_by_year = imdb_dataset['duration'].groupby(imdb_dataset['Released_Year']).describe()

avg_runtime_by_year = Runtime_by_year['mean']
avg_runtime_min = Runtime_by_year['mean'] - Runtime_by_year['std']
avg_runtime_max = Runtime_by_year['mean'] + Runtime_by_year['std']

fig, ax = plt.subplots(figsize=(15,5))
ax.plot(avg_runtime_by_year, color='coral')
ax.plot(avg_runtime_min, color='peachpuff')
ax.plot(avg_runtime_max, color='peachpuff')
ax.fill_between(Runtime_by_year.index, avg_runtime_min, avg_runtime_max, color='peachpuff')
ax.set_title('The average movie runtime over the years', fontsize=15)
ax.set_xlabel('Released Year')
ax.set_ylabel('Duration (minutes)')
plt.xticks(rotation = 90, fontsize=5)
plt.show()

# Find the most popular genres
# First split the rows with more than one genre
imdb_dataset['genre']=imdb_dataset['Genre'].str.split(r'\s*,\s*').explode('Genre')
print(imdb_dataset['genre'])

# Get the number of times a genre appears in top 1000 movies
genre_count= imdb_dataset.genre.value_counts().head(10)
print(genre_count)

#using numpy find the 1st and 10th most popular genre
b = np.array([genre_count])
print(b.max())
print(b.min())

# Get only the top 10 genres
imdb_dataset.genre.value_counts().head(10).plot(kind='barh')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.title('The 10 most popular genres')
plt.show()

# Concatenate the IMDB Rating, Metascore and No.of votes of the top 3 movies
x = [9.3, 9.2, 9]
y = [80, 100, 84]
z = [2343110, 134966411, 534858444]
print(np.concatenate([x, y, z]))







