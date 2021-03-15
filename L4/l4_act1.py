import pandas as pd
from efficient_apriori import apriori

pd.set_option('max_columns', None)

dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

#遍历所有数据
transactions = []
for i in range(0, dataset.shape[0]):
    temp = []
    for j in range(0, dataset.shape[1]):
        if str(dataset.values[i, j]) != 'nan':
            temp.append(dataset.values[i,j])
    transactions.append(temp)

itemsets, rules = apriori(transactions, min_support = 0.02, min_confidence = 0.3)

print('频繁项集:', itemsets)
print('关联规则:', rules)