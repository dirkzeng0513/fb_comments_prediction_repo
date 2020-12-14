'''
function for data read-in and initial datatype processing(the important part is how to handle the date format)
'''
import pandas as pd
import numpy as np


# alternative of datetime field parsing /* parse_dates = ['datefield']
def load_data(csv_path, dtypes=False, header=0):
    if dtypes:
        results = pd.read_csv(csv_path, dtype=dtypes, header=header)  # parse_dates = ['datefield']*/)
    else:
        results = pd.read_csv(csv_path, header=header)
    # dropping duplicate values
    results.drop_duplicates(keep=False, inplace=True)
    # replace N/A in numeric variables to zeros (use it with extra care if NaN has practical meanings)
    # txn_data.select_dtypes(include = ['float64','int64']).fillna(0, inplace=True) inpace = True will return None type
    results.loc[:, (results.dtypes == 'int64') | (results.dtypes == 'float64')] = \
        results.loc[:, (results.dtypes == 'int64') | (results.dtypes == 'float64')].replace(np.nan, 0)
    return results
