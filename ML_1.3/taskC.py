'''
Уберите из данных все заведения, у которых средний чек неизвестен или превышает 2500. Пока есть опасение, что их слишком мало, чтобы мы смогли обучить на них что-нибудь. Выведите количество заведений, которое получилось после очистки.
'''

import pandas as pd

base = 'docs/'
data = pd.read_csv(base + 'organisations.csv')
features = pd.read_csv(base + 'features.csv')
rubrics = pd.read_csv(base + 'rubrics.csv')

data.drop(data[data.average_bill.isna()].index, inplace = True)
data.drop(data[data.average_bill > 2500].index, inplace = True)

print(data.org_id.count())
