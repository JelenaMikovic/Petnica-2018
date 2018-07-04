import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mixed = pd.read_csv("C:\\Users\\admin\\Desktop\\New folder\\order_products__prior.csv")
orders = len(set(mixed['order_id']))
products = len(set(mixed['product_id']))

print("average: " + str(orders/products))

array = [0]*orders*3

for i in mixed['order_id']:
    array[i] += 1

a = np.array(array)
b = np.array(range(0, 3*n))

plt.plot(b, a)
plt.show()