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

column_names = ['Sepal Length (cm)', 'Sepal Width (cm)', 'Petal Length (cm)', 'Petal Width (cm)', 'Class']

iris_data_frame = pd.read_csv("../irisdata.csv", names = column_names)
#iris_data_frame.columns = 
sb.set_theme()
sb.histplot(iris_data_frame['Sepal Length (cm)'])
plt.show()

print(iris_data_frame.describe())