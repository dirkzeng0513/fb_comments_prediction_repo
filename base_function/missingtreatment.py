'''
Identify null/infinite fields
'''


def null_inf_check(input_df):
    ## check any missing or infinite values
    print(input_df.isnull().any())  # Note: np.isnan cannot be applied to object type

    # check if all the values are finite (notnull = isfinite)
    print(input_df.notnull().all())  # Note np.isfinitecannot be applied to object type

    ## check missing row count by columns
    print(input_df.isnull().sum())


'''
visualize the missing data
'''


def plot_missing(input_df):
    import seaborn as sns
    sns.heatmap(input_df.isnull(),
                yticklabels=False,
                cbar=False,
                cmap='viridis')


'''
Basic missing data imputation with static values 

Requiring a dictionary with missing attribute names and imputed values
'''


def impute_missing_static_values(input_df, imput_dict):
    # run imputation
    for key in imput_dict:
        input_df[key].fillna(imput_dict[key], inplace=True)
