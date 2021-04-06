def null_count(df):
    return df.isnull().sum().sum()


def list_2_series(list_2_series, df):
    series = pandas.Series(list_2_series)
    return df[list] = series