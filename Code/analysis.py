# analysis.py
# The purpose of this program is to carry out analysis on the Iris Data Set and output the findings as text and images.
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
import file_i_o as f
import io
import numpy as np

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
#sb.set_theme()
#sb.histplot(iris_data_frame['sepal_length'])
#sb.pairplot(iris_data_frame, hue = 'class')
#plt.show()

#print(iris_data_frame.describe())
cols = iris_data_frame.columns
#print(type(cols))
# print(iris_data_frame.rows)
#print(type(iris_data_frame))
#print(setosa_df.describe())
#print(versicolor_df.describe())
#print(virginica_df.describe())
#print(s_length)
#print(s_width)
#print(p_length)
# print(p_width.describe())
# print(f.check_file_exists('file.txt'))
output_file = 'analysis_output.txt'
#f.read_df_to_file(iris_data_frame.info(buf = io.StringIO()), output_file) - doesn't work
if not f.check_file_exists(output_file):
    #f.read_df_to_file(cols, output_file)
    f.read_df_to_file(iris_data_frame.describe(), cols, output_file)

#print(iris_data_frame.info().to_numpy())

#print((iris_data_frame.info()))
#print(type(iris_data_frame.describe()))
#print(type(iris_data_frame.head()))


#df_to_nparray = iris_data_frame.to_numpy()
#df_to_nparray_rounded = np.df_to_nparray.round(decimals = 1)
#print(df_to_nparray_rounded)
#np.savetxt(filename,df_to_nparray_rounded)