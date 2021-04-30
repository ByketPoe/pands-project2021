# file_i_o.py
# The purpose of this program is to store functions relating to file input/output.
# author: Emma Farrell

# The modules requried for file functions are imported.

# os will be used to check if the files exist. 
# tabulate is a module found online used to print dataframes etc. in a tabulated format. 
# matplotlib.pyplot is used to save the figures created in the analysis script.  
import os
import tabulate as t
import matplotlib.pyplot as plt

# check_file_exists takes in a file path and uses the .exists function from the os module to check if the file exists. 
# The function returns a boolean; True if the file exists otherwise False. 
def check_file_exists(file_path):
    return os.path.exists(file_path)

# read_df_to_file takes in four arguments: a dataframe, a string to become the title of the table, a list for column headers and a file name. 
# It writes the dataframe to the text file with some added formatting at the beginning and end to separate out all of the tables in the file. 
def read_df_to_file(data_frame, title, col_headers, filename):
    # title_border, title_dressing and footer are variables that store strings used create headers and footers for each table written to the text file. 
    title_border = '=============================================='
    title_dressing = ' *** '
    footer = '\\\\\\\\\=============================================================/////'
    # The file is opened in append/text mode. Append mode ensures that previous text will not be overwritten. 
    with open(filename, 'at') as ft:
        # The header is formed using tabs, new lines, formatting strings created above and the title passed into the function. 
        ft.write('\t\t\t\t')
        ft.write(title_border + '\n')
        ft.write('\t\t\t\t')
        ft.write(title_dressing + title + title_dressing + '\n')
        ft.write('\t\t\t\t')
        ft.write(title_border + '\n\n')
        # The tabulate function from the tabulate module is used to write the dataframe passed into the function to the file in a tabulated format. 
        # The list of column names is passed into the argument headers. 
        # There are various styles available, and they are set using the tablefmt argument. 
        # This uses the github style, chosen for showing borders around the columns making data easier to read. 
        ft.write(t.tabulate(data_frame, headers=col_headers, tablefmt="github"))
        # The footer under the table is written to the file to separate out the tables visually. 
        ft.write('\n\n')
        ft.write('\t')
        ft.write(footer + '\n\n\n\n')

# The save_fig function takes in the file name that the figure will be saved to. 
# The .savefig function is called from the matplotlib.pyplot module. This saves the current figure to the file passed into the function. 
def save_fig(fig_filename):
    plt.savefig(fig_filename)