#test dataPreparing
from dataPreparing import *
df, b, c=get_data('star_classification.csv', 'class')
print(c)
#print(df.corr)
df['class'] = lables(df, 'class')
print(df.groupby('class').size())