# file_i_o.py
# The purpose of this program is to store functions relating to file input/output.
# author: Emma Farrell
import os
import sys
import numpy as np
import pandas as pd
import tabulate as t

def check_file_exists(file_path):
    return os.path.exists(file_path)

def read_df_to_file(data_frame, title, col_headers, filename):
    title_border = '======================================'
    title_dressing = ' *** '
    footer = '\\\\\\\\\========================================================/////'
    with open(filename, 'at') as ft:
        ft.write('\t\t\t')
        ft.write(title_border + '\n')
        ft.write('\t\t\t')
        ft.write(title_dressing + title + title_dressing + '\n')
        ft.write('\t\t\t')
        ft.write(title_border + '\n\n')
        ft.write(t.tabulate(data_frame, headers=col_headers, tablefmt="github"))
        ft.write('\n\n')
        ft.write('\t')
        ft.write(footer + '\n\n\n\n')

    #df_rounded = data_frame.round(1)
    #print(df_rounded)
    #df_to_nparray = df_rounded.to_numpy()
    #print(cols_df)
    #df_list = df_to_nparray.tolist()
    #print(df_list)
    #cols_list = cols_df.tolist()
    #colsdf_to_nparray = cols_df.to_numpy()
    #print(cols_df)
    #np.set_printoptions(suppress=True, precision=1, floatmode='fixed')
    #print(df_to_nparray)
    #with open(filename, 'w') as fn:
        #pd.cols_df.tofile(filename)
        #for col_name in cols_list:
            #fn.write(col_name + '\t')
            #fn.write('\t')
        #fn.write('\n')

        #for row in df_list:
            #fn.write('\n')
            #for col in row:
                #col = str(col)
                #fn.write(col + '\t\t\t\t\t')
            #fn.write('\n')

    #with open(filename, 'a') as fn:
        #np.savetxt(filename, df_to_nparray, fmt = '%1.1f', delimiter='\t')
        #fn.write('\n')
        #np.savetxt(filename, df_to_nparray, fmt='%1.1f', delimiter=', ')

    #with open(filename, "at") as fn:
        #np.savetxt(filename, df_to_nparray, fmt='%1.1f')
    #with open(filename, "wt", encoding="utf-8") as fn:
        #fn.write(df_to_nparray)
        #fn.write(data_frame)


#def save_fig():