import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

base = pd.read_csv('C:\\Users\\admin\\Desktop\\New folder\\orders.csv')

orders = len(set(Baza['order_id']))
users = len(set(Baza['user_id']))

print("average " + str(orders/users))

array = [0]*orders*3

for i in base['user_id']:
    array[i] += 1

a = np.array(array)
b = np.array(range(0, 3*n))

plt.plot(b, a)
plt.show()