import pandas as pd 

def get_data(path, classes):
    df = pd.read_csv(path)
    head = df.head()
    number_of_classes = df.groupby(classes).size()
    return df, head, number_of_classes

def lables(data):
    