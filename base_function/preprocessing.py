# '''
# Date format transformation
# '''
# # datetime transformation
import pandas as pd
from datetime import datetime


def date_trans(input_df, datetime_format='%Y/%m/%d:%I:%M:%S %p', datetime_field=False, date_field=False):
    # to handle missing field: NaT
    def dateFunc(x):
        try:
            return datetime.strptime(x, datetime_format)
        except:
            return pd.NaT

    # for datetime fields
    if datetime_field:
        for column in datetime_field:
            input_df[column] = input_df[column].apply(lambda x: dateFunc(x))
    # for date fields
    if date_field:
        for column in date_field:
            input_df[column] = pd.to_datetime(input_df[column], errors='coerce')  # errors to handle missing time attr
            # input_df[column] = input_df[column].apply(dateutil.parser.parse, dayfirst = dayfirst_)
    return input_df


'''
add new datefeatures
'''


def new_time_var(input_df, timestamp):
    # extract to create aggregated date fields (concatenate two string columns)
    input_df['yr'] = input_df[timestamp].dt.year.astype(str)
    input_df['week'] = input_df[timestamp].dt.isocalendar().week.astype(str).apply(lambda x: x.zfill(2))
    input_df['month'] = input_df[timestamp].dt.month.astype(str).apply(lambda x: x.zfill(2))
    input_df['yr_mth'] = input_df[timestamp].dt.year.astype(str) + '_' + input_df[timestamp].dt.month.astype(str).apply(
        lambda x: x.zfill(2))
    input_df['yr_week'] = input_df[timestamp].dt.year.astype(str) + '_' + input_df[
        timestamp].dt.isocalendar().week.astype(str).apply(lambda x: x.zfill(2))
    input_df['day_of_mth'] = input_df[timestamp].dt.day.astype(str)
    input_df['day_of_wk'] = input_df[timestamp].apply(lambda x: x.weekday()).astype(str)
    return input_df
