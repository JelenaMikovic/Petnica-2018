import pandas as pdb

orders = pdb.read_csv('C:\\Users\\admin\\Desktop\\New folder\\orders.csv')
prods = pdb.read_csv('C:\\Users\\admin\\Desktop\\New folder\\products.csv')

print("Narudzbina ima ",orders.count()['order_id'])
print("Proizvoda ima ",prods.count()['product_id'])
print("Usera ima ",orders['user_id'].drop_duplicates().count())