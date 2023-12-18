import pandas as pd 
from sklearn.preprocessing import LabelEncoder

def get_data(path, classes):
    df = pd.read_csv(path)
    head = df.head()
    number_of_classes = df.groupby(classes).size()
    return df, head, number_of_classes

def lables(data, classes):
    tf = LabelEncoder()
    data[classes] = tf.fit_transform(data[classes])
    return data[classes]