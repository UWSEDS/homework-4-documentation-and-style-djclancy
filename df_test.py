"""
Create a dataframe method that returns a boolean of
true if and only if three things are satisfied.
1) columns of the dataframe match the input named
	column
2) the values in each column are of the same type
3) there are at least 10 rows
"""

import numpy as np
import pandas as pd

def dataframe_config_prop(data_frame, cols):
    '''
    The purpose of this method is to return a boolean of
    true if and only if three things happen:
    1) columns of data_frame match the column in "columns"
    2) the values in each column are of the same type
    3) there are at least 10 rows
    '''
    columns_of_data_frame = data_frame.columns.tolist()
    columns_of_data_frame.sort()
    cols.sort()
    # see if the sorted columns are the same
    if columns_of_data_frame != cols:
        raise ValueError("Columns don't agree")
    # find out if there are fewer than 10 indices
    if len(data_frame.index) < 10:
        raise ValueError("Not 10+ rows long")
    # find out if the columns are each of the same type
    if not df_cols_of_one_type(data_frame):
        raise ValueError("Columns of different types")
    return True

def df_cols_of_one_type(data_frame):
    '''
    Tests to make sure all columns in a dataframe
    called "data_frame" are of the same type.
    Returns a boolean which is True if and only if
    each column is of a single type.
    '''
    if has_desired_len(data_frame):
        columns_of_data_frame = data_frame.columns
        bool_val = True
        for y in columns_of_data_frame:
            for j in range(0, len(data_frame[y])):
                temp_bool = type(data_frame[y][j]) == type(data_frame[y][0])
                bool_val = bool_val and temp_bool
    else:
        bool_val = True
    return bool_val

def has_nan(data_frame):
    '''
    Tests for a nan value.
    Returns a boolean, which is True if and only if
    there is a NaN
    '''
    count_of_nans = data_frame.isnull().sum().sum()
    if count_of_nans == 0:
        boolval = False
    else:
        boolval = True
    return boolval

def has_desired_len(data_frame, length=1):
    '''
    Tests to make sure the dataframe data_frame is sufficiently long.
    Returns a boolean, which is True if and only if
    the data_frame has more than length number of rows.
    '''
    row_count = data_frame.shape[0]
    if row_count >= length:
        bool_val = True
    else:
        bool_val = False
    return bool_val


## Tests below
def test_dataframe():
    '''
    A test for dataframe_config_prop when the value returned
    should be true.
    '''
    d_f = pd.DataFrame({'A':[x for x in range(0, 10)],
                        'B':[str(x) for x in range(0, 10)]})
    cols = ['B', 'A']
    assert dataframe_config_prop(d_f, cols)

def test_for_nan_with_nan():
    '''
    A test for has_nan when the value returned
    should be true.
    '''
    d_f = pd.DataFrame({'A':[1, np.nan]})
    assert has_nan(d_f)

def test_for_nan_without_nan():
    '''
    A test for has_nan when the value returned should be false
    '''
    d_f = pd.DataFrame({'A':[1, 2]})
    assert not has_nan(d_f)

def test_for_len_with_long_df():
    '''
    A test for hasdesired_len when the value returned should be true
    '''
    d_f = pd.DataFrame({'A':[1, 2]})
    assert has_desired_len(d_f)

def test_for_len_with_short_df():
    '''
    A test for has_desired_len when the value returned should
    be false
    '''
    d_f = pd.DataFrame({'A':[]})
    assert not has_desired_len(d_f)

def test_for_cols_yes():
    '''
    A test for df_cols_of_one_type when the value returned should
    be true
    '''
    d_f = pd.DataFrame({'A':[1, 2, 1], 'B':["st", "str", "stri"]})
    assert df_cols_of_one_type(d_f)

def test_for_cols_no():
    '''
    A test for df_cols_of_one_type when the value returned should
    be false
    '''
    d_f = pd.DataFrame({'A':[1, 'st']})
    assert not df_cols_of_one_type(d_f)
