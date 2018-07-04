import pandas as pd

mixed = pd.read_csv("C:\\Users\\admin\\Desktop\\New folder\\order_products__prior.csv")
orders = len(set(mixed['order_id']))
products = len(set(mixed['product_id']))

niz = [0]*products*3

for i in mixed['product_id']:
    array[i] += 1
array.sort()

array2 = array[-10:]

for i in array2:
print(i)