# analysis.py
# The purpose of this program is to carry out analysis on the Iris Data Set and output the findings.
# author: Emma Farrell

# When this gets run, the analysis gets carried out and outputted to a file + images
# Summary data - mean, std deviation, mode etc.
# Plots, histograms, scatter plots, bar charts
# file type: csv
# need to pivot? 
# df.head() to print out the first few lines to give idea of the content

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb

# Split classes into different files

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

iris_data_frame = pd.read_csv("../irisdata.csv", names = column_names)

setosa_df = iris_data_frame[iris_data_frame['class'] == 'Iris-setosa']
versicolor_df = iris_data_frame[iris_data_frame['class'] == 'Iris-versicolor']
virginica_df = iris_data_frame[iris_data_frame['class'] == 'Iris-virginica']

s_length = iris_data_frame['sepal_length']
s_width = iris_data_frame['sepal_width']
p_length = iris_data_frame['petal_length']
p_width = iris_data_frame['petal_width']
#iris_data_frame.columns = 
sb.set_theme()
#sb.histplot(iris_data_frame['sepal_length'])
sb.pairplot(iris_data_frame)
plt.show()

#print(iris_data_frame.describe())
#print(setosa_df.describe())
#print(versicolor_df.describe())
#print(virginica_df.describe())
#print(s_length)
#print(s_width)
#rint(p_length)
print(p_width.describe())