'''
Add function for parallelized computation (assuming it's a quad-core processor), for large dataset
https://sebastianraschka.com/Articles/2014_multiprocessing.html
https://towardsdatascience.com/make-your-own-super-pandas-using-multiproc-1c04f41944a1
'''

import numpy as np
from multiprocessing import Pool
import pandas as pd


def parallel_function(input_df, func, n_cores):
    df_split = np.array_split(input_df, n_cores)
    pool = Pool(n_cores)
    output_df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return output_df
