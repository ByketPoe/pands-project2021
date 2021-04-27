# file_i_o.py
# The purpose of this program is to store functions relating to file input/output.
# author: Emma Farrell
import os
import sys
import numpy as np
import pandas as pd

def check_file_exists(file_path):
    return os.path.exists(file_path)

def read_df_to_file(data_frame, cols_df, filename):
    df_rounded = data_frame.round(1)
    #print(df_rounded)
    df_to_nparray = df_rounded.to_numpy()
    colsdf_to_nparray = cols_df.to_numpy()
    print(colsdf_to_nparray)
    #np.set_printoptions(suppress=True, precision=1, floatmode='fixed')
    #print(df_to_nparray)
    with open(filename, "at") as fn:
        #pd.cols_df.tofile(filename)
        np.savetxt(filename, colsdf_to_nparray, '%s')
        fn.write('\n')
        #np.savetxt(filename, df_to_nparray, fmt='%1.1f')

    with open(filename, "at") as fn:
        np.savetxt(filename, df_to_nparray, fmt='%1.1f')
    #with open(filename, "wt", encoding="utf-8") as fn:
        #fn.write(df_to_nparray)
        #fn.write(data_frame)


#def save_fig():