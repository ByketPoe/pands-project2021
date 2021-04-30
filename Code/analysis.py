# analysis.py
# The purpose of this program is to carry out analysis on the Iris Data Set and output the findings as text and images.
# author: Emma Farrell

# Section 1: Modules
# The modules requried for this analysis are imported.

# Pandas is used to save the data into a dataframe to make it easy to view and manipulate.
# Matplotlib and Seaborn are both used in the generation of plots
# I created a module called file_i_o to store functions that handle file input and output.
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb
import file_i_o as f


# Section 2: Data Input
# This section will deal with reading in the data and saving it in different formats.

# The file that stores the data does not provide column names, so they are defined and stored as a list.
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# The read_csv function from the pandas module is called to read the data from the irisdata csv file.
# The file is stored in a separate folder, so the path to the file is provided. 
# The list of column names created above is passed as an argument into this function. 
# This assigns the column names to the columns in the order in which they appear in the list and in the file. 
# The function returns a dataframe. This is a useful data type in the pandas module that makes viewing and manipulating data easier for analysis purposes. 
# The dataframe is saved to the variable iris_data_frame. 
iris_data_frame = pd.read_csv("../irisdata.csv", names = column_names)

# The data in the dataframe is subdivided by species and saved to separate variables. This does not affect the original dataframe. 
# One of the useful aspects of pandas dataframes is that it allows querying of the dataframe using conditional statements. 
# In this case, this takes the data from the rows where the column 'species' equals the specified string. 
# These new dataframe subdivisions are save to variables. We can now do separate analysis for each species. 
# This will be useful for the calculations that will be read into the text file at the end of this script. 
setosa_df = iris_data_frame[iris_data_frame['species'] == 'Iris-setosa']
versicolor_df = iris_data_frame[iris_data_frame['species'] == 'Iris-versicolor']
virginica_df = iris_data_frame[iris_data_frame['species'] == 'Iris-virginica']


# Section 3: Data Output - Plotting
# This section of code will create plots from the data and save them to image files. 

# The name of the file that the histograms will be saved to is defined and assigned to a variable. 
histplot_file = 'fig1_hist.png'

# A list of the plots to be made is created and stored in a variable. 
histplot_list = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# An if statement checks if the histogram image file exists. 
# The check_file_exists function is in the module file_i_o created for this project. 
if not f.check_file_exists(histplot_file):
    # The plt.figure function sets the width and height of the plot in inches. 
    plt.figure(figsize=(12, 8))
    # A for loop iterates through an enumerated version of the list of histogram plots created above. 
    # The enumerate() function takes in an iterable (such as a list) and returns a list of tuples consisting of each list item's index and the item itself. 
    # 'i' will refer to each tuple in the list as it is iterated over. The items in the tuple can be accessed using indexing. 
    # In this case, in the first iteration, i[1] will refer to 'sepal_length', in the third iteration, i[1] will refer to 'petal_length' etc. 
    # i[0] will always refer to the index that the item had in the original list e.g. i[0] for the second iteration (sepal_width) will be 1. 
    for i in enumerate(histplot_list):
        # Subplots are useful for displaying multiple plots in one output.
        # The subplot function sets how many rows and columns of plots there will be and assigns an ID to each figure. 
        # To output one row of four plots, the function would be plt.subplot(1, 4). In this case there will be two rows and two columns of plots. 
        # The last argument is the figure ID. They cannot be zero, and list indexing starts at 0, so 1 is added to get around this. 
        plt.subplot(2, 2, i[0]+1)
        # The histplot function from the seaborn module creates the histrogram. 
        # The data from iris_data_frame created previously will be plotted on the histogram. 
        # The 'x=i[1]' argument tells the function what to use as the x axis of the plot. 
        # In this case, the second item (index 1) of the current tuple (i) will be the x axis (sepal_length, sepal_width etc.). 
        # The hue argument is set to species. This colour codes the data according to species, allowing to differentiate and compare on the plot. 
        # The bins argument sets how many portions the histogram will be divided into on the x axis. 
        # Increasing the number of bins allows for a better impression of the shape and spread of the data. 
        sb.histplot(data = iris_data_frame, x=i[1], hue='species', bins=20)
    # The save_fig function is in the module file_i_o created for this project.
    # The function saves the histograms created into the file at the path created above. 
    f.save_fig(histplot_file)

# Pairplots are useful for creating plots that show correlation between variables in a dataset and so are used in this analysis. 
# The name of the file that the pairplot will be saved to is defined and assigned to a variable. 
pairplot_file = 'fig2_pairplot.png'

# The pairplot is created using the data in iris_data_frame. 
# The plot is colour coded according the the species column, similar to what was done with the histograms above. 
sb.pairplot(iris_data_frame, hue = 'species')

# An if statement checks if the pairplot image file exists. 
# The check_file_exists function is in the module file_i_o created for this project. 
if not f.check_file_exists(pairplot_file):
    # The save_fig function is in the module file_i_o created for this project.
    # The function saves the pairplot created into the file at the path created above. 
    f.save_fig(pairplot_file)


# Section 4: Data Output - Textfile
# This section of code will create data summaries of the data and save them to a text file. 

# Lists of columns are created to be used in the output text file. 
# The .columns function gets all of the columns from the iris_data_frame datafram and the result is saved to the variable cols. 
cols = iris_data_frame.columns
# The summary created by the .describe function below created a dataframe with an added column to describe the calculation (e.g. count). 
# This list needed to be created to account for this and the extra column is called 'value'. 
summary_cols = ['value', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width']
# The correlation calculation .corr used below outputs a table with the first column showing the variables to compare with the column headers. 
# This list needed to be created to account for this and the first column name is left blank as it is not required. 
corr_cols = ['', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# The name of the file that the text output will be saved to is defined and assigned to a variable. 
output_file = 'analysis_output.txt'

# An if statement checks if the text file exists. 
# The check_file_exists function is in the module file_i_o created for this project. 
if not f.check_file_exists(output_file):
    # Various data summaries are saved to the text file created above. 
    # The read_df_to_file function is in the module file_i_o created for this project. 
    # It takes in four arguments, a dataframe, a title to describe the data, a list of column names and a file name. 
    # It outputs the data to a text file in a tabulated format. 
    # The .head function returns the first five rows of a dataframe, and is useful for showing a sample of the data in the dataframe. 
    f.read_df_to_file(iris_data_frame.head(), 'Data Sample (first five rows)', cols, output_file)
    # The .describe function returns a table showing various calculations of the data such as count, mean, percentiles (25%, 50% and 75%) etc. 
    # Here, the describe function is called for the data in its entirety and broken down by species. 
    f.read_df_to_file(iris_data_frame.describe(), 'Data Summary (all species)', summary_cols, output_file)
    f.read_df_to_file(setosa_df.describe(), 'Data Summary (Setosa)', summary_cols, output_file)
    f.read_df_to_file(versicolor_df.describe(), 'Data Summary (Versicolor)', summary_cols, output_file)
    f.read_df_to_file(virginica_df.describe(), 'Data Summary (Virginica)', summary_cols, output_file)
    # The .corr function returns a dataframe showing correlation calculations for each pair of variables.  
    # Correlation is useful for showing how related two sets of data are on a scale from 0-1. The closer to 1, the more correlation there is. 
    # A negative number shows an inverse relationship, i.e. as one variable increases, the other decreases. 
    # Data being compared with itself (e.g. comparing sepal length with sepal length) will have a correlation of 1 as it is all the same data. 
    # Therefore, the left to right descending diagonals of the tables all have values of 1. 
    # Here, the corr function is called for the data in its entirety and broken down by species.
    f.read_df_to_file(iris_data_frame.corr(), 'Variable Correlations (all species)', corr_cols, output_file)
    f.read_df_to_file(setosa_df.corr(), 'Variable Correlations (Setosa)', corr_cols, output_file)
    f.read_df_to_file(versicolor_df.corr(), 'Variable Correlations (Versicolor)', corr_cols, output_file)
    f.read_df_to_file(virginica_df.corr(), 'Variable Correlations (Virginica)', corr_cols, output_file)