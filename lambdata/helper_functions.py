def null_count(df):
    return df.isnull().sum().sum()


def list_2_series(list_2_series, df):
    series = pandas.Series(list_2_series)
    return df[list].append(series)


class BodyMassIndex:
    def __init__(self, name, height, weight):
        self.name = str(name)
        self.height = float(height)
        self.weight = float(weight)
        
    def calculate(self):
        print(self.name, 'has a BMI of:', self.weight / self.height**2)
