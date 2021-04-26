# file_i_o.py
# The purpose of this program is to store functions relating to file input/output.
# author: Emma Farrell
import os

def check_file_exists(file_path):
    return os.path.exists(file_path)

def read_df_to_file(data_frame, filename):
    with open(filename, "wt") as fn:
        #fn.write(data_frame.describe())
        fn.write(data_frame)


#def save_fig():