import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


imdb_data = pd.read_csv('imdb_top_1000.csv')

print(imdb_data.head(10))
print(imdb_data.tail(10))
print(imdb_data.shape)
print(imdb_data.columns)

missing_values_count = imdb_data.isnull().sum()

print(missing_values_count)

